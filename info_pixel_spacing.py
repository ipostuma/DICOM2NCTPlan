import pydicom as dicom
import argparse

parser = argparse.ArgumentParser(description='A simple script to extract ROI for NCTPlan.')
parser.add_argument('File', metavar='Image', type=str, nargs='+', help='please provide the PATH to the DicomImage file')
args = parser.parse_args()

image = dicom.dcmread(args.File[0])
   
print image.PixelSpacing[0]," ",image.PixelSpacing[1]
