import numpy as np
import scipy as sp
from numpy.random import random
import math
class SoReg(object):
    def __init__(self):
        pass
    @staticmethod
    def buildmodel(trainset=None,relation=list()):
        ui = {}
        vj = {}
        number_factor = 10
        number_iterration = 50
        user_item = {}
        item_user = {}
        for line in trainset:
            if not ui.has_key(line[0]):
                ui.setdefault(line[0],random((10,1)))
            if not vj.has_key(line[1]):
                vj.setdefault(line[1],random((10,1)))
        for line in trainset:
            if not user_item.has_key(line[0]):
                user_item[line[0]]={}
                user_item[line[0]][line[1]]=line[2]
            else:
                user_item[line[0]][line[1]]=line[2]
            if not item_user.has_key(line[1]):
                item_user[line[1]]={}
                item_user[line[1]][line[0]]=line[2]
            else:
                item_user[line[1]][line[0]]=line[2]
        user_relation = {}
        for line in relation:
                user_relation[line[0]]=line[1]

        #calculate the similarity
        avg = 0
        user_item_avg = {}
        for user in user_item:
            for item in user_item[user]:
                avg+=user_item[user][item]
            user_item_avg[user]=float(avg/len(user_item[user]))
            avg = 0
        user_relation_item = {}
        for user in user_relation:
            if user_item.has_key(user):
                for item in user_item[user]:
                    if user_item.has_key(user_relation[user]):
                        if user_item[user_relation[user]].has_key(item):
                            if user_relation_item.has_key(user):
                                if user_relation_item[user][user_relation[user]]:
                                    user_relation_item[user][user_relation[user]].append(int(item))
                                else:
                                    user_relation_item[user][user_relation[user]]=[]
                                    user_relation_item[user][user_relation[user]].append(int(item))
                            else:
                                user_relation_item[user]={}
                                user_relation_item[user][user_relation[user]]=[]
                                user_relation_item[user][user_relation[user]].append(int(item))
        sim = 0
        sim_relation = 0
        sim_user = 0
        user_relation_sim = {}
        for user in user_relation_item:
            for relation_user in user_relation_item[user]:
                for i in xrange(len(user_relation_item[user][relation_user])-1):
                    sim+=float(user_item[relation_user][str(user_relation_item[user][relation_user][i])]-user_item_avg[relation_user])*float(user_item[user][str(user_relation_item[user][relation_user][i])]-user_item_avg[user])
                    sim_relation+=float(user_item[relation_user][str(user_relation_item[user][relation_user][i])]-user_item_avg[relation_user])**2
                    sim_user+=float(user_item[user][str(user_relation_item[user][relation_user][i])]-user_item_avg[user])**2
            sim=float(sim)/float(math.sqrt(sim_relation)*math.sqrt(sim_user))
            user_relation_sim[user]={}
            user_relation_sim[user][relation_user]=sim
            sim = 0
        #calculate the the square of the ranking
        gamma = 0.001
        lamb=0.02
        number_iterration = 50
        rate = 0
        error = 0
        for i in xrange(2):
            for user in user_item:
                for item in user_item[user]:
                    rate = np.sum(ui[user]*vj[item])
                    error = user_item[user][item]-rate
                    #print error
                    if error:
                        if user_relation_item.has_key(user):
                            for relation_user in user_relation_item[user]:
                                if int(item) in user_relation_item[user][relation_user]:
                                    sim += user_relation_sim[user][relation_user]
                    #print sim
                        ui[user]+=gamma*(error*vj[item]-lamb*ui[user]+lamb*sim)
                    #print ui[user]
                        vj[item]+=gamma*(error*ui[user]-lamb*vj[item])
                    #print vj[item]
                        gamma=gamma*0.9
                    sim=0
            
        print 'done the train'
        return ui,vj,user_item_avg
    @staticmethod
    def pred(testdata,ui,vj,user_item_avg):
        rat = 0
        pred_item_rat = {}
        for line in testdata:
            if pred_item_rat.has_key(line[0]):
                if ui.has_key(line[0]) and vj.has_key(line[1]):
                    rat = np.sum(ui[line[0]]*vj[line[1]])
                else:
                    if user_item_avg.has_key(line[0]):
                        rat = user_item_avg[line[0]]
                    else:
                        rat = 3
                pred_item_rat[line[0]][line[1]]=rat
            else:
                if ui.has_key(line[0]) and vj.has_key(line[1]):
                    rat = np.sum(ui[line[0]]*vj[line[1]])
                else:
                    if user_item_avg.has_key(line[0]):
                        rat = user_item_avg[line[0]]
                    else:
                        rat = 3
                pred_item_rat[line[0]]={}
                pred_item_rat[line[0]][line[1]]=rat
        T = len(testdata)
        eru = 0
        for line in testdata:
            eru+=math.sqrt((line[2]-pred_item_rat[line[0]][line[1]])**2)
        eru = float(eru/T)
        print eru





























































