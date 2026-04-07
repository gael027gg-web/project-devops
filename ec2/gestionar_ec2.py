import boto3
import sys
from botocore.exceptions import ClientError

# Especificamos la región para evitar el NoRegionError
REGION = 'us-east-1'

try:
    ec2 = boto3.client('ec2', region_name=REGION)
except Exception as e:
    print(f"Error al conectar con AWS: {e}")
    sys.exit(1)

def listar():
    """Lista todas las instancias y su estado actual."""
    print(f"--- Listando instancias en {REGION} ---")
    try:
        response = ec2.describe_instances()
        found = False
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']} | Estado: {instance['State']['Name']}")
                found = True
        if not found:
            print("No se encontraron instancias en esta región.")
    except ClientError as e:
        print(f"Error de AWS: {e}")

def gestionar_instancia(accion, instance_id):
    """Maneja el inicio, detención y terminación de una instancia."""
    try:
        if accion == "iniciar":
            ec2.start_instances(InstanceIds=[instance_id])
            print(f"✅ Orden enviada: Iniciando instancia {instance_id}")
        elif accion == "detener":
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"✅ Orden enviada: Deteniendo instancia {instance_id}")
        elif accion == "terminar":
            ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"⚠️ Orden enviada: Terminando (eliminando) instancia {instance_id}")
    except ClientError as e:
        print(f"❌ Error al ejecutar '{accion}': {e}")

if __name__ == "__main__":
    # Verificación de seguridad de argumentos
    if len(sys.argv) < 2:
        print("Uso: python3 gestionar_ec2.py <listar|iniciar|detener|terminar> [instance_id]")
        sys.exit(1)

    comando = sys.argv[1].lower()

    if comando == "listar":
        listar()
    elif comando in ["iniciar", "detener", "terminar"]:
        if len(sys.argv) < 3:
            print(f"Error: El comando '{comando}' requiere un ID de instancia.")
        else:
            gestionar_instancia(comando, sys.argv[2])
    else:
        print(f"Comando '{comando}' no reconocido.")
