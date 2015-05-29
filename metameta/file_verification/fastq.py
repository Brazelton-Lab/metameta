#!/usr/bin/env python

'''Verifies a FASTQ file'''

__version__ '0.0.0.1'

from line_verifier import verify_lines
from screed.fastq import fastq_iter

def verify_fastq(handle):
    '''Returns True if FASTQ file is valid and False if file is not valid'''
    
    lines = []
    for fastqEntry in fastq_iter(handle):
        entry = '>%s\n%s\n+\n%s\n' % (fastqEntry['name'],
                                      fastqEntry['sequence'],
                                      fastqEntry['accuracy'])
        lines.append(entry)
    regex = r'^@.+\n[ACGTURYKMSWBDHVNX]+\n\+.*\n.+\n$'
    delimiter = r'\n'
    fastqStatus = verify_lines(lines, regex, delimiter)
    return fastqStatus
