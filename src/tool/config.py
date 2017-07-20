import os.path
class Config(object):
    def __init__(self,fileName):
        self.config = {}
        self.readConfiguration(fileName)
    def readConfiguration(self,fileName):
        path = fileName
        if not os.path.exists(path):
            print 'config file is not found!'
            raise IOError
        with open(path) as f:
            for ind,line in enumerate(f):
                if line.strip()<>'':
                    try:
                        key,value=line.strip().split('=')
                        self.config[key]=value
                    except ValueError:
                        print 'config file is not in the correct format! Error Line:%d'%(ind)
    def __getitem__(self, item):
        if not self.contains(item):
            print 'parameter '+item+' is invalid!'
            exit(-1)
        return self.config[item]
    def getOptions(self,item):
        if not self.contains(item):
            print 'parameter '+item+' is invalid!'
            exit(-1)
        return self.config[item]
    
    def contains(self,key):
        return self.config.has_key(key)


