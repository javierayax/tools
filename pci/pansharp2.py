#-------------------------------------------------------------------------------
# Name:        pansharp
# Purpose:
#
# Author:      jescudero
#
# Created:     16/01/2017
# Copyright:   (c) 80797366 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
from pci.pansharp2 import pansharp2

inputImgMS = arcpy.GetParameterAsText(0)
inputImgPan = arcpy.GetParameterAsText(1)
outImgPS = arcpy.GetParameterAsText(2)

pansharp2(inputImgMS, [] ,[], inputImgPan, outImgPS, [], "", "", "", "", "")