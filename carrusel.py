from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Carrusel Avengers')

def exit():
    respuesta = messagebox.askokcancel('Popup', 'Deseas salir?')
    if respuesta == True:
        root.quit()

def back(img_num):
    global l
    global btn_back
    global btn_next

    # se indica a la etiqueta que tiene que olvidar su contenido
    l.grid_forget()
    l = Label(root, image= lista[img_num])
    btn_next = Button(root, text='-->', command= lambda: back(img_num + 1 ))

    if img_num == 0:
        btn_back = Button(root, text='N/A', state=DISABLED)
    else:
        btn_back = Button(root, text='<--', command= lambda: back(img_num - 1))

    l.grid(row=0, column=0, columnspan=3)
    btn_next.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)
 

def next(img_num):
    global l
    global btn_back
    global btn_next

    # se indica a la etiqueta que tiene que olvidar su contenido
    l.grid_forget()
    l = Label(root, image= lista[img_num])
    btn_back = Button(root, text='<--', command= lambda: back(img_num -1 ))

    if img_num == 6:
        btn_next = Button(root, text='N/A', state=DISABLED)
    else:
        btn_next = Button(root, text='-->', command= lambda: next(img_num + 1))

    l.grid(row=0, column=0, columnspan=3)
    btn_next.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)
    

img1= ImageTk.PhotoImage(Image.open('images/BlackP.jpeg'))
img2= ImageTk.PhotoImage(Image.open('images/Hulk.jpeg'))
img3= ImageTk.PhotoImage(Image.open('images/BlackW.jpeg'))
img4= ImageTk.PhotoImage(Image.open('images/Thor.jpeg'))
img5= ImageTk.PhotoImage(Image.open('images/IronMan.jpeg'))
img6= ImageTk.PhotoImage(Image.open('images/Capitan.jpeg'))
img7= ImageTk.PhotoImage(Image.open('images/Spider.jpeg'))

lista = [img1, img2, img3, img4, img5, img6, img7]

l=Label(root, image=img1)
l.grid(row=0, column=0, columnspan=3)

btn_back = Button(root, text='N/A', state=DISABLED)
btn_next = Button(root, text='-->', command= lambda: next(1))
btn_next.grid(row=1, column=2)
btn_back.grid(row=1, column=0)

btn_exit= Button(root, text='exit', command= exit)
btn_exit.grid(row=2, column=1)


root.mainloop()
