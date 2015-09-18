#! /usr/bin/env python

"""filters GFF3 file by coverage values

Usage:

    filter_gff3.py [--delimiter] [--greater_than] [--less_than]
                   <gff3> <coverage_file>  <coverage_threshold> <output>

Synopsis:

    Creates a new GFF3 file containing only annotations greater than or less
    than a given threshold value.

Required Arguments:

    gff3_file           GFF3 formatted annotation file
    coverage_file       TSV file generated by compute_gene_abundance.py
    coverage_threshold  threshold for acceptable coverage values
    output              name of output GFF3 file

Optional Arguments:

    delimiter           character that delimits the CSV file [Default: '\t']
    greater_than        specifies that all coverages greater than
                        coverage_threshold should be written to output
    less_than           specifies that all coverages less than
                        coverage_threshold should be written to output
    Note: either greater_than OR less_than MUST be specified
"""

from __future__ import print_function

__version__ = '0.0.0.1'