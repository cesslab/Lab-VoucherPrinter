import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class VoucherPrinter(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        root_frame = tk.Frame(self)

        self.title("CESS Payment Voucher Printer")

        root_frame.grid_columnconfigure(0, weight=1)
        root_frame.grid_rowconfigure(0, weight=1)

        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)

        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root_frame.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menu_bar)
        self.frames = {}

        for Frame in (PrimaryFrame, ResultsPage):
            frame = Frame(root_frame, self)
            frame.grid(row=0, column=0, sticky="snew")
            self.frames[Frame] = frame

        self.show_frame(PrimaryFrame)

    def show_frame(self, frame):
        current_frame = self.frames[frame]
        current_frame.tkraise()


class PrimaryFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.file_path_label = ttk.Label(self, text="Start Page", font=("Arial", 12))
        self.file_path_label.pack(pady=10, padx=10)

    def open_payoff_file(self):
        file_name = filedialog.askopenfile(parent=self.parent, filetypes=[("File", "*.pay")])
        try:
            file = open(file_name)
            self.file_path_label.config(text=file_name)
            file.read()
        except Exception as e:
            messagebox.showerror("Error", "Unable to open file. Error: {}.".format(e))


class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=('Arial', 12))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = VoucherPrinter()
app.mainloop()
