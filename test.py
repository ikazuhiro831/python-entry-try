# def hantei(arg):
#   if arg > 60 :
#     print("合格" + str(arg))
#   else :
#     print("不合格" + str(arg))

# # hantei(70)

# score = 0

# for index in range(1,101):
#   score = score + 1
#   hantei(score)

with open('./test.txt', 'r') as file:
  print(file.read())