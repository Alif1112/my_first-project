a=('Any Number chacking Tools! 😎😎😎 🧐✔')
print(a)
while True:
    x=input("enter your name:")

    d=input(x.upper()+"! enter your number:")
    def number_check(fun):
            print(x.upper(),"! Your Operator Name:",fun +' and your Number is Right.')

    a=len(d)
    if a==11:
        print("The Number is pending.")
        print("The number Chacking Sucussfully.")
        k=(d[0:3])
        p="014"
        n="017"
        if (k==p)or(k==n):
            
            print(x.upper(),"! Your Operator Name:'Grameen_phone'and your Number is Right.")
        o="019"    
        if (k==o):
            print(x.upper(),"! Your Operator Name:'Banglalink' and your Number is Right.")
        v="018"
        if (v==k):
            print(x.upper()+"! Your Operator Name:'robi' and your Number is Right.")
        l="016"
        if (l==k):
            number_check("'Teletalk'")
        b="015"
        if (b==k):
            number_check("'Citycell'")
        oi="013"
        if oi==k:
            number_check("'Airtel'")
   
        else:
            print('your number is not valided')
        
        break
            

    else:

        print("This Number is rong, Sum cracter mistack!.")
        print("please try it.")