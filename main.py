import random
while True: 
    x = ("a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","2","4","5","6","7","8","9","0")
    y = int(input('какая длина пароля будет?'))
    if y>0 and y<=9:
      z = ''.join(random.choice(x) for i in range(y))
      print (z)
    else:
      print("напиши цыфру от 1 до 9")
