class Example:
    CLASS_ATTR = 1

    def __init__(self):
        self.prop = 2

    # def usual_method(self, param1):
    #     print(self.CLASS_ATTR)
    #     print(self.prop)
    #     print(param1)

    @staticmethod
    def stat_method(param1, param2):
        print(Example.CLASS_ATTR)
        print(param1)
        print(param2)

    # @classmethod
    # def class_method(cls, param1):
    #     print(cls.CLASS_ATTR)
    #     print(cls.stat_method(1, 2))


e = Example()
# e.usual_method(1)

# static method
# e.stat_method(1, 2)
Example.stat_method(1, 2)

# class method
# e.class_method(1)
# Example.class_method(1)
#
#
# print(Example.CLASS_ATTR)




