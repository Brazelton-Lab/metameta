from metameta_utilities import *
import re

class VerifyFile():
    '''To verify files'''

    def __init__(self, in_file, log_file = None):
        self.inFile = in_file
        self.logFile = log_file

    def verify(self, regex_string, delimiter):
        for entry in entry_generator(self.inFile, logFile):
            wholeEntry = '\n'.join(entry) + '\n'
            matches = re.findall(regex_string, wholeEntry)
            if len(matches) != 1:
                splitRegex = regexString[1:-1].split(delimiter)
                splitEntry = wholeEntry.split(delimiter)
            for regex, entry in zip(splitRegex[:-1], splitEntry[:-1]):
                if not regex.startswith('^'):
                        regex = '^' + regex
                if not regex.endswith('$'):
                    regex += '$'
                splitMatches = re.match(regex, entry)
                    if len(splitMatches) != 1:
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

        def fasta(self):
            regexString = r'^>.+\n[ACGTURYKMSWBDHVNX]+\n$'
            delimiter = r'\n'
            return self.verify(regexString, delimiter)

        def fastq(self):
            regexString = r'^@.+\n[ACGTURYKMSWBDHVNX]+\n\+.*\n.+\n$'
            delimiter = r'\n'
            return self.verify(regexString, delimiter)

        def fastr(self):
            regexString = r'^\+.+\n[\dx-]*\d\n$'
            delimiter = r'\n'
            return self.verify(regexString, delimiter)

        def gff3(self):
            regexString = r'^[a-zA-Z0-9.:^*$@!+_?-|]+\t.+\t.+\t\d+\t\d+\t'\
                          + r'\d+\.?\d*\t[+-.]\t[0-2]\t.*\n$'
            delimiter = r'\t'
            return self.verify(regexString, delimiter)

        def sam(self):
            regexString = r'^[!-?A-~]{1,255}\t'\
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
            return self.verify(regexString, delimiter)
