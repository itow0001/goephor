'''
Created on Apr 27, 2016

@author: iitow
'''

from pluginable import Plugin


class env(Plugin):
    ''' This class Represents an example
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def set(self, key, value, **defaults):
        self.EnvManager.set(key, value)
