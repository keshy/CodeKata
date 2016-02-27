__author__ = 'shankar'


# Given a properties file (like in java spring)
# application.yarn.support=True
# application.yarn.resourceManager.protocol=https
# application.yarn.resourceManager.protocol.supportEnabled=True
# some.other.property=Value

# Note that some individual keys have the ability to have a value and also have a deeper node to support another sub key.
# like in lines 6 and 7 above
# Write a parser that would do lookUpByKey(key) and lookUpByKeyPrefix(prefix)


class PropertyParser:
    def __init__(self, file):
        self.file = file
        self.propertyMap = {}
        self.readFile()

    def readFile(self):
        f = open(self.file, 'r')
        for line in f.readlines():
            keyValue = line.strip().split("=")
            if len(keyValue) != 2:
                continue
            self.propertyMap[keyValue[0].strip()] = keyValue[1]

    def lookUpByKey(self, key):
        try:
            return self.propertyMap.get(key)
        except Exception as e:
            print "Key does not exist"
            return None

    def lookUpByKeyPrefix(self, prefix):
        if prefix is None:
            return None

        result = []
        keys = self.propertyMap.keys()
        for key in keys:
            if prefix == key[:len(prefix)]:
                result.append((key, self.propertyMap.get(key)))

        return result


if __name__ == "__main__":

    c = PropertyParser("../resource/application.properties")
    print ("Looking up by specific key")
    print ("%s" % c.lookUpByKey("log4j.appender.console.target"))
    print ("Look up by key prefix...")
    result = c.lookUpByKeyPrefix("log4j.appender")
    for k in result:
        print ("%s=%s" % (k[0],k[1]))





