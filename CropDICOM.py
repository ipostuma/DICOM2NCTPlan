import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt
import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser(description='A simple script to extract ROI for NCTPlan.')
parser.add_argument('File', metavar='Image'  , type=str, nargs='+', help='Please provide the PATH to the DicomImage file')
parser.add_argument('MAX' , metavar='maximum', type=int, nargs='+', help='Highest pixel value')
parser.add_argument('OFF_z', metavar='Zoffset', type=int, nargs='+', help='Provide the Z offset value of the stack in  mm.')
args = parser.parse_args()

image = dicom.read_file(args.File[0])
imageMax = image.LargestImagePixelValue
#print imageMax
#print dir(image)

# get all attributes and print them
#
#print dir(roi)
#for i in range(92):
#    print dir(image)[i]
#    if(dir(image)[i] != "PixelData"):
#        print getattr(image,dir(image)[i])
#    print ""
    
#print "xy offset"
#print image.ImagePositionPatient
#print ""
#print "xy pixel spacing"    
#print image.PixelSpacing
#myimage  = np.zeros((256,256))
CropImage = (image.pixel_array[126:382,126:382]*255/args.MAX[0]).astype('uint8')
#plt.imshow(CropImage, cmap=plt.cm.bone)
#plt.show()

#print CropImage

result = Image.fromarray(CropImage)
print image.SliceLocation," ",image.ImagePositionPatient
#print float(image.AcquisitionTime)*float(image.TableSpeed)
#print "Save img_%i.tiff"%(1+(int(image.SliceLocation)+136)/2)
result.save("img_%i.tiff"%(image.SliceLocation+args.OFF_z[0]))
