from pyfirmata import Arduino, util
import serial.tools.list_ports

class Arduino_Board():
    def __init__(self, port):

        port, discription = self.detect_board()

        if not port:
            print('Not Arduino is connected')
            exit(1)
        else:
            print('connected to', discription )

        self.board = self.arduino(port)
       
    def arduino(self,port):
        return Arduino(port)

    def detect_board(self):
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if "Arduino" in port.description:
                return port.device, port.description
        return None, None

    def low(self,pin): 
        self.board.digital[pin].write(0)

    def high(self,pin):
        self.board.digital[pin].write(1)

    def readpin(self,pin):
        return self.board.digital[pin].read()


    