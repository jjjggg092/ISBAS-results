#!/bin/bash
if [[ $# -lt 1 ]]; then
        echo usage: $0 grdfile
fi

grdfile=$1
grdbase=$(basename $grdfile .grd)
minz=$2
maxz=$3
zinc=$4
gmt makecpt -Cjet -D -Z -T$minz/$maxz/$zinc > mycpt.cpt
grd2kml.csh $grdbase mycpt.cpt
