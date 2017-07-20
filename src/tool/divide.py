test = []
train = []
with open('uir.index') as f:
    import random
    for line in f:
        if random.random()<0.4:
            test.append(line)
        else:
            train.append(line)

with open('testset3.txt','w') as f:
    f.writelines(test)
with open('trainset3.txt','w') as f:
    f.writelines(train)
