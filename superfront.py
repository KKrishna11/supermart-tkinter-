from tkinter import *
from tkinter import font
from turtle import bgcolor, done, left, right, width
from unicodedata import category
from matplotlib.pyplot import fill, text
from numpy import pad, place, product
import pymysql
from tkinter import ttk
from tkinter import ttk
import turtle
from tkinter import *
from db import add_order_in_db, delete_product_from_db, get_order_details, get_products, insert_product_in_db, search_products, update_product_detail

mainwindow = None  #------------------------------------------------------------------------------------------------------------------main window 

def show_intro():
    def draw_circle(turtle, color, size, x, y): #--------------------------------------------------------------start from here (krishna :D)
        # logo.setup(400,400)
        turtle.speed(1)
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x,y)
        turtle.begin_fill()
        turtle.pendown()
        turtle.circle(size)
        turtle.penup()
        turtle.end_fill()
        turtle.pendown()

    logo = turtle.Turtle()
    # logo.shape("turtle")
    logo.speed(100)


    draw_circle(logo, "#BDB76B", 80, 25, 0)
    draw_circle(logo, "#906652", 80, 0, 0)
    draw_circle(logo, "#ECF3F9", 80, -25, 0)

    logo.penup()
    logo.goto(0,-50)
    logo.color('black')
    logo.write("WELCOME TO SUPERMART ", align="center", font=("Rockwell Condensed", 16, "bold"))
    logo.goto(0,-80)
    window=object = turtle.Screen()
    # window.setup(width=1,height=0.95)
    # krishna
    window.exitonclick()
        
show_intro()            #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def new_order():
    
    mainwindow.destroy()
    secondwindow=Tk()
    secondwindow.geometry("1600x1000")
    secondwindow.title("NEW ORDER ")
    secondwindow.configure(bg="#BDB76B")
    total_var = StringVar(secondwindow)
    customer_name_var = StringVar(secondwindow)
    # Add a Treeview widget---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # created frame for tree 
    frame=Frame(secondwindow)
    frame.place(x=0,y=20)
    frame.configure(bg="#BDB76B")
    tree2= ttk.Treeview(frame,column=("p1", "p2","p3","p4"), show= 'headings', height= 33) #----------------tree 2  
    s = ttk.Style()
    s.configure(tree2,background="#8fd7c3")
    tree2.column("# 1",anchor="s")
    tree2.heading("# 1", text= "PRODUCT ID")
    tree2.column("# 2", anchor= "s")
    tree2.heading("# 2", text= "PRODUCT NAME ")
    tree2.column("# 3", anchor= "s")
    tree2.heading("# 3", text="PRICE PER UNIT ")
    tree2.column('#4',anchor="s")
    tree2.heading("#4",text="QUANTITY")
    # Insert the data in Treeview widget--------------------------------------------------------- appending product in for loops 
    product_names = []
    for index, product in enumerate(get_products()):   #------------------ get product function cindb 
        product_names.append(product[1])
        tree2.insert('', index=index, iid=index, text= "1",values=(product[0], product[1], product[2], product[3]))
    tree2.pack(side="left",anchor=W,padx=0,pady=30)
    # scroll  setting     
    verticalbar=ttk.Scrollbar(frame,orient="vertical",command=tree2.yview)
    verticalbar.pack(side="right",fill='y') 
    tree2.configure(yscrollcommand=verticalbar.set)
    # scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=tree2.yview)
    # tree.configure(yscroll=scrollbar.set)
    # scrollbar.grid(row=0, column=1, sticky='ns')
    
    frame3=Frame(secondwindow,bg="#BDB76B")  #------------------------frame3
    frame3.pack(fill=X,expand=0)
    
    frame2=Frame(secondwindow,bg="#BDB76B")
    
    frame4=Frame(secondwindow,bg="#BDB76B") #-----------------------frame4
    frame4.pack(side="top",anchor=NE)
    
    frame5=Frame(secondwindow,bg="#BDB76B") #----------------------frame5
    frame5.pack(side="right",anchor=NE)
    
    frame6=Frame(secondwindow,bg="#BDB76B") #----------------------frame6
    frame6.place(x=1050,y=175)
    
    
    frame8=Frame(secondwindow,width = 1,height=1,bg="#BDB76B") #---------------frame8
    frame8.place(x=1200,y=290)
    
    frame7=Frame(secondwindow,bg="#BDB76B") #----------------------frame7
    frame7.place(x=1050,y=510)
    
    NAME=Label(frame3,text="Customer Name: ",font="calibri ",bg= "#BDB76B")
    NAME.pack(side="left")
    entry_name=Entry(frame3, textvariable=customer_name_var)
    entry_name.pack(side="left")
    EXbutton=Button(frame3,text="EXIT",command=lambda: exicut(secondwindow))
    EXbutton.pack(side="right",padx=20)
    
    Custome2r=Label(frame3,text="Total : ", font="calibri",bg= "#BDB76B")
    Custome2r.pack(side="left")
    Customer_nAME=Entry(frame3, textvariable=total_var)
    Customer_nAME.pack(side="left")
    
    def add_order():
        from datetime import datetime
        order_details = {
            'customer_name': customer_name_var.get(),
            'total': total_var.get(),
            'od_dt': datetime.today(),
            'order_details': cart
        }
        add_order_in_db(order_details)
        secondwindow.destroy()
        # display_main_window()
        backbutton_for_previous()
        
    
    addorder=Button(frame3,text="Add Order  ",font=("calibri",15,'bold'),command=add_order,bg="#BDB76B")
    addorder.pack(anchor=W,padx=50)
    frame2.pack(side="right",anchor="ne")
    
    
    done=StringVar()
    selected_product_var = StringVar(frame5)
    cart = []
    product=ttk.Combobox(frame5,width=35, textvariable=selected_product_var)
    product['values']=', '.join([name for name in product_names]).split(', ')
    product.pack(side="right",padx=50)
    product.current()
    
    product_label=Label(frame5,text="  PRODUCT ",font=("Calibri",20),bg= "#BDB76B")
    product_label.pack(side="top",padx=6,pady=20)

    category=ttk.Combobox(frame4,width=35,textvariable=done)
    category['values']=("All", "food","beverages","electronic","daily needs")
    category.set('All')
    category.pack(side="right",padx=50)
    category.current()
    
    category_label=Label(frame4,text="CATEGORY ",font=("Calibri",20),bg= "#BDB76B")
    category_label.pack(side="left",padx=6,pady=20)
    
    quantityvar=IntVar(frame6)
    
    quantity_entry=Entry(frame6,textvariable=quantityvar,width=35)
    quantity_entry.pack(side="right",pady=70,padx=68)
    
    quantity_label=Label(frame6,text="    QUANTITY",font=("Calibri",20),bg= "#BDB76B")
    quantity_label.pack(side="right",pady=80)
    
    cart_tree=ttk.Treeview(frame7,column=("cd1",'cd2'),show="headings",height=10)
    def add_to_cart():
        cart.append({
            "product_name": selected_product_var.get(),
            "quantity": quantityvar.get(),
        })
        cart_tree.insert('', index=len(cart)-1, iid=len(cart)-1, text="", values=(
            cart[-1]['product_name'], 
            cart[-1]['quantity'],
        ))
    
    add_to_cart_btn = Button(frame8, text="Add to Cart 🛒", font=("Calibri", 20,"bold"), bg="#BDB76B", command=add_to_cart)
    add_to_cart_btn.pack(side="right", pady=100)
    
    cart_tree.column("#1",anchor="s")
    cart_tree.heading("#1",text=" PRODUCT NAME : ")
    cart_tree.column("#2",anchor="s")
    cart_tree.heading("#2",text="QUANTITY")
    
      
    cart_tree.pack(side="right")
    
def exicut(sec):
    sec.destroy()
    

def mng_window():
    win=Tk()
    win.geometry('1600x900')
    win.configure(bg="#BDB76B")
    canvas=Canvas(win,width=1600,height=200,bg="#BDB76B")
    canvas.pack()
    canvas.create_line(0,140,1600,140,width=2)
    win.title('MANAGE PRODUCT')
    search_var = StringVar(win)
    # select colour 
    f1=Frame(win,bd=10,width=1600,height=70,relief=RIDGE).place(x=0,y=0)
    pname=Label(win,text='Product Name',font='arial 18',bg="#BDB76B").place(x=10,y=85)
    entrynm=Entry(win,font='arial 18',width=40,bd=5,textvariable=search_var).place(x=200,y=85)
    back=Button(win,text='Back',font='arial 18', command=backbutton_for_previous,bg="#906652",fg="white").place(x=1400,y=85)
    p1=StringVar(win)
    product_name=StringVar(win)
    price=StringVar(win)
    quantitystrorage=IntVar(win)
    categorystrorage=StringVar(win)    
    #button
    
    def search():
        print(search_products(search_var.get()))
    
    srch=Button(win,text='SEARCH',font='arial 18', command=search,bg="#906652",fg="white").place(x=750,y=85)
    m=Label(win,text='MANAGE PRODUCT',font=("Calibri", 25, "bold"),fg="black",bg="#BDB76B").place(x=660,y=8)
    #frame 
    tv = ttk.Treeview(win)
    
    f2=Frame(win,bd=10,width=680,height=550,relief=RIDGE,bg= "#BDB76B").place(x=820,y=210)
    pid=Label(win,text='Product ID',font='Calibri',bg="#BDB76B").place(x=870,y=240) 
    e1=Entry(win,font='arial 18',width=20,bd=3,textvariable=p1).place(x=1020,y=240)
    
    nm=Label(win,text='Product Name     ',font='Calibri',bg="#BDB76B").place(x=870,y=310)
    e2=Entry(win,font='arial 18',width=20,bd=3,textvariable=product_name).place(x=1020,y=310)
    
    pr=Label(win,text='Price',font='Calibri',bg="#BDB76B").place(x=890,y=500) 
    e4=Entry(win,font='arial 18',width=20,bd=3,textvariable=price).place(x=1020,y=500)
    
    
    # finaaly back  
    quantity_one_label=Label(win,text="Quantity",font="Calibri",bd=3,bg="#BDB76B").place(x=875,y=390)
    quantity_one_entry=Entry(win,font='arial 18',width=20,bd=3,textvariable=quantitystrorage).place(x=1020,y=390)
     
    category_one_label=Label(win,text="Category",font="Calibri",bd=3,bg="#BDB76B").place(x=875,y=450)
    category_one_entry=Entry(win,font='arial 18',width=20,bd=3,textvariable=categorystrorage).place(x=1020,y=450)
    #button
    def delete_product():
        id = p1.get()
        try:
            delete_product_from_db(int(id))
        except:
            print("Enter int")
            pass

    def insert_product():
        productadd=p1.get()
        productnameadd=product_name.get()
        productpriceadd=price.get()
        product_quantity=quantitystrorage.get()
        product_category=categorystrorage.get()
        product = {'product_id': productadd, 'product_name': productnameadd, 'price': productpriceadd, 'quantity': product_quantity, 'category': product_category}
        insert_product_in_db(product)
        index = len(tv.get_children()) + 1
        tv.insert(parent='', index=index, iid=index, text='', values=(
            product['product_id'],
            product['product_name'],
            product['price'], 
            product['quantity'], 
            product['category'])
        )
    
    def update_product():
        productadd=p1.get()
        productnameadd=product_name.get()
        productpriceadd=price.get()
        product_quantity=quantitystrorage.get()
        product_category=categorystrorage.get()
        details = {'product_name': productnameadd, 'price': productpriceadd, 'quantity': product_quantity}
        update_product_detail(productadd, details)
        
        mng_window()
        
        # sys.exit(0)
        
        
         
    ad=Button(win,text='ADD',font='arial 22',command=insert_product,bg="#906652").place(x=900,y=570)
    d=Button(win,text='DELETE',font='arial 22', command=delete_product,bg="#906652").place(x=1300,y=570)
    U=Button(win,text='UPDATE',font='arial 22', command=update_product,bg="#906652").    place(x=1080,y=570)
    
    # product_frame = Frame(win, bd=10, width=700, height=550, relief=RIDGE, bg="#FF00FF").place(x=10, y=200)
    tv['columns']=('Product Id', 'Product Name', 'Price', 'Quantity', 'Category')  #---------------------------------------------------------------tv as tree 3
    tv.column('#0', width=0, stretch=NO)
    tv.column('Product Id', anchor=CENTER, width=54, stretch=True)
    tv.column('Product Name', anchor=CENTER, width=54)
    tv.column('Price', anchor=CENTER, width=54)
    tv.column('Quantity', anchor=CENTER, width=54)
    tv.column('Category', anchor=CENTER, width=54)  

    tv.heading('#0', text="", anchor=CENTER)
    tv.heading('Product Id', text='Product Id', anchor=CENTER)
    tv.heading('Product Name', text='Product Name', anchor=CENTER)
    tv.heading('Price', text='Price', anchor=CENTER)
    tv.heading('Quantity', text='Quantity', anchor=CENTER)
    tv.heading('Category', text='Category', anchor=CENTER)

    for index, product in enumerate(get_products()):
        tv.insert(parent='', index=index, iid=index, text='', values=(product[0],product[1],product[2], product[3], product[4]))
    tv.pack(anchor=W, fill='y', expand=0, padx=20, pady=20, ipadx=250, ipady=120)
    
    win.mainloop()

def backbutton_for_previous():
    def display_main_window():
        global mainwindow
        mainwindow=Tk()
        mainwindow.geometry('1600x1000')
        mainwindow.title('SUPERMARKET ')
        # select color 
        mainwindow.configure(bg="#BDB76B")  #FDE5B4,bg="#f88379
        SCREEN_WIDTH = 1600
        opframe=Frame(mainwindow,bd=10,width=SCREEN_WIDTH,height=100,relief=RIDGE,bg='#ECF3F9').place(x=0,y=1)
        sup=Label(mainwindow,text='SUPERMART 🏪',font=("Calibri", 35, "bold"),bg="#ECF3F9",fg="black")
        sup.place(x=SCREEN_WIDTH*0.5 - 160,y=15)

        def matplotlib_not_working_full_screen(): #-----------------------------------------------------------matplotlib
            
            import numpy as np
            import matplotlib.pyplot as plt
            # creating the dataset
            data = {'food':10,'beverages':2, 'daily needs':2,
                    'electronic':1}
            category = list(data.keys())
            values = list(data.values())
            
            fig = plt.figure(figsize = (10, 5))
            
            # creating the bar plot
            plt.bar(category, values, color ='maroon',
                    width = 0.4)
            
            plt.xlabel("CATEGORY SOLD DAILY ")
            plt.ylabel("CATEGORY SOLD UNIT ")
            plt.title("SUPERMARKET ANALYSIS ")
            plt.show()
            
            
            # import matplotlib.pyplot as plt
            # import numpy as np
            # x = np.array(["ORDER NO ", "600 rs", "500 rs ", "400 rs ","300 rs", "200 rs ", "100 rs ","50","20","10",])
            # y = np.array([9, 8, 1, 1,1,1,1,1,1,1])
            # fig = plt.figure(figsize = (10, 9))
            # plt.xlabel("CATEGORY SOLD DAILY ")
            # plt.ylabel("CATEGORY SOLD UNIT ")
            # plt.title("SUPERMARKET  CUSTOMER AND ORDER ANALYSIS ")
            # plt.barh(x, y)
            # plt.show()
        
        
        ana=Button(mainwindow,text='ANALYTICS',font='arial 15', bg="#906652",fg="white",command=matplotlib_not_working_full_screen).place(x=100,y=150)

        mng=Button(mainwindow,text='MANAGE',font='arial 15',command=mng_window, bg="#906652",fg="white").place(x=900,y=150)

        od=Button(mainwindow,text='NEW ORDER',font='arial 15',command=new_order, bg="#906652",fg="white").place(x=1200,y=150)
        s = ttk.Style()
        # s.configure("Treeview",background="#24282f")
        ttk.Style().configure("Treeview", background="#383838",
        foreground="white", fieldbackground="red")
        # Add a Treeview widget
        tree= ttk.Treeview(mainwindow, column=("c1", "c2","c3","c4"),show= 'headings', height= 8) #-----------------------------------------tree 1
        tree.column("# 1",anchor="s")
        tree.heading("# 1", text= "ORDER NO ")
        tree.column("# 2", anchor= "s")
        tree.heading("# 2", text= "CUSTOMER  NAME ")
        tree.column("# 3", anchor= "s")
        tree.heading("# 3", text="TOTAL COST ")
        tree.column('#4',anchor="s")
        tree.heading("#4",text="DATE")
        # Insert the data in Treeview widget

        for index, order_details in enumerate(get_order_details()):
            print(order_details)
            tree.insert('', index=index, iid=index, text="", values=(
                order_details[0], 
                order_details[1], 
                order_details[2], 
                order_details[3]
            ))

        tree.pack(side="bottom", fill="both",expand=0,ipady=100,pady=200,padx=50)
        erticalbar=ttk.Scrollbar(orient="vertical",command=tree.yview)
        erticalbar.pack(side="right",fill='y') 
        tree.configure(yscrollcommand=erticalbar.set)
        mainwindow.mainloop()
        global display_main_window
    display_main_window()
backbutton_for_previous()