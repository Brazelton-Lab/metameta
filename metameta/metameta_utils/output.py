#!/usr/bin/env python

'''print statement with improved functionality'''

__version__ '0.0.0.1'

def output(message, program_verbosity, message_verbosity, log_file = None,\
           fatal = False):
    '''Writes verbosity dependant message to either STDOUT or a log file'''
    
    if int(program_verbosity) >= int(message_verbosity):
        if fatal:
            fatalMessage = '\nAbove error is fatal. Exiting program.'
            message += fatalMessage
        if log_file == None:
            print(message)
        else:
            with open(log_file, 'a') as out_handle:
                out_handle.write(message + '\n')
        if fatal:
            sys.exit(1)
