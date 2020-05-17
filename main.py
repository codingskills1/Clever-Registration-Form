from tkinter import * 
import tkinter as tk 
from tkinter.ttk import *
from tkinter import messagebox 
import sys 

window = Tk()

window.title("Registration Form")

window.geometry("800x700")

# Labels 
top_label = Label(window, text = "Athlete Information", font=("Arial Bold", 20))
name_label = Label(window, text = "Athlete's name", font=("Arial Bold", 10))
firstname_label = Label(window, text = "First Name")
lastname_label = Label(window, text = "Last Name")
Birth_label = Label(window, text = "Birth Date", font=("Arial Bold", 10))
birth_spin_label = Label(window, text = "Month")
day_label = Label(window, text = "Day")
year_label = Label(window, text = "Year")
grade_label = Label(window, text = "Grade", font=("Arial Bold", 10))
gender_label = Label(window, text = "Gender", font=("Arial Bold", 10))
address_label = Label(window, text = "Address", font=("Arial Bold", 10))
address_guide_label = Label(window, text = "Street Address")
address_guide_label2 = Label(window, text = "Street Address Line 2")
city_label = Label(window, text = "City")
province_label = Label(window, text = "State / Province")
postal_label = Label(window, text = "Postal / Zip Code")
country_label = Label(window, text = "Country")

# Entries 
name_entry = Entry(window, width = 30)
last_entry = Entry(window, width = 30)
address_entry = Entry(window, width = 50)
address_entry2 = Entry(window, width = 50)
city_entry = Entry(window, width = 20)
province_entry = Entry(window, width = 20)
postal_entry = Entry(window, width = 20)
country_entry = Entry(window, width = 20)

name_entry.focus()

# Spin Box 

spin_state = StringVar()

v = ["January", "February", "March", "April", "May" , "June", "July", "August", "September", "Octobor", "November", "December"]

default = v[0]

spin_state.set(default)

spin = Spinbox(window, values = v, textvariable = spin_state)

spin_day_state = IntVar()

spin_day_state.set(8)

grade_values = ["elementary", "secondary", "highschool", "university"]

grade_state = StringVar()

grade_state.set(grade_values[0])

spin_grade = Spinbox(window, values = grade_values, textvariable = grade_state)

spin_year_state = IntVar()

spin_year_state.set(1970)

spin_day = Spinbox(window, from_ = 1, to_ = 31, textvariable = spin_day_state, width = 8)

spin_year = Spinbox(window, from_ = 1970, to_ = 2020, textvariable = spin_year_state, width = 10)

# Radio Buttons 
selected = IntVar()
selected.set(1)

r1 = Radiobutton(window, text = "Male", value = 1, variable = selected)
r2 = Radiobutton(window, text = "Female", value = 2, variable = selected)

# Place Radio Buttons 
r1.place(x = 140, y = 310)
r2.place(x = 140, y = 340)

# Place Spins 
spin.place(x = 140, y = 160)
spin_day.place(x = 300, y = 160)
spin_year.place(x = 380, y = 160)
spin_grade.place(x = 140, y = 240)

# Place Labels 
top_label.place(x = 20, y = 20)
name_label.place(x = 20, y = 80)
firstname_label.place(x = 140, y = 100)
lastname_label.place(x = 340, y = 100)
Birth_label.place(x = 20, y = 160)
birth_spin_label.place(x = 140, y = 180)
day_label.place(x = 300, y = 180)
year_label.place(x = 380, y = 180)
grade_label.place(x = 20, y = 240)
gender_label.place(x = 20, y = 320)
address_label.place(x = 20, y = 400)
address_guide_label.place(x = 140, y = 420)
address_guide_label2.place(x = 140, y = 470)
city_label.place(x = 140, y = 520)
province_label.place(x = 280, y = 520)
postal_label.place(x = 140, y = 570)
country_label.place(x = 280, y = 570)

# Place Entries 
name_entry.place(x = 140, y = 80)
last_entry.place(x = 340, y = 80)
address_entry.place(x = 140, y = 400)
address_entry2.place(x = 140, y = 450)
city_entry.place(x = 140, y = 500)
province_entry.place(x = 280, y = 500)
postal_entry.place(x = 140, y = 550)
country_entry.place(x = 280, y = 550)


# Validation 
def validation():
	# Name Entry Validation 
	if name_entry.get() == "":
		messagebox.showerror("error", "Enter Your Name")

	elif len(name_entry.get()) < 2:
		messagebox.showerror("error", "Enter a Valid Name")

	elif len(name_entry.get()) > 15:
		messagebox.showerror("error", "Your Name is too long")

	# Last Name Entry Validation 
	if last_entry.get() == "":
		messagebox.showerror("error", "Enter Your Lastname")

	elif len(last_entry.get()) < 2:
		messagebox.showerror("error", "Enter Valid Lastname")

	elif len(last_entry.get()) > 15:
		messagebox.showerror("error", "Your LastName is too long")

	# Address Validation 
	if address_entry.get() == "":
		messagebox.showerror("error", "Enter Your Address")

	elif len(address_entry.get()) < 8:
		messagebox.showerror("error", "Enter Valid Adress")

	elif len(address_entry.get()) > 100:
		messagebox.showerror("error", "Please Enter the rest of your address in the next line")

	# City Validation 
	if city_entry.get() == "":
		messagebox.showerror("error", "Enter Your City")

	elif len(city_entry.get()) < 2:
		messagebox.showerror("error", "Enter Valid City")

	elif len(city_entry.get()) > 40:
		messagebox.showerror("error", "your city name is not valid")

	# Province Validation 
	if province_entry.get() == "":
		messagebox.showerror("error", "Enter Your province")

	elif len(province_entry.get()) < 2:
		messagebox.showerror("error", "Enter Valid province")

	elif len(province_entry.get()) > 40:
		messagebox.showerror("error", "your province name is not valid")

	# Postal Validation (Zip Code)
	if postal_entry.get() == "":
		messagebox.showerror("error", "Enter Your Postal code(Zip Code)")

	elif len(postal_entry.get()) < 5:
		messagebox.showerror("error", "Enter Valid Postal code")

	elif len(postal_entry.get()) > 35:
		messagebox.showerror("error", "Your Postal Code is not valid is too long")

	# Country Validation

	if country_entry.get() == "":
		messagebox.showerror("error", "Enter Your Country")

	elif len(country_entry.get()) < 2:
		messagebox.showerror("error", "Enter Valid Country")

	elif len(country_entry.get()) > 20:
		messagebox.showerror("error", "your Country name is not valid")

	else:
		messagebox.showinfo("Successful", "You Registered Successfully")
		sys.exit()


# Button 
validation_button = tk.Button(window, text = "Register", fg = "black", bg = "white", command = validation)

validation_button.place(x = 20, y = 600)

window.mainloop()