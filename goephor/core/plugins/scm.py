'''
Created on Apr 28, 2016

@author: iitow
'''
from pluginable import Plugin
from modules.git_kit import Repo_actions
from modules.terminal import shell

class git(Plugin):
    ''' This class Represents a call to git
    '''
    def __init__(self, action_manager):
        self.action_manager = action_manager
        self.verbose = self.action_manager.verbose
        self.debug = self.action_manager.debug
        self.EnvManager = self.action_manager.EnvManager
        Plugin.__init__(self, self.action_manager)
    
    def clone(self,new_local_path,remote,**defaults):
        new_local_path = self.EnvManager._sanitize(new_local_path)
        remote = self.EnvManager._sanitize(remote)
        repo = Repo_actions(self.EnvManager._sanitize(new_local_path))
        has_cloned = repo.clone(remote, **defaults)
        if has_cloned:
            return True
        else:
            raise Exception(output.get('Unable to Clone %s' % remote))
    
    def delete(self,local_path,**defaults):
        repo = Repo_actions(local_path)
        has_attached = repo.attach(local_path)
        if has_attached:
            session = shell("rm -rf %s" % (local_path))
            if session.get('code') == 0:
                return True
        else:
            print "[Pass] not a repo @ %s " % (local_path)
    
    