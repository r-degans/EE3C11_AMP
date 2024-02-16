#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:33:20 2023

@author: anton
"""

from SLiCAP import *

prj = initProject("Hearing Loop")

from applicationDescription import *
from specifications import *
from measurementData import *
from coupledCoilsSimple import *
from coupledCoils import *