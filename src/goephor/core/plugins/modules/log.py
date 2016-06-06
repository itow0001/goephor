'''
Created on Jun 3, 2016

:author: iitow
'''
import sys
def colors(color_type,output):
    types = {'header': '\033[95m',
              'info': '\033[94m',
              'success': '\033[92m',
              'warning': '\033[93m',
              'fail': '\033[91m',
              'error': '\033[91m',
              'end': '\033[0m'}
    trans = types.get(color_type,None)
    #if not trans:
    #    print "[info] transform %s not found" % color_type
    #    return output
    #else:
    if not output:
        output = ""
    output = trans+str(output)+types.get('end')
    return output
    
def message(message_type,output):
    output_final = colors(message_type,output)
    return output_final
    #return output_final
