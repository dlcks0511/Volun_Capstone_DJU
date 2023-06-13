import os
import time
import h2b
import stt

class Pororo:
    def __init__(self, data_pin, latch_pin, clock_pin, no):
        #self.data = [0] * MAX_BRAILLE_NO
        self.data_pin = data_pin
        self.latch_pin = latch_pin
        self.clock_pin = clock_pin
        self.braille_no = no
        self.resPin = [[0,]*6 for i in range(no)]
    
    def begin(self):
        print("점자 모듈을 시작합니다.")

    def on(self, no, index):    # 몇번째인지, 인덱스
        self.resPin[no][index] = 1      

    def off(self, no, index):
        self.resPin[no][index] = 0

    def refresh(self):
        os.system("cls")
        for i in range(0,6,2):
            for j in range(3):
                print(f"{self.resPin[j][i]}{self.resPin[j][i+1]}", end=' ')
            print()
                

    def all_off(self):
        for i in range(3):
            for j in range(6):
                self.resPin[i][j] = 0


no_module = 3
pp = Pororo(2,3,4,no_module)

while True:
    #say = input("Input message")
    word = stt.stt()
    braille_list = h2b.text(word)

    for i in braille_list:
        
        for j in range(6):
            if i[j]==0:
                pp.on(0, j)
        pp.refresh()
        print(word)
        time.sleep(1)
        pp.all_off()
        pp.refresh()


    """
    for i in range(no_module):
        for j in range(6):
            pp.on(i, j)
            pp.refresh()
            time.sleep(1)
            
            pp.off(i, j)
            pp.refresh()
            time.sleep(1)
            """