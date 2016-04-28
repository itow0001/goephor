'''
Created on Apr 26, 2016

@author: iitow
'''
import importlib
import sys
from environment import EnvManager
import time


class Manager(object):
    ''' manages creation of action dict to a obj
    '''
    def __init__(self, config, EnvManager):
        self.chain = []
        self.config = config
        self.EnvManager = EnvManager

    def pprint_chain(self):
        print ""
        for action in self.chain:
            print action
        print ""

    def to_obj(self, action, action_manager):
        ''' Converts action dictionary to action obj
        '''
        try:
            path = action.keys()[0]
            resolve_path = path.split('.')
            IMP = resolve_path[0]
            CLASS = resolve_path[1]
            definition = resolve_path[2]
            parameters = []
            defaults = {}
            for param in action.get(path):
                if isinstance(param, dict):
                    name = param.keys()[0]
                    value = param.get(name)
                    defaults[name] = value
                else:
                    parameters.append(param)
        except Exception as e:
            print '[Error] %s' % (str(e))
            sys.exit(1)
        try:
            action_obj = Action(IMP,
                                CLASS,
                                definition,
                                parameters,
                                defaults,
                                action_manager)
            return action_obj
        except Exception as e:
                print '[Error]# %s' % (str(e))
                sys.exit(1)

    def add(self, action_obj):
        ''' adds an action obj to chain
        '''
        self.chain.append(action_obj)

    def insert(self, index, action_obj):
        self.chain.insert(index, action_obj)

    def get_index(self, memory_address):
        cnt = 1
        for action in self.chain:
            if str(memory_address) == str(action):
                return cnt
            cnt += 1
        return None


class Action(object):
    ''' Object containing instructions to create and execute actions
    '''
    def __init__(self, IMP, CLASS, DEF, parameters, defaults, action_manager):
        self.IMP = IMP
        self.CLASS = CLASS
        self.DEF = DEF
        self.EnvManager = EnvManager()
        self.parameters = self.EnvManager.sanitize(parameters)
        self.defaults = self.EnvManager.sanitize(defaults)
        self.action_manager = action_manager
        self.instance = self._init_instance()
        self.duration = None
        self.session = None

    def __repr__(self):
        ''' Override container name so we can match the array in the chain
        '''
        return object.__repr__(self.instance)

    def get_receipt(self):
        return {"IMP": self.IMP,
                "CLASS": self.CLASS,
                "DEF": self.DEF,
                "parameters": self.parameters,
                "defaults": self.defaults,
                "duration": self.duration,
                "session": self.session}

    def pprint(self):
        ''' print state about the object pretty
        '''
        print self.IMP
        print self.CLASS
        print self.DEF
        print self.parameters
        print self.defaults

    def _init_instance(self):
        ''' Initializes the class
        '''
        IMP = 'core.plugins.%s' % (self.IMP)
        _module = importlib.import_module(IMP)
        CLASS = getattr(_module, self.CLASS)
        CLASS = CLASS(self.action_manager)
        return CLASS

    def execute(self):
        ''' execute the instruction
        '''
        DEF = getattr(self.instance, self.DEF)
        start = time.time()
        self.session = DEF(*self.parameters, **self.defaults)
        end = time.time()
        self.duration = end - start
        return self.session
