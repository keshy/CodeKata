__author__ = 'shankar'

import json
import argparse
from datetime import datetime


class Pruner:
    def __init__(self, inputFile, outputFileName):
        self.inputFile = inputFile
        self.outputFile = outputFileName
        self.prunedDict = {}

    def pruneFile(self):
        # get all unique device IDs.

        with open(self.inputFile, 'r') as f:
            for line in f.readlines():
                try:
                    jsonLine = json.loads(line)
                    # remove timestamp to store as key.
                    # the key in the dict can then be used to match further lines to do de-duplication

                    del(jsonLine['timestamp'])
                    del(jsonLine['devicestatus']['timestamp'])
                    try:
                        del(jsonLine['threat']['timestamp'])
                    except KeyError as e:
                        pass

                    self.prunedDict[json.dumps(jsonLine)] = line
                except Exception as e:
                    print ("Encountered error: %s" % e)
                    continue
        f.close()
        print ("Got %s events of unique set of devices" % len(self.prunedDict))

        if len(self.prunedDict) != 0:
            outputFile = open(self.outputFile, "w")
            for (k, v) in self.prunedDict.iteritems():
                outputFile.write("%s" % v)

            print ("Wrote all processed records to file")
            outputFile.close()
        return len(self.prunedDict)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Prune raw hdfs logs')
    parser.add_argument('-i', '--inputFile', type=str, required=True,
                        help='an integer for the accumulator')
    parser.add_argument('-o', '--output', type=str,
                        default="pruned_%s",
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    p = Pruner(args.inputFile, args.output)
    start = datetime.now()
    size = p.pruneFile()
    end = datetime.now()

    print "Job complete - time taken for %s events = %s seconds" % (size, (end-start).seconds)
