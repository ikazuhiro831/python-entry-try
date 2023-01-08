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

# with open('./test.txt', 'r') as file:
#   print(file.read())

# class Card:
#   def __init__(self, date ,user_name):  #メソッド     classの中では関数ではない
#     self.date = date                    #プロパティ
#     self.user_name = user_name
#   def message(self):
#     return 'この投稿は' + self.user_name + 'が' + self.date + 'に投稿しました'

# date_a = '2023-01-08'
# user_name_a = 'Taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2023-01-11'
# user_name_b = 'Piroko'
# card_b = Card(date_b, user_name_b)   #インスタンス化

# # print(card_a.user_name)
# # print(card_a.date)
# # print(card_a.message())

# print(card_b.message())

import math
print(math.pi)

import numpy
numpy_list = [1,4,6,934,2342,23434234,121]
print(numpy.sum(numpy_list))
