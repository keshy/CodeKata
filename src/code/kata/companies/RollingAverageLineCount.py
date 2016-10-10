__author__ = 'shankar'

import os

def getAverageLineCountForFolder(folderPath):

    files = os.listdir(folderPath)

    totalCount = 0.0
    lineCount = 0.0

    for file in files:
        print ("Opening file : %s" % file)
        f = open('%s/%s' % (folderPath, file) , 'r')
        for line in f.readlines():

            totalCount += len(line.strip())
            lineCount += 1

    return (totalCount/lineCount)

if __name__ == "__main__":

    print ("Rolling average for files in folder %s = %s " % ('../resource/test', getAverageLineCountForFolder('../resource/test')))










