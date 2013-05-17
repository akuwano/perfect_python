#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

# pickle
def save_task(task, file):
    pickle.dump(task, file)

def load_task(file):
    return pickle.load(file)

f = open('./pickletest.dat', 'wb')
taskdata = ['test', 'aaaaa', 0, 100]
print(pickle.dumps(taskdata))
#pickle.dump(taskdata, f)
save_task(taskdata, f)
f.close()
f = open('./pickletest.dat', 'rb')
print(load_task(f))
f.close()
