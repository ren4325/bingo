import random

num = 0
b = []
c = []
d = []

a = [x for x in range(1, 76, 1)]

def Newnum():
    num = random.choice(a)

    a.remove(num)

    if len(b) == 25:
        if len(c) == 25:
            d.append(num)
        else:
            c.append(num)
            
    else:
        b.append(num)

    #数字を表示
    new = tkinter.Label(text = num, font = ("MSゴシック", "200"))
    new.side = tkinter.RIGHT
    new.place(x = 500, y = 100)

    #履歴を表示
    lognum = tkinter.Label(text = (b), font = ("MSゴシック", "25"))
    lognum.place(x = 90, y = 400)

    lognum = tkinter.Label(text = (c), font = ("MSゴシック", "25"))
    lognum.place(x = 90, y = 450)

    lognum = tkinter.Label(text = (d), font = ("MSゴシック", "25"))
    lognum.place(x = 90, y = 500)



#---GUI---

import tkinter

root = tkinter.Tk()

root.title("BINGO")
root.state("zoomed")

#ボタン
btn = tkinter.Button(text = "BINGO", command = Newnum,width = 30, height = 5, bg = "red")
btn.pack(side = tkinter.BOTTOM)

root.mainloop()