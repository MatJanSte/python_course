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
#aTuple = (1, 2, 'cos')
####################################
# aString = "Uwielbiam pisac w Pythonie"
#
# print "Liczba znakow to w zdaniu", len(aString)
#
# print "Trzeci znak to ", aString[2]
#
# for znak in aString:
#     print znak
####################################
# aString = "Uwielbiam"
# aString += " pisac"
#
# print aString + " w Pythonie"
###################################
# aString = "Uwielbiam pisac w Pythonie"
#
# print "5 pierwszych znakow to " + aString[:5]
# print "A 8 ostatnich to "+ aString[-8:]
#
# a = 1
# b = 2.2
#
# aString = "Liczba a =" + str(a) + ", a liczba b = " + str(b)
#
# print aString
###################################3
# a = 5.234
# formatedString = "Wartosc zmiennej a=%f" % a
# print formatedString
#
# formatedString = "Wartosc zmiennej a=%.2f" % a
# print formatedString
#
#
# b = 12
# print "Wartosc zmiennej b = %03d" % b
#
# print "Trzy sformatowane kolejne cyfry to %f-%02d-%.2f" % (1.25312, 2, 2.35495)
# def zadanie2(list1, list2):
#     # type your code
#     x  = 0
#     clist = []
#     if len(list1) > len(list2):
#         for i in range(len(list2)):
#             clist.append(list1[i])
#             clist.append(list2[i])
#             x += 1
#         for j in range(len(list1)):
#             if j < x:
#                 pass
#             else:
#                 clist.append(list1[j])
#                 pass
#             pass
#         pass
#     else:
#         for i in range(len(list1)):
#             clist.append(list1[i])
#             clist.append(list2[i])
#             x += 1
#         for j in range(len(list2)):
#             if j < x:
#                 pass
#             else:
#                 clist.append(list2[j])
#                 pass
#             pass
#         pass
#     print clist
#     pass
#############################################################
# def zadanie3(listTuples):
#     # type your code
#     alist, blist, clist = listTuples
#     a = len(alist) - 1
#     b = len(blist) - 1
#     c = len(clist) - 1
#     dlist = []
#     if alist[a] < blist[b]:
#         if alist[a] < clist[c]:
#             dlist.append(alist)
#             if clist[c] < blist[b]:
#                 dlist.append(clist)
#                 dlist.append(blist)
#             else:
#                 dlist.append(blist)
#                 dlist.append(clist)
#         else:
#             dlist.append(clist)
#             dlist.append(alist)
#             dlist.append(blist)
#     else:
#         if blist[b] < clist[c]:
#             dlist.append(blist)
#             if alist[a] < clist[c]:
#                 dlist.append(alist)
#                 dlist.append(clist)
#             else:
#                 dlist.append(clist)
#                 dlist.append(alist)
#         else:
#             dlist.append(clist)
#             dlist.append(blist)
#             dlist.append(alist)
#     pass
# zadanie3([(1, 3), (3, 3, 2), (2, 1)])
# #test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])
