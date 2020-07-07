# class aaa():
#  def pub_function(self):
#     print("公有方法")
#  def _pri_function(self):
#     print("私有方法")
#  def __pri_function(self):
#     print("私有方法2")
#
#
# print(aaa.pub_res)
# print(aaa._pri_res)
# print(aaa().pub_function())
# print(aaa()._pri_function())


# class Parent():
#
#     money = 100000000000
#     house = 1000000
#     _yi_wu = "鞋子"
#     def shou_yi(self):
#         print("点石成金")
# p = Parent(123)
# print(p.a)
#
# class Child(Parent):
#     ai_hao = "花钱"
#     def __init__(self,*args,**kwargs):
#      super()._init_(*args,**kwargs)
#
#     def shou_yi(self):
#         print("影分身之术")
#
# c = Child()
# print(c.ai_hao)
# print(c.money)
from practice import day2
# from practice.day2 import a as day2_a

# a = "我是day3中的a变量"
#
# def name():
#     print("我是day3中的name方法")
# class Test():
#     print("我是day3中的Test类")

# print(day2_a)
# print(name())
# print(Test)
#
# if __name__ == '__main__':
#     # print(module_1.a)
#     name()
#     print(Test)

# t = (1,2,3)
# l = [4,5,6,7,8,9,10]
# s = {7,8,9,23,24}
# print(list(t))
# print(tuple(l))
# print(set(s))
# print(list(s))
# a = 123
# b = "456"
# print(a + int(b))
# print(str(a) + b)
# f = open("aaa.txt",'w')
# f.write("hello kitty")
# f.close()
#
#
# f = open("aaa.txt",'r')

# print(f.read())
# print(f.read(10))
# print(f.readline())
# print(f.readlines())
# f.close()


# a = "吴彦祖宁国分祖"
# print(a[0])
# print(a[-1])
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[2:])
# print(a[:-2])

# for i in range(1,10):
#     for j in range(1,i + 1):
#         print("%d x %d = %d"%(j,i,i*j),end="\t")
#     print()
#
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print("{} x {} = {}".format(j,i,i*j),end="\t")
#         print()

# l = [1,24,23,4,5,7,9,88,100]
#
# # l[0] = 20
# print(l)
# l[1:7] = 66,88,33,44,55,77
# print(l)


# 猜数字游戏
# flag = True
# import random
# a=random.randint(0,100)
# while flag:
#    b=int(input('请输入数字'))
#    if b>a :
#       print('大了')
#    elif(b<a):
#       print('小了')
#    else:
#       print('猜对了')
#       flag = False
# l = [2,3,4,5,6,7,8]
# l.append("陈冠希")
# l.append("黎明")
# l.append({'123',123})
# l.insert(1,"宁国吴彦祖")
# print(l)
#
# print(l.pop())
# print(l)
#
# print(l.pop(1))
# print(l)
#
# l.remove(2)
# print(l)
#
# l = [2,3,4,34,45,56,67,78,1,2,3,]
# l.remove(3)
# print(l)
#
# l = [True,1,2,3,5,6,2,6,7]
# l.remove(1)
# print(l)

# d = {"name":"小明","age":18,"sex":"男"}
#
# d.update({"addr":"上海闵行","学历":"本科"})
# print(d)

