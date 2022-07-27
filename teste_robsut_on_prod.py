import requests
import time

def doTest(nameDevice, iteractions):
    headers = {'Content-type': 'application/json'}
    try:
        for i in range (int(iteractions)):
            response = requests.post(url= "https://server4iot.herokuapp.com/devices/jose", data = "{\"name\": \"%s\" ,\"type\": 1}" % nameDevice, headers = headers)
            print(response)
            if response.status_code == 201:
                print(f"Dispositivo {nameDevice} instânciado no servidor com sucesso!")
            else: 
                print("Falha ao conectar-se")

        time.sleep(1)

    except Exception as exception:
        print("\n Requisição sem sucesso \n")
        print(exception)

def main():
    for i in range (1, 11):
        doTest(f"LED {i}", 1)

if __name__ == "__main__":
    main()