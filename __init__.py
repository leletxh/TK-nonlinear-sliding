from decimal import Decimal
import time
from tkinter import *
def move(currently_x,currently_y,to_x,to_y,n,win,debug = False,sleep = 0.01,wait_on_startup = True) -> None:
    if debug:
        print("start sliding")
    if wait_on_startup:
        time.sleep(0.5)
    while(not((Decimal(str(currently_x)).quantize(Decimal("0")) == to_x)and(Decimal(str(currently_y)).quantize(Decimal("0")) == to_y))):
        x = (to_x - currently_x)/5
        y = (to_y - currently_y)/5
        currently_x = currently_x+x
        currently_y = currently_y+y
        n.place(y=currently_x, x=currently_y)
        if debug:
            print(to_x + x,to_y + y)
        win.update()
        time.sleep(sleep)
    if debug:
        print("Stop sliding")
    n.place(y=to_x, x=to_y)
    win.update()
