#-------------------------------------------------------------------------------
# Name:        import Img
# Purpose:
#
# Author:      jescudero
#
# Created:     16/01/2017
# Copyright:   (c) 80797366 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys
import tarfile
import fnmatch
import subprocess
import numpy as np

#librerias PCI
from pci.fimport import fimport
from pci.pansharp2 import *
from pci.api import gobs, datasource as ds
from pci.pcimod import pcimod
from pci.prx import *
from pci.model import model
from pci.sieve import *

#libreria ArcPy
#import arcpy
import arcpy
from arcpy.sa import *
from arcpy import env
env.overwriteOutput="True"