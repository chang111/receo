import sys
sys.path.append("..")
from tool.config import Config
from tool.file import FileIO
from algorithm.SoReg import SoReg

if __name__ == '__main__':

    print'='*80
    print'this is the algorithm of the test'
    algor = -1
    conf = -1
    conf = Config('../conf/SoReg.conf')
    trainset = []
    testset = []
    relation = []
    ui={}
    vj={}
    user_item_avg={}
    trainset = FileIO.loadDataSet(conf,conf['ratings'],bTest=False)
    testset =   FileIO.loadDataSet(conf,conf['testset'],bTest=True)
    relation = FileIO.loadRelationship(conf,conf['social'])
    ui,vj,user_item_avg=SoReg.buildmodel(trainset,relation)
    SoReg.pred(testset,ui,vj,user_item_avg)
#sotre the data
