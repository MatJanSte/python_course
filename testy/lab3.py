# aList = [ i**2 for i in range(10)]
# bList = [ (i-1)**2 for i in range(10)]
#
# # with pair
# for p in zip(aList, bList):
#     print p[0], p[1]
#
# # or by
# for a, b in zip(aList, bList):
#     print a, b
# import timeit
#
# size=1000000
#
# start = timeit.default_timer()
#
# list1 = [i for i in range(size)]
# list2 = [i for i in range(size)]
# list3 = [0 for i in range(size)]
#
# start = timeit.default_timer()
#
# for i in range(size):
#     list3[i] = list1[i] + list2[i]
#
# t1 = float(timeit.default_timer()-start)
# print "Czas :", str(t1)
#
#
# import numpy as np
#
# list1 = np.array(range(size))
# list2 = np.array(range(size))
# list3 = np.zeros_like(list2)
#
# start = timeit.default_timer()
#
# for i in range(size):
#     list3[i] = list1[i] + list2[i]
#
# t2 = float(timeit.default_timer()-start)
# print "Czas :", str(t2)
#
#
# start = timeit.default_timer()
#
# list3 = list1 + list2
#
# t3 = float(timeit.default_timer()-start)
# print "Czas :", str(t3)
#
# print "t2/t1", t2/t1
# print "t1/t3", t1/t3
# print "t2/t3", t2/t3

# import numpy as np
# tab2D = np.ones((10,5), dtype=int)
#
# print tab2D.shape # >> (10, 5)
# print "Pierwszy wymiar", tab2D.shape[0] # >> Pierwszy wymiar 10
# print "Drugi wymiar", tab2D.shape[1] # >> Drugi wymiar 5
#
#
# tab2D = np.zeros((4,4))
# tab2D[:2,:2] = 2
# print tab2D #>> [[ 2.  2.  0.  0.]
#                         #        [ 2.  2.  0.  0.]
#                         #        [ 0.  0.  0.  0.]
#                         #            [ 0.  0.  0.  0.]]

# import numpy as np
#
# tab = np.zeros(10)
# tab[[1,4,8,9]] = 2
# print tab
#
# mask = tab == 0
# print mask
#
# tab[ mask ] = -1
# print tab
#
# from random import randint
# tab = np.array( [ randint(0,9) for i in range(10)])
#
# print "Liczby losowe wieksze od 5:"
# for e in tab[tab > 5]:
#     print e

#
# import numpy as np
# xy = np.zeros((10,2))
# xy[:, 0] = np.linspace(-1, 1, 10)
# print xy[:,0] #>>[-1.         -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111 0.33333333 0.55555556  0.77777778  1. ]
#
# xy[:, 1] = np.exp( xy[:, 0] )
# print xy


# zdanie="Jaki ten python jest latwy i czytelny"
# with open("tmp.txt", "w") as plik:
#     for slowo in zdanie.split():
#         plik.write(slowo + "\n")

# import os
#
# currentDir = "."
#
# for entry in os.listdir(currentDir):
#     if os.path.isdir(entry):
#         print entry + " is directory"
#     elif os.path.isfile(entry):
#         print entry + " is file"


# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y)
# plt.plot(x, np.cos(x))
#
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y, "b.")
# plt.plot(x, np.cos(x), "b-")
#
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y, color="blue", marker=".", linestyle="")
# plt.plot(x, np.cos(x), color="blue", marker="", linestyle="-")
#
# plt.show()

# import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(2)
# print axes.shape #>> (2, )
#
# fig, axes = plt.subplots(2,2)
# print axes.shape #>> (2, 2)

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# fig, (ax1, ax2) = plt.subplots(2)
#
# ax1.plot(x, y, color="blue", marker=".", linestyle="")
# ax2.plot(x, np.cos(x), color="blue", marker="", linestyle="-")
#
# ax1.grid(True)
# ax2.set_xlabel("x")
# ax1.set_ylabel("y")
# ax1.set_title("sin(x)")
# ax2.set_title("cos(x)")
#
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
#
# fig = plt.figure()
#
# line,  = plt.plot(x, np.zeros_like(x))

# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
#
# fig = plt.figure()
#
# line,  = plt.plot(x, np.zeros_like(x))
#
# plt.xlim([0, np.pi])
# plt.ylim([-1, 1])
#
# def update_plot(frame):
#     a  = float(frame)/100
#     line.set_ydata(np.sin(a*x))
#
# anim = FuncAnimation(fig, update_plot, frames=300, interval=1, repeat=False)
#
# plt.show()