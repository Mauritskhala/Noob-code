#Something used to simulate Galton Board
import datetime
from random import*
while True:    
    _floor = int(input('floor ='))
    Num = int(input('num='))
    Num_backup = Num
    x = range(0,_floor)
    Count = [0]*(_floor+1)
    start_time = datetime.datetime.now()
    while Num > 0:
        Num -= 1
        position = float((_floor+2)/2)
        for i in x:
            if random() < 0.5:
                position += 0.5
            else:
                position -= 0.5
            Count[int(position-1)] += 1
    end_time = datetime.datetime.now()
    time = float((end_time-start_time).total_seconds())
    speed = float(Num_backup)/time
    print(speed,'\n',Count)
