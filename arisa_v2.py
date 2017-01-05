from time import time, sleep, localtime
import datetime


# TODO: build a manager for this, for now creating each instance will do...
# think of an alternate way to do this with sleep being the primary way
# to change the timebar, again 60 ticks will work perfectly, no reason to change it



class Timebar:
    INC = '~'
    DONE = '#'

    def __init__(self, dur):
        self.dur = dur
        self.tb = Timebar.INC * 60
        self.curr_time = int(time())
        self.next_update = self.curr_time + self.time_increment()
        self.end_time = self.curr_time + self.dur * 60
        # self.increment = int(len(self.tb)//self.dur)


    def update_tb(self, tick_inc):
        # updates timebar
        if self.to_update_check():
            self.tb = self.tb[:self.tb.find(Timebar.INC)] \
            + Timebar.DONE * tick_inc \
            + self.tb[self.tb.find(Timebar.INC) + tick_inc:]

            self.set_update(self.time_increment())
        else:
            pass

    def to_update_check(self):
        # check to see if you need to update the timabar
        return int(time()) == self.next_update

    def time_increment(self):
        # time increment to update 1 tick
        return int((self.dur * 60) // len(self.tb))
        
    def set_update(self, inc):
        # sets the time for when the next tick will change on the timebar
        if self.next_update <= self.end_time:
            self.next_update += inc

    def run(self):
        #runs the timebar
        while time() <= self.end_time:
            a = localtime()
            self.update_tb(1)
            print("   ",self.dur,'[' + self.tb + ']', datetime.time(a.tm_hour, a.tm_min, a.tm_sec), end = '\r')
            sleep(0.01)
        print("\n")


if __name__ == '__main__':
    s = Timebar(25).run()
    t = Timebar(5).run()
    u = Timebar(25).run()
    v = Timebar(5).run()
    w = Timebar(25).run()
    x = Timebar(5).run()
    y = Timebar(25).run()
    z = Timebar(30).run()