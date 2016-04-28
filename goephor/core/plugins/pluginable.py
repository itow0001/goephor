'''
Created on Apr 25, 2016

@author: iitow
'''
from modules.environment import EnvManager
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
            ''' This wrapper adds functionality to all child class functions
            '''
            dfs = {}
            env_key = None
            for key, value in defaults.iteritems():
                # check for set_env in **defaults
                if key == 'set_env':
                    env_key = value
                else:
                    dfs[key] = value
            result = func(*parameters, **dfs)
            # after function pass it to environment
            if env_key:
                EnvManager().set(env_key, str(result))
            return result
        return wrapper


class Plugin(object):
    ''' This is the base class for plugin which all plugins must inherit from.
    '''
    __metaclass__ = DecoMeta

    def __init__(self, action_manager):
        self.action_manager
        self.EnvManager = self.action_manager.EnvManager
        self.envs = self.EnvManager.envs
