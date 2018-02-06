import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class PrimaryFrame(tk.Frame):
    def __init__(self, root_frame, voucher_printer):
        tk.Frame.__init__(self, root_frame)

        self.voucher_printer = voucher_printer

        self.label = ttk.Label(self, text="File Path:", font=('Arial', 12))
        self.label.pack(pady=10, padx=10)


class ResultsFrame(tk.Frame):
    def __init__(self, root_frame, voucher_printer):
        tk.Frame.__init__(self, root_frame)

        self.voucher_printer = voucher_printer

        label = ttk.Label(self, text="Results", font=('Arial', 12))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back", command=lambda: root_frame.show_frame(PrimaryFrame))
        button1.pack()


class Voucher:
    def __init__(self, file_name):
        self.file_loaded = True
        self.file_name = file_name


class VoucherPrinterTk(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        root_frame = tk.Frame(self)

        root_frame.pack(side="top", fill="both", expand=True)
        root_frame.grid_columnconfigure(0, weight=1)
        root_frame.grid_rowconfigure(0, weight=1)

        self.title("CESS Payment Voucher Printer")

        self.frames = {}
        for Frame in (PrimaryFrame, ResultsFrame):
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

        self.show_frame(PrimaryFrame)

    def show_frame(self, frame):
        current_frame = self.frames[frame]
        current_frame.tkraise()

    def open_payoff_file(self):
        file_name = filedialog.askopenfilename(parent=self, filetypes=[("File", "*.pay")])
        self.frames[PrimaryFrame].label.config(text='File: ' + file_name)
        try:
            file = open(file_name, "r")
            self.voucher_printer.load_file(file.read())
        except Exception as e:
            messagebox.showerror("Error", "Unable to open file. Error: {}.".format(e))


app = VoucherPrinterTk()
app.mainloop()
