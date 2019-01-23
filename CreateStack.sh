MAX=`python info_pixel_max.py $*`
off=`python info_z_min.py $*`
for i in $* #232
do
    python CropDICOM.py $i $MAX $off
done
