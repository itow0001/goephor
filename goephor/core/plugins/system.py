'''
Created on Apr 25, 2016

@author: iitow
'''
from pluginable import Plugin
from modules.terminal import shell

class terminal(Plugin):
    ''' This class Represents all system calls/actions
    '''
    def __init__(self,action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self,self.action_manager)
        
    def shell(self,cmd,**defaults):
        session = shell(cmd,**defaults)
        return session

if __name__ == '__main__':
    act = Actions()
        
        
    
    
        