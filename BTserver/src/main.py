from time import sleep

from exceptions.exceptions import *

from services.microcontroller import MicroController
from services.api import RequestAPI

from utils.system import System

api = None
arduino = None

def __DEFINATIONS():
    global api, arduino
    
    try:
        if(arduino == None):
            arduino = MicroController

        if(api == None):
            api = RequestAPI("INFO22")

        else:
            print("conexao estabelecida")
    
    except NullControllerException as error:
        print(error)

    except InactiveApiException as error:
        print(error)
        sleep(3)
        System.clear()
        print("tentando se conectar novamente...")
        sleep(2)
        System.clear()
        __DEFINATIONS()

def main():

    __DEFINATIONS()    
    lastStateAir = not api.isActiveAir()

    while(True):
        stateAir = api.isActiveAir()
        if( stateAir == True and lastStateAir == False ):
            # arduino.send("ligar")
            print("ligar")
            lastStateAir = True

        elif( stateAir == False and lastStateAir == True):
            print("desligar")
            lastStateAir = False
        sleep(10)
        
if __name__ == "__main__":
    main()
