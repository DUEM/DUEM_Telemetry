#!/bin/bash


cd /home/pi/DUEM_Telemetry/
source .telem/bin/activate

uwsgi --http --ini uwsgi.ini    
