#!/usr/bin/env python

'''obtains read depth data for a FASTA/Q file from a BAM file

Usage:

    generate_fastr.py <fastaq> <bam> <output>

Synopsis:

    reads alignment data from a BAM file to produce a FASTR file
    containing read depth data for the FASTA/Q file

Arguments:

    fastaq             FASTA or FASTQ file used as the mapping reference
    bam                BAM file containing alignment data
    output             Name of FASTR file containing read depth data to write
'''

__version__ = '0.0.0.11'

import argparse
from biofile_verifiers.verify_fasta import verify_fasta
from biofile_verifiers.verify_fastq import verify_fastq
from biofile_verifiers.verify_binary import verify_binary
from metameta.metameta_utils.compress_fastr import compress_fastr
from metameta.metameta_utils.decompress_fastr import decompress_fastr
from metameta.metameta_utils.output import output
from metameta.metameta_utils.write_fastr import write_fastr
import pysam
from screed.fasta import fasta_iter
from screed.fastq import fastq_iter
import sys

def main():
    if args.fastaq[1] != 'fasta' and args.fastaq[1] != 'fastq':
        message = args.fastaq[1] + ' is not a FASTA or FASTQ file.'
        output(message, args.verbosity, 0, log_file = args.log_file,\
               fatal = True)
    if not fastr_file.endswith('.fastr'):
        fastr_file += '.fastr'
    if args.bam[1] == 'sam':
        message = 'Your alignment file is a SAM file. Please convert it\n'\
                  + 'into a BAM file, then sort and index it using the\n'\
                  + 'following commands:\n\n'\
                  + 'samtools view -h -S -b -F 4 -o <BAM file> <SAM file>\n'\
                  + 'samtools sort <BAM file> <sorted BAM file>\n'\
                  + 'samtools index <sorted BAM file>\n\n'\
                  + 'Then run this tool again with the BAM file.\n'\
                  + 'This allows generate_fastr to run with essentially\n'\
                  + 'zero memory and it runs roughly 20x faster than with\n'\
                  + 'a SAM file.'
        output(message, args.verbosity, 0, log_file = args.log_file,\
               fatal = True)
    elif args.bam[1] != 'bam':
        message = 'Must specify if alignment file is a SAM or a BAM'
        output(message, args.verbosity, 0, log_file = args.log_file,\
               fatal = True)
    header = ''
    sequenceLength = 0
    sequenceDepth = []
    readType = ''
    with pysam.Samfile(sam_bam_file, 'rb') as alignmentFile:
        with open(args.fastaq, 'rU') as fastaqFile:
        for fastaEntry in entry_generator(args.fastaq[0]):
            # Don't include '+' in header
            header = entry[0][1:]
            output('Analyzing read depth for: ' + header, args.verbosity, 2,\
                   log_file = args.log_file)
            sequenceId = header.split(' ')[0]
            sequenceLength = len(entry[1])
            sequenceDepth = [0 for base in range(sequenceLength)]
            for pileupColumn in alignmentFile.pileup(sequenceId):
                basePosition = pileupColumn.pos
                baseReadDepth = pileupColumn.n
                sequenceDepth[basePosition] = baseReadDepth
            output('Compressing sequence: ' + str(sequenceDepth),\
                   args.verbosity, 2, log_file = args.log_file)
            fastrSequence = compress_fastr(sequenceDepth)
            output('Compressed sequence: ' + fastrSequence, args.verbosity, 2,\
                   log_file = args.log_file)
            sections = len(fastrSequence.split('-'))
            if sections > 1:
                message = 'Appending read depth for ' + header[1:-1] +\
                          ' to ' + fastr_file
                output(message, args.verbosity, 2,\
                       log_file = args.log_file)
                write_fastr([header], [fastrSequence], fastr_file)
            else:
                message = header + ' has a read depth of zero for '+\
                              'each base. Not appending to ' + fastr_file
                output(message, args.verbosity, 2,\
                       log_file = args.log_file)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = __doc__,
                                        formatter_class = argparse.\
                                        RawDescriptionHelpFormatter)
    parser.add_argument('fastaq',
                        default = None,
                        nargs = '?',
                        help = 'FASTA or FASTQ file to analyze the read' +\
                        ' depth of using the given BAM file, default is FASTA')
    parser.add_argument('bam',
                        default = None,
                        nargs = '?',
                        help = 'BAM file containing mapping' +\
                        'data for given FASTA/Q file')
    parser.add_argument('output',
                        default = None,
                        nargs = '?',
                        help = 'name of FASTR file to be written')
    parser.add_argument('--fastq',
                        action = 'store_true',
                        help = 'specifies FASTA/Q input file as a FASTQ file')
    parser.add_argument('--compressed',
                        action = 'store_true',
                        help = 'compresses FASTR output file')
    parser.add_argument('-l', '--log_file',
                        default = None,
                        help = 'log file to print all messages to')
    parser.add_argument('-v', '--verbosity',
                        action = 'count',
                        default = 0,
                        help = 'increase output verbosity')
    parser.add_argument('--verify',
                        action = 'store_true',
                        help = 'verify input files before use')
    parser.add_argument('--version',
                        action = 'store_true',
                        help = 'prints tool version and exits')
    args = parser.parse_args()

    if args.version:
        print(__version__)
    elif args.fastaq == None:
        print(__doc__)
    elif args.fastaq == None or\
         args.bam == None or\
         args.output == None:
        message = 'Need to specify a FASTA/Q, BAM, and output file.'
        output(message, args.verbosity, 0, fatal = True)
    else:
        if args.verify:
            output('Verifying: ' + args.fastaq, args.verbosity, 1,\
                   log_file = args.log_file)
            verify_file(args.fastaq[0], log_file = args.log_file)
            output(args.fastaq[0] + ' is valid', args.verbosity, 1,\
                   log_file = args.log_file)
            output('Verifying: ' + args.bam[0], args.verbosity, 1,\
                   log_file = args.log_file)
            verify_file(args.bam[0] + ' is valid', log_file = args.log_file)
            output(args.bam[0], args.verbosity, 1,\
                   log_file = args.log_file)
        output('Generating FASTR file: ' + args.output, args.verbosity, 1,\
               log_file = args.log_file)
        generate_output(args.fastaq[0], args.bam[0],\
                       args.fastaq[1], args.bam[1], args.output)
        output(args.output + '.fastr generated successfully.', args.verbosity,\
               2, log_file = args.log_file)
    output('Exiting generate__fastr.py', args.verbosity, 1,\
           log_file = args.log_file)    
    sys.exit(0)
