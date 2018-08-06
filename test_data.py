import lib_paths

import dataplumbing as dp
import numpy as np
import tensorflow as tf

from model import *

##########################################################################################
# Data
##########################################################################################

# Load data
#
path_file = 'CMV_TCR_data_min10k_min10reads_shuffled_100k.tab'
samples = dp.load_repertoires(path_file)
xs, cs, ys = dp.process_repertoires(samples, snip_size=6)

print(xs.shape)
print(cs.shape)
print(ys.shape)

