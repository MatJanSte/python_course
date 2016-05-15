#!/usr/bin/python
# import lab2a
# def funkcja(argument1):
#     """
#
#     :param argument1: #zmienna
#     :return:
#     """
#     a = argument1[3]
#     return a
# print funkcja("to jest string")
#
# lab2a.gaugan("to jest liczba nie wierz mu")
#
# # def oblicz(a,b):
# #     return float(a - b)/a
# # print oblicz(2, 1)
#
# def oblicz(a,b):
#     a = float(a)
#     b = float(b)
#     return (a - b)/a
# a = "2"
# print oblicz(a, 1)

# def moja_funkcja():
#     return 5
# moja_funkcja=3
# # moja_funkcja()
################################################################3
# def funkcja1():
#     print "Hellow"
#
# funkcja2 = funkcja1
# funkcja1()
# funkcja2()
#
# def suma(a, b):
#     return a + b
# print suma(5, 2)
# def roznica(a, b):
#     return a - b
# print roznica(5, 2)
# suma = roznica
# print suma(5, 2)
########################################
# def calka(fun, a, b):
#     dx = (b - a) / 99
#     Int = 0
#     for i in range(100):
#         Int += (fun(i*dx) + fun((i+1)*dx))/2*dx
#     return Int
#
# def x_kwadrat(x):
#     return x
#
# print "Calka =", calka(x_kwadrat, 0., 10.)
######################################################

# alist=[1, 2., 4, 2, 3]
# alist.remove(2)
# print alist

# aList= [1,2,3]
# bList = [3,2,1]
# print aList + bList # >> [1, 2, 3, 3, 2, 1]

###############################################################

# aList = [1, 'cos', 2]
# isInList = 'cos' in aList
# print isInList # >> True
# print 5 in aList # >> False
#
# if 'cos' in aList:
#     print 'cos is in the aList'


###############################################

# aList = [1, 2, 3, 4]
# sum = 0
# for a in aList:
#     sum += a
# print sum

# for i in range(7):
#     print i
#######################################
# aList = list()
# for i in range(100):
#     aList.append(i**2) # << wypelnienie listy kwadratem kolejnych liczb 0, 1, ..., 99
# def inicjalizacja(index):
#     a = index / 2
#     b = index*a
#     return b
# aList = [ inicjalizacja(i) for i in range(100)]
# print aList
###########################################
# aList = [ i for i in range(100)]
# bList = [2*element for element in aList]
# print aList
# print "\n"
# print bList

##############
aTuple = (1, 2, 'cos')

