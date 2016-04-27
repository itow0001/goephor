'''
Created on Apr 27, 2016

@author: iitow
'''

from pluginable import Plugin
from modules.environment import EnvManager

class env(Plugin):
    ''' This class Represents an example
    '''
    def __init__(self,action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self,self.action_manager)
    
    def set(self,key,value,**defaults):
        value = self.EnvManager._sanitize(value)
        self.EnvManager.set(key, value)
        