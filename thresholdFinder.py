from fuzzywuzzy import fuzz
import difflib
import heapq


# test class!

def extractLines(input):
    inputFile = open(input, "r", encoding="utf8")
    return set(inputFile)


# TODO sort files and compare only adjacent lines!
def getThreshlold(lines):
    threshold = 1
    matcher = difflib.SequenceMatcher()
    # min_len = sum(len(s) for s in heapq.nsmallest(2, lines, key=len))
    while lines.__len__() > 1:
        line1 = lines.pop()
        for line2 in lines:
            # threshold = min(1 - fuzz.ratio(line1, line2) / fuzzLen, threshold)
            matcher.set_seqs(line1, line2)
            threshold = min(1 - 2 * matcher.find_longest_match(0, len(line1), 0, len(line2)).size / len(line1 + line2), threshold) #0.018587360594795488 0.05797101449275366
            # threshold = min(1 - 2 * matcher.find_longest_match(0, len(line1), 0, len(line2)).size / min_len, threshold)
    return threshold


th1 = getThreshlold(extractLines("input/elib.txt"))
th2 = getThreshlold(extractLines("input/sch.txt"))
print(th1, th2)

maxTreshold = min(th1, th2)
print(maxTreshold)
