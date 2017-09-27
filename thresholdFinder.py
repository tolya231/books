from fuzzywuzzy import fuzz
import difflib
import heapq
#test class!

def extractLines(input):
    inputFile = open(input, "r", encoding="utf8")
    return inputFile.readlines()


def getThreshlold(lines):
    threshold = 0
    matcher = difflib.SequenceMatcher()
    # maxLen = len(max(lines))
    maxList = maxLen = sum(len(s) for s in heapq.nlargest(2, lines, key=len))
    for line1 in lines:
        for line2 in lines:
            #if ratio = 100 then for different lines result will be incorrect (100/
            # threshold = max(1 - fuzz.ratio(line1, line2) / maxLen, threshold)
            matcher.set_seq1(line1)
            matcher.set_seq2(line2)
            # threshold = max(1 - 2 * matcher.ratio() / (len(line1) + len(line2)), threshold)
            threshold = max(1 - 2 * matcher.ratio() / maxLen, threshold)
    return threshold


th1 = getThreshlold(extractLines("input/elib.txt"))
th2 = getThreshlold(extractLines("input/sch.txt"))
print(th1, th2)

maxTreshold = max(th1, th2)
print(maxTreshold)
