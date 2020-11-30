from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tksheet
import pandas
import datetime
import webbrowser
import csv
import requests
import sys
import streamtologger


# noinspection PyAttributeOutsideInit
class Nse:
    def __init__(self, window: Tk):
        self.seconds = 500
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.previous_date = None
        self.previous_time = None
        self.first_run = True
        self.stop = False
        self.logging = False
        self.dates = [""]
        self.indices = ["BANKNIFTY","NIFTY"]
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                      'like Gecko) '
                                      'Chrome/80.0.3987.149 Safari/537.36',
                        'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
        self.url_oc = "https://www.nseindia.com/option-chain"
        self.session = requests.Session()
        self.cookies = {}
        self.login_win(window)

    def get_data(self, event=None):
        if self.first_run:
            return self.get_data_first_run()
        else:
            return self.get_data_refresh()

    def get_data_first_run(self):
        request = None
        response = None
        self.index = self.index_var.get()
        try:
            url = f"https://www.nseindia.com/api/option-chain-indices?symbol={self.index}"
            request = self.session.get(self.url_oc, headers=self.headers, timeout=5)
            self.cookies = dict(request.cookies)
            response = self.session.get(url, headers=self.headers, timeout=5, cookies=self.cookies)
        except Exception as err:
            print(request)
            print(response)
            print(err, "1")
            messagebox.showerror(title="Error", message="Error in fetching dates.\nPlease retry.")
            self.dates.clear()
            self.dates = [""]
            self.date_menu.config(values=tuple(self.dates))
            self.date_menu.current(0)
            return
        if response is not None:
            try:
                json_data = response.json()
            except Exception as err:
                print(response)
                print(err, "2")
                json_data = {}
        else:
            json_data = {}
        if json_data == {}:
            messagebox.showerror(title="Error", message="Error in fetching dates.\nPlease retry.")
            self.dates.clear()
            self.dates = [""]
            try:
                self.date_menu.config(values=tuple(self.dates))
                self.date_menu.current(0)
            except TclError as err:
                print(err, "3")
            return
        self.dates.clear()
        for dates in json_data['records']['expiryDates']:
            self.dates.append(dates)
        try:
            self.date_menu.config(values=tuple(self.dates))
            self.date_menu.current(0)
        except TclError as err:
            print(err, "4")

        return response, json_data

    def get_data_refresh(self):
        request = None
        response = None
        try:
            url = f"https://www.nseindia.com/api/option-chain-indices?symbol={self.index}"
            response = self.session.get(url, headers=self.headers, timeout=5, cookies=self.cookies)
            if response.status_code == 401:
                self.session.close()
                self.session = requests.Session()
                url = f"https://www.nseindia.com/api/option-chain-indices?symbol={self.index}"
                request = self.session.get(self.url_oc, headers=self.headers, timeout=5)
                self.cookies = dict(request.cookies)
                response = self.session.get(url, headers=self.headers, timeout=5, cookies=self.cookies)
                print("reset cookies")
        except Exception as err:
            print(request)
            print(response)
            print(err, "5")
            try:
                self.session.close()
                self.session = requests.Session()
                url = f"https://www.nseindia.com/api/option-chain-indices?symbol={self.index}"
                request = self.session.get(self.url_oc, headers=self.headers, timeout=5)
                self.cookies = dict(request.cookies)
                response = self.session.get(url, headers=self.headers, timeout=5, cookies=self.cookies)
                print("reset cookies")
            except Exception as err:
                print(request)
                print(response)
                print(err, "6")
                return
        if response is not None:
            try:
                json_data = response.json()
            except Exception as err:
                print(response)
                print(err, "7")
                json_data = {}
        else:
            json_data = {}
        if json_data == {}:
            return

        return response, json_data

    def login_win(self, window: Tk):
        self.login = window
        self.login.title("NSE")
        window_width = self.login.winfo_reqwidth()
        window_height = self.login.winfo_reqheight()
        position_right = int(self.login.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.login.winfo_screenheight() / 2 - window_height / 2)
        self.login.geometry("260x90+{}+{}".format(position_right, position_down))

        self.index_var = StringVar()
        self.index_var.set(self.indices[0])
        self.dates_var = StringVar()
        self.dates_var.set(self.dates[0])

        index_label = Label(self.login, text="Index: ", justify=LEFT)
        index_label.grid(row=0, column=0, sticky=N + S + W)
        self.index_menu = Combobox(self.login, textvariable=self.index_var, values=self.indices)
        self.index_menu.config(width=15)
        self.index_menu.grid(row=0, column=1, sticky=N + S + E)
        date_label = Label(self.login, text="Expiry Date: ", justify=LEFT)
        date_label.grid(row=1, column=0, sticky=N + S + E)
        self.date_menu = Combobox(self.login, textvariable=self.dates_var)
        self.date_menu.config(width=15)
        self.date_menu.grid(row=1, column=1, sticky=N + S + E)
        self.date_get = Button(self.login, text="Refresh", command=self.get_data)
        self.date_get.grid(row=1, column=2, sticky=N + S + E)
        sp_label = Label(self.login, text="Strike Price: ")
        sp_label.grid(row=2, column=0, sticky=N + S + E)
        self.sp_entry = Entry(self.login, width=18)
        self.sp_entry.grid(row=2, column=1, sticky=N + S + E)
        start_btn = Button(self.login, text="Start", command=self.start)
        start_btn.grid(row=2, column=2, sticky=N + S + E + W)
        self.sp_entry.focus_set()
        self.get_data()

        def focus_widget(event, mode: int):
            if mode == 1:
                self.get_data()
                self.date_menu.focus_set()
            elif mode == 2:
                self.sp_entry.focus_set()

        self.index_menu.bind('<Return>', lambda event, a=1: focus_widget(event, a))
        self.index_menu.bind("<<ComboboxSelected>>", self.get_data)
        self.date_menu.bind('<Return>', lambda event, a=2: focus_widget(event, a))
        self.sp_entry.bind('<Return>', self.start)

        self.login.mainloop()

    def start(self, event=None):
        self.expiry_date = self.dates_var.get()
        if self.expiry_date == "":
            messagebox.showerror(title="Error", message="Incorrect Expiry Date.\nPlease enter correct Expiry Date.")
            return
        try:
            self.sp = int(self.sp_entry.get())
            self.login.destroy()
            self.main_win()
        except ValueError as err:
            print(err, "8")
            messagebox.showerror(title="Error", message="Incorrect Strike Price.\nPlease enter correct Strike Price.")

    def change_state(self, event=None):

        if not self.stop:
            self.stop = True
            self.options.entryconfig(self.options.index(0), label="Start   (Ctrl+X)")
            messagebox.showinfo(title="Stopped", message="Scraping new data has been stopped.")
        else:
            self.stop = False
            self.options.entryconfig(self.options.index(0), label="Stop   (Ctrl+X)")
            messagebox.showinfo(title="Started", message="Scraping new data has been started.")

            self.main()

    def export(self, event=None):
        sheet_data = self.sheet.get_sheet_data()

        try:
            with open("NSE-Option-Chain-Analyzer.csv", "a", newline="") as row:
                data_writer = csv.writer(row)
                data_writer.writerows(sheet_data)

            messagebox.showinfo(title="Export Complete",
                                message="Data has been exported to NSE-Option-Chain-Analyzer.csv.")
        except Exception as err:
            print(err, "9")
            messagebox.showerror(title="Export Failed",
                                 message="An error occurred while exporting the data.")

    def log(self, event=None):
        if not self.logging:
            streamtologger.redirect(target="nse.log", header_format="[{timestamp:%Y-%m-%d %H:%M:%S} - {level:5}] ")
            self.logging = True
            self.options.entryconfig(self.options.index(2), label="Logging: On   (Ctrl+L)")
            messagebox.showinfo(title="Started", message="Debug Logging has been enabled.")
        elif self.logging:
            sys.stdout = self.stdout
            sys.stderr = self.stderr
            streamtologger._is_redirected = False
            self.logging = False
            self.options.entryconfig(self.options.index(2), label="Logging: Off   (Ctrl+L)")
            messagebox.showinfo(title="Stopped", message="Debug Logging has been disabled.")

    # def links(self, link: str, event=None):

    #     if link == "developer":
    #         webbrowser.open_new("https://github.com/VarunS2002/")
    #     elif link == "readme":
    #         webbrowser.open_new("https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer/blob/master/README.md/")
    #     elif link == "license":
    #         webbrowser.open_new("https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer/blob/master/LICENSE/")
    #     elif link == "releases":
    #         webbrowser.open_new("https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer/releases/")
    #     elif link == "sources":
    #         webbrowser.open_new("https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer/")

    #     self.info.attributes('-topmost', False)

    def about_window(self) -> Toplevel:
        self.info = Toplevel()
        self.info.title("About")
        window_width = self.info.winfo_reqwidth()
        window_height = self.info.winfo_reqheight()
        position_right = int(self.info.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.info.winfo_screenheight() / 2 - window_height / 2)
        self.info.geometry("250x150+{}+{}".format(position_right, position_down))
        self.info.attributes('-topmost', True)
        self.info.grab_set()
        self.info.focus_force()

        return self.info

    def about(self, event=None):
        self.info = self.about_window()
        self.info.rowconfigure(0, weight=1)
        self.info.rowconfigure(1, weight=1)
        self.info.rowconfigure(2, weight=1)
        self.info.rowconfigure(3, weight=1)
        self.info.rowconfigure(4, weight=1)
        self.info.columnconfigure(0, weight=1)
        self.info.columnconfigure(1, weight=1)

        heading = Label(self.info, text="Option-Chain-Analyzer", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        heading.grid(row=0, column=0, columnspan=2, sticky=N + S + W + E)
        version_label = Label(self.info, text="Version:", relief=RIDGE)
        version_label.grid(row=1, column=0, sticky=N + S + W + E)
        version_val = Label(self.info, text="3.5", relief=RIDGE)
        version_val.grid(row=1, column=1, sticky=N + S + W + E)
        dev_label = Label(self.info, text="Developer:", relief=RIDGE)
        dev_label.grid(row=2, column=0, sticky=N + S + W + E)
        dev_val = Label(self.info, text="Varun Shanbhag", fg="blue", cursor="hand2", relief=RIDGE)
        dev_val.bind("<Button-1>", lambda click, link="developer": self.links(link, click))
        dev_val.grid(row=2, column=1, sticky=N + S + W + E)
        readme = Label(self.info, text="README", fg="blue", cursor="hand2", relief=RIDGE)
        readme.bind("<Button-1>", lambda click, link="readme": self.links(link, click))
        readme.grid(row=3, column=0, sticky=N + S + W + E)
        licenses = Label(self.info, text="License", fg="blue", cursor="hand2", relief=RIDGE)
        licenses.bind("<Button-1>", lambda click, link="license": self.links(link, click))
        licenses.grid(row=3, column=1, sticky=N + S + W + E)
        releases = Label(self.info, text="Releases", fg="blue", cursor="hand2", relief=RIDGE)
        releases.bind("<Button-1>", lambda click, link="releases": self.links(link, click))
        releases.grid(row=4, column=0, sticky=N + S + W + E)
        sources = Label(self.info, text="Sources", fg="blue", cursor="hand2", relief=RIDGE)
        sources.bind("<Button-1>", lambda click, link="sources": self.links(link, click))
        sources.grid(row=4, column=1, sticky=N + S + W + E)

        self.info.mainloop()

    def close(self, event=None):
        ask_quit = messagebox.askyesno("Quit", "All unsaved data will be lost.\nProceed to quit?", icon='warning',
                                       default='no')
        if ask_quit:
            self.session.close()
            self.root.destroy()
            sys.exit()
        elif not ask_quit:
            pass

    def main_win(self):
        self.root = Tk()
        self.root.focus_force()
        self.root.title("Option-Chain-Analyzer")
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth() / 3 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 3 - window_height / 2)
        self.root.geometry("815x510+{}+{}".format(position_right, position_down))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        menubar = Menu(self.root)
        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label="Stop   (Ctrl+X)", command=self.change_state)
        self.options.add_command(label="Export to CSV   (Ctrl+S)", command=self.export)
        self.options.add_command(label="Logging: Off   (Ctrl+L)", command=self.log)
        self.options.add_separator()
        #self.options.add_command(label="About   (Ctrl+M)", command=self.about)
        self.options.add_command(label="Quit   (Ctrl+Q)", command=self.close)
        menubar.add_cascade(label="Menu", menu=self.options)
        self.root.config(menu=menubar)

        self.root.bind('<Control-s>', self.export)
        self.root.bind('<Control-l>', self.log)
        self.root.bind('<Control-x>', self.change_state)
        self.root.bind('<Control-m>', self.about)
        self.root.bind('<Control-q>', self.close)

        top_frame = Frame(self.root)
        top_frame.rowconfigure(0, weight=1)
        top_frame.columnconfigure(0, weight=1)
        top_frame.pack(fill="both", expand=True)

        output_columns = (
            'Time', 'LTP', 'Call_CHOI\n(in K)', 'Put__CHOI\n(in K)', 'Difference\n(in K)', 'Call_OI\n(in K)',
            'Put_OI\n(in K)', 'OI_PCR', 'CHOI_PCR')
        
        ##orignal_columns_names = ['Time', 'Value', 'Call Sum\n(in K)', 'Put Sum\n(in K)', 
         #'Difference\n(in K)', 'Call Boundary\n(in K)', 'Put Boundary\n(in K)', 'Call ITM', 'Put ITM']
        
        ## Names are change as per new program modification refer the Backup program for correct Names
        self.sheet = tksheet.Sheet(top_frame, column_width=85, align="center", headers=output_columns,
                                   header_font=("TkDefaultFont", 10, "bold"), empty_horizontal=0,
                                   empty_vertical=20, header_height=35)
        self.sheet.enable_bindings(
            ("toggle_select", "drag_select", "column_select", "row_select", "column_width_resize",
             "arrowkeys", "right_click_popup_menu", "rc_select", "copy", "select_all"))
        self.sheet.grid(row=0, column=0, sticky=N + S + W + E)

        bottom_frame = Frame(self.root)
        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.rowconfigure(1, weight=1)
        bottom_frame.rowconfigure(2, weight=1)
        bottom_frame.rowconfigure(3, weight=1)
        bottom_frame.rowconfigure(4, weight=1)
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)
        bottom_frame.columnconfigure(2, weight=1)
        bottom_frame.columnconfigure(3, weight=1)
        bottom_frame.columnconfigure(4, weight=1)
        bottom_frame.columnconfigure(5, weight=1)
        bottom_frame.columnconfigure(6, weight=1)
        bottom_frame.columnconfigure(7, weight=1)
        bottom_frame.pack(fill="both", expand=True)

        oi_ub_label = Label(bottom_frame, text="Open Interest Upper Boundary", relief=RIDGE,
                            font=("TkDefaultFont", 10, "bold"))
        oi_ub_label.grid(row=0, column=0, columnspan=4, sticky=N + S + W + E)
        max_call_oi_sp_label = Label(bottom_frame, text="Strike Price:", relief=RIDGE,
                                     font=("TkDefaultFont", 10, "bold"))
        max_call_oi_sp_label.grid(row=1, column=0, sticky=N + S + W + E)
        self.max_call_oi_sp_val = Label(bottom_frame, text="", relief=RIDGE)
        self.max_call_oi_sp_val.grid(row=1, column=1, sticky=N + S + W + E)
        max_call_oi_label = Label(bottom_frame, text="OI (in K):", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        max_call_oi_label.grid(row=1, column=2, sticky=N + S + W + E)
        self.max_call_oi_val = Label(bottom_frame, text="", relief=RIDGE)
        self.max_call_oi_val.grid(row=1, column=3, sticky=N + S + W + E)
        oi_lb_label = Label(bottom_frame, text="Open Interest Lower Boundary", relief=RIDGE,
                            font=("TkDefaultFont", 10, "bold"))
        oi_lb_label.grid(row=0, column=4, columnspan=4, sticky=N + S + W + E)
        max_put_oi_sp_label = Label(bottom_frame, text="Strike Price:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        max_put_oi_sp_label.grid(row=1, column=4, sticky=N + S + W + E)
        self.max_put_oi_sp_val = Label(bottom_frame, text="", relief=RIDGE)
        self.max_put_oi_sp_val.grid(row=1, column=5, sticky=N + S + W + E)
        max_put_oi_label = Label(bottom_frame, text="OI (in K):", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        max_put_oi_label.grid(row=1, column=6, sticky=N + S + W + E)
        self.max_put_oi_val = Label(bottom_frame, text="", relief=RIDGE)
        self.max_put_oi_val.grid(row=1, column=7, sticky=N + S + W + E)

        oi_label = Label(bottom_frame, text="CH_OI_Suggetion:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        oi_label.grid(row=2, column=0, columnspan=2, sticky=N + S + W + E)
        self.oi_val = Label(bottom_frame, text="", relief=RIDGE)
        self.oi_val.grid(row=2, column=2, columnspan=2, sticky=N + S + W + E)
        pcr_label = Label(bottom_frame, text="TOI_PCR:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        pcr_label.grid(row=2, column=4, columnspan=2, sticky=N + S + W + E)
        self.pcr_val = Label(bottom_frame, text="", relief=RIDGE)
        self.pcr_val.grid(row=2, column=6, columnspan=2, sticky=N + S + W + E)
        call_exits_label = Label(bottom_frame, text="Long_Short:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        call_exits_label.grid(row=3, column=0, columnspan=2, sticky=N + S + W + E)
        self.call_exits_val = Label(bottom_frame, text="", relief=RIDGE)
        self.call_exits_val.grid(row=3, column=2, columnspan=2, sticky=N + S + W + E)
        put_exits_label = Label(bottom_frame, text="Put Exits:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        put_exits_label.grid(row=3, column=4, columnspan=2, sticky=N + S + W + E)
        self.put_exits_val = Label(bottom_frame, text="", relief=RIDGE)
        self.put_exits_val.grid(row=3, column=6, columnspan=2, sticky=N + S + W + E)
        call_itm_label = Label(bottom_frame, text="Long Count:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        call_itm_label.grid(row=4, column=0, columnspan=2, sticky=N + S + W + E)
        self.call_itm_val = Label(bottom_frame, text="", relief=RIDGE)
        self.call_itm_val.grid(row=4, column=2, columnspan=2, sticky=N + S + W + E)
        put_itm_label = Label(bottom_frame, text="Short Count:", relief=RIDGE, font=("TkDefaultFont", 10, "bold"))
        put_itm_label.grid(row=4, column=4, columnspan=2, sticky=N + S + W + E)
        self.put_itm_val = Label(bottom_frame, text="", relief=RIDGE)
        self.put_itm_val.grid(row=4, column=6, columnspan=2, sticky=N + S + W + E)

        self.root.after(100, self.main)

        self.root.mainloop()

    def get_dataframe(self):
        try:
            response, json_data = self.get_data()
        except TypeError:
            return
        if response is None or json_data is None:
            return

        pandas.set_option('display.max_rows', None)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.width', 400)

        df = pandas.read_json(response.text)
        df = df.transpose()

        ce_values = [data['CE'] for data in json_data['records']['data'] if
                     "CE" in data and str(data['expiryDate'].lower() == str(self.expiry_date).lower())]
        pe_values = [data['PE'] for data in json_data['records']['data'] if
                     "PE" in data and str(data['expiryDate'].lower() == str(self.expiry_date).lower())]
        underlying_stock = ce_values[0]['underlying']
        points = pe_values[0]['underlyingValue']
        ce_data = pandas.DataFrame(ce_values)
        pe_data = pandas.DataFrame(pe_values)
        ce_data_f = ce_data.loc[ce_data['expiryDate'] == self.expiry_date]
        pe_data_f = pe_data.loc[pe_data['expiryDate'] == self.expiry_date]
        if ce_data_f.empty:
            messagebox.showerror(title="Error",
                                 message="Invalid Expiry Date.\nPlease restart and enter a new Expiry Date.")
            self.change_state()
            return
        columns_ce = ['openInterest', 'changeinOpenInterest', 'totalTradedVolume', 'impliedVolatility', 'lastPrice',
                      'change', 'bidQty', 'bidprice', 'askPrice', 'askQty', 'strikePrice']
        columns_pe = ['strikePrice', 'bidQty', 'bidprice', 'askPrice', 'askQty', 'change', 'lastPrice',
                      'impliedVolatility', 'totalTradedVolume', 'changeinOpenInterest', 'openInterest']
        ce_data_f = ce_data_f[columns_ce]
        pe_data_f = pe_data_f[columns_pe]
        merged_inner = pandas.merge(left=ce_data_f, right=pe_data_f, left_on='strikePrice', right_on='strikePrice')
        merged_inner.columns = ['Open Interest', 'Change in Open Interest', 'Traded Volume', 'Implied Volatility',
                                'Last Traded Price', 'Net Change', 'Bid Quantity', 'Bid Price', 'Ask Price',
                                'Ask Quantity', 'Strike Price', 'Bid Quantity', 'Bid Price', 'Ask Price',
                                'Ask Quantity', 'Net Change', 'Last Traded Price', 'Implied Volatility',
                                'Traded Volume', 'Change in Open Interest', 'Open Interest']
        return merged_inner, df['timestamp']['records'], underlying_stock, points


    def set_values(self):
        self.root.title(f"Option-Chain-Analyzer - {self.underlying_stock} - {self.expiry_date} - {self.sp}")

        self.max_call_oi_val.config(text=self.max_call_oi)
        self.max_call_oi_sp_val.config(text=self.max_call_oi_sp)
        self.max_put_oi_val.config(text=self.max_put_oi)
        self.max_put_oi_sp_val.config(text=self.max_put_oi_sp)
        
        
        

        red = "#f7ebeb"
        green = "#ebf7f5"
        default = "SystemButtonFace"
        
        long_list = []
        short_list = []

        if (self.put_sum > self.call_sum):
            #self.oi_val.config(text="Bearish", bg=red)
            self.oi_val.config(text="Buy CE", bg=green)
            int_long = 1
            long_list.append(int_long)
            
        else:
            #self.oi_val.config(text="Bullish", bg=green)
            self.oi_val.config(text="Buy PE", bg=red)
            int_short = 1
            short_list.append(int_short)
        
        if self.put_call_ratio >= 1:
            self.pcr_val.config(text=self.put_call_ratio, bg=green)
        else:
            self.pcr_val.config(text=self.put_call_ratio, bg=red)

        def set_itm_labels(call_change: float, put_change: float) -> str:
            label = "NA"
            if put_change > call_change:
                if put_change >= 0:
                    if call_change <= 0:
                        label = "NA"
                    elif put_change / call_change > 1.5:
                        label = "NA"
                else:
                    if put_change / call_change < 0.5:
                        label = "NA"
            if call_change <= 0:
                label = "NA"
            return label

      
    
        ## put_exit column 
        self.put_exits_val.config(text= "Empty" , bg=default)
        
        
        
        output_values = [self.str_current_time, self.points, self.call_sum, self.put_sum, self.difference,
                         self.call_boundary, self.put_boundary, self.call_itm, self.put_itm]
        self.sheet.insert_row(values=output_values)

        last_row = self.sheet.get_total_rows() - 1

        # Logic for CH_OI table colour background change

        if self.first_run or self.points == self.old_points:
            self.old_points = self.points
        elif self.points > self.old_points:
            self.sheet.highlight_cells(row=last_row, column=1, bg=green)
            #self.old_points = self.points
        else:
            self.sheet.highlight_cells(row=last_row, column=1, bg=red)
            #self.old_points = self.points
        
        if self.first_run or self.old_call_sum == self.call_sum:
            self.old_call_sum = self.call_sum
        elif self.call_sum > self.old_call_sum:
            self.sheet.highlight_cells(row=last_row, column=2, bg=green)
            self.old_call_sum = self.call_sum
        else:
            self.sheet.highlight_cells(row=last_row, column=2, bg=red)
            self.old_call_sum = self.call_sum
        
        ## Put old and current logic
        
        if self.first_run or self.old_put_sum == self.put_sum:
            self.old_put_sum = self.put_sum
        elif self.put_sum > self.old_put_sum:
            self.sheet.highlight_cells(row=last_row, column=3, bg=green)
            self.old_put_sum = self.put_sum
        else:
            self.sheet.highlight_cells(row=last_row, column=3, bg=red)
            self.old_put_sum = self.put_sum
        
              
        
        if self.first_run or self.old_difference == self.difference:
            self.old_difference = self.difference
        elif self.difference > self.old_difference:
            self.sheet.highlight_cells(row=last_row, column=4, bg=green)
            self.old_difference = self.difference
        else:
            self.sheet.highlight_cells(row=last_row, column=4, bg=red)
            self.old_difference = self.difference
       
        
        if self.first_run or self.old_call_boundary == self.call_boundary:
            self.old_call_boundary = self.call_boundary
        elif self.call_boundary > self.old_call_boundary:
            self.sheet.highlight_cells(row=last_row, column=5, bg=green)
            #self.old_call_boundary = self.call_boundary
        else:
            self.sheet.highlight_cells(row=last_row, column=5, bg=red)
            #self.old_call_boundary = self.call_boundary
        
        
        if self.first_run or self.old_put_boundary == self.put_boundary:
            self.old_put_boundary = self.put_boundary
        elif self.put_boundary > self.old_put_boundary:
            self.sheet.highlight_cells(row=last_row, column=6, bg=green)
            #self.old_put_boundary = self.put_boundary
        else:
            self.sheet.highlight_cells(row=last_row, column=6, bg=red)
            #self.old_put_boundary = self.put_boundary
        
        # Call and put vLong Short ## Change the Call_Exit lable in above display
                        
        if (self.points > self.old_points) and ((self.call_boundary + self.put_boundary) > (self.old_call_boundary + self.old_put_boundary)) :
            self.call_exits_val.config(text= "Long Bulidup" , bg=green)
            int_long = 1
            long_list.append(int_long)
        elif (self.points > self.old_points) and ((self.call_boundary + self.put_boundary) < (self.old_call_boundary + self.old_put_boundary)) :
            self.call_exits_val.config(text= "Short Covering" , bg=green)
            int_long = 1
            long_list.append(int_long)
        elif (self.points < self.old_points) and ((self.call_boundary + self.put_boundary) < (self.old_call_boundary + self.old_put_boundary)) :
            self.call_exits_val.config(text= "Long Unwinding" , bg=red)
            int_short = 1
            short_list.append(int_short)
        elif (self.points < self.old_points) and ((self.call_boundary + self.put_boundary) > (self.old_call_boundary + self.old_put_boundary)) :
            self.call_exits_val.config(text= "Short Buildup" , bg=red)
            int_short = 1
            short_list.append(int_short)
        elif self.first_run :
            self.call_exits_val.config(text= "First Run" , bg=green)
        else:
            self.call_exits_val.config(text= "No Change" , bg=green)
        
        

        ## ITM cell logic
            
        if self.first_run or self.old_call_itm == self.call_itm:
            self.old_call_itm = self.call_itm
        elif self.call_itm > self.old_call_itm:
            self.sheet.highlight_cells(row=last_row, column=7, bg=green)
            #self.old_call_itm = self.call_itm
        else:
            self.sheet.highlight_cells(row=last_row, column=7, bg=red)
            #self.old_call_itm = self.call_itm
        
        
        if self.first_run or self.old_put_itm == self.put_itm:
            self.old_put_itm = self.put_itm
        elif self.put_itm > self.old_put_itm:
            self.sheet.highlight_cells(row=last_row, column=8, bg=green)
            #self.old_put_itm = self.put_itm
        else:
            self.sheet.highlight_cells(row=last_row, column=8, bg=red)
            #self.old_put_itm = self.put_itm
        
        
        
        if self.first_run :
            self.old_total_short = 0
            self.old_total_long = 0
        
        
        total_long = sum(long_list)+0
        total_short = sum(short_list)+0
        
        new_total_long = total_long + self.old_total_long
        new_total_short = total_short + self.old_total_short
                
        self.call_itm_val.config(text= new_total_long, bg=default)
        self.put_itm_val.config(text= new_total_short, bg=default)

  
        
        #Updating the new data to old data
        self.old_points = self.points
        self.old_put_boundary = self.put_boundary
        self.old_call_boundary = self.call_boundary
        self.old_call_itm = self.call_itm
        self.old_put_itm = self.put_itm
        self.old_total_long = new_total_long
        self.old_total_short = new_total_short
        
        

        if self.sheet.get_yview()[1] >= 0.9:
            self.sheet.see(last_row)
            self.sheet.set_yview(1)
        self.sheet.refresh()

    def main(self):
        if self.stop:
            return

        try:
            df, current_time, self.underlying_stock, self.points = self.get_dataframe()
        except TypeError:
            self.root.after((self.seconds * 1000), self.main)
            return

        self.str_current_time = current_time.split(" ")[1]
        current_date = datetime.datetime.strptime(current_time.split(" ")[0], '%d-%b-%Y').date()
        current_time = datetime.datetime.strptime(current_time.split(" ")[1], '%H:%M:%S').time()
        if self.first_run:
            self.previous_date = current_date
            self.previous_time = current_time
        elif current_date > self.previous_date:
            self.previous_date = current_date
            self.previous_time = current_time
        elif current_date == self.previous_date:
            if current_time > self.previous_time:
                self.previous_time = current_time
            else:
                self.root.after((self.seconds * 1000), self.main)
                return

        call_oi_list = []
        for i in range(len(df)):
            int_call_oi = int(df.iloc[i, [0]][0])
            call_oi_list.append(int_call_oi)
        call_oi_index = call_oi_list.index(max(call_oi_list))
        self.max_call_oi = round(max(call_oi_list) / 1000, 1)

        put_oi_list = []
        for i in range(len(df)):
            int_put_oi = int(df.iloc[i, [20]][0])
            put_oi_list.append(int_put_oi)
        put_oi_index = put_oi_list.index(max(put_oi_list))
        self.max_put_oi = round(max(put_oi_list) / 1000, 1)

        total_call_oi = sum(call_oi_list)
        total_put_oi = sum(put_oi_list)
        try:
            self.put_call_ratio = round(total_put_oi / total_call_oi, 4)
        except ZeroDivisionError:
            self.put_call_ratio = 0

        
        ## My logic for Change in OI PCR

        call_oi_list_change = []
        for i in range(len(df)):
            int_call_oi_change = int(df.iloc[i, [1]][0])
            call_oi_list_change.append(int_call_oi_change)
        call_oi_index_change = call_oi_list_change.index(max(call_oi_list_change))
        self.max_call_oi_change = round(max(call_oi_list_change) / 1000, 1)

        put_oi_list_change = []
        for i in range(len(df)):
            int_put_oi_change = int(df.iloc[i, [19]][0])
            put_oi_list_change.append(int_put_oi_change)
        put_oi_index_change = put_oi_list_change.index(max(put_oi_list_change))
        self.max_put_oi_change = round(max(put_oi_list_change) / 1000, 1)

        total_call_oi_change = sum(call_oi_list_change)
        total_put_oi_change = sum(put_oi_list_change)
        
        try:
            self.put_call_ratio_change = (total_put_oi_change / total_call_oi_change)
        except ZeroDivisionError:
            self.put_call_ratio_change = 0
            
        ## Logic end for CHOI PCR

        self.max_call_oi_sp = df.iloc[call_oi_index]['Strike Price']
        self.max_put_oi_sp = df.iloc[put_oi_index]['Strike Price']


        try:
            index = int(df[df['Strike Price'] == self.sp].index.tolist()[0])
        except IndexError as err:
            print(err, "10")
            messagebox.showerror(title="Error",
                                 message="Incorrect Strike Price.\nPlease enter correct Strike Price.")
            self.root.destroy()
            return
               
        # Logic for Change in OI Call

        a = df[['Change in Open Interest']][df['Strike Price'] == self.sp]
        b1 = a.iloc[:, 0]
        c1 = b1.get(index)
        b2 = df.iloc[:, 1]
        c2 = 0
        b3 = df.iloc[:, 1]
        c3 = 0
        for numi in range(15):
            c33 = b3.get((index + numi), 'Change in Open Interest')
            c3 = c3+c33
        for numi in range(15):
            c33 = b3.get((index - numi), 'Change in Open Interest')
            c3 = c3+c33
        if isinstance(c2, str):
            c2 = 0
        if isinstance(c3, str):
            c3 = 0
        
        self.call_sum = round((c1 + c2 + c3) / 1000, 1)
        call_sum_oi = self.call_sum 
        
        # Logic for Open intrest calculation call
        aa = df[['Open Interest']][df['Strike Price'] == self.sp]
        b11 = aa.iloc[:, 0]
        c11 = b11.get(index)
        b31 = df.iloc[:, 0]
        c31 = 0
        for numi in range(15):
            c331 = b31.get((index + numi), 'Open Interest')
            c31 = c31+c331
        for numi in range(15):
            c331 = b31.get((index - numi), 'Open Interest')
            c31 = c31+c331
        if isinstance(c31, str):
            c31 = 0
        
        self.call_boundary = round((c11 + c31) / 1000, 1)
        call_boundary_oi = self.call_boundary
        
        if self.call_boundary == -0:
            self.call_boundary = 0.0
            
        # Logic for Change in OI Put
   
        o1 = a.iloc[:, 1]
        p1 = o1.get(index)
        o2 = df.iloc[:, 19]
        p2 = 0
        p3 = 0
        for numi in range(15):
            p33 = o2.get((index + numi), 'Change in Open Interest')
            p3 = p3+p33
        for numi in range(15):
            p33 = o2.get((index - numi), 'Change in Open Interest')
            p3 = p3+p33
        
        self.p4 = o2.get((index + 4), 'Change in Open Interest')
        o3 = df.iloc[:, 1]
        self.p5 = o3.get((index + 4), 'Change in Open Interest')
        self.p6 = o3.get((index - 2), 'Change in Open Interest')
        self.p7 = o2.get((index - 2), 'Change in Open Interest')
        if isinstance(p2, str):
            p2 = 0
        if isinstance(p3, str):
            p3 = 0
        if isinstance(self.p4, str):
            self.p4 = 0
        if isinstance(self.p5, str):
            self.p5 = 0
        self.put_sum = round((p1 + p2 + p3) / 1000, 1)
        
        put_sum_oi = self.put_sum
        # Logic for Open intresrt Put
        o11 = a.iloc[:, 1]
        p11 = o11.get(index)
        o21 = df.iloc[:, 20]
        p31 = 0
        for numi in range(15):
            p331 = o21.get((index + numi), 'Open Interest')
            p31 = p31+p331
        for numi in range(15):
            p331 = o21.get((index - numi), 'Open Interest')
            p31 = p31+p331

        if isinstance(p31, str):
            p31 = 0
        
        self.put_boundary = round((p11 + p31) / 1000, 1)
        put_boundary_oi = self.put_boundary
        if self.put_boundary == -0:
            self.put_boundary = 0.0
        
        # Logic for CHOI diffrance  
        self.difference = round(self.put_sum - self.call_sum, 2)
        
             
        
        # PCR logic
        
        self.put_itm = round(put_sum_oi / call_sum_oi, 4) #OI_PCR logic
        self.call_itm = round(put_boundary_oi / call_boundary_oi,4) #CHOI_PCR logic
        
        
        
        if self.stop:
            return

        self.set_values()

        if self.first_run:
            self.first_run = False
        self.root.after((self.seconds * 900), self.main)
        return

    @staticmethod
    def create_instance():
        master_window = Tk()
        Nse(master_window)
        master_window.mainloop()


if __name__ == '__main__':
    Nse.create_instance()


