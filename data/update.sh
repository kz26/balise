#!/bin/bash
# A very simple database update script

files=( "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz" "http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz" "http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz" "http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNumv6.dat.gz" )

rm -f *.dat *.gz
for f in ${files[@]}
do
	wget "$f"
done
gunzip *.gz
