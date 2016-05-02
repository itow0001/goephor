'''
Created on Apr 25, 2016

@author: iitow
'''
from pluginable import Plugin
from modules.terminal import shell, rsync


class terminal(Plugin):
    '''
    General nix system commands go here
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def shell(self, cmd,**defaults):
        session = shell(cmd)
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')
    
    def rsync(self,user,rsa_private_path,server,src,dest,option,**defaults):
        session = rsync(server,src,dest,user=user,rsa_private=rsa_private_path)
        if not session.get('code') == 0:
            raise Exception(session.get('stdout'))
        return session.get('stdout')
