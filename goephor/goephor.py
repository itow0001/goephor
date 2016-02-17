'''
Created on Jan 9, 2016

@author: iitow
'''
from core.engine import Queue
import optparse, sys, os

def menu():
    p = optparse.OptionParser(description='A tool json friendly build tool',
                                        prog='relpunch',
                                        version='1.0',
                                        usage= "usage: %prog  ")
    p.add_option('-f' ,'--file' ,action ='store', type="string", dest="file", default="" ,help="config json file path")
    p.add_option('-l' ,'--list' ,action ='store_true', dest="list", default=False ,help="list all actions")
    p.add_option('-e' ,'--execute' ,action ='store_true', dest="execute", default=False ,help="Execute all actions")
    p.add_option('-v' ,'--verbose' ,action ='store_true', dest="verbose", default=False ,help="print all available info out")
    p.add_option('-d' ,'--document' ,action ='store_true', dest="docs", default=False ,help="Scan code and produce git README.md")
    p.add_option('-r' ,'--receipt' ,action ='store', dest="receipt", default="./receipt.json" ,help="path to execution receipt")
    (options,args) = p.parse_args()
    options = options.__dict__
    return options



if __name__ == '__main__':
    options = menu()
    if options.get("docs"):
        manager = Manager(os.getcwd(),'./README.md')
        manager.formatter()
        sys.exit(0)
    queue = Queue(options.get("file"))
    if options.get("execute"):
        queue.init_actions(receipt_path=options.get('receipt'))
    if options.get("list"):
        queue.stat_actions()


    
    
    
    