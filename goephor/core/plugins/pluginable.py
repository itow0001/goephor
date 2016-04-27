'''
Created on Apr 25, 2016

@author: iitow
'''
from modules.environment import Env
import types

import types

class DecoMeta(type):
    ''' Meta class for enforcing global definitions
    '''
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.iteritems():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = cls.deco(attr_value)
        return super(DecoMeta, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def deco(cls, func):
        def wrapper(*parameters, **defaults):
            ''' This wrapper adds functionality to all child class definitions
            '''
            dfs = {}
            env_key = None
            for key,value in defaults.iteritems():
                ### check for set_env in **defaults
                if key=='set_env':
                    env_key = value
                else:
                    dfs[key]=value
            result = func(*parameters, **dfs)
            ### after function pass it to environment
            if env_key:
                Env().set(env_key, result)
            return result
        return wrapper

class Plugin(object):
    ''' This is the base class for plugin which all plugins must inherit from.
    '''
    __metaclass__ = DecoMeta
    def __init__(self,action_manager):
        self.action_manager
        self.Env = Env()
 
    def set_env(self,key,value):
        ''' Sets environment variable
        '''
        self.Env.set(key,value)
    
    def get_env(self,key):
        ''' Gets an environment variable
        '''
        return self.Env.get(key)
        
    def _has_keys(self,str):
        """ Collect all environment variables
        @param str: command string
        """
        matches = re.findall(r'(?<={)[^}]*', str)
        return matches

    def _sanitize(self,str):
        """ Replace all environment variables into command
        @param str: command string
        """
        for match in _has_keys(str):
            old = '${%s}' % match
            new = os.environ.get(match)
            if new:
                str = str.replace(old, new)
        return str
        