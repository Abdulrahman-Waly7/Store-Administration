from tkinter import *
from tkinter import ttk
from manager_databases.products_db import ProductsDatabase
import json
from subprocess import Popen
#-------------------------- إنشاء نافذة البرنامج ----------------------------
root = Tk()
width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())
root.state('zoomed')
root.title('Company Name')
root.config(bg='#ABB2B9')


#---------------------------- إنشاء المتغيرات ------------------------------------
search_icon = PhotoImage(file='images\\search_icon.png')
add_icon = PhotoImage(file='images\\add_icon.png')
back_icon = PhotoImage(file='images\\left_arrow.png')
search = PhotoImage(file='images\\search.png')

pro_db = ProductsDatabase('login_signup_page\\databases\\products_db.db')

id = IntVar()
name = StringVar()
count = StringVar()
buy_price = StringVar()
low_sell_price = StringVar()
sell_price = StringVar()
trader = StringVar()
date_of_buy = StringVar()


#---------------------------- إنشاء الدوال ----------------------------------------
def get_data(event):
    selected_row = products_table.focus()
    data = products_table.item(selected_row)
    global row
    row = data['values']
    return row


def save(e):
    data = get_data(e)
    with open('data_file.json', 'w') as wf:
        json.dump(data, wf)
    Popen(['python', 'login_signup_page\\update_product.py'])
    quit()

    
def display_all():
    load()
    products_table.delete(*products_table.get_children())
    for row in products_table.fetch():
        products_table.insert('', END, values=row)

def delete():
    pro_db.remove(row[0])
    display_all()

def search_componenets():
    search_combo = ttk.Combobox(downside_frame, justify='right', state='readonly')
    search_combo['values'] = ('الاسم', 'الصنف', 'الكود', 'المورد')
    search_combo.place(x=downside_frame_width*.8, y=downside_frame_height*.1, width=downside_frame_width*.1)
    search_entry = Entry(downside_frame, fg='#117A65')
    search_entry.place(x=downside_frame_width*.64, y=downside_frame_height*.1, width=downside_frame_width*.15)
    search_button = Button(downside_frame, image=search, bg='#117A65', bd=0, cursor='hand2', command=root.search_componenets)
    search_button.place(x=downside_frame_width*.61, y=upside_frame_height*.1)

def display_all():
    load()
    products_table.delete(*products_table.get_children())
    for row in pro_db.fetch():
        products_table.insert('', END, values=row)

def load():
    global data, got_date, got_trader, got_sell_price, got_low_sell_price, got_buy_price, got_count, got_name, got_id
    with open('data_file.json', 'r') as rf:
        data = json.load(rf)
    if data != []:
        got_date, got_trader, got_sell_price, got_low_sell_price, got_buy_price, got_count, got_name, got_id= data
        got_id
        name.set(got_name)
        count.set(got_count)
        buy_price.set(got_buy_price)
        low_sell_price.set(got_low_sell_price)
        sell_price.set(got_sell_price)
        trader.set(got_trader)
        date_of_buy.set(got_date)
        pro_db.update(
            got_id, got_name, got_count, got_buy_price, got_low_sell_price, got_sell_price, got_trader, got_date
        )


#------------------Upside Frame ---------------------------
upside_frame = Frame(root, bg='#117A65')
upside_frame_height = height*.05
upside_frame_width = width
upside_frame.place(x=0, y=0, width=upside_frame_width, height=upside_frame_height)

logo_img = PhotoImage(file='images\\logos\\products.png')
logo = Label(upside_frame, image=logo_img, bg='#117A65')
logo.place(x=upside_frame_width*.95, y=1)

back_btn = Button(upside_frame, image=back_icon, bg='#117A65', bd=0)
back_btn.place(x=upside_frame_width*.005, y=upside_frame_height*.15)


#-------------- Downside Frame -------------------------------
downside_frame = Frame(root, bg='#117A65')
downside_frame_height = height*.12
downside_frame_width = width
downside_frame.place(x=0, y=height*.88, width=downside_frame_width, height=downside_frame_height)

def add_product_page():
    other_script_path = 'login_signup_page\\add_product.py'
    Popen(['python', 'login_signup_page\\add_product.py'])
    quit()

add_button = Button(downside_frame, image=add_icon, bg='#117A65', bd=0, cursor='hand2', command=add_product_page)
add_button.place(x=downside_frame_width*.96, y=upside_frame_height*.1)
search_button = Button(downside_frame, image=search_icon, bg='#117A65', bd=0, cursor='hand2')
search_button.place(x=downside_frame_width*.92, y=upside_frame_height*.1)
#------------------ View Frame ------------------------------
show_frame = Frame(root, bg='#ABB2B9')
show_frame_width = width
show_frame_height = height-upside_frame_height-downside_frame_height
show_frame.place(x=0, y=upside_frame_height, width=show_frame_width, height=show_frame_height)

scroll_y = Scrollbar(show_frame, orient=VERTICAL, width=20)
products_table = ttk.Treeview(show_frame,
                            columns=('date_of_buy', 'trader', 'sell_price', 'low_sell_price', 'buy_price', 'count', 'name','id'),
                            yscrollcommand=scroll_y.set)
products_table.place(x=0, y=0, width= show_frame_width-20, height=show_frame_height)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=products_table.yview)

products_table['show'] = 'headings'
products_table.heading('date_of_buy', text='تاريخ الشراء')
products_table.heading('trader', text='المورد')
products_table.heading('sell_price', text='سعر البيع قطاعي')
products_table.heading('low_sell_price', text='سعر البيع جملة')
products_table.heading('buy_price', text='سعر الشراء')
products_table.heading('count', text='عدد القطع')
products_table.heading('name', text='اسم المنتج')
products_table.heading('id', text='ID')


display_all()
products_table.bind('<ButtonRelease-1>', save)


root.mainloop()