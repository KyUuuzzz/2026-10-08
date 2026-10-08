
x = int (input('請輸入數字:'))
if  0<=x<=15 and x%1 == 0:
    _1_2 = x%2
    _2_2 = (x//2)%2
    _3_2 = (x//2//2)%2
    _4_2 = (x//2//2//2)%2
    print('二進制=',_4_2,_3_2,_2_2,_1_2) 
    _1_8 = x%8
    _2_8 = (x//8)%8
    print('八進制=',_2_8,_1_8)
    if x == 10 :
        print('十六進制=',"A")
    elif x == 11 :
        print('十六進制=',"B")   
    elif x == 12 :
        print('十六進制=',"C")  
    elif x == 13 :
        print('十六進制=',"D")
    elif x == 14 :
        print('十六進制=',"E")    
    elif x == 15 :
        print('十六進制=',"F") 
    elif x<10 :
        print('十六進制=',x)           
else:
    print('輸入錯誤')    
