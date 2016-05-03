'''
Created on Apr 27, 2016

:author: iitow
'''
from pluginable import Plugin


class example(Plugin):
    ''' This class Represents an example
    '''
    def __init__(self, action_manager):
        '''
        example Constructor
        
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def runme(self, var1,var2, **defaults):
        '''
        This is an example of setting up an action
        :param var1: String
        :param var2: String
        :return: runme_output
        :example:
        ```
        - example.example.runme:
            - "hello"
            - "world"
        ```
        '''
        print "This var [%s] was passed in " % var1
        print "This var [%s] was passed in " % var2
        print "\nhere are the defaults:"
        for key, value in defaults.iteritems():
            print "%s : %s" % (key, value)
        return "runme_output"
