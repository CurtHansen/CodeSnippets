def main(var1, var2, **kwargs):

    print "here is var1: {}".format(var1)
    print "here is var2: {}".format(var2)
    print "kwargs has {} elements".format(len(kwargs))

    sub1(**kwargs)

def sub1(var3, var4, **kwargs):
    print "here is var3: {}".format(var3)
    print "here is var4: {}".format(var4)
    print "kwargs has {} elements".format(len(kwargs))

    sub2(**kwargs)

def sub2(var5, var6, **kwargs):
    print "here is var5: {}".format(var5)
    print "here is var6: {}".format(var6)
    print "kwargs has {} elements".format(len(kwargs))


if __name__ == '__main__':
    main(var1=1,var2=2,var3=3,var4=4,var5=5,var6=6,var7=7)
