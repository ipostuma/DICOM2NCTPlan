Zoff=`python info_z_min.py $1*`
XYoff=`python info_xy_off.py $1*`
pxSP=`python info_pixel_spacing.py $1*`
RTSTRUCT=$2

python ExtractROI.py $RTSTRUCT $pxSP $XYoff $Zoff
