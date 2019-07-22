#!/bin/bash
# Basic while loop
counter=1
while [ $counter -le 31 ]
do
    gdalwarp -t_srs EPSG:4326 -r near -of GTiff $counter.tif ./reprojected/$counter.tif
    ((counter++))
done
echo All done