       
import sys      
A = int(input('請輸入A:'))
B = int(input('請輸入B:'))

if (A != 0 and A != 1) or (B != 0 and B != 1) :
    print('輸入錯誤')
    sys.exit()
if A != B:
      middle = 1
else:
      middle = 0

S = int(input('請輸入S:'))
if (S == 0) or (S == 1):
    if middle == 1 and S == 1:
        start = 1
    else:
        start = 0
else:
    print('輸入錯誤')
    sys.exit()
print('第一個閘輸出=',middle)
print('允許啟動=',start)
    
