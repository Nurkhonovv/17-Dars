# a = int(input("Son kiriting: "))
# if a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz Son Kiritdingiz")
# elif a % 3 == 0:
#     print("Fizz son kiritdingiz")
# elif a % 5 == 0:
#     print("buzz son kiritdingiz")
# else:
#     raise TypeError("Xato Son Kiritdingiz")

#####git add .   git commit -m " comment  "   git push  >>>>>>>   git hubga push qilish uchun

# def fizzBuzz(son):
#     try:
#         if son % 3 == 0 and son % 5 == 0:
#             print("Fizz buz")
#         elif son % 3 == 0:
#             print("Fizz")
#         elif son % 5 == 0:
#             print("Buzz")
#         else:
#             raise TypeError("FizzBuzzdan hech biri emas")
#     except TypeError as t:
#         print(t.args)
# fizzBuzz(15)
# fizzBuzz(12)
# fizzBuzz(10)
# fizzBuzz(11)
# def fizzBuzz(son):
#     try:
#         if son % 3 == 0 and son % 5 == 0:
#             print("Fizz buz")
#         elif son % 3 == 0:
#             print("Fizz")
#         elif son % 5 == 0:
#             print("Buzz")
#         else:
#             raise TypeError("FizzBuzzdan hech biri emas")
#     except TypeError as t:
#         print(t.args)
# fizzBuzz(15)
# fizzBuzz(12)
# fizzBuzz(10)
# fizzBuzz(11)



# try:
#     print("salom")
#     print(salom)
# except Exception as e:
#     print(e.args)
# finally:
#     print("Hamma vazifa tugadi")
import random as r
imkon = 0
randomSon = r.randint(1, 100)

while True:
    try:

        son = int(input("Son kiriting:"))

        if(son > randomSon ):
            imkon += 1
            print("Katta son tanladi")
        elif son < randomSon:
            imkon += 1
            print("Kichik son tanladiz")
        else:
            print("Son topildi")
            break

        if(imkon > 5):
            raise Exception("Imkoniyat tugadi")
    except Exception as e:
        print(e.args)
        break
    finally:
        print("Oyin tugadi")

