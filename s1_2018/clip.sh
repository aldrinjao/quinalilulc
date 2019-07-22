#!/bin/bash
# Basic while loop
counter=1
while [ $counter -le 31 ]
do

    gdalwarp -of GTiff -cutline /home/sarai/Desktop/RS/albay/extent.shp -crop_to_cutline ./reprojected/$counter.tif ./clipped/$counter.tif
    # gdalwarp -t_srs EPSG:4326 -r near -of GTiff ./raw/$counter.tif ./reprojected/$counter.tif
    ((counter++))
done
echo All done