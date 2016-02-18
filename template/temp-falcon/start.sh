#!/bin/bash

set -e
LOGFILE=/home/lontong/www/example-project/example-project.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2
USER=ubuntu

# user/group to run as
cd /home/lontong/www/example-project
source /home/lontong/env/env-project/bin/activate
exec python apps.py
