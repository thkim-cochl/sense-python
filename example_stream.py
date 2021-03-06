# Copyright 2019 Cochlear.ai Ltd. All Rights Reserved.

import json
import pprint

from common.sense import SenseStreamer
from common.sense import sense_stream_request
from common.sense import sense_stream_response

apikey = 'Your API-key here'
task = 'event'

with SenseStreamer(task) as stream:
    audio_generator = stream.generator()
    requests = sense_stream_request(audio_generator,apikey,task)
    responses = sense_stream_response(requests)
    
    for i in responses:
        pprint.pprint(i.outputs)