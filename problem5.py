a = int(input("введите число: "))
b = 1000
if a %2==0:
    print( "ваше число четное" )
else:
    print( "число нечетное" )
    if a %3==0:
        print( "ваше число делится на 3 без остатка")
    else:
        print( "ваше число не делится на 3 без остатка" )
        if a**2 > b:
            print( "ваше число во 2 степени больше 1000" ) 

        else:
            print( "ваше число во 2 степени меньше 1000" )

