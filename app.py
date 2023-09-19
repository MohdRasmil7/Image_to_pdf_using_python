from tkinter import *
from tkinter.filedialog import askopenfile,asksaveasfile,asksaveasfilename,askopenfilenames
from PIL import Image
import img2pdf as img2pdf


window=Tk()
window.title("Image to pdf app")
window.configure(background="#80578f")
window.geometry("600x600")
#image upload


def img_upload():
    #img path(opening and converting)
    global file_path
    file_path=askopenfile(multiple=TRUE,mode='r',filetypes=[('Image Files', '*.jpeg *.png *.jpg')])
    if file_path:
        img = Image.open(file_path.name)

        #pdf path (saving)
        pdf_path = asksaveasfile(defaultextension=".pdf",filetypes=[('PDF Files','*.pdf')])
        if pdf_path:
            pdf_path=pdf_path.name
            img.save(pdf_path)
            print("image converted to {pdf_path}")


    

#title
title=Label(text="Image To Pdf convertor",background="#80578f",fg="#2f4f4a",font=('opensans 30 bold italic'))
title.place(x=30,y=20)


#file open button
open_img=Button(window,text="click to upload image",fg='#2f4f4a',font=('opensans 25 bold italic'),background='#949096',bd=10,command=lambda:[img_upload()])
open_img.place(x=100,y=250)






window.mainloop()