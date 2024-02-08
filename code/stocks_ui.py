from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd
from calculate import *

stock_data = pd.read_csv('stock_data.csv')


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Stock Market Trade')
        self.window.geometry("500x400+10+10")

        self.label1 = Label(self.window, text="Stock (Enter Symbol)")
        self.label1.place(x=45, y=100)

        self.symbol_data=tuple(stock_data['Stock Symbol'])
        self.cb_symbol=Combobox(self.window, values=self.symbol_data)
        self.cb_symbol.place(x=160, y=100)

        self.label2 = Label(self.window, text="Input Price")
        self.label2.place(x=95, y=140)

        self.field2 = Entry(self.window)
        self.field2.place(x=160, y=140)


        self.buy_sell_data=tuple(['BUY', 'SELL'])
        self.buy_sell=Combobox(self.window, values=self.buy_sell_data)
        self.buy_sell.place(x=160, y=220)

        self.label3 = Label(self.window, text="BUY/SELL")
        self.label3.place(x=95, y=220)


        self.label4 = Label(self.window, text="Operation")
        self.label4.place(x=100, y=180)
        self.data=("Trade","Dividend Yield", "P/E Ratio", "Volumne Weighted Stock Price", "GBCE")
        self.cb=Combobox(self.window, values=self.data)
        self.cb.place(x=160, y=180)

        self.button = Button(self.window, text="Execute!", command=self.click_button)
        self.button.pack()
        self.button.place(x=180, y=270)

        self.window.mainloop()

    def click_button(self):

        stock_sym = self.cb_symbol.get()
        price = self.field2.get()
        bs_trade = self.buy_sell.get()
        operation = self.cb.get()

        if operation == "Trade":
            operation_result = trade(stock_sym, price, bs_trade)
        elif operation == "Dividend Yield":
            operation_selected = "Dividend Yield"
            operation_result = dividend_yeild(stock_sym, price)
        elif operation == "P/E Ratio":
            operation_result = pe_ratio(stock_sym, price)
        elif operation == "Volumne Weighted Stock Price":
            operation_result = calculate_vwsp()
        elif operation == "GBCE":
            operation_result =calculate_gbce()
        else:
            operation_result = "Operation Selected is Invalid"
    
        self.label4 = Label(self.window, text="{}".format(operation_result))
        self.label4.place(x=100, y=320)


if __name__ == "__main__":
    gui = GUI()