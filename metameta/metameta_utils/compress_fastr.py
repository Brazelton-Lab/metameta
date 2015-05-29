#!/usr/bin/env python

'''Compresses a FASTR sequence'''

def compress_fastr(sequence):
    '''Eliminates repeats in a sequence and returns a string'''
    
    compressedSequence = []
    if type(sequence) == str:
        sequence = sequence.split('-')
    lastRead = None
    readRepeats = 0
    for read in enumerate(sequence):
        if read[1] == lastRead:
            readRepeats += 1
        else:
            if readRepeats != 0:
                compressedSequence.append(str(readRepeats + 1) + 'x' +\
                                 str(lastRead))
                readRepeats = 0
            elif read[0] != 0:
                compressedSequence.append(str(lastRead))
            lastRead = read[1]
        if read[0] + 1 == len(sequence):
            if readRepeats != 0:
                compressedSequence.append(str(readRepeats + 1) + 'x' +\
                                 str(lastRead))
            else:
                compressedSequence.append(str(lastRead))
            compressedSequence = '-'.join(compressedSequence)
    return compressedSequence
