import requests
import time

def doTest(nameDevice, iteractions):
    try:
        for i in range (int(iteractions)):
            requests.post(url= "http://localhost:8080/trigger/%s" % nameDevice)
            time.sleep(1)
            requests.post(url= "http://localhost:8080/deactivate/%s" % nameDevice)
            time.sleep(1)
        
        print("Teste completado com sucesso. Verifique o resultado !")
    except Exception as exception:
        print("\n Requisição sem sucesso \n")
        print(exception)

def main():
    nameDevice = input("Digite o nome do dispositivo a ser testado: ")
    iteractions = input("Digite o número de iterações do dispositivo: ")
    doTest(nameDevice, iteractions)
    

if __name__ == "__main__":
    main()