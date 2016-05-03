'''
Created on Apr 26, 2016

:author: iitow
'''
from pluginable import Plugin


class statement(Plugin):
    '''
    Conditional statements go here
    '''
    def __init__(self, action_manager):
        '''
        statement Constructor
        
        :param action_manager: Obj, from action_manager class
        '''
        self.action_manager = action_manager
        Plugin.__init__(self, self.action_manager)
        self.address = object.__repr__(self)

    def add_obj(self, clause):
        '''
        Private def to add action out of band
        :param clause: dict, if statement 
        '''
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
        '''
        Represents an if statement
        :param arg1: int,str
        :param operator: String, follows python rules
        :param arg12 int,str
        :param THEN: List, several other actions
        :param ELSE: List, several other actions
        :example:
        ```
           -  condition.statement.IF:
                                - "${var1}"
                                - "=="
                                - "${var2}"
                                - THEN:
                                  - system.terminal.shell:
                                    - "echo 'THEN IS HAPPENING'"
                                - ELSE:
                                  - system.terminal.shell:
                                    - "echo 'ELSE IS HAPPENING'"
        ```
        '''
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
