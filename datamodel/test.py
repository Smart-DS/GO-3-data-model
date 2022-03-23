#import Bid-DS-data-model.datamodel.input.data.InputDataFile
import datamodel.base
import datamodel.input.static
import datamodel.input.timeseries
import datamodel.input.data as data
from datamodel.base import *
import os

path = '../input/json_data/'
json_file = os.path.join(path,'PSY_RTS_GMLC_data.json')
json_file = os.path.join(path,'PSY_RTS_GMLC_data_fixed_load_commit.json')
json_file = os.path.join(path,'PSY_RTS_GMLC_data_fixed_load_commit_v3_output.json')
test = data.InputDataFile.load(json_file)
print('Succeeded!')

