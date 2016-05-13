'''
Created on May 13, 2016

@author: iitow
'''
from pluginable import Plugin

class utils(Plugin):
    '''
    Utils class for parsing strings
    '''
    def __init__(self, action_manager):
        '''
        utils Constructor
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def replace(self,name,old,new,**defaults):
        '''
        String replace on environment variable
        ```
        string.utils.replace:
           - "env variable"
           - "old substring"
           - "new substring"
        ```
        '''
        env = self.EnvManager.get(name)
        if not env:
            error = "env not found %s" % (name)
            raise Exception(error)
        new_env = env.replace(old,new)
        self.EnvManager.set(name,new_env)
        if self.verbose:
            print "[replace] %s=%s" % (name,new_env)
            
        

        