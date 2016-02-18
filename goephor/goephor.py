'''
Created on Jan 9, 2016

@author: iitow
'''
import argparse

from core.engine import Chain



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
                        default='./receipt.json',
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

if __name__ == '__main__':
    options = menu()
    chain = Chain(options.file)
    if options.execute:
        chain.init_actions(receipt_path=options.receipt)
    if options.dump:
        chain.stat_actions()
