'''
Created on Apr 28, 2016

@author: iitow
'''
from modules.remote import Run
from pluginable import Plugin

class ssh(Plugin):
    '''
    This class can perform ssh commands
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
        self.verbose = self.action_manager.verbose
        self.debug = self.action_manager.debug
        self.EnvManager = self.action_manager.EnvManager

    def cmd(self, cmdstr, server, user, rsa_private_path, **defaults):
        session = Run(server,rsa_private_path,user)
        output = session.cmd(cmdstr)
        if not output.get('code') == 0:
            raise Exception(output.get('stdout'))
        return output.get('stdout')
        
        
        
        
        
        