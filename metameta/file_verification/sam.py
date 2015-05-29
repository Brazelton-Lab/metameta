#!/usr/bin/env python

'''Verifies a SAM file'''

__version__ '0.0.0.1'

from line_verifier import verify_lines
from file_iterators.sam import sam_iter

def verify_sam(handle):
    '''Returns True if SAM file is valid and False if file is not valid'''
    
    lines = []
    for samEntry in sam_iter():
        entry = '\t'.join(samEntry) + '\n'
        lines.append(entry)
    regex = r'^[!-?A-~]{1,255}\t'\
            + r'([0-9]{1,4}|[0-5][0-9]{4}|'\
            + r'[0-9]{1,4}|[1-5][0-9]{4}|'\
            + r'6[0-4][0-9]{3}|65[0-4][0-9]{2}|'\
            + r'655[0-2][0-9]|6553[0-7])\t'\
            + r'\*|[!-()+-<>-~][!-~]*\t'\
            + r'([0-9]{1,9}|1[0-9]{9}|2(0[0-9]{8}|'\
            + r'1([0-3][0-9]{7}|4([0-6][0-9]{6}|'\
            + r'7([0-3][0-9]{5}|4([0-7][0-9]{4}|'\
            + r'8([0-2][0-9]{3}|3([0-5][0-9]{2}|'\
            + r'6([0-3][0-9]|4[0-7])))))))))\t'\
            + r'([0-9]{1,2}|1[0-9]{2}|'\
            + r'2[0-4][0-9]|25[0-5])\t'\
            + r'\*|([0-9]+[MIDNSHPX=])+\t'\
            + r'\*|=|[!-()+-<>-~][!-~]*\t'\
            + r'([0-9]{1,9}|1[0-9]{9}|2(0[0-9]{8}|'\
            + r'1([0-3][0-9]{7}|4([0-6][0-9]{6}|'\
            + r'7([0-3][0-9]{5}|4([0-7][0-9]{4}|'\
            + r'8([0-2][0-9]{3}|3([0-5][0-9]{2}|'\
            + r'6([0-3][0-9]|4[0-7])))))))))\t'\
            + r'-?([0-9]{1,9}|1[0-9]{9}|2(0[0-9]{8}|'\
            + r'1([0-3][0-9]{7}|4([0-6][0-9]{6}|'\
            + r'7([0-3][0-9]{5}|4([0-7][0-9]{4}|'\
            + r'8([0-2][0-9]{3}|3([0-5][0-9]{2}|'\
            + r'6([0-3][0-9]|4[0-7])))))))))\t'\
            + r'\*|[A-Za-z=.]+\t'\
            + r'[!-~]+\n$'
    delimiter = r'\t'
    samStatus = verify_lines(lines, regex, delimiter)
    return samStatus