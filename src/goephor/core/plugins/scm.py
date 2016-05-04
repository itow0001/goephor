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
        '''
        git Constructor
        
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
    
    def clone(self,new_local_path,remote,**defaults):
        '''
        Clone a git repo
        
        :param new_local_path: String, full path and desired dir name
        :param remote: String, git repo
        :example:
        ```
               - scm.git.clone:
                      - "/tmp/goephor"
                      - "git@github.west.isilon.com:eng-tools/goephor"
        ```
        
        '''
        repo = Repo_actions(new_local_path)
        has_cloned = repo.clone(remote, **defaults)
        if has_cloned:
            return True
        else:
            raise Exception(output.get('Unable to Clone %s' % remote))
    
    def delete(self,local_path,**defaults):
        '''
        Delete a local repo
        :param local_path: String
        :example:
        ```
            - scm.git.delete:
                - "/tmp/goephor"
        ```
        '''
        repo = Repo_actions(local_path)
        has_attached = repo.attach(local_path)
        if has_attached:
            session = shell("rm -rf %s" % (local_path))
            if session.get('code') == 0:
                return True
        else:
            print "[Pass] not a repo @ %s " % (local_path)
    
    