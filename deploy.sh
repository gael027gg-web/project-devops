#!/bin/bash

COMANDO=$1
INSTANCE=$2
DIRECTORIO=$3
BUCKET=$4

python3 ec2/gestionar_ec2.py $COMANDO $INSTANCE

bash s3/backup_s3.sh $DIRECTORIO $BUCKET
