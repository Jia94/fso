#!/usr/bin/env python
""" This is the job control script"""

# Import modules
from ftplib   import FTP
from datetime import datetime, timedelta
from string import ascii_uppercase
import imp
try:
    imp.find_module('pandas')
    pd_found = True
    import pandas as pd
except ImportError:
    pd_found = False
import time
try:
    import numpy as np
    np_found = True
except ImportError:
    np_found = False
import os
import shutil
import sys

FSO_HOME='/home/zwtd/FSO'

os.chdir(FSO_HOME)

CURR_DATE=2018101600

###STEP1 Check gfs###

os.system(singularity exec -e -B china_FSO:/FSO3.4 -B china_working:/gjx_working -B china_static:/gjx_static -B /home/data/raw/gfs:/gfs fso3.simg ./scripts/wrf_check_gfs.py)
 
###STEP2 check obs###

os.system(singularity exec -e -B china_FSO:/FSO3.4 -B china_working:/gjx_working -B china_static:/gjx_static -B /data1/input/little_r:/little_r fso3.simg ./scripts/wrf_obsproc.py)

###STEp3 RUN WPS ###

os.system(singularity exec -e -B china_FSO:/FSO3.4 -B china_working:/gjx_working -B china_static:/gjx_static -B /home/data/raw/gfs:/gfs fso3.simg ./scripts/wrf_wps.py)