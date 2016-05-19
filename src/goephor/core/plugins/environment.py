'''
Created on Apr 27, 2016

:author: iitow
'''

from pluginable import Plugin


class env(Plugin):
    ''' Environment specific tasks go here
    '''
    def __init__(self, action_manager):
        '''
        env Constructor

        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def set(self,
            key,
            value,
            **defaults):
        '''
        Set an environment variable

        :param key: String
        :param value: String
        '''
        self.EnvManager.set(key, value)
        if self.verbose:
            print "[set] %s=%s" % (key, value)
