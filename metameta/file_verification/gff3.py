#!/usr/bin/env python

'''Verifies a GFF3 file'''

__version__ '0.0.0.1'

from line_verifier import verify_lines
from file_iterators.gff3 import fastr_iter

def verify_gff3(handle):
    '''Returns True if GFF3 file is valid and False if file is not valid'''
    
    lines = []
    for gff3Entry in gff3_iter():
        entry = '\t'.join(gff3Entry) + '\n'
        lines.append(entry)
    regex = r'^[a-zA-Z0-9.:^*$@!+_?-|]+\t.+\t.+\t\d+\t\d+\t'\
            + r'\d+\.?\d*\t[+-.]\t[0-2]\t.*\n$'
    delimiter = r'\t'
    gff3Status = verify_lines(lines, regex, delimiter)
    return gff3Status
