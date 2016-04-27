'''
Created on Apr 25, 2016

@author: iitow
'''

from plugins import *
from plugins.modules.action import Manager
from plugins.modules.environment import Env
import os
import plugins
import importlib
import inspect
import re
import sys
import types

class Run(object):
    ''' Runs the Chain
    '''
    def __init__(self, config_file):
        ''' Constructor
        '''
        self.config_file = config_file
        self.config = self.read_config(config_file)
        self.set_envs()
        self.action_manager = Manager()
        self.load_actions()

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
    
    def set_envs(self):
        E = Env()
        for env in self.config.get('globals'):
            key = env.keys()[0]
            value = E._sanitize(env.get(key))
            E.set(key,value)

    def load_actions(self):
        ''' loads actions in to chain resolves yaml/json to a object
        '''
        for action in self.config.get('actions'):
            action_obj = self.action_manager.to_obj(action,self.action_manager)
            self.action_manager.add(action_obj)
    
    def execute_actions(self):
        ''' Executes all action objects
        '''
        for action in self.action_manager.chain:
            try:
                action.execute()
            except Exception as e:
                print '[Error] %s' % (str(e))
                sys.exit(1)
    
if __name__ == '__main__':
    config = '../test.yaml'
    run = Run(config)
    #run._imports()
    run.execute_actions()
            
        
    
        