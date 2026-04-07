#!/bin/bash

DIRECTORIO=$1
BUCKET=$2

FECHA=$(date +%Y%m%d)

ARCHIVO=backup_$FECHA.tar.gz

tar -czf $ARCHIVO $DIRECTORIO

aws s3 cp $ARCHIVO s3://$BUCKET/

echo "Backup enviado a S3"
