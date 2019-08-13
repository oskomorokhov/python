class Celsius:
    def __init__(self, temp=0):
        self._temp = temp

    def to_fahrenheit(self):
        return (self._temp * 1.8) + 32

    @property
    def temp(self):
        print("Getting value")
        return self._temp

    @temp.setter
    def temp(self, value):
        print("Setting value")
        if value < -273:
            raise ValueError("Temp can't be lower than -273C")
        self._temp = value


t = Celsius()
print(t.temp)
t.temp = -273
print(t._temp)
print(t.to_fahrenheit())


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)


jdoe = Employee('Joe', 'Doe')
print(jdoe.full_name)
