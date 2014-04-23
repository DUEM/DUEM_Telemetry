#!/bin/bash

source /root/DUEM_Telemetry/.telem/bin/activate

cd /root/DUEM_Telemetry/

uwsgi --http --ini uwsgi.ini    
