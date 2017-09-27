import re
from fuzzywuzzy import fuzz
import difflib

class comparator:

    matcher = difflib.SequenceMatcher()
    sch_map = {}
    elib_map = {}

    #construct comparator
    def __init__(self):
        self.editFiles('input/elib.txt', False)
        self.editFiles('input/sch.txt', True)

    #True if str1 and str2 is similar, False otherwise
    #TODO find good threshold (use difflib?)
    def isSimilar(self, str1, str2):
        # self.matcher.set_seqs(str1, str2)
        # return (1 - 2 * self.matcher.ratio() / (len(str1) + len(str2))) >= 0.9997884297520662
        return fuzz.ratio(str1, str2) > 92

    #true if str in set, false otherwise
    def inAnotherSet(self, str, set):
        for elem in set:
            if self.isSimilar(str, elem):
                return True
        return False

    #elements from set1 which are not in set2
    def similarSet(self, set1, set2):
        result = set()
        for elem1 in set1:
            if self.inAnotherSet(elem1, set2):
                continue
            else:
                result.add(elem1)
        return result

    #sort records in result file by name
    def sortRes(self, filename):
        with open(filename, 'r', encoding="utf8") as result:
            lines = result.readlines()
            lines.sort()
        with open(filename, 'w', encoding="utf8") as result:
            for line in lines:
                result.write(line)


    # difference in files based on Levenstein distance
    def diff(self, file_one, file_two):
        with open(file_one, 'r', encoding="utf8") as text_one, open(file_two, 'r', encoding="utf8") as text_two:
            return self.similarSet(set(text_one), set(text_two))
            # return set(text_one) ^ set(text_two)


    #delete all not words and digits and capitalize each string. flag = true <=> sch, false <=> elib
    def editFiles(self, filename, flag):
        books = {}
        with open(filename, 'r', encoding="utf8") as file:
            lines = file.readlines()
        with open(filename, 'w', encoding="utf8") as file:
            for line in lines:
                tmp = line
                line = line.capitalize()
                line = re.sub(r'[\W_]+', " ", line)
                #matching of the raw record with the processed
                books[line] = tmp
                file.write(line + '\n')
        if flag:
            self.sch_map = books
        else:
            self.elib_map = books



