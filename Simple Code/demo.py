import schedule
import time


def ok():
    print("Hello")


schedule.every(1).seconds.do(ok)
