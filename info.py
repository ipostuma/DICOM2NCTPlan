import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description='A simple script to extract ROI for NCTPlan.')
parser.add_argument('File', metavar='Image', type=str, nargs='+', help='please provide the PATH to the DicomImage file')
args = parser.parse_args()

image = dicom.dcmread(args.File[0])

print "xy offset"
print image.ImagePositionPatient
print ""
print "xy pixel spacing"    
print image.PixelSpacing
