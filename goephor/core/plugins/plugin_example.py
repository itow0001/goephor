'''
Created on Apr 27, 2016

@author: iitow
'''
from pluginable import Plugin


class example(Plugin):
    ''' This class Represents an example
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)

    def runme(self, var, **defaults):
        print "This var [%s] was passed in " % var
        print "\nhere are the defaults:"
        for key, value in defaults.iteritems():
            print "%s : %s" % (key, value)
