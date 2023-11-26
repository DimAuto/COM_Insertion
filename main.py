from serial_comm import SerialComm
import time
import argparse

class Operations(object):
    def __init__(self, ser1, ser2) -> None:
        self.ser1 = ser1
        self.ser2 = ser2
        time.sleep(3)
          
    def remove_text(self):
        print("RUNNING")
        while(1):
            try:
                mes = self.ser1.read_serial()
                mes = mes.decode("utf-8")
                if "Initializing" not in mes:
                    mes = mes +"\r\n"
                    w_mes = mes.encode("utf-8")
                    self.ser2.write_serial(w_mes)
            except Exception as e:
                print(str(e))
        print("Stopped")

        








if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter a the device port')
    parser.add_argument("-p", "--port", type=str)
    args = parser.parse_args()

    ser = SerialComm(device=args.port, baud= 115200, stop_char= "\r\n", ftdi_serial= None) #iris_bare
    
    ser2 = SerialComm(device='COM99', baud= 115200, stop_char= "\r\n", ftdi_serial= None) #iris_bare

    op = Operations(ser, ser2)
    op.remove_text()
