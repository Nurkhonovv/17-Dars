a = int(input("Son kiriting: "))
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz Son Kiritdingiz")
elif a % 3 == 0:
    print("Fizz son kiritdingiz")
elif a % 5 == 0:
    print("buzz son kiritdingiz")
else:
    raise TypeError("Xato Son Kiritdingiz")
