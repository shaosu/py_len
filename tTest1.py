import  os

from   PyQt5.QtSerialPort import  *


def TestHotoUseSerialPort():
    com1=QSerialPort
    com1.setBaudRate(9600,dir="")
    com1.setParity(QSerialPort.parity().numerator)

    return  true



print("I am form Lubuntu yet!")


