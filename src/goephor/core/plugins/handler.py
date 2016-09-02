'''
Created on Jul 1, 2016

@author: iitow
'''
import ConfigParser
import fileinput
import json
import yaml
from pluginable import Plugin
from modules.terminal import shell, rsync
from modules.log import message

class file(Plugin):
    '''
    General class can read configuration files
    '''
    def __init__(self, action_manager):
        '''
        terminal Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)  

    def readconfig(self,path,**defaults):
        '''
        General read configs into environment currently only supports ConfigParser
        :param path: String, full path to file
        :return: key value pairs become environment variables
        :example:
        ```
        - handler.file.readconfig:
           - "${CFG}"
        ```
        '''
        print "[read] @ %s" % (path)
        self._configparser(path)
        pass

    def readfile(self,path,**defaults):
        '''
        General read
        :param path: String, full path to file
        :return: String
        :example:
        ```
        - handler.file.readfile:
           - "${PATHTOFILE}"
           - set_env: "SOMEVAR"
        ```
        '''
        print "[read] @ %s" % (path)
        with open(path,'r') as f:
            return f.read()
        return None
    
    def readfile_replace(self,path,**defaults):
        '''
        reads a file in replaces tokens with updates
        :param path: String, full path to file
        :param defaults: key,value [token, new]
        :return: String
        :example:
        ```
        - handler.file.readfile_replace:
           - "${PATHTOFILE}"
           - TOKEN1: "VALUE1"
           - set_env: "SOMEVAR"
        ```
        '''
        output = ''
        for line in fileinput.input(path, inplace=True):
            for key, value in defaults.iteritems():
                if key in line:
                    line = line.replace(key,value)
            output = "%s%s"%(output,line)
            print line 
        return output

    def _configparser(self,path):
        '''
        Private, adds configparser values to environment 
        '''
        cfg = ConfigParser.SafeConfigParser()
        cfg.read(path)
        sections = cfg.sections()
        if not sections:
            raise Exception('Unable to read config @ %s' % (path))
        for section in sections:
            for pairs in cfg.items(section):
                key = pairs[0]
                value = self.action_manager.EnvManager._sanitize(pairs[1])
                self.action_manager.EnvManager.set(key,value)
                msg = message('info',"[set] %s=" % (key),debug=self.debug)
                print "%s%s" % (msg,value)
