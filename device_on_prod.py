from asyncio.log import logger
from itsdangerous import json
from requests import post
import paho.mqtt.client as paho
import requests
from paho import mqtt
import time

def publisMessage(client, msg, topic):
    time.sleep(1) 
    client.publish(topic, payload= msg, qos=2)
    print("Mensagem publicada no tópico: " + topic + " : " + msg)

def newRequestRecived(client, msgRecived, topic):

    if (msgRecived == "30"):
        publisMessage(client, "9", topic+"Alive")
    elif (msgRecived == "11"): 
        print("Acionando dispositivo: " + topic)
    elif (msgRecived == "10"):
        print("Desligando dispositivo: " + topic)
    else: 
        print("Não soube tratar a mensagem recebida: " + msgRecived)
        

def initializeMqtt(deviceName):
    def on_connect(client, userdata, flags, rc, properties=None):
        print("CONNACK recebido, código %s." % rc)

    def on_message(client, userdata, msg):
        print("Recebendo mensagem no tópico: " +  msg.topic + " ---> " + "Mesangem: " + str(msg.payload.decode()))
        newRequestRecived(client, str(msg.payload.decode()), deviceName)

    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.on_connect = on_connect

    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set("juninhocb", "palmeiras")
    client.connect("11ecd64be4a14dd0b10818f3c750d86b.s2.eu.hivemq.cloud", 8883)
    
    client.on_message = on_message

    client.subscribe(deviceName, qos=2)
    print("Inscrito no tópico: "+ deviceName)
    
    client.loop_forever()

def sendPostToServer(deviceName):
    headers = {'Content-type': 'application/json'}
    print("\n")

    try:
        response = requests.post(url= "https://server4iot.herokuapp.com/devices/jose", data = "{\"name\": \"%s\" ,\"type\": 1}" % deviceName, headers = headers)
        if (response.status_code == 201):
            print("Dispositivo criado com sucesso! *Ou reconectado, Código: %d" % response.status_code)
            initializeMqtt(deviceName)
        print("Dispositivo não conectado, código da requisição: " + str(response.status_code))
    except Exception as e: 
        logger.error("Excessão causada pelo motivo: " + str(e))
        

def main(): 
    device = input("Nome do Dispositivo para se conectar: ")
    print("Ok, dispositivo: " + device + " será instanciado!")
    sendPostToServer(device)


if __name__ == '__main__':
   main()



