#!/usr/bin/env python

'''General function for analyzing lines against a regex'''

__version__ '0.0.0.1'

from metameta_utils.output import output

def verify_lines(lines, regex, delimiter):
    '''checks each line against regex for validity

    If a line does not match the regex, the line and regex
    are broken down by the delimiter and each segmetn is analyzed
    to produce and accurate error message.
    '''
    
    cRegex = re.compile(regex)
    for line in lines:
        match = re.match(cRegex, line)
        if not match:
            splitRegex = regex.split(delimiter)
            splitLine = line.split(delimiter)
            for regexSegment, lineSegment in zip(splitRegex, splitLine):
                if not regexSegment.startswith('^'):
                    regexSegment = '^' + regex
                if not regexSegment.endswith('$'):
                    regexSegment += '$'
                cRegexSegment = re.compile(regexSegment)
                matchSegment = re.match(cRegexStatement, lineSegment)
                if not matchSegment:
                    message = 'The following line:\n\n' + entry + '\n'\
                                  + 'Does not match the regular expression:\n'\
                                  + '\n' + regex + '\n'\
                                  + 'See https://docs.python.org/3.4/'\
                                  + 'library/re.html for information '\
                                  + 'on how to interpret regular expressions.'\
                                  + '\nThe entire entry containing the error'\
                                  + ' follows:\n\n' + wholeEntry + '\n'
                        try:
                            output(message, 1, 1, log_file = logFile)
                        else:
                            print(message)
                        return False
    return True
