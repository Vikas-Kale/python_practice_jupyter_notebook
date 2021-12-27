def is_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

def is_prime(num1):
    count=0
    for i in range(1,num1+1):
        if num1%i==0:
            count+=1
    if count==2:
        return "prime"
    else:
        return "not_prime"

while True:
    print("########### Enter responce #############")
    responce=int(input("1.To check is even or odd:- \n2.To check is prime or not:- \t 3.For exit:- "))
    if responce ==1:
        num=int(input("Enter number which you want to check even or odd:- "))
        print(is_even(num))

    elif responce ==2:
        num1=int(input("Enter a number which you want to check prime or not:- "))
        print(is_prime(num1))

    elif responce==3:
        print("Exit")
        break
