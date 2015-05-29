#!/usr/bin/env python

'''Verifies a FASTR file, compressed or decompressed'''

__version__ '0.0.0.1'

from line_verifier import verify_lines
from file_iterators.fastr import fastr_iter

def verify_fastr(handle):
    '''Returns True if FASTR file is valid and False if file is not valid'''
    
    lines = []
    for fastqEntry in fastq_iter:
        entry = '>%s\n%s\n' % (fastrEntry['name'],
                               fastrEntry['sequence'])
        lines.append(entry)
    regex = r'^\+.+\n[\dx-]*\d\n$'
    delimiter = r'\n'
    fastrStatus = verify_lines(lines, regex, delimiter)
    return fastrStatus
