from tkinter import*

window = Tk()
window.title('hello kitty')
window.geometry('260x245+400+200')

def input_into_entry(symbol):
    entry.insert(END, symbol)
    
def clear():
    entry.delete(0, END)
def count_result():
    text = entry.get()
    result = 0
    if '+' in text:
        splitted_txt = text.split('+')
        first = float(splitted_txt[0])
        second = float(splitted_txt[1])
        result = first + second
        
    if '-' in text:
        splitted_txt = text.split('-')
        first = float(splitted_txt[0])
        second = float(splitted_txt[1])
        result = first - second
        
    if '*' in text:
        splitted_txt = text.split('*')
        first = float(splitted_txt[0])
        second = float(splitted_txt[1])
        result = first * second

    if '/' in text:
        splitted_txt = text.split('/')
        first = float(splitted_txt[0])
        second = float(splitted_txt[1])
        result = first / second
    clear()
    entry.insert(0, result)



entry = Entry(window, width=15, font =('',20))
entry.place(x = 0, y = 0)

btn1 = Button(window, bg='pink' , fg = 'black', text = '1', command = lambda : input_into_entry('1'))
btn1.place(x = 0, y = 40, width = 50, height = 50)

btn2 = Button(window, bg='pink' , fg = 'black', text = '2', command = lambda : input_into_entry('2'))
btn2.place(x = 50, y = 40, width = 50, height = 50)

btn3 = Button(window, bg='pink' , fg = 'black', text = '3', command = lambda : input_into_entry('3'))
btn3.place(x = 100, y = 40, width = 50, height = 50)

btn4 = Button(window, bg='pink' , fg = 'black', text = '4', command = lambda : input_into_entry('4'))
btn4.place(x = 0, y = 90, width = 50, height = 50)

btn5 = Button(window, bg='pink' , fg = 'black', text = '5', command = lambda : input_into_entry('5'))
btn5.place(x = 50, y = 90, width = 50, height = 50)

btn6 = Button(window, bg='pink' , fg = 'black', text = '6', command = lambda : input_into_entry('6'))
btn6.place(x = 100, y = 90, width = 50, height = 50)

btn7 = Button(window, bg='pink' , fg = 'black', text = '7', command = lambda : input_into_entry('7'))
btn7.place(x = 0, y = 140, width = 50, height = 50)

btn8 = Button(window, bg='pink' , fg = 'black', text = '8', command = lambda : input_into_entry('8'))
btn8.place(x = 50, y = 140, width = 50, height = 50)

btn9 = Button(window, bg='pink' , fg = 'black', text = '9', command = lambda : input_into_entry('9'))
btn9.place(x = 100, y = 140, width = 50, height = 50)

btn0 = Button(window, bg='pink' , fg = 'black', text = '0', command = lambda : input_into_entry('0'))
btn0.place(x = 0, y = 190, width = 50, height = 50)

btnpl = Button(window, bg='pink' , fg = 'black', text = '+', command = lambda : input_into_entry('+'))
btnpl.place(x = 150, y = 40, width = 50, height = 50)

btnmi = Button(window, bg='pink' , fg = 'black', text = '-', command = lambda : input_into_entry('-'))
btnmi.place(x = 150, y = 90, width = 50, height = 50)

btnum = Button(window, bg='pink' , fg = 'black', text = 'x', command = lambda : input_into_entry('*'))
btnum.place(x = 150, y = 140, width = 50, height = 50)

btnra = Button(window, bg='pink' , fg = 'black', text = ':', command = lambda : input_into_entry('/'))
btnra.place(x = 150, y = 190, width = 50, height = 50)

btnc = Button(window, bg='pink' , fg = 'black', text = 'C', command = clear)
btnc.place(x = 100, y = 190, width = 50, height = 50)

btnza = Button(window, bg='pink' , fg = 'black', text = ',', command = lambda : input_into_entry(','))
btnza.place(x = 50, y = 190, width = 50, height = 50)

btnre = Button(window, bg='pink' , fg = 'black', text = '= (uwu)', command = count_result)
btnre.place(x = 200, y = 40, width = 50, height = 200)


window.mainloop()