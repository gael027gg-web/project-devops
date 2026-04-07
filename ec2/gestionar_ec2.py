import boto3
import sys

ec2 = boto3.client('ec2')

def listar():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'], instance['State']['Name'])

def iniciar(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print("Instancia iniciada")

def detener(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print("Instancia detenida")

def terminar(instance_id):
    ec2.terminate_instances(InstanceIds=[instance_id])
    print("Instancia terminada")

if __name__ == "__main__":
    comando = sys.argv[1]

    if comando == "listar":
        listar()

    elif comando == "iniciar":
        iniciar(sys.argv[2])

    elif comando == "detener":
        detener(sys.argv[2])

    elif comando == "terminar":
        terminar(sys.argv[2])
