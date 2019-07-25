#!/usr/bin/env python
# coding: utf-8

# # AI_1_2

# print("Input number of rows: ")
# row = int(input())
# print("Input number of columns: ")
# col= int(input())
# lt = [[0 for col in range(col)] for row in range(row)]
# for i in range(row):
#     for j in range(col):
#        lt[i][j]= i*j
# print(lt)

# # AI_1_1

# import math
# str = input()
# list = str.split (",")
# li = []
# lt=[]
# c=50
# h=30
# for i in list:
# 	li.append(int(i))
# print(li)
# for i in range(0,len(li)):
#     lt.append(round(math.sqrt((2*c*li[i])/h)))
# print(lt)    


# # AI_1_3

# print("write the words seperated by comma")
# y=input()
# y=y.split(",")
# y=sorted(y)
# print(",".join(y))

# # AI_1_4

# i=input()
# w={}
# for x in i.split():
#     w[x]=w.get(x,0)+1
# sorted(w)
# for y in w:
#     print("{}:{}".format(y,w[y]))
#    

# # AI_1_5

# class practice:
#     def first(self,str):
#         import math
#        # str = input()
#         list = str.split (",")
#         li = []
#         lt=[]
#         c=50
#         h=30
#         for i in list:
#             li.append(int(i))
#         print(li)
#         for i in range(0,len(li)):
#             lt.append(round(math.sqrt((2*c*li[i])/h)))
#         print(lt)  
#     def second(self,row,col):
#         
#         lt = [[0 for col in range(col)] for row in range(row)]
#         for i in range(row):
#             for j in range(col):
#                lt[i][j]= i*j
#         print(lt)
#     def third(self,y):
#         y=y.split(",")
#         y=sorted(y)
#         print(",".join(y))
#     def fourth(self,i):
#         w={}
#         for x in i.split():
#             w[x]=w.get(x,0)+1
#         sorted(w)
#         for y in w:
#             print("{}:{}".format(y,w[y]))
# print("THIS IS THE SQRT QUE")
# ob1=practice()
# str=input()
# ob1.first(str)
# print("THIS IS THE 2D MATRIX QUESTION")
# row = int(input("no. of rows"))
# col= int(input("no. of columns"))
# ob1.second(row,col)
# print("THE WORD SORT")
# print("write the words seperated by comma")
# y=input()
# ob1.third(y)
# print("THE DICTIONARY PROBLEM")
# print("enter a string and see the magic")
# i=input()
# ob1.fourth(i)
# print("FINALLY THE ASSIGNMENT IS COMPLETED!!")





