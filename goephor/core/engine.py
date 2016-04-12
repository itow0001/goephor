'''
Created on Jan 8, 2016

@author: iitow
'''
import importlib
import json
import os
import re
import sys

sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../modules"))
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../core"))
sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../plugins"))


class Chain(object):
    ''' This the action object Chain
    '''
    def __init__(self, config_file, actions_key):
        ''' Queue Constructor
        @param config_file: defines all actions in a build
        '''
        self.actions_key = actions_key
        self.config_type = None
        self.config = self.read_config(config_file)
        self.envs = self.set_envs(self.config)
        if self.config.get(self.actions_key):
            self.action_objs = self.load_actions(self.config,self.actions_key)
        
    def read_config(self,config_file):
        """ Allows for reading .yaml or .json files based on extention
        @param config_file: defines all actions in a build
        @return: dict
        """
        ext = config_file.rsplit('.',1)[1]
        data = None
        if 'yaml' in ext:
            data = self._read_yaml(config_file)
            self.config_type = ext
        elif 'json' in ext:
            data = self._read_json(config_file)
            self.config_type = ext
        if not data:
            print "[Error] file @ %s" % (config_file)
            sys.exit(1)
        return data

    def _read_yaml(self, config_file):
        """ Reads in the yaml config
        @param config_file: defines all actions in a build
        @return: dict
        """
        data = None
        try:
            import yaml
            with open(config_file) as file:
                data = yaml.load(file)
                return data
        except Exception:
            print "[Error] %s" % (config_file)
            raise
  
    def _read_json(self, config_file):
        """ Reads in the json config
        @param config_file: defines all actions in a build
        @return: dict
        """
        data = None
        try:
            with open(config_file) as file:
                data = json.loads(file.read())
                return data
        except Exception:
            print "[Error] %s" % (config_file)
            raise

    def set_envs(self, config):
        """ Setup the environment variables
        @param config: defines all actions in a build as dict
        @return: envs
        """
        envs = config.get("globals")
        for env in envs:
            value = self._replace_keys(envs, env.values()[0])
            env[env.keys()[0]] = value
            os.environ[env.keys()[0]] = value
        return envs

    def _replace_keys(self, envs, value):
        """ Private global string replace all previously defined variables with string
        @param envs: Dict of envirnment variables
        @param value: The replaceable key
        @return: full string keys have been replaced with appropriate string
        """
        keys = self._has_keys(value)
        if keys:
            for key in keys:
                for env in envs:
                    if env.keys()[0] == key:
                        orig = "${%s}" % (key)
                        sys_env = os.environ.get(key)
                        if sys_env:
                            value = value.replace(orig, sys_env)
                        else:
                            value = value.replace(orig, env.values()[0])
        return value

    def _has_keys(self, value):
        """ returns all keys in a given env path
        @param value: The replaceable key
        @return: keys which have been requested from a given path ${var}
        """
        try:
            matches = re.findall(r'(?<={)[^}]*', value)
            return matches
        except Exception:
            print "[Error] malformed global variable"
            raise

    def stat_actions(self):
        """ displays all info about objects in the queue
        """
        print "\n\n"
        print "[INFO]"
        print self.config.get("name")
        print "\n   [DESCRIPTION]"
        print self.config.get("description")
        print "\n   [GLOBALS]"
        for env in self.envs:
            key = env.keys()[0]
            value = env.values()[0]
            print "  %s : %s" % (key.rjust(25), value)
        print "\n   [QUEUE]"
        for action_obj in self.action_objs:
            action_obj.pprint()

    def load_actions(self, config, actions_key):
        """ load all actions in list
        @param config: json dict
        @param actions_key: dictionary key name to load actions 
        @return: list of all actionable objects
        """
        actions = config.get(actions_key)
        action_objs = []
        id_cnt = 0
        for action in actions:
            action_obj = Action(action.keys()[0], action.values()[0])
            action_obj.ID = id_cnt
            action_obj.GLOBALS = self.envs
            action_objs.append(action_obj)
            id_cnt += 1
        return action_objs

    def init_actions(self, receipt_path="./",strict=True):
        """ call all actions in action array
        @param receipt_path: path spit out build receipt
        """
        if self.config.get(self.actions_key):
            for action_obj in self.action_objs:
                print action_obj.pprint()
                output = self._init_action(action_obj,strict=strict)
                action_obj.RETURN = output
            self.create_receipt(receipt_path)
        else:
            print "[Error] actions key %s not found passing" % self.actions_key
            sys.exit(1)

    def _init_action(self, obj,strict=True):
        """ Single Action obj Translate dictionary actions to python calls in /core
        @param obj: nest dictionary containing all calls
        @return: info about build output
        """
        args = obj.OPTS.get("args",[])
        kwargs = obj.OPTS.get("kwargs",{})
        try:
            if obj.IMP == 'self':
                RETURN = getattr(self, obj.DEF)(*args, **kwargs)
            else:
                mod = self._load_plugin(obj.IMP)
                RETURN = getattr(mod, obj.DEF)(*args, **kwargs)
            obj.EXECUTED += 1
            return RETURN
        except Exception:
            obj.pprint()
            if strict:
                raise

    def _load_plugin(self, name):
        """ Private loads module dynamically
        @param name: module name
        """
        mod = __import__("%s" % name)
        return mod

    def create_receipt(self, receipt_path):
        """ Create a post build receipt
        @param receipt_path: path spit out build receipt
        """
        receipt_path = "%s/%s_receipt.%s" % (receipt_path,self.actions_key,self.config_type)
        receipt = self.config
        receipt["results"] = []
        for obj in self.action_objs:
            result = obj.get_receipt()
            receipt.get("results").append(result)
        with open(receipt_path,'w') as file:
            if self.config_type == 'yaml':
                import yaml
                file.write(yaml.dump(receipt, default_flow_style=False))
            elif self.config_type == 'json':
                file.write(json.dumps(receipt, indent=4, sort_keys=True))


class Action(object):
    """ Stores action-able object state
    """
    def __init__(self, IMP, DEF):
        """ Action object constructor
        """
        self.IMP = IMP
        self.DEF = DEF.keys()[0]
        self.OPTS = DEF.values()[0]
        self.ID = 0
        self.RETURN = None
        self.EXECUTED = 0
        self.GLOBALS = None

    def get_receipt(self):
        """ format of a single actions receipt
        @return: dict
        """
        return {"IMP": self.IMP,
                "DEF": self.DEF,
                "OPTS": self.OPTS,
                "ID": self.ID,
                "RETURN": self.RETURN,
                "EXECUTED": self.EXECUTED,
                "GLOBALS": self.GLOBALS}

    def pprint(self, verbose=False):
        """ format of a printing a single action
        """
        print "[ID: %s]" % self.ID
        print "    IMP: %s" % self.IMP
        print "    DEF: %s" % self.DEF
        print "   OPTS: %s" % self.OPTS
        if self.RETURN:
            if self.RETURN.get('code'):
                print "   CODE: %s" % self.RETURN.get('code')
        print "[GLOBALS]"
        for env in self.GLOBALS:
            print "%s : %s" % (env.keys()[0].rjust(25), env.values()[0])
        if verbose:
            print self.RETURN
