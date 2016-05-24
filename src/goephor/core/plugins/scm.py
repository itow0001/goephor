'''
Created on Apr 28, 2016

@author: iitow
'''
from pluginable import Plugin
from modules.git_kit import Branch_actions, Repo_actions
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

    def clone(self,
              user,
              new_local_path,
              remote,
              **defaults):
        '''
        Clone a git repo

        :param user: String, username
        :param new_local_path: String, full path and desired dir name
        :param remote: String, git repo
        :example:
        ```
               - scm.git.clone:
                      - "root"
                      - "/tmp/goephor"
                      - "git@github.west.isilon.com:eng-tools/goephor"
        ```
        '''
        repo = Repo_actions(new_local_path, user=user)
        if defaults.get('branch'):
            branch = defaults.get('branch')
            has_cloned = repo.clone(remote,branch)
        else: 
            has_cloned = repo.clone(remote)
        if has_cloned:
            return True
        else:
            raise Exception('Unable to Clone %s' % remote)

    def checkout(self, user, local_path, branch):
        '''
        checkout a local branch
        :param user: String, username
        :param local_path: String, full path and desired dir name
        :param branch: String
        ```
                - scm.git.checkout:
                      - "root"
                      - "/tmp/goephor"
                      - "refactor"
        ```
        '''
        repo = Repo_actions(local_path, user=user)
        branch_obj = Branch_actions(repo)
        branch_is = branch_obj.checkout(branch)
        if not branch_is:
            raise Exception('Unable to checkout %s' % branch)
        return branch_is

    def delete(self, local_path, **defaults):
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
