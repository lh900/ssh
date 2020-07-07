# try:
#     f = open("bbbb.txt",'r')
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")
#
# print("操作完文件")

class CustomException(Exception):

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value

a = 0
try:
    if a == 0:
        print('a = {} 触发异常'.format(a) )
        raise CustomException('值不能为0')
    print ('a = {} 未触发异常'.format(a))
except CustomException as e :
    print(e)


