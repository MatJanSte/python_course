def test(fun, *args):
    print "".join(['-' for i in range(40)])
    print fun.__name__[:-1].upper()+" "+fun.__name__[-1]
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print "Yes, "+decoded.replace("my","your")
        else:
            print "No, "+decoded.replace("my","your").replace("has","has not")+" yet"
    else:
        print "Is correct? "+ str(res == args[-1])
    print "".join(['-' for i in range(40)])

def zadanie1(listObject):
    # type your code
    alist = listObject
    blist = [alist[0]]
    x = 0
    for i in alist:
        if i == blist[x]:
            pass
        else:
            blist.append(i)
            x += 1
            pass
        pass
    return blist
pass

test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1, 2, 3, 5, 68, 24])
###############################################################################################
def zadanie2(list1, list2):
    # type your code
    x = 0
    clist = []
    if len(list1) > len(list2):
        for i in range(len(list2)):
            clist.append(list1[i])
            clist.append(list2[i])
            x += 1
        for j in range(len(list1)):
            if j < x:
                pass
            else:
                clist.append(list1[j])
                pass
            pass
        pass
    else:
        for i in range(len(list1)):
            clist.append(list1[i])
            clist.append(list2[i])
            x += 1
        for j in range(len(list2)):
            if j < x:
                pass
            else:
                clist.append(list2[j])
                pass
            pass
        pass
    print clist
    print "To jest poprawne rozwiazanie"
    return clist
pass
test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12, 'c', '5'], [1, 12, 2, 'c', 19, '5', 1, 2, 19, 'dd', ':P', ':('])
####################################################################################################3
def zadanie3(listTuples):
    # type your code
    alist, blist, clist = listTuples
    a = len(alist) - 1
    b = len(blist) - 1
    c = len(clist) - 1
    dlist = []
    if alist[a] < blist[b]:
        if alist[a] < clist[c]:
            dlist.append(alist)
            if clist[c] < blist[b]:
                dlist.append(clist)
                dlist.append(blist)
            else:
                dlist.append(blist)
                dlist.append(clist)
        else:
            dlist.append(clist)
            dlist.append(alist)
            dlist.append(blist)
    else:
        if blist[b] < clist[c]:
            dlist.append(blist)
            if alist[a] < clist[c]:
                dlist.append(alist)
                dlist.append(clist)
            else:
                dlist.append(clist)
                dlist.append(alist)
        else:
            dlist.append(clist)
            dlist.append(blist)
            dlist.append(alist)
    print dlist
    pass
test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])