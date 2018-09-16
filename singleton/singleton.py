def singleton(cls) :
    print(1)
    instances = {}
    print(2, instances)
    def getInstances() :
        print(4)
        if cls not in instances :
            instances[cls] = cls()
        print(5, instances)
        return instances[cls]
    print(3)
    return getInstances


class Counter :
    def __init__(self) :
        self.count = 0

    def inc(self) :
        self.count += 1


print(type(Counter))
ctr = singleton(Counter)
print(type(ctr))
print(id(ctr))

ctr2 = singleton(Counter)
print(id(ctr2))