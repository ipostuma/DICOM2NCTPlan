# INCIPIT
This directory contains scripts that help to convert DICOM images to a format which is good for NCTPlan.

## HOW TO USE THESE SCRIPTS
The most important scripts are the ones that create the tiff images and the ROI data: *CreateStack.sh* and *getROI.sh*.

### CreateStack.sh usage
```
$ bash CreateStack.sh ALL_THE_DICOM_FILES #to create the image stack
```

The parameter you need to give the the bash script is the base name of the dicom files images followed by a \*.

### getROI.sh usage

```
$ bash getROI.sh DICOM_FILES_BASE_NAME RTSTRUCT_FILE
```

DICOM\_FILES\_BASE\_NAME is the common part of the dicom file names, RTSTRUCT\_FILE has to be the path to the RTSTRUCT file.
