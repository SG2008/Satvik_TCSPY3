import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line {0} ok.".format(linenum)
    else:
        msg = "test at line {0} FAILED".format(linenum)
    print(msg)


xs = [1,2,5,5,8]
ys = [2,8,11]
zs = xs+ys
zs.sort()


def test_suite():
    test(mergeA(xs, ys) == [2, 8])
    test(mergeA([1,3,4,5,5], [1,2,4,5,6]) == [1, 4, 5])
    test(mergeB(xs, ys) == [1, 5, 5])
    test(mergeB([1,3,4,5,5], [1,2,4,5,6]) == [3, 5])
    test(mergeC(xs, ys) == [11])
    test(mergeC([1,3,4,5,5], [1,2,4,5,6]) == [2, 6])
    test(mergeD(xs, ys) == [1, 5, 5, 11])
    test(mergeD([1,3,4,5,5], [1,2,4,5,6]) == [2, 3, 5, 6])


def mergeA(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1
        print(result)


def mergeB(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            return result          # And we're done.

        if yi >= len(ys):     # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            yi += 1
        print(result)


def mergeC(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
        print(result)


def mergeD(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
        print(result)


test_suite()

