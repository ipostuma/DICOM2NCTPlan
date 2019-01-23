import numpy as np
import pydicom as dicom
import argparse

parser = argparse.ArgumentParser(description='A simple script to extract ROI for NCTPlan.')
parser.add_argument('File', metavar='Image', type=str, nargs='+', help='please provide the PATH to the DicomImage file')
args = parser.parse_args()


image = dicom.dcmread(args.File[0])
Zmin = image.SliceLocation

for dcm in args.File:
    img = dicom.dcmread(dcm)
    if(Zmin > img.SliceLocation):
        Zmin = img.SliceLocation

print int(-1*Zmin)

