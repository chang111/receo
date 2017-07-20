import os.path
from os import makedirs,remove
from re import compile,findall,split
class FileIO(object):
    def __init__(self):
        pass
    @staticmethod
    def writeFile(dir,file,content,op = 'w'):
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(dir+file,op) as f:
            f.writelines(content)

    @staticmethod
    def deleteFile(filePath):
        if os.path.exists(filePath):
            remove(filePath)
    @staticmethod
    def loadDataSet(conf, file,bTest):
        trainingData = []
        testData = []
        with open(file) as f:
            ratings = f.readlines()
        for lineNo, line in enumerate(ratings):
            items = split(' |,|\t', line.strip())
            try:
                userId = items[0]
                itemId = items[1]
                rating  = items[2]
            except ValueError:
                print 'Error! Have you added the option -header to the rating.setup?'
                exit(-1)
            if not bTest:
                trainingData.append([userId, itemId, float(rating)])
            else:
                testData.append([userId, itemId, float(rating)])
        if not bTest:
            return trainingData
        else:
            return testData

    @staticmethod
    def loadRelationship(conf, filePath):
        relation = []
        with open(filePath) as f:
            relations = f.readlines()
            # ignore the headline
        # order of the columns
        for lineNo, line in enumerate(relations):
            items = split(' |,|\t', line.strip())
            userId1 = items[0]
            userId2 = items[1]
            relation.append([userId1, userId2])
        return relation




