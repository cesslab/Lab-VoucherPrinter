import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

from vprinter.voucher import Voucher
from vprinter.configuration import ConfigurationSettings


class VoucherPrinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frames = {}

        self.geometry("800x600")
        self.title("CESS Payment Voucher Printer")

        self.init_frames()
        self.setup_menu()

        self.voucher = Voucher()

        self.total_rows = 1

        self.show_frame(PrimaryFrame)

    def show_frame(self, frame):
        current_frame = self.frames[frame]
        current_frame.tkraise()

    def init_frames(self):
        frames = (PrimaryFrame, ResultsFrame)
        for F in frames:
            frame = F(self)
            frame.grid(row=0, column=0, sticky="snew")
            self.frames[F] = frame

    def setup_menu(self):
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open Z-Tree Payoff File", command=self.open_payoff_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

    def open_payoff_file(self):
        file_name = filedialog.askopenfilename(parent=self, filetypes=[("File", "*.pay")])
        if self.voucher.open_file(file_name):
            self.frames[PrimaryFrame].build_table(self.voucher.subjects, self.voucher.payoffs)
        else:
            messagebox.showerror("Error", "Unable to open file. Error: {}.".format(self.voucher.error))


class PrimaryFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.setup_toolbar()
        self.config_settings = ConfigurationSettings()

    def setup_toolbar(self):
        toolbar = tk.Frame(self)
        open_file_icon_path = os.path.join("images", "folder-open-o.png")
        open_button = ttk.Button(toolbar, command=self.parent.open_payoff_file)
        try:
            img = ImageTk.PhotoImage(file=open_file_icon_path)
            open_button.config(image=img)
            open_button.image = img
            open_button.pack(side=tk.LEFT, padx=2, pady=2)
        except Exception as e:
            print("Error: {}".format(e))

        toolbar.grid(row=0, column=0, sticky="nwe")

    def calibrate(self):
        pass

    def build_table(self, subjects, payoffs):
        rows = len(subjects)
        for row in range(1, rows):  # Rows
            a = ttk.Entry(self)
            a.insert(tk.END, subjects[row])
            a.grid(row=row, column=0)

            b = ttk.Entry(self)
            b.insert(tk.END, payoffs[row])
            b.grid(row=row, column=1)

        config_label = ttk.Label(text='Select a print configuration')
        config_label.grid(row+1, column=0)
        combo = ttk.Combobox(self)
        combo['values'] = self.config_settings.to_list()
        button1 = ttk.Button(self, text="Calibrate", command=lambda: self.calibrate())
        button1.grid(row=rows+1, column=0)


class ResultsFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Results", font=('Arial', 12))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back", command=lambda: parent.show_frame(PrimaryFrame))
        button1.pack()


