'''
Created on Jan 9, 2016

@author: iitow
'''
#import argparse
import optparse

from core.engine import Chain


''' python 2.6 is not funtional using this.
When we resolve package dependences we can revisit this.

def menu():
    parser = argparse.ArgumentParser(
        description='A json friendly build management tool')
    parser.add_argument('-f',
                        action="store",
                        dest="file",
                        help='json file containing build instructions')
    parser.add_argument('-r',
                        action="store",
                        dest="receipt",
                        default='./',
                        help='Location to dump a build receipt')
    parser.add_argument('-d',
                        action="store_true",
                        dest="dump",
                        default=False,
                        help='dump all objects in the chain')
    parser.add_argument('-e',
                        action="store_true",
                        dest="execute",
                        default=False,
                        help='execute all values in the chain')
    parser.add_argument('-v',
                        action="store_true",
                        dest="verbose",
                        default=False,
                        help='Turn on verbosity')
    parser.add_argument('-t',
                        action="store_true",
                        dest="test",
                        default=False,
                        help='Perform unit tests')
    parser.add_argument('--version',
                        action='version',
                        version='%(prog)s 1.0')
    return parser.parse_args()
'''
def menu():
    """ represents the menu of configuration class
    """
    p = optparse.OptionParser(description='A json friendly build management tool',
                                        prog='goephor',
                                        version='1.0',
                                        usage= "usage: %prog  ")
    p.add_option('-e' ,'--force' ,action ='store_true', dest="execute", default=False ,help="execute all values in the chain")
    p.add_option('-f' ,'--file' ,action ='store', type="string", dest="file", default="iitow" ,help="your ldap username")
    (options,args) = p.parse_args()
    return options

if __name__ == '__main__':
    options = menu()
    if options.execute:
        main_actions = Chain(options.file,'actions')
        main_actions.init_actions(receipt_path=options.receipt)
    if options.dump:
        chain = Chain(options.file,'actions')
        chain.stat_actions()
        
        
        
        
        
        
