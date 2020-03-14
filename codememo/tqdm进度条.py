from tqdm import tqdm,trange
import time
import numpy as np
'''
for i in trange(100):
  time.sleep(0.1)
  pass
'''
list = np.arange(1,100,1)
for i in tqdm(list):
    i += 2
    time.sleep(0.1)