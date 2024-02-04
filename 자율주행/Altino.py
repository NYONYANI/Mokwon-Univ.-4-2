import time  #운영 체제의 시간 관련 모듈 
import serial #블루투스 시리얼 통신을 위한 모듈
from timeit import default_timer as timer #
import threading # 쓰레드 생성하기 위한 모듈  

te=0
tx_d = [2,28,35,1,10,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
rx_data= [0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0]
rx_d = []
rx_d56 = [0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0]
rx_ddata = [0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0]
rx_dsensor1 = [0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0]

ser = serial.Serial() #B
ser.baudrate = 115200 #Bluetooth serial baudrate
ser.timeout = 2000
port='com7'

rxcnt=0
speed = 0
connectstate = 0

class SensorData :
    CDS = 0
    IR = [0,0,0,0,0,0,0,0]
    Bat = 0
    Acc = [0,0,0,0]
    Mag = [0,0,0,0]
    Gyro = [0,0,0,0]
    MCur = [0,0,0]
    Temp = 0    
    StVar = 0
    StCur = 0    
    Remote = 0
    MTemp = 0
    CNT = 0

sensor=SensorData
    
def startTimer():
    global connectstate
    global rxcnt
    
    if connectstate == 1 :
        try :
            timer = threading.Timer(0.08, startTimer)
            timer.start()
            sensor = SensorFun(10)            
        except KeyboardInterrupt:            
            Close()

def Open(portName=port) :
    global connectstate
    global ser   
    ser.port=portName #Bluetooth serial port
    ser.open()
    connectstate = 1
    delay(1000)
    startTimer()
    print("Bluetooth connect")

def BT(portName=port) :
    Open(portName)

def Bt(portName=port) :
    Open(portName)

def bt(portName=port) :
    Open(portName)
    
def Close() :
    global connectstate
    delay(1000)
    connectstate = 0    
    ser.close()
    print("Bluetooth disconnect")

def close() :
    Close()

def delay(ms):
    time.sleep(ms/1000)

def Delay(ms):
    delay(ms)

def check():
    tx_d[26]=255
    te=tx_d[1]
    ircheck =tx_d[21] | 0x01
    tx_d[21]=ircheck
    
    for i in range(3,28):
        te=te+tx_d[i]

    te=te%256
    tx_d[2]=te
    ser.write(bytearray(tx_d))

def Go(left, right):
    if left>1000:
        left=1000
    if left<-1000:
        left=-1000
    if right>1000:
        right=1000
    if right<-1000:
        right=-1000

    if left<0:
        left=32768-left
    
    if right<0:
        right=32768-right
    
    tx_d[7]=int(right//256)
    tx_d[8]=int(right%256)
     
    tx_d[10]=int(left//256)
    tx_d[11]=int(left%256)

def go(left,right) :
    Go(left,right)

def GO(left,right) :
    Go(left,right)

def Display(dot):     
    if type(dot)==int :
        if dot > 128 :
            dot=dot-128
        elif dot>0:
            dot=128+dot
        
        tx_d[12]=dot
    else :
        tx_d[12]=128+ord(dot)

    tx_d[13]=0
    tx_d[14]=0
    tx_d[15]=0
    tx_d[16]=0
    tx_d[17]=0
    tx_d[18]=0
    tx_d[19]=0
    tx_d[20]=0

def display(dot):
    Display(dot)

def DISPLAY(dot):
    Display(dot)

def DisplayLine(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8):
    tx_d[12]=0
    tx_d[13]=dot8
    tx_d[14]=dot7
    tx_d[15]=dot6
    tx_d[16]=dot5
    tx_d[17]=dot4
    tx_d[18]=dot3
    tx_d[19]=dot2
    tx_d[20]=dot1

def displayline(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8):
    DisplayLine(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)

def displayLine(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8):
    DisplayLine(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)

def DISPLAYLINE(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8):
    DisplayLine(dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8)

def Displayon(x, y) :
    tx_d[12]=0
    
    dotx=tx_d[21-x]
    tx_d[21-x]=dotx | pow(2,(y-1))  

def displayon(x,y):
    Displayon(x,y)

def DisplayOn(x,y):
    Displayon(x,y)

def DisplayON(x,y):
    Displayon(x,y)

def DISPLAYON(x,y):
    Displayon(x,y)

def Displayoff(x, y) :
    tx_d[12]=0
    
    dotx=tx_d[21-x]
    tx_d[21-x]= dotx & (255-pow(2,(y-1)))  

def displayoff(x,y):
    Displayoff(x,y)

def DisplayOff(x,y):
    Displayoff(x,y)

def DisplayOFF(x,y):
    Displayoff(x,y)

def DISPLAYOFF(x,y):
    Displayoff(x,y)

def Sound(buzzer) :
    tx_d[22]=buzzer

def sound(buzzer):
    Sound(buzzer)

def SOUND(buzzer):
    Sound(buzzer)

def Light(led) :
    tx_d[21]=int(led//256)
    tx_d[23]=int(led%256)

def light(led):
    Light(led)

def LIGHT(led):
    Light(led)

def Led(led):
    Light(led)    

def led(led):
    Light(led)    

def LED(led):
    Light(led)   

def Steering(value):
    if value>127:
        value=127
    if value<-127:
        value=-127
	
    if value<0:
        value=128-value
    
    tx_d[24]=1
    tx_d[5]=value            
    
def steering(value):
    Steering(value)

def STEERING(value):
    Steering(value)

def Stop() :
    Go(0,0)
    Steering(0)
    Sound(0)
    Display(0)
    Led(0)

def stop() :
    Stop()

def SensorFun(command) :
    try:
        tx_d[4]=command
        check()
        
        rx_data=ser.read(56)
        for cnt in range(0,56) :
            for cnt1 in range(0,55) :
                rx_d56[cnt1]=rx_d56[cnt1+1]

            rx_d56[55]=rx_data[cnt]
        
            rx_check_sum=0        
            if rx_d56[0]==2 and rx_d56[55] == 3 and rx_d56[1] == 56 :
                rx_check_sum = rx_d56[0]
                rx_check_sum = rx_check_sum +rx_d56[1]
                
                for cnt3 in range(3,56) :
                    rx_check_sum = rx_check_sum + rx_d56[cnt3]
                
                rx_check_sum = rx_check_sum % 256

                if rx_check_sum == rx_d56[2]:
                    for cnt3 in range(7,54) :
                        rx_dsensor1[cnt3]=rx_d56[cnt3]

                    for cnt2 in range(0,56) :
                        rx_d56[cnt2]=0
   
        sensordata1 = SensorData

        sensordata1.IR[1]=rx_dsensor1[7] * 256 + rx_dsensor1[8]
        sensordata1.IR[2]=rx_dsensor1[9] * 256 + rx_dsensor1[10]
        sensordata1.IR[3]=rx_dsensor1[11] * 256 + rx_dsensor1[12]
        sensordata1.IR[4]=rx_dsensor1[13] * 256 + rx_dsensor1[14]
        sensordata1.IR[5]=rx_dsensor1[15] * 256 + rx_dsensor1[16]
        sensordata1.IR[6]=rx_dsensor1[17] * 256 + rx_dsensor1[18]

        sensordata1.MCur[0]=rx_dsensor1[19] * 256 + rx_dsensor1[20]
        sensordata1.MCur[1]=rx_dsensor1[21] * 256 + rx_dsensor1[22]

        sensordata1.Temp = rx_dsensor1[49] * 256 + rx_dsensor1[50]

        sensordata1.CDS = rx_dsensor1[43] * 256 + rx_dsensor1[44]

        sensordata1.Acc[0]=rx_dsensor1[25] * 256 + rx_dsensor1[26]
        sensordata1.Acc[1]=rx_dsensor1[27] * 256 + rx_dsensor1[28]
        sensordata1.Acc[2]=rx_dsensor1[29] * 256 + rx_dsensor1[30]

        temp=0
        temp=sensordata1.Acc[0]//16
        sensordata1.Acc[0]=temp

        temp=0
        temp=sensordata1.Acc[1]//16
        sensordata1.Acc[1]=temp

        temp=0
        temp=sensordata1.Acc[2]//16
        sensordata1.Acc[2]=temp

        if sensordata1.Acc[0]>2048 :
            sensordata1.Acc[0]=sensordata1.Acc[0]- 4096
 
        if sensordata1.Acc[1]>2048 :
            sensordata1.Acc[1]=sensordata1.Acc[1]-4096
         
        if sensordata1.Acc[2]>2048 :
            sensordata1.Acc[2]=sensordata1.Acc[2]-4096

        sensordata1.Mag[0]=rx_dsensor1[31] * 256 + rx_dsensor1[32]
        sensordata1.Mag[1]=rx_dsensor1[33] * 256 + rx_dsensor1[34]
        sensordata1.Mag[2]=rx_dsensor1[35] * 256 + rx_dsensor1[36]
            
        sensordata1.StVar = rx_dsensor1[45] * 256 + rx_dsensor1[46]
        sensordata1.StCur = rx_dsensor1[23] * 256 + rx_dsensor1[24]
        sensordata1.Bat = rx_dsensor1[47] * 256 + rx_dsensor1[48]

        sensordata1.Remote = rx_dsensor1[51]
        sensordata1.MTemp = rx_dsensor1[52]

        sensordata1.Gyro[0]=rx_dsensor1[37] * 256 + rx_dsensor1[38]
        sensordata1.Gyro[1]=rx_dsensor1[39] * 256 + rx_dsensor1[40]
        sensordata1.Gyro[2]=rx_dsensor1[41] * 256 + rx_dsensor1[42]
  
        if sensordata1.Mag[0]>32768 :
            sensordata1.Mag[0]=sensordata1.Mag[0]-65535
        
        if sensordata1.Mag[1]>32768 :
            sensordata1.Mag[1]=sensordata1.Mag[1]-65535
        
        if sensordata1.Mag[2]>32768 :
            sensordata1.Mag[2]=sensordata1.Mag[2]-65535
        
        if sensordata1.Gyro[0]>32768 :
            sensordata1.Gyro[0]=sensordata1.Gyro[0]-65535

        if sensordata1.Gyro[1]>32768 :
            sensordata1.Gyro[1]=sensordata1.Gyro[1]-65535
        
        if sensordata1.Gyro[2]>32768 :
            sensordata1.Gyro[2]=sensordata1.Gyro[2]-65535

        sensordata1.CNT =sensordata1.CNT+1
        
        return sensordata1
    
    except :
        pass




    
    
