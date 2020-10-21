
# 所谓单例就是一个类从始至终只能产生一个实例
# 在__new__方法中把类实例绑定到类变量_instance上，如果cls._instance为None表示该类还没有实例化过，实例化该类并返回。
# 如果cls_instance不为None表示该类已实例化，直接返回cls_instance


class Singleton():
    def __init__(self):
        print("init")

    def __new__(cls, *args, **kwargs):
        print(cls)
        print("new !!")
        # if not hasattr(cls, '_instance'):
        #     cls._instance = object.__new__(cls, *args, **kwargs)
        #     print("new !!")
        #
        return object.__new__(cls, *args, **kwargs)

    def dump(self):
        print("dump")

ss = Singleton()
print(ss.dump())

exit()
class Testclass(Singleton):
    a = 1


test1 = Testclass()
test2 = Testclass()
print(test1, test2)

