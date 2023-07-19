from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from calculate import BMICalculate, Units


class GUI:
    

    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")
        self.master.geometry('220x220+600+220' )
        self.master.resizable(False, False)
        self.master.config(bg="plum2")

        self.height = StringVar()
        self.weight = StringVar()
        self.height_unit = StringVar()
        self.weight_unit = StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.height_label = Label(self.master, text="Height", bg="purple" , fg="plum1")
        self.height_label.grid(row=0, column=0, padx=5, pady=5)

        self.height_entry = Entry(self.master, textvariable=self.height, width=10 , bg="plum" , fg="purple")
        self.height_entry.grid(row=0, column=1, padx=5, pady=5)

        self.height_unit_combobox = ttk.Combobox(self.master, textvariable=self.height_unit, width=5  )
        self.height_unit_combobox["values"] = ("cm", "m", "in" )
        self.height_unit_combobox.current(0)
        self.height_unit_combobox.grid(row=0, column=2, padx=5, pady=5 )

        self.weight_label = Label(self.master, text="Weight", bg="purple" , fg="plum1")
        self.weight_label.grid(row=1, column=0, padx=5, pady=5)

        self.weight_entry = Entry(self.master, textvariable=self.weight, width=10 , bg="plum" , fg="purple")
        self.weight_entry.grid(row=1, column=1, padx=5, pady=5)

        self.weight_unit_combobox = ttk.Combobox(self.master, textvariable=self.weight_unit, width=5 )
        self.weight_unit_combobox["values"] = ("kg", "g", "lb")
        self.weight_unit_combobox.current(0)

        self.weight_unit_combobox.grid(row=1, column=2, padx=5, pady=5)

        self.calculate_button = Button(self.master, text="Calculate", command=self.calculate , bg="purple" , fg="plum1")
        self.calculate_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def calculate(self):
        height = self.height.get()
        weight = self.weight.get()
        height_unit = self.height_unit.get()
        weight_unit = self.weight_unit.get()
        units = Units(height_unit, weight_unit)
        try:
            bmi = BMICalculate(height, weight, units).calculate()
            messagebox.showinfo("BMI", f"Your BMI is {bmi}")
            self.height_entry.delete(0, END)
            self.weight_entry.delete(0, END)
            self.height_unit_combobox.set("")
            self.weight_unit_combobox.set("")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values")



