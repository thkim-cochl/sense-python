# Copyright 2019 Cochlear.ai Ltd. All Rights Reserved.

import json
from common.sense import sense
import pprint
import time

apikey = 'Your API-key here'
filename = 'test_samples/event/filename.wav'
file_format = 'wav'
task = 'event'

result = sense(filename,apikey,file_format,task)
result = json.loads(result.outputs)
pprint.pprint(result)

