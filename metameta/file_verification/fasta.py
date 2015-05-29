#!/usr/bin/env python

'''Verifies a FASTA file'''

__version__ '0.0.0.1'

from line_verifier import verify_lines
from screed.fasta import fasta_iter

def verify_fasta(handle):
    '''Returns True if FASTA file is valid and False if file is not valid'''
    
    lines = []
    for fastaEntry in fasta_iter(handle, parse_description = False):
        entry = '>%s\n%s\n' % (fastaEntry['name'], fastaEntry['sequence'])
        lines.append(entry)
    regex = r'^>.+\n[ACGTURYKMSWBDHVNX]+\n$'
    delimiter = r'\n'
    fastaStatus = verify_lines(lines, regex, delimiter)
    return fastaStatus
