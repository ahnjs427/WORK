#!/usr/bin/env python

import tractor.api.query as tq
import os
from pprint import pprint

jobs = tq.jobs("active or ready")
pprint (jobs)



   
