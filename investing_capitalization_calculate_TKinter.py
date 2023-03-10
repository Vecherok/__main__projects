import tkinter as tk
from tkinter import messagebox
import decimal

class My_GUI:

    def __init__(self):
        pass
        self.root = tk.Tk()
        self.root.geometry('700x500')
        self.root.title('investing capitalization calculate')
        
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Upload file', command=self.upload_file)

        
        self.infomenu = tk.Menu(self.menubar, tearoff=0)
        self.infomenu.add_command(label='Show the program version', command=self.program_version)
        self.infomenu.add_separator()
        self.infomenu.add_command(label='Help', command=self.help_info)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.infomenu, label="Info")

        self.root.configure(bg='#FFE668', menu=self.menubar)

        self.label = tk.Label(self.root, text = 'Bank "Nadurim & Co" offers you to open a deposit', font=('Arial', 17),bg="black", fg="#FFD500")
        self.label.pack(pady=15)   

        self.mainframe = tk.Frame(self.root,highlightthickness=2, highlightbackground="black", bg='#FFE668')
        self.mainframe.pack(fill="both")

        self.currencyframe = tk.Frame(self.mainframe, bg="#FFD500")
        self.currencyframe.columnconfigure(0, weight=1)
        self.currencyframe.columnconfigure(1, weight=3)
        self.carrencylabel = tk.Label(self.currencyframe, text = 'Select the deposit currency, please', font=('Arial', 10),bg="gray", fg="#FFD500")
        self.carrencylabel.grid(row=1, column=1, padx=30)
        self.currency_check = tk.IntVar()
        self.cbtnusd = tk.Checkbutton(self.currencyframe, text="USD($)", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.currency_check)
        self.cbtnusd.grid(row=0, column=0, sticky="news")
        self.cbtneur = tk.Checkbutton(self.currencyframe, text="EUR(€)", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.currency_check)
        self.cbtneur.grid(row=1, column=0, sticky="news")
        self.cbtncny = tk.Checkbutton(self.currencyframe, text="CNY(¥)", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.currency_check)
        self.cbtncny.grid(row=2, column=0, sticky="news")
        self.currencyframe.pack(fill="x", pady=3)

        self.amountframe = tk.Frame(self.mainframe, bg="#FFD500")
        self.amountframe.columnconfigure(0, weight=1)
        self.amountframe.columnconfigure(1, weight=3)
        self.amountentry = tk.Entry(self.amountframe, width=10, bg="gray", fg="#FFD500", font=("Arial", 12),highlightthickness=3, highlightbackground="black")
        self.amountentry.grid(row=0, column=0)
        self.amountentrylabel = tk.Label(self.amountframe, text = 'Enter the deposit amount, please', font=('Arial', 10), bg="gray", fg="#FFD500")
        self.amountentrylabel.grid(row=0, column=1, padx=30)
        self.amountframe.pack(fill="x", pady=3)

        self.periodframe = tk.Frame(self.mainframe, bg="#FFD500")
        self.periodframe.columnconfigure(0, weight=1)
        self.periodframe.columnconfigure(1, weight=3)
        self.periodentry = tk.Scale(self.periodframe, bg="gray", fg="#FFD500", font=("Arial", 12),from_=1, to=50, orient='horizontal')
        self.periodentry.grid(row=0, column=0,sticky="we")
        self.periodentrylabel = tk.Label(self.periodframe, text = 'Сhoose for how many years the deposit', font=('Arial', 10), bg="gray", fg="#FFD500")
        self.periodentrylabel.grid(row=0, column=1)
        self.periodframe.pack(fill="x", pady=3)

        self.capitalizationframe = tk.Frame(self.mainframe, bg="#FFD500")
        self.capitalizationframe.columnconfigure(0, weight=1)
        self.capitalizationframe.columnconfigure(1, weight=3)
        self.capitalizationlabel = tk.Label(self.capitalizationframe, text = 'Select the period of capitalization', font=('Arial', 10),bg="gray", fg="#FFD500")
        self.capitalizationlabel.grid(row=1, column=1, padx=30)
        self.capitalization_check = tk.IntVar()
        self.monthcapbnt = tk.Checkbutton(self.capitalizationframe, text="Monthly capitalization", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.capitalization_check)
        self.monthcapbnt.grid(row=0, column=0, sticky="news")
        self.quarcapbtn = tk.Checkbutton(self.capitalizationframe, text="Quarterly capitalization", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.capitalization_check)
        self.quarcapbtn.grid(row=1, column=0, sticky="news")
        self.annualcapbtn = tk.Checkbutton(self.capitalizationframe, text="Annual capitalization", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.capitalization_check)
        self.annualcapbtn.grid(row=2, column=0, sticky="news")
        self.capitalizationframe.pack(fill="x", pady=3)

        self.irateframe = tk.Frame(self.mainframe, bg="#FFD500")
        self.irateframe.columnconfigure(0, weight=1)
        self.irateframe.columnconfigure(1, weight=3)
        self.iratelabel = tk.Label(self.irateframe, text = "<=== Your annual unterest rate will be", font=('Arial', 10), bg="gray", fg="#FFD500")
        self.iratelabel.grid(row=0, column=1, padx=30)
        self.iratevalue = tk.Entry(self.irateframe, width=10, font=('Arial', 12), bg="gray", fg="#FFD500", highlightthickness=3, highlightbackground="black")
        self.iratevalue.grid(row=0, column=0)
        self.irateframe.pack(fill="x", pady=3)

        self.capitalization_check = tk.IntVar()
        self.capitalizationisactive = tk.Checkbutton(self.mainframe, text="Сhoose to capitalize interest", font=("Arial", 12), bg="gray", fg="#FFD500", variable=self.capitalization_check)
        self.capitalizationisactive.pack(fill="x", pady=3)

        self.calculatebutton = tk.Button(self.root, text="Calculate", font=('Arial', 16), command=self.calculate)
        self.calculatebutton.pack(padx=20, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def calculate(self):
        deposit_amount = (self.amountentry.get())
        years_amount = int(self.periodentry.get())
        annual_interest_rate = (self.iratevalue.get())

        capitalization_frequency = 4
        currency = 'CNY'

        if self.capitalization_check.get() == 0:
            messagebox.showinfo(title='results', message="message1")
        else:
            # summ = round((deposit_amount * pow((1 + annual_interest_rate / (100 * capitalization_frequency)),(years_amount * capitalization_frequency))),2)
            # Profit = summ - deposit_amount

            # message1 = f"In {years_amount} years you'll have {summ} {currency} in your account\nProfit will be {Profit} {currency}"

            # messagebox.showinfo(title='results', message=message1)
            messagebox.showinfo(title='results', message="message2")

        # if self.capitalization_check == 0:
        #     capitalization_frequency = 12
        # elif self.capitalization_check == 1:
        #     capitalization_frequency = 4
        # else:
        #     capitalization_frequency = 1

        # if self.currency_check.get() == 0:
        #     currency = 'USD'
        # elif self.currency_check.get() == 1:
        #     currency = 'EUR'
        # else:
        #     currency = 'CNY'
        

        # print(self.textbox.get('1.0', tk.END))      ---------  getting data from the textbox from star till the end


    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def help_info(self):
        
        return messagebox.INFO("Some support info...")

    def upload_file():
        pass

    def program_version():
        pass


My_GUI()



# import decimal, re
# from tracemalloc import stop

# def monthly_capitalization_calculate(p,t,r,n):
#     '''
#     What data does the function take
#         p - deposit amount
#         t - years amount
#         r - annual interest rate
#         n - how many times a year is the interest rate calculated
#     '''
#     p, t, r, n = decimal.Decimal(p), decimal.Decimal(t), decimal.Decimal(r), decimal.Decimal(n)
#     summ = round((p * pow((1 + r / (100 * n)),(t * n))),2)
#     print(f"In {years_amount} years you'll have {summ} {currency} in your account")
#     Profit = summ - p
#     print(f'Profit will be {Profit} {currency}') 

# print(f'Bank "Nadurim & Co" offers you to open a deposit\nEnter the deposit amount:')
# deposit_amount = input().replace(',', '.')
# deposit_amount = re.sub ('[^\d.]', "", deposit_amount)

# print(f'Enter deposit currency :')
# currency = input()

# print(f'How many years deposit?')
# years_amount = input().replace(',', '.')
# years_amount = float(re.sub ('[^\d.]', "", years_amount))

# print(f'What annual interest rate would you like? :')
# annual_interest_rate = input()
# annual_interest_rate = re.sub ('[^\d.]', "", annual_interest_rate)

# print(f'Monthly, quarterly or annual capitalization? \n\
# For monthly enter 1, for quarterly enter 2, for yearly enter 3 (Default - monthly):')
# capitalization_type = int(input())

# capitalization_frequency = 12
# if capitalization_type == 2:
#     capitalization_frequency = 4
# elif capitalization_type == 3:
#     capitalization_frequency = 1
#     if years_amount < 1:
#         print(f'Wrong COMBO, bro ;) Annual capitalization is possible when the deposit period exceeds one year')
#         exit()

# monthly_capitalization_calculate(deposit_amount,years_amount,annual_interest_rate,capitalization_frequency)




# label = tk.Label(root, text = 'Bank "Nadurim & Co" offers you to open a deposit', font=('Arial', 17),bg="black", fg="#FFD500")
# label.pack(pady=15)

# textbox = tk.Text(root, height=1 , font=('Arial', 15))
# textbox.pack(padx=10)

# myentry = tk.Entry(root)
# myentry.pack()

# button = tk.Button(root, text="Enter", font=('Arial', 18))
# button.pack(pady=10)

# frame = tk.Frame(button)
# frame.pack()

    

    
