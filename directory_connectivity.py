import os
import sys

curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(curr_dir,'..','passion-backend'))

import aiprediction

prediction = aiprediction.aiprediction()
prediction.pred("1010100110101001101010011010100121010100121010100110101001101010012")
