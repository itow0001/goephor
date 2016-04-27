'''
Created on Apr 26, 2016

@author: iitow
'''
import ctypes
from pluginable import Plugin
class statement(Plugin):

    def __init__(self,action_manager,debug=False):
        self.debug = debug
        self.action_manager = action_manager
        Plugin.__init__(self,self.action_manager)
        self.address = object.__repr__(self)
        if self.debug:
            print "CHAIN BEFORE:"
            self.action_manager.pprint_chain()
    
    def add_obj(self,clause):
        cnt = 0
        for action in clause:
            action_obj = self.action_manager.to_obj(action,self.action_manager)
            index = self.action_manager.get_index(self.address)
            if index:
                index = index+cnt
                if self.debug:
                    print "index:%s" % (str(index))
                self.action_manager.insert(index,action_obj)
            cnt +=1

    
    def IF(self,arg1,operator,arg2,THEN=[],ELSE=[]):
        if arg1.isdigit() and arg2.isdigit():
            statem = "%d %s %d" % (int(arg1),operator,int(arg2))
        else:
            statem = "'%s' %s '%s'" % (arg1,operator,arg2)
        if self.debug:
            print statem
        if eval(statem):
            self.add_obj(THEN)
        else:
            self.add_obj(ELSE)
        if self.debug:
            print "CHAIN AFTER:"
            self.action_manager.pprint_chain()
        
            


                
                

        
            
        
        