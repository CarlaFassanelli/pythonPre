"""
import time
for h in range(0,24,1):
    for m in range (0,60,1):
        for sin range (0,60,1):
            print(h,m,s)
"""
"""
import time
h=0
m=0
s=20
while h>=0 and m>=0 and s>=0:
    print(h,":",m ,":",s)
    time.sleep(1)
    s-=1
    if s<0:
        m -=1
        s= 59
    if m<0:
        h -= 1
        m=59
print("Fin del programa")
"""
"""
##horas: [0,23,1]
##minutos:[0,59,1]
##segundos:[0,59,1]
import time
for h in range(0,24,1):
    for m in range(0,60,1):
        for s in range(0,60,1):
            print(h,":",m,":",s)
            time.sleep(1)
"""

import time
h=int(time.strftime("%H"))
m=int(time.strftime("%M"))
s=int(time.strftime("%S"))
while(h<24):
    while(m<60):
        while(s<60):
            print(h,":",m,":",s)
            time.sleep(1)
            s=s+1
        m=m+1
        s=0
    h=h+1
    m=0














