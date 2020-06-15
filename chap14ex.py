import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line {0} ok.".format(linenum)
    else:
        msg = "test at line {0} FAILED".format(linenum)
    print(msg)


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()

def test_suite():
    test(merge(xs, []) == xs)
    test(merge([], ys) == ys)


def merge(xs, ys):

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result

        if yi >= len(ys):
            result.extend(xs[xi:])
            return result


        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


test_suite()