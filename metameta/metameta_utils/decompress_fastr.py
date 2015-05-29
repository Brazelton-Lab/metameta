#!/usr/bin/env python

'''Decompresses FASTR sequence'''

def decompress_fastr(sequence):
    '''Returns decompressed FASTR  sequence'''
    
    depthSequence = sequence.split('-')
    decompressedSequence = []
    for base in depthSequence:
        try:
            int(base)
            decompressedSequence.append(int(base))
        except ValueError:
            sep = base.split('x')
            sep[1] = sep[1].rstrip('\n')
            decompressedSequence += [int(sep[1]) for i in range(int(sep[0]))]
    decompressedSequence = '-'.join([str(i) for i in decompressedSequence])
    return decompressedSequence
