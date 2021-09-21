import json
import requests
import boto3
import time
im

def lambda_handler(event, context):
    ssm = boto3.client('ssm')
    urlApagado = ssm.get_parameter(Name='cuby-urlApagado', WithDecryption=True)
    print('FIRST TRY: Starting Lambda')

    while True :
        try:
            ip = requests.get(urlApagado["Parameter"]["Value"])
            if ip.status_code == 200 :
                print(ip.text)
                resultJsonDict = json.loads(ip.text)
                if resultJsonDict["status"] == "ok" :
                    print("Shutdown command sent successfully")
                    break
                else :
                    print("http ok but command fail, gonna try again")
            else :
                print("Status Code: " + str(ip.status_code) + ", Additional Data: " + ip.text)
        except requests.RequestException as e:
            print("Failed http")
            continue
    