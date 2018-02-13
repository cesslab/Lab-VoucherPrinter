import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from vprinter import ui
from vprinter.voucher import Voucher


class PrimaryFrame(tk.Frame):
    def __init__(self, root_frame, voucher_printer):
        tk.Frame.__init__(self, root_frame)

        self.voucher_printer = voucher_printer


class VoucherPrinterGUI(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        root_frame = tk.Frame(self)
        self.geometry("800x600")

        root_frame.grid_columnconfigure(0, weight=1)
        root_frame.grid_rowconfigure(0, weight=1)

        self.title("CESS Payment Voucher Printer")

        self.frames = {}
        for Frame in (ui.PrimaryFrame, ui.ResultsFrame):
            frame = Frame(root_frame, self)
            frame.grid(row=0, column=0, sticky="snew")
            self.frames[Frame] = frame

        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open Z-Tree Payoff File", command=self.open_payoff_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root_frame.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

        self.voucher = Voucher()

        self.total_rows = 1

        self.show_frame(ui.PrimaryFrame)

    def show_frame(self, frame):
        current_frame = self.frames[frame]
        current_frame.tkraise()

    def calibrate(self):
        pass

    def build_table(self, subjects, payoffs):
        rows = len(subjects)
        for row in range(1, rows):  # Rows
            a = ttk.Entry(self)
            a.insert(tk.END, subjects[row])
            a.grid(row=self.total_rows, column=0)

            b = ttk.Entry(self)
            b.insert(tk.END, payoffs[row])
            b.grid(row=self.total_rows, column=1)

            self.total_rows += 1

        button1 = ttk.Button(self, text="Calibrate", command=lambda: self.calibrate())
        button1.grid(row=self.total_rows, column=0)

    def open_payoff_file(self):
        file_name = filedialog.askopenfilename(parent=self, filetypes=[("File", "*.pay")])
        if self.voucher.open_file(file_name):
            self.build_table(self.voucher.subjects, self.voucher.payoffs)
        else:
            messagebox.showerror("Error", "Unable to open file. Error: {}.".format(self.voucher.error))


class ResultsFrame(tk.Frame):
    def __init__(self, root_frame, voucher_printer):
        tk.Frame.__init__(self, root_frame)

        self.voucher_printer = voucher_printer

        label = ttk.Label(self, text="Results", font=('Arial', 12))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back", command=lambda: root_frame.show_frame(PrimaryFrame))
        button1.pack()


