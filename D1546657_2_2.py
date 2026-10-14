       
import sys      
A = int(input('請輸入A:'))
B = int(input('請輸入B:'))
S = int(input('請輸入S:'))
if (A != 0 and A != 1) or (B != 0 and B != 1) or (S != 0 and S != 1):
    print('輸入錯誤')
    sys.exit()
    if A != B:
      middle = 1
else:
      middle = 0
if middle == 1 and S == 1:
    start = 1
else:
    start = 0
print('第一個閘輸出=',middle)
print('允許啟動=',start)
    
    
