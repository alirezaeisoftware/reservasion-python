from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from myclass import *
item=-1
def creat_win(win_title):
    w=Toplevel()
    w.geometry('450x450+400+400')
    w.title(win_title)
    return w
def creat_lb_entry(win_name,lb_txt,r,c):
    Label(win_name,text=lb_txt).grid(row=r,column=c)
    ent=Entry(win_name)
    ent.grid(row=r,column=c+1)
    return ent
def creat_2button(win_name,txt_button,r,c):
    Button(win_name,text='Back',command=lambda :win_name.destroy()).grid(row=r,column=c)
    bnt=Button(win_name,text=txt_button)
    bnt.grid(row=r,column=c+1)
    return bnt 
def creat_listbox(classname,win,txt_lb,r,c):
    Label(win,text=txt_lb).grid(row=r,column=c)
    lstobject=classname.open_file()
    lstvar=StringVar(value=lstobject)
    lstbox=Listbox(win,listvariable=lstvar,justify='right')
    lstbox.grid(rowspan=r+4,column=c)
    return lstbox,lstobject
win=Tk()
win.geometry('500x300+200+200')
win.title('نوبت دهی')
menubar=Menu()
win.config(menu=menubar)

patientmenu=Menu(tearoff=0)
doctormenu=Menu(tearoff=0)
prescription=Menu(tearoff=0)
def newPatient():
    win_add=creat_win('ثبت بیمار جدید')
    entname=creat_lb_entry(win_add,'نام', 0, 0)
    entfamil=creat_lb_entry(win_add,'فامیل', 1, 0)
    bntadd=creat_2button(win_add, 'ثبت', 3, 0)
    def fadd():
        name=entname.get()
        famil=entfamil.get()
        c=Patient(name, famil)
        c.save()
        messagebox.showinfo('ثبت','ثبت با موفقیت انجام شد')
        win_add.destroy()
    bntadd.config(command=fadd)
def editPatient():
    win_edit=creat_win('ویرایش بیماران')
    lstbox,lstobject=creat_listbox(Patient, win_edit,'لیست بیماران', 0, 0)
    entnewname=creat_lb_entry(win_edit,'نام', 1, 1)
    entnewfamil=creat_lb_entry(win_edit,'فامیل', 2, 1)
    bntedit=creat_2button(win_edit,'ویرایش', 4, 1)
    def fedit():
        global item
        newname=entnewname.get()
        newfamil=entnewfamil.get()
        lstobject[item].edit(newname,newfamil)
        messagebox.showinfo('ویرایش','ویرایش با موفقیت انجام شد')
        win_edit.destroy()
    bntedit.config(command=fedit)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entnewname.config(textvariable=nameval)
        entnewfamil.config(textvariable=StringVar(value=lstobject[item].famil))
    lstbox.bind('<<ListboxSelect>>',fselect)
def deletePatient():
    win_delete=creat_win('حذف بیماران')
    lstbox,lstobject=creat_listbox(Patient, win_delete,'لیست بیماران', 0, 0)
    entnewname=creat_lb_entry(win_delete,'نام', 1, 1)
    entnewfamil=creat_lb_entry(win_delete,'فامیل', 2, 1)
    bntedit=creat_2button(win_delete,'حذف', 4, 1)
    def fdelete():
        global item
        newname=entnewname.get()
        newfamil=entnewfamil.get()
        lstobject[item].delete(newname,newfamil)
        messagebox.showinfo('حذف','حذف با موفقیت انجام شد')
        win_delete.destroy()
    bntedit.config(command=fdelete)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entnewname.config(textvariable=nameval)
        entnewfamil.config(textvariable=StringVar(value=lstobject[item].famil))
    lstbox.bind('<<ListboxSelect>>',fselect)

def newDocter():
    win_add=creat_win('ثبت دکتر جدید')
    entname=creat_lb_entry(win_add,'نام', 0, 0)
    entfamil=creat_lb_entry(win_add,'فامیل', 1, 0)
    entcode=creat_lb_entry(win_add,'کد نظام پزشکی', 2, 0)
    bntadd=creat_2button(win_add, 'ثبت', 3, 0)
    def fadd():
        name=entname.get()
        famil=entfamil.get()
        code=entcode.get()
        c=Docter(name, famil , code)
        c.save()
        messagebox.showinfo('ثبت','ثبت با موفقیت انجام شد')
        win_add.destroy()
    bntadd.config(command=fadd)

def editDocter():
    win_edit=creat_win('ویرایش پزشکان')
    lstbox,lstobject=creat_listbox(Docter, win_edit,'لیست پزشکان', 0, 0)
    entnewname=creat_lb_entry(win_edit,'نام', 1, 1)
    entnewfamil=creat_lb_entry(win_edit,'فامیل', 2, 1)
    entnewcode=creat_lb_entry(win_edit,'کد نظام پزشکی', 3, 1)
    bntedit=creat_2button(win_edit,'ویرایش', 4, 1)
    def fedit():
        global item
        newname=entnewname.get()
        newfamil=entnewfamil.get()
        newcode=entnewcode.get()
        lstobject[item].edit(newname,newfamil,newcode)
        messagebox.showinfo('ویرایش','ویرایش با موفقیت انجام شد')
        win_edit.destroy()
    bntedit.config(command=fedit)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entnewname.config(textvariable=nameval)
        entnewfamil.config(textvariable=StringVar(value=lstobject[item].famil))
        entnewcode.config(textvariable=StringVar(value=lstobject[item].code))
    lstbox.bind('<<ListboxSelect>>',fselect)

def deleteDocter():
    win_delete=creat_win('حذف پزشک')
    lstbox,lstobject=creat_listbox(Docter, win_delete,'لیست پزشکان', 0, 0)
    entnewname=creat_lb_entry(win_delete,'نام', 1, 1)
    entnewfamil=creat_lb_entry(win_delete,'فامیل', 2, 1)
    entnewcode=creat_lb_entry(win_delete,'کد نظام پزشکی', 3, 1)
    bntedit=creat_2button(win_delete,'حذف', 4, 1)
    def fdelete():
        global item
        newname=entnewname.get()
        newfamil=entnewfamil.get()
        newcode=entnewcode.get()
        lstobject[item].delete(newname,newfamil,newcode)
        messagebox.showinfo('حذف','حذف با موفقیت انجام شد')
        win_delete.destroy()
    bntedit.config(command=fdelete)
    def fselect(event):
        global item
        item=lstbox.curselection()[0]
        nameval=StringVar(value=lstobject[item].name)
        entnewname.config(textvariable=nameval)
        entnewfamil.config(textvariable=StringVar(value=lstobject[item].famil))
        entnewcode.config(textvariable=StringVar(value=lstobject[item].code))
    lstbox.bind('<<ListboxSelect>>',fselect)
patientmenu.add_command(label='گرفتن نوبت ')
patientmenu.add_command(label='ثبت بیمار جدید',command=newPatient)
patientmenu.add_command(label='ویرایش بیمار' , command=editPatient)
patientmenu.add_command(label='حذف بیمار' , command=deletePatient)

doctormenu.add_command(label='اضافه کردن نوبت')
doctormenu.add_command(label='ثبت دکتر جدید' , command=newDocter)
doctormenu.add_command(label='ویرایش دکتر' , command=editDocter)
doctormenu.add_command(label='حدف دکتر' , command=deleteDocter)


prescription.add_command(label='نشان دادن تجویز')



menubar.add_cascade(label='بیمار',menu=patientmenu)
menubar.add_cascade(label='دکتر',menu=doctormenu)
menubar.add_cascade(label='تجویز',menu=prescription)
win.mainloop()