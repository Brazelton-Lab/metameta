#!/usr/bin/env python

'''generic bioinformatic functions

Usage:

    metameta_utilities.py <functions>

<functions> will give the help for that each function
listed (multiple functions can be specified).

This file simply contains a number of generic bioinformatic
related functions useful to many programs in metameta. It
is meant to be imported by other scripts. Functions that
perform tasks represntative of another tool will be contained
in that tool, e.g. all functions for writing FASTR files
are in generate_fastr.py

Functions:
    entry_generator
    file_type
    filter_by_size
    gff_dict
    output
    same_gene
    verify_file
'''

__version__ = '0.0.0.13'

import argparse
import re
import string
import sys

def filter_by_size(unfiltered_list, tuple_pos = None, min_length = None,\
                   max_length = None, log_file = None):
    '''Filters a list of lists, or tuples, by size

    Input:

        unfiltered_list:
                A list of lists or tuples to be filtered by size.

        tuplePos:
                If unfiltered_list is a list of tuples, or there is a list,
                withing the each list, this argument
                specifies which item of the tuple contains the list
                to sort by length. Default is None.

        min_length:
                The minimum length a list must be to pass filtering.
                Default is None.

        max_length:
                The maximum length a list must be to pass filtering.
                Default is None.

        log_file:
                A log file to write output to. Defaults to None, which writes
                to stdout.

    Output:

        Returns the tuple (shortLists, idealLists, longLists)

        shortLists:
                A list of the lists or tuples with length less than min_length.

        idealLists:
                A list of lists or tuples with length greater than or equal to
                min_length and less than or equal to max_length.

        longLists:
                A list of the lists or tuples with length greater than
                max_length.        
    '''
    
    shortLists = []
    idealLists = []
    longLists = []
    listsToFilter = []
    if tuple_pos != None:
        for subTuple in unfiltered_list:
            listsToFilter.append(subTuple[tuple_pos])
    else:
        for subList in unfiltered_list:
            listsToFilter.append(subList)
    position = 0
    for subList in listsToFilter:
        subLength = len(subList)
        if min_length != None and subLength < min_length:
            message = str(listsToFilter[position]) + ' in '\
                      + str(unfiltered_list[position])\
                      + ' is less than the minimum length of '\
                      + str(min_length)
            output(message, args.verbosity, 2, log_file = log_file)
            shortLists.append(unfiltered_list[position])
        elif max_length != None and subLength > max_length:
            message = str(listsToFilter[position]) + ' in '\
                      + str(unfiltered_list[position])\
                      + ' is greater than the maximum length of '\
                      + str(max_length)
            output(message, args.verbosity, 2, log_file = log_file)
            longLists.append(unfiltered_list[position])
        else:
            message = str(listsToFilter[position]) + ' in '\
                      + str(unfiltered_list[position])\
                      + ' is within the length parameters: '\
                      + 'minimum length = ' + str(min_length)\
                      + ' and maximum length = ' + str(max_length)
            output(message, args.verbosity, 2, log_file = log_file)
            idealLists.append(unfiltered_list[position])
        position += 1
    return (shortLists, idealLists, longLists)

def gff_dict(gff_file):
    '''Reads a GFF file into a dictionary

    Input:

        gff_file:
                The GFF3 file to be read.

    Output:

            A dictionary where each key is a contig header. Each value is a
            list of tuples where each tuple contains nine items corresponds
            to the nine columns in a GFF3 entry.
    '''

    from collections import defaultdict
    annotations = defaultdict(list)
    for entry in entry_generator(gff_file, 'gff3'):
        annotations[entry[0]].append(tuple(entry))
    return annotations

def same_gene(clusterStart, clusterEnd, gffStart, gffEnd):
    '''Determines if a cluster and annotation on a contig cover the same gene

    Input:

        clusterStart:
                The start of the cluster.

        clusterEnd:
                The end of the cluster.

        gffStart:
                The start of the GFF annotation.

        gffEnd:
                The end of the GFF annotation.

    Output:

            Boolean: True or False
    '''
    
    sameGene = False
    # Cluster encompasses GFF
    if clusterStart <= gffStart and clusterEnd >= gffEnd:
        sameGene = True
    # GFF encompasses Cluster
    elif clusterStart >= gffStart and clusterEnd <= gffEnd:
        sameGene = True
    # GFF overlaps clusters by at least 50%
    else:
        overlap = 0
        if clusterEnd > gffEnd and clusterStart > gffStart:
            overlap = gffEnd - clusterStart
        elif gffEnd > clusterEnd and gffStart > clusterStart:
            overlap = clusterEnd - gffStart
        overlapRatio = float(overlap)/float(clusterEnd - clusterStart)
        if overlapRatio >= 0.5:
            sameGene = True
    return sameGene
