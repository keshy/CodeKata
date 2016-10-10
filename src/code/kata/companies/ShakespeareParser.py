import operator

def getCountForText(textString, file):


    f = open(file, "r")

    text = f.read()
    words = text.split()

    count = 0
    for word in words:
        if word.lower() == textString.lower():
            count += 1

    return count

def getNMostFrequentlyOccuringWords(n, file):

    f = open(file, "r")
    wordCount = {}

    text = f.read()
    words = text.split()

    for word in words:
            if word in wordCount:
                wordCount[word] = wordCount.get(word) + 1
            else:
                # add word into map
                wordCount[word] = 1

    # sort dictionary by value
    sortedDict = sorted(wordCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedDict[:n]


def getNMostCommonBigrams(n, file):
    f = open(file, "r")
    bigramCount = {}

    text = f.read()
    words = text.split()

    if len(words) < 2:
        return None

    bigrams = []
    i = 0
    while i < len(words):
        bigrams.append(" ".join(words[i:i+2]))
        i += 1

    for word in bigrams:
            if word in bigramCount:
                bigramCount[word] = bigramCount.get(word) + 1
            else:
                # add word into map
                bigramCount[word] = 1

    # sort dictionary by value
    sortedDict = sorted(bigramCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedDict[:n]

if __name__ == "__main__":
    print ("Count of %s appearing in file = %s" % ("shakespeare", getCountForText("shakespeare", "../resource/test_file")))
    print ("Top %s frequent words in file = %s " % (10, getNMostFrequentlyOccuringWords(10, "../resource/test_file")))
    print ("Top %s frequent bigrams in file = %s " % (10, getNMostCommonBigrams(10, "../resource/test_file")))
