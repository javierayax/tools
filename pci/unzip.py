#-------------------------------------------------------------------------------
# Name:        unzip
# Purpose:
#
# Author:      jescudero
#
# Created:     16/01/2017
# Copyright:   (c) 80797366 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, tarfile

inputFile = r"D:\SIIMA\test\images\LC80100582016325LGN00.tar.gz"

tar = tarfile.open(inputFile)
name = os.path.basename(inputFile).split(".")[0]
folder = os.path.dirname(inputFile)
outFolder = os.path.join(folder, name)
if not os.path.exists(outFolder):
    os.mkdir(outFolder)
tar.extractall(outFolder)
tar.close()
