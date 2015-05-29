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
from metameta_utils.output import output
