A = int(input('請輸入A:'))
B = int(input('請輸入B:'))
if A == 1 or 0  :
    if  B == 0 or 1:
        if A or B == 1:
            print("OR=1")
        else:
            print('OR=0') 
        if A and B == 1:
            print('AND=1')
        else:
            print('AND=0')
        if A != B:  
            print("XOR=1")
        else:
           print('XOR=0')  
    else:
        print('輸入錯誤')  
else:
    print('輸入錯誤')
