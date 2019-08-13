class MyClass(object):

    # class-wide attribute
    a = [1, 2, 3, 4, 5]

    def __init__(self, attrib1=0):
        # instance-wide attribute
        self.attrib1 = attrib1

    def ins_method1(self, *args, **kwargs):
        # instance-method
        print(f"i'm a class instance {self} method")
        return

    @classmethod
    def cls_method1(cls, *args, **kwargs):
        # class-wide method
        print(f"i'm a class {cls} method")
        cls.a.append('bar')
        print(cls.a)
        return

    @staticmethod
    def st_method1(*args, **kwargs):
        # static method can't modify neither class nor instance data
        print(f"i'm just a regular method that you can call from any class instance")
        return


class MyOtherClass(MyClass):

    def __init__(self):
        # obtain all attributes and methods from parent
        super().__init__()


obj = MyClass()
print(f"class instance attribute {obj.attrib1}")
obj.ins_method1()
obj.cls_method1()
obj.st_method1()
MyClass.st_method1()
print(obj.a)
print(MyClass.a)


other_obj = MyOtherClass()
print(other_obj.a)
other_obj.ins_method1()
