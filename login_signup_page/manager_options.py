from tkinter import *
from subprocess import Popen
from databases.master_db import Database
from databases.managers_db import ManagersDatabase
from databases.employees_db import EmployeesDatabase

root = Tk()

width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())
root.state('zoomed')
root.title('Company Name')
root.config(bg='#ABB2B9')


#---------------------------- variables -----------------------------
products_img = PhotoImage(file='images\\products.png')
items_img = PhotoImage(file='images\\items.png')
selling_bill_img = PhotoImage(file='images\\selling_bill.png')
buying_bill_img = PhotoImage(file='images\\buying_bill.png')
money_lock_img = PhotoImage(file='images\\money_lock.png')
expenses_img = PhotoImage(file='images\\expenses.png')
storage_img = PhotoImage(file='images\\storage.png')

products_path = 'login_signup_page\\manager_options\\products.py'

#---------------------------- Functions -----------------------------
def products_page():
    Popen(['python', products_path])
    quit()

def options2():
    customers_btn = Button(root, text='العملاء', image=items_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    customers_btn.place(x=width*.1, y=height*.02, width=width*.2, height=height*.2)
    traders_btn = Button(root, text='الموردون', image=items_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    traders_btn.place(x=width*.7, y=height*.02, width=width*.2, height=height*.2)
    reports_btn = Button(root, text='تقارير نهائية', image=items_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    reports_btn.place(x=width*.1, y=height*.32, width=width*.2, height=height*.2)
    storage_btn = Button(root, text='تقارير المخزن', image=storage_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    storage_btn.place(x=width*.7, y=height*.32, width=width*.2, height=height*.2)
    calculator_btn = Button(root, text='الآلة الحاسبة', image=items_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    calculator_btn.place(x=width*.1, y=height*.62, width=width*.2, height=height*.2)
    settings_btn = Button(root, text='الإعدادات', image=items_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    settings_btn.place(x=width*.7, y=height*.62, width=width*.2, height=height*.2)

def options1():
    products_btn = Button(root, text='الأصناف', image=items_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    products_btn.place(x=width*.1, y=height*.02, width=width*.2, height=height*.2)
    types_btn = Button(root, text='المنتجات', image=products_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'), command=products_page)
    types_btn.place(x=width*.7, y=height*.02, width=width*.2, height=height*.2)
    sales_btn = Button(root, text='المشتريات', image=buying_bill_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    sales_btn.place(x=width*.1, y=height*.32, width=width*.2, height=height*.2)
    buys_btn = Button(root, text='المبيعات', image=selling_bill_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    buys_btn.place(x=width*.7, y=height*.32, width=width*.2, height=height*.2)
    money_btn = Button(root, text='المصروفات', image=money_lock_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    money_btn.place(x=width*.1, y=height*.62, width=width*.2, height=height*.2)
    expenses_btn = Button(root, text='الصندوق', image=expenses_img, compound=TOP, fg='#117A65', bg='#ABB2B9', cursor='hand2', font=('tajawal', 12, 'bold'))
    expenses_btn.place(x=width*.7, y=height*.62, width=width*.2, height=height*.2)

options1()
round_button = PhotoImage(file='images\\options_button.png')
options1_btn = Button(root, image=round_button, bd=0, bg='#ABB2B9', command=options2)
options1_btn.place(x=width*.48, y=height*.9, width=10, height=10)

options2_btn = Button(root, image=round_button, bd=0, bg='#ABB2B9', command=options1)
options2_btn.place(x=width*.52, y=height*.9, width=10, height=10)

root.mainloop()