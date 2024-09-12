from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "red"
        title = Label(self.root, text="Billing Software", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="red", fg="gold", relief=GROOVE)
        title.pack(fill=X)
        
    # ================tiffin=======================
    
        self.idly = IntVar()
        self.dosa = IntVar()
        self.kichdi = IntVar()
        self.vegkichdi = IntVar()
        self.masalakichdi = IntVar()
        self.semiyakichdi = IntVar()
        self.ragisemiya = IntVar()
        self.srupma= IntVar()
        self.dalupma= IntVar()
        
    # ============lunch==============================
       
        self.vegetablerice = IntVar()
        self.sambarrice = IntVar()
        self.paruppurice = IntVar()
        self.kuska = IntVar()
        self.veggiesrice = IntVar()
        self.varietyrice = IntVar()
        
     #=============hotdrinks=============================
        
        self.coffee = IntVar()
        self.bmilk = IntVar()
        self.smmilk = IntVar()
        self.pkmilk = IntVar()
        self.karupattimilk = IntVar()
        self.palkovamilk = IntVar()
        self.paruthimilk = IntVar()
        self.thenmilk = IntVar()
        self.masalamilk = IntVar()
        self.milagumilk = IntVar()

        
        
    # ==============Total product price================
    
        self.tiffin_price = StringVar()
        self.lunch_price = StringVar()
        self.hot_drinks_price = StringVar()
        
    # ==============Customer==========================
    
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        
    # ===============Tax================================
    
        self.tiffin_tax = StringVar()
        self.lunch_tax = StringVar()
        self.hot_drinks_tax = StringVar()
        
    # =============customer retail details======================
    
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="gold", bg="red")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", font=('times new roman', 15, 'bold'),fg="gold", bg="red")
        cname_lbl.grid(row=0, column=0,columnspan=2, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="red", font=('times new roman', 15, 'bold'),fg="gold")
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="red", font=('times new roman', 15, 'bold'),fg="gold")
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================Tiffin====================================
    
        F2 = LabelFrame(self.root, text="Tiffin", font=('times new roman', 15, 'bold'), bd=10, fg="gold", bg="red")
        F2.place(x=5, y=180, width=400, height=500)
        F2.grid_columnconfigure(0,weight=1)
        F2.grid_columnconfigure(1,weight=1)

        idly_lbl = Label(F2, text="Idly", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        idly_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        idly_txt = Entry(F2, width=10, textvariable=self.idly, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        idly_txt.grid(row=0, column=1, padx=5, pady=5)

        dosa_lbl = Label(F2, text="Dosa", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        dosa_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        dosa_txt = Entry(F2, width=10, textvariable=self.dosa, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        dosa_txt.grid(row=1, column=1, padx=5, pady=5)

        kichdi_lbl = Label(F2, text="Kichdi", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        kichdi_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        kichdi_txt = Entry(F2, width=10, textvariable=self.kichdi, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        kichdi_txt.grid(row=2, column=1, padx=5, pady=5)

        vegkichdi_lbl = Label(F2, text="Veg Kichdi", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        vegkichdi_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        vegkichdi_txt = Entry(F2, width=10, textvariable=self.vegkichdi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        vegkichdi_txt.grid(row=3, column=1, padx=5, pady=5)

        masalakichdi_lbl = Label(F2, text="Masala Kichdi", font =('times new roman', 16, 'bold'), bg = "red", fg = "gold")
        masalakichdi_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        masalakichdi_txt = Entry(F2, width=10, textvariable=self.masalakichdi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        masalakichdi_txt.grid(row=4, column=1, padx=5, pady=5)

        semiyakichdi_lbl = Label(F2, text="Semiya Kichdi", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        semiyakichdi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        semiyakichdi_txt = Entry(F2, width=10, textvariable=self.semiyakichdi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        semiyakichdi_txt.grid(row=5, column=1, padx=5, pady=5)

        ragisemiya_lbl = Label(F2, text="Ragi Semiya", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        ragisemiya_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        ragisemiya_txt = Entry(F2, width=10, textvariable=self.ragisemiya, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        ragisemiya_txt.grid(row=5, column=1, padx=5, pady=5)

        srupma_lbl = Label(F2, text="Rava Upma", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        srupma_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        srupma_txt = Entry(F2, width=10, textvariable=self.srupma, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        srupma_txt.grid(row=5, column=1, padx=5, pady=5)

        dalupma_lbl = Label(F2, text="Dal Upma", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        dalupma_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        dalupma_txt = Entry(F2, width=10, textvariable=self.dalupma, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        dalupma_txt.grid(row=5, column=1, padx=5, pady=5)

    # ==========Lunch=========================
    
        F3 = LabelFrame(self.root, text="Lunch", font=('times new roman', 15, 'bold'), bd=10, fg="gold", bg="red")
        F3.place(x=340, y=180, width=400, height=500)
        F3.grid_columnconfigure(0,weight=1)
        F3.grid_columnconfigure(1,weight=1)

        vegetablerice_lbl = Label(F3, text="Vegetable Rice", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        vegetablerice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        vegetablerice_txt = Entry(F3, width=10, textvariable=self.vegetablerice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        vegetablerice_txt.grid(row=0, column=1, padx=5, pady=5)

        sambarrice_lbl = Label(F3, text="Sambar Rice", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        sambarrice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sambarrice_txt = Entry(F3, width=10, textvariable=self.sambarrice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sambarrice_txt.grid(row=0, column=1, padx=5, pady=5)

        paruppurice_lbl = Label(F3, text="Paruppu Rice", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        paruppurice_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        paruppurice_txt = Entry(F3, width=10, textvariable=self.paruppurice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        paruppurice_txt.grid(row=1, column=1, padx=5, pady=5)

        kuska_lbl = Label(F3, text="Kuska", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        kuska_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        kuska_txt = Entry(F3, width=10, textvariable=self.kuska, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        kuska_txt.grid(row=2, column=1, padx=5, pady=5)

        veggiesrice_lbl = Label(F3, text="Veggies Rice", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        veggiesrice_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        veggiesrice_txt = Entry(F3, width=10, textvariable=self.veggiesrice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        veggiesrice_txt.grid(row=3, column=1, padx=5, pady=5)

        varietyrice_lbl = Label(F3, text="Variety Rice", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        varietyrice_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        varietyrice_txt = Entry(F3, width=10, textvariable=self.varietyrice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        varietyrice_txt.grid(row=4, column=1, padx=5, pady=5)


    # ===========hotdrinks================================
    
        F4 = LabelFrame(self.root, text="Hot Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="gold", bg="red")
        F4.place(x=670, y=180, width=400, height=500)
        F4.grid_columnconfigure(0, weight=1)
        F4.grid_columnconfigure(1, weight=1)

        coffee_lbl = Label(F4, text="Coffee", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        coffee_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        coffee_txt = Entry(F4, width=10, textvariable=self.coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coffee_txt.grid(row=0, column=1, padx=5, pady=5)

        bmilk_lbl = Label(F4, text="Badam Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        bmilk_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        bmilk_txt = Entry(F4, width=10, textvariable=self.bmilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        bmilk_txt.grid(row=1, column=1, padx=5, pady=5)

        smmilk_lbl = Label(F4, text="Sukku Malli Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        smmilk_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        smmilk_txt = Entry(F4, width=10, textvariable=self.smmilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        smmilk_txt.grid(row=2, column=1, padx=5, pady=5)

        pkmilk_lbl = Label(F4, text="Panamkarkandu Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        pkmilk_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        pkmilk_txt = Entry(F4, width=10, textvariable=self.pkmilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        pkmilk_txt.grid(row=3, column=1, padx=5, pady=5)

        karupattimilk_lbl = Label(F4, text="Karupatti Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        karupattimilk_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        karupattimilk_txt = Entry(F4, width=10, textvariable=self.karupattimilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        karupattimilk_txt.grid(row=4, column=1, padx=5, pady=5)

        palkovamilk_lbl = Label(F4, text="Palkova Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        palkovamilk_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        palkovamilk_txt = Entry(F4, width=10, textvariable=self.palkovamilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        palkovamilk_txt.grid(row=5, column=1, padx=5, pady=5)

        paruthimilk_lbl = Label(F4, text="Paruthi Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        paruthimilk_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        paruthimilk_txt = Entry(F4, width=10, textvariable=self.paruthimilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        paruthimilk_txt.grid(row=5, column=1, padx=5, pady=5)

        thenmilk_lbl = Label(F4, text="Then Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        thenmilk_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thenmilk_txt = Entry(F4, width=10, textvariable=self.thenmilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        thenmilk_txt.grid(row=5, column=1, padx=5 ,pady=5)

        masalamilk_lbl = Label(F4, text="Masala Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        masalamilk_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        masalamilk_txt = Entry(F4, width=10, textvariable=self.masalamilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        masalamilk_txt.grid(row=5, column=1, padx=5, pady=5)

        milagumilk_lbl = Label(F4, text="Milagu Milk", font=('times new roman', 16, 'bold'), bg="red", fg="gold")
        milagumilk_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        milagumilk_txt = Entry(F4, width=10, textvariable=self.milagumilk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        milagumilk_txt.grid(row=5, column=1, padx=5, pady=5)

    # =================BillArea======================
    
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)
      

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
    
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="gold", bg="red")
        F6.place(x=0, y=680, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Tiffin Price", font=('times new roman', 14, 'bold'), bg="red", fg="gold")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.tiffin_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Lunch Price", font=('times new roman', 14, 'bold'), bg="red", fg="gold")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.lunch_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Hot Drinks Price", font=('times new roman', 14, 'bold'), bg="red", fg="gold")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.hot_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Tiffin Tax", font=('times new roman', 14, 'bold'), bg="red", fg="gold")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.tiffin_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Lunch Tax", font=('times new roman', 14, 'bold'), bg="red", fg="gold")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.lunch_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Hot Drinks Tax", font=('times new roman', 14, 'bold'), bg="red", fg="gold")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.hot_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
    
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=780, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="red", bd=2, fg="gold", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="red", fg="gold", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="red", bd=2, fg="gold", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="red", fg="gold", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================

    def total(self):
        self.i = self.idly.get()*20
        self.d = self.dosa.get()*20
        self.k = self.kichdi.get()*35
        self.vk= self.vegkichdi.get()*35
        self.mk = self.masalakichdi.get()*40
        self.sk = self.semiyakichdi.get()*35
        self.rsk= self.ragisemiya.get()*40
        self.sru = self.srupma.get()*35
        self.du= self.dalupma.get()*40
        self.total_tiffin_price = float(self.i+self.d+self.k+self.vk+self.mk+self.sk+self.rsk+self.sru+self.du)

        self.tiffin_price.set("Rs. "+str(self.total_tiffin_price))
        self.t_tax = round((self.total_tiffin_price*0.18), 2)
        self.tiffin_tax.set("Rs. "+str(self.t_tax))

        self.vrice = self.vegetablerice.get()*50
        self.srice= self.sambarrice.get()*50
        self.pr = self.paruppurice.get()*50
        self.kuskarice = self.kuska.get()*50
        self.veggrice = self.veggiesrice.get()*40
        self.varrice = self.varietyrice.get()*30
        self.total_lunch_price = float(self.vrice+self.srice+self.pr+self.kuskarice+self.veggrice+self.varrice)

        self.lunch_price.set("Rs. " + str(self.total_lunch_price))
        self.l_tax = round((self.total_lunch_price*0.18), 2)
        self.lunch_tax.set("Rs. " + str(self.l_tax))

        self.coff = self.coffee.get()*20
        self.bm = self.bmilk.get()*20
        self.smm= self.smmilk.get()*20
        self.pkm = self.pkmilk.get()*20
        self.kpm = self.karupattimilk.get()*20
        self.pkovam = self.palkovamilk.get()*20
        self.parm = self.paruthimilk.get()*20
        self.thm = self.thenmilk.get()*20
        self.masm = self.masalamilk.get()*20
        self.milm= self.milagumilk.get()*20
        self.total_hot_drinks_price = float(self.coff+self.bm+self.smm+self.pkm+self.kpm+self.pkovam+self.parm+self.thm+self.masm+self.milm)

        self.hot_drinks_price.set("Rs. "+str(self.total_hot_drinks_price))
        self.hd_tax = round((self.total_hot_drinks_price * 0.18), 2)
        self.hot_drinks_tax.set("Rs. "+str(self.hd_tax))

        self.total_bill = float(self.total_tiffin_price+self.total_lunch_price+self.total_hot_drinks_price+self.t_tax+self.l_tax+self.hd_tax)

#==============welcome-bill==============================

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tSaptingala")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")
       
#=========billArea=================================================

    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.tiffin_price.get() == "Rs. 0.0" and self.lunch_price.get() == "Rs. 0.0" and self.hot_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            
    # ============tiffin===========================
    
        if self.idly.get() != 0:
            self.txtarea.insert(END, f"\n Idly\t\t{self.idly.get()}\t\t{self.i}")
        if self.dosa.get() != 0:
            self.txtarea.insert(END, f"\n Dosa\t\t{self.dosa.get()}\t\t{self.d}")
        if self.kichdi.get() != 0:
            self.txtarea.insert(END, f"\n Kichdi\t\t{self.kichdi.get()}\t\t{self.k}")
        if self.vegkichdi.get() != 0:
            self.txtarea.insert(END, f"\n Veg Kichdi\t\t{self.vegkichdi.get()}\t\t{self.vk}")
        if self.masalakichdi.get() != 0:
            self.txtarea.insert(END, f"\n Masala Kichdi\t\t{self.masalakichdi.get()}\t\t{self.mk}")
        if self.semiyakichdi.get() != 0:
            self.txtarea.insert(END , f"\n Semiya Kichdi\t\t{self.semiyakichdi.get()}\t\t{self.sk}")
        if self.ragisemiyakichdi.get() != 0:
            self.txtarea.insert(END , f"\n Ragi Semiya\t\t{self.ragisemiyakichdi.get()}\t\t{self.rsk}")
        if self.srupma.get() != 0:
            self.txtarea.insert(END , f"\n Rava Upma\t\t{self.srupma.get()}\t\t{self.sru}")
        if self.dalupma.get() != 0:
            self.txtarea.insert(END , f"\n Dal Upma\t\t{self.dalupma.get()}\t\t{self.du}")
            
    # ==============lunch============================
    
        if self.vegetablerice.get() != 0:
            self.txtarea.insert(END, f"\n Vegetable Rice\t\t{self.vegetablerice.get()}\t\t{self.vrice}")
        if self.sambarrice.get() != 0:
            self.txtarea.insert(END, f"\n Sambar Rice\t\t{self.sambarrice.get()}\t\t{self.srice}")
        if self.paruppurice.get() != 0:
            self.txtarea.insert(END, f"\n Paruppu Rice\t\t{self.paruppurice.get()}\t\t{self.pr}")
        if self.kuska.get() != 0:
            self.txtarea.insert(END, f"\n Kuska\t\t{self.kuska.get()}\t\t{self.kuskarice}")
        if self.veggiesrice.get() != 0:
            self.txtarea.insert(END, f"\n Veggies Rice\t\t{self.veggiesrice.get()}\t\t{self.veggrice}")
        if self.varietyrice.get() != 0:
            self.txtarea.insert(END, f"\n Variety Rice\t\t{self.varietyrice.get()}\t\t{self.varrice}")
            
        #================hotDrinks==========================
        
        if self.coffee.get() != 0:
            self.txtarea.insert(END, f"\n Coffee\t\t{self.coffee.get()}\t\t{self.coff}")
        if self.bmilk.get() != 0:
            self.txtarea.insert(END, f"\n Badam Milk\t\t{self.bmilk.get()}\t\t{self.bm}")
        if self.smmilk.get() != 0:
            self.txtarea.insert(END, f"\nSukku Malli Milk\t\t{self.smmilk.get()}\t\t{self.smm}")
        if self.pkmilk.get() != 0:
            self.txtarea.insert(END, f"\n Panamkarkandu Mil;\t\t{self.pkmilk.get()}\t\t{self.pkm}")
        if self.karupattimilk.get() != 0:
            self.txtarea.insert(END, f"\n Karupatti Milk\t\t{self.karupattimilk.get()}\t\t{self.kpm}")
        if self.palkovamilk.get() != 0:
            self.txtarea.insert(END, f"\n Palkova Milk\t\t{self.palkovamilk.get()}\t\t{self.pkovam}")
        if self.paruthimilk.get() != 0:
            self.txtarea.insert(END, f"\n Paruthi Milk\t\t{self.paruthimilk.get()}\t\t{self.parm}")
        if self.thenmilk.get() != 0:
            self.txtarea.insert(END, f"\n Then Milk\t\t{self.thenmilk.get()}\t\t{self.thm}")
        if self.masalamilk.get() != 0:
            self.txtarea.insert(END, f"\n Masala Milk\t\t{self.masalamilk.get()}\t\t{self.masm}")
        if self.milagumilk.get() != 0:
            self.txtarea.insert(END, f"\n Milagu Milk\t\t{self.milagumilk.get()}\t\t{self.milm}")
            self.txtarea.insert(END, f"\n--------------------------------")
            
        # ===============taxes==============================
        
        if self.tiffin_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Tiffin Tax\t\t\t{self.tiffin_tax.get()}")
        if self.lunch_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Lunch Tax\t\t\t{self.lunch_tax.get()}")
        if self.hot_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Hot Drinks Tax\t\t\t{self.hot_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for de in f1:
                    self.txtarea.insert(END, de)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.idly.set(0)
            self.dosa.set(0)
            self.kichdi.set(0)
            self.vegkichdi.set(0)
            self.masalakichdi.set(0)
            self.semiyakichdi.set(0)
            self.ragisemiya.set(0)
            self.srupma.set(0)
            self.dalupma.set(0)

    # ============lunch==============================
    
            self.vegetablerice.set(0)
            self.sambarrice.set(0)
            self.paruppurice.set(0)
            self.kuska.set(0)
            self.veggiesrice.set(0)
            self.varietyrice.set(0)
            
    # =============hotdrinks=============================
    
            self.coffee.set(0)
            self.bmilk.set(0)
            self.smmilk.set(0)
            self.pkmilk.set(0)
            self.karupattimilk.set(0)
            self.palkovamilk.set(0)
            self.paruthimilk.set(0)
            self.thenmilk.set(0)
            self.masalamilk.set(0)
            self.milagumilk.set(0)
            
    # ====================taxes================================
    
            self.tiffin_price.set("")
            self.lunch_price.set("")
            self.hot_drinks_price.set("")

            self.tiffin_tax.set("")
            self.lunch_tax.set("")
            self.hot_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()