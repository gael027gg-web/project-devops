# Project DevOps - Automatización de Infraestructura AWS

Este proyecto implementa una solución de automatización para la gestión de instancias EC2 y la ejecución de respaldos en Amazon S3.

## Estructura del Repositorio
- ec2/gestionar_ec2.py: Script en Python (Boto3) para control de instancias.
- s3/backup_s3.sh: Script en Bash para compresión y carga a S3.
- config/config.env: Variables de entorno (ID de instancia y Bucket).
- deploy.sh: Orquestador principal del flujo.

## Cómo ejecutar
`./deploy.sh <comando> <instance_id> <directorio> <bucket>`

## Flujo DevOps Aplicado
1. Desarrollo de scripts automatizados.
2. Gestión de configuración mediante variables de entorno.
3. Control de versiones con estrategia de ramas (Feature, Develop, Master).
