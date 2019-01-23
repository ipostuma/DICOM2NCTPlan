import pydicom as dicom
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser(description='A simple script to extract ROI for NCTPlan.')
parser.add_argument('File', metavar='RTSTRUCT_file', type=str, nargs=1, help='please provide the PATH to the RTSTRUCT file')
parser.add_argument('PX_x', metavar='PixelSpacingX', type=float, nargs=1, help='Provide the x pixel spacing.')
parser.add_argument('PX_y', metavar='PixelSpacingY', type=float, nargs=1, help='Provide the y pixel spacing.')
parser.add_argument('OFF_x', metavar='PixelSpacingX', type=float, nargs=1, help='Provide the x offset in mm.')
parser.add_argument('OFF_y', metavar='PixelSpacingY', type=float, nargs=1, help='Provide the y offset in mm.')
parser.add_argument('OFF_z', metavar='PixelSpacingY', type=float, nargs=1, help='Provide the z offset in mm.')
args = parser.parse_args()

roi = dicom.read_file(args.File[0])
ctrs = roi.ROIContourSequence

# create a dictionary
# {ROIName : [index,  ROINumber]}
ctrsName = roi.StructureSetROISequence
nameDict = {}
for i in range(len(ctrsName)):
    nameDict[ctrsName[i].ROIName] = [i,ctrsName[i].ROINumber]

def getContouData(sequence, filename):
    myfile = open(filename.replace(" ","_")+".txt",'w')
    myfile.write("# %13s %14s %14s\n"%("x","y","z"))
    for layer in sequence:
        #print layer.ContourNumber
        i=0
        #print ""
        for data in layer.ContourData:
            #if (i>0 and i%3==0):
            #    print ""
            if ((i+1)%3==0):
                myfile.write("%15.5f\n"%(data+args.OFF_z[0]))
            elif((i+2)%3==0):
                myfile.write("%15.5f"%(data-args.PX_y[0]*127+args.OFF_y[0]))
            else:
                myfile.write("%15.5f"%(data-args.PX_x[0]*127+args.OFF_x[0]))
            i+=1
    myfile.close()

        
for i in range(len(ctrsName)):
    ROI = ctrs[nameDict[ctrsName[i].ROIName][0]].ContourSequence
    getContouData(ROI,ctrsName[i].ROIName)
