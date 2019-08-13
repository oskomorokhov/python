#!/usr/bin/env checkio --domain=py run microwave-ovens

# https://py.checkio.org/mission/microwave-ovens/

# There is a lunch place at your work with the 3 microwave ovens (Мicrowave1, Мicrowave2, Мicrowave3), which are the subclasses of the MicrowaveBase class. Every microwave can be controlled by a RemoteControl. The RemoteControl uses the next commands:
#
# set_time("xx:xx"), where "xx:xx" - time in minutes and seconds, which shows how long the food will be warming up. For example: set_time("05:30");
# add_time("Ns"),add_time("Nm"), where N - the number of seconds("s") or minutes("m"), which should be added to the current time;
# del_time("Ns"),del_time("Nm"), where N - the amount of the seconds("s") or minutes("m"), which should be subtracted from the current time;
# show_time()- shows the current time for the microwave.
#
# The default time is 00:00. The time can't be less than 00:00 or greater than 90:00, even if add_time or del_time causes it.
#
# Your task is to create a few classes - one for the MicrowaveBase, three for the three different microwaves, and one for the RemoteControl - just as described above. The RemoteControl will have 1 parameter - an instance of the Microwave (for example, RemoteControl(microwave_1), where microwave_1 = Microwave1()) that shows which Microwave should be controlled by the current RemoteControle.Only the third oven works properly and shows the full time. The other two have some flaws with their displays - the first shows '_' instead of the first digit and the second does the same with the last digit. They show time like this:
# microwave_1 = Microwave1()
# microwave_2 = Microwave2()
# microwave_3 = Microwave3()
#
# RemoteControl(microwave_1).show_time() == "_0:00"
# RemoteControl(microwave_2).show_time() == "00:0_"
# RemoteControl(microwave_3).show_time() == "00:00"
#
# In this mission you could use theBridgedesign pattern. Its main task is -  to decouple an abstraction from its implementation so that the two can vary independently.
#
# Example:
# microwave_1 = Microwave1()
# microwave_2 = Microwave2()
# microwave_3 = Microwave3()
#
# remote_control_1 = RemoteControl(microwave_1)
# remote_control_1.set_time("01:00")
#
# remote_control_2 = RemoteControl(microwave_2)
# remote_control_2.add_time("90s")
#
# remote_control_3 = RemoteControl(microwave_3)
# remote_control_3.del_time("300s")
# remote_control_3.add_time("100s")
#
# remote_control_1.show_time() == "_1:00"
# remote_control_2.show_time() == "01:3_"
# remote_control_3.show_time() == "01:40"
#
#
#
# Input:methods of the RemoteControl class and time.
#
# Output:time on the display of the microwave.
#
# Precondition:00:00<= time<= 90:00
#
#
# END_DESC

from datetime import timedelta


class MicrowaveBase:
    def __init__(self, time="00:00"):
        # set default time for all MVs
        self.time = time


class Microwave1(MicrowaveBase):
    def __init__(self):
        # init parent class, gain its attributes
        super().__init__()
        # MV1's 1st digit is bad (index)
        self.bad_digit = "0"


class Microwave2(MicrowaveBase):
    def __init__(self):
        super().__init__()
        # MV2's last digit is bad (index)
        self.bad_digit = 4


class Microwave3(MicrowaveBase):
    def __init__(self):
        super().__init__()
        # MV3's digits are OK
        self.bad_digit = None


class RemoteControl:
    def __init__(self, object=None):
        # if initialized with MV instance as arg, get it
        self.object = object
        # store default time locally, just in case...
        self.dtime = object.time

    def show_time(self):
        # check if MV instance has a bad digit. If found, replace it with '_' and return
        if self.object.bad_digit:
            self.object.time = [x for x in self.object.time]
            self.object.time[int(self.object.bad_digit)] = '_'
            self.object.time = "".join(self.object.time)
        return self.object.time

    def set_time(self, time="00:00"):
        # set MV instance time to time from arg
        self.object.time = time

    def add_time(self, seconds):

        # parse the arg, convert to int
        seconds = int(
            seconds[:-1]) if seconds[-1] == "s" else int(seconds[:-1])*60
        # set current time as timedelta 1 and time from arg as timedelta 2
        self.t1 = timedelta(minutes=int(
            self.object.time[:2]), seconds=int(self.object.time[3:]))
        self.t2 = timedelta(minutes=0, seconds=seconds)
        # if time is greater than 90:00 after add operation, reset current time to 90:00
        self.object.time = str(
            self.t1+self.t2)[2:] if (self.t1+self.t2).seconds <= 5400 else "90:00"

    def del_time(self, seconds):

        seconds = int(
            seconds[:-1]) if seconds[-1] == "s" else int(seconds[:-1])*60
        self.t1 = timedelta(minutes=int(
            self.object.time[:2]), seconds=int(self.object.time[3:]))
        self.t2 = timedelta(minutes=0, seconds=seconds)
        # if time delta is less than 0 reset current time to 00:00
        self.object.time = self.dtime if (
            self.t1-self.t2).days < 0 else str(self.t1-self.t2)[2:]
