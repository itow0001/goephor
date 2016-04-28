'''
Created on Apr 26, 2016

@author: iitow
'''
from pluginable import Plugin


class statement(Plugin):
    def __init__(self, action_manager):
        self.action_manager = action_manager
        self.verbose = self.action_manager.verbose
        self.debug = self.action_manager.debug
        self.EnvManager = self.action_manager.EnvManager
        Plugin.__init__(self, self.action_manager)
        self.address = object.__repr__(self)

    def add_obj(self, clause):
        cnt = 0
        for action in clause:
            action_obj = self.action_manager.to_obj(action,
                                                    self.action_manager)
            index = self.action_manager.get_index(self.address)
            if index:
                index = index+cnt
                self.action_manager.insert(index, action_obj)
            cnt += 1

    def IF(self, arg1, operator, arg2, THEN=[], ELSE=[]):
        arg1 = self.EnvManager._sanitize(arg1)
        arg2 = self.EnvManager._sanitize(arg2)
        if arg1.isdigit() and arg2.isdigit():
            statem = "%d %s %d" % (int(arg1), operator, int(arg2))
        else:
            statem = "'%s' %s '%s'" % (arg1, operator, arg2)
        if self.verbose:
            print "\n[eval] %s" % statem
        if eval(statem):
            if self.verbose:
                print "\n[THEN]"
            self.add_obj(THEN)
        else:
            if self.verbose:
                print "\n[ELSE]"
            self.add_obj(ELSE)

