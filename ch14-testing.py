'''
14-1

from Tkinter import *

def closewindow(window):
    window.destroy()

window = Tk()

label = Label(window, text = 'lable')
label.pack(side ='left')

buttonClose = Button(window, text='Good bye!',command= lambda:closewindow(window))
buttonClose.pack(side = 'right')

window.mainloop()
'''
'''
14-2

from Tkinter import *

if __name__ =='__main__':

    window = Tk()

    frame = Frame(window)
    frame.pack(side='left')

    Num = IntVar()
    Num.set(0)

    button= Button(frame,textvariable = Num, font = ('Courier',20,'bold italic'),
                   bg = 'green',fg= 'white',
                   command = lambda: Num.set(Num.get()+1) )
    button.pack(side='left')

    window.mainloop()
'''
'''
14-4

from Tkinter import *

def countNum(str):
    print str
    a_count.set(0)
    t_count.set(0)
    c_count.set(0)
    g_count.set(0)
    for s in str:
        if s =='T':
            t_count.set(t_count.get()+1)
        elif s == 'A':
            a_count.set(a_count.get()+1)
        elif s == 'C':
            c_count.set(c_count.get()+1)
        else:
            g_count.set(g_count.get()+1)


if __name__ =='__main__':

    window = Tk()

    frame= Frame(window,bg= 'blue')
    frame.pack()

    lable_e = Label(frame,text ='DNA:')
    lable_e.grid(row= 0,column = 0)

    dnastr= StringVar()
    dnastr.set('ATCGG')
    entry = Entry(frame,textvariable = dnastr)
    entry.grid(row= 0,column = 1)

    a_count = IntVar()
    a_count.set(0)
    t_count = IntVar()
    t_count.set(0)
    c_count = IntVar()
    c_count.set(0)
    g_count = IntVar()
    g_count.set(0)

    lable_a = Label(frame,text ='A:')
    lable_a.grid(row= 1,column = 0)
    lable_a1 = Label(frame,textvariable =a_count)
    lable_a1.grid(row= 1,column = 1)
    lable_c = Label(frame,text ='C:')
    lable_c.grid(row= 2,column = 0)
    lable_c1 = Label(frame,textvariable =c_count)
    lable_c1.grid(row= 2,column = 1)
    lable_t = Label(frame,text ='T:')
    lable_t.grid(row= 3,column = 0)
    lable_t1 = Label(frame,textvariable =t_count)
    lable_t1.grid(row= 3,column = 1)
    lable_g = Label(frame,text ='G:')
    lable_g.grid(row= 4,column = 0)
    lable_g1 = Label(frame,textvariable =g_count)
    lable_g1.grid(row= 4,column = 1)

    button = Button(frame,text ='Count',command=lambda:countNum(dnastr.get()))
    #button.grid(row = 0,column = 1)
    button.grid(row= 5,column = 1)
    window.mainloop()
'''
'''
14-5
'''
import Tkinter

def coverttmp(string):
    print string
    tmpf = float(string)
    temp_value.set((tmpf-100)/5.0)
def windowquit(root):
    root.destroy()

if __name__ == '__main__':

    window = Tkinter.Tk()

    frame = Tkinter.Frame(window)
    frame.pack()

    lable = Tkinter.Label(frame,text = 'Temperature in Fahrenheit')
    lable.grid(row = 0, column = 0)

    temp_value = Tkinter.StringVar()
    temp_value.set('0.0')

    entry = Tkinter.Entry(frame, textvariable = temp_value )
    entry.grid(row = 1, column = 0)

    button_c = Tkinter.Button(frame, text = 'Convert',command = lambda:coverttmp(temp_value.get()))
    button_c.grid(row = 2, column = 0)

    button_q = Tkinter.Button(frame, text = 'Quit',command = lambda:windowquit(window))
    button_q.grid(row = 3, column = 0)

    window.mainloop()


