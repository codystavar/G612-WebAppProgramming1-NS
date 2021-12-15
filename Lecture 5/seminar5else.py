#elseif
N = input("Input a number ")
N = int(N)

if (N%2):
 print("Weird")
else: 
    if (N>=2 and N<=5):
        print("Not weird")
    else: 
        if(N>=6 and N<=20):
            print("Weird")
        else: 
            if (N>20):
                print("Not weird")

