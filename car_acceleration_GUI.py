# Assignment 4_GUI
# Author : Parth Goyal
# Date created : October 1, 2021
# Date last changed : October 12, 2021
# This program creates a GUI that calculates the average acceleration of cars,
# distance covered and the max average acceleration.


# Calling the library
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import colorchooser

# Constant
DEFAULT_TIME = int(10)  # Set default time = 10s

ls_acc = []  # List for car names along with the calculated accelerations

# Defining functions

def f_avg_acc():    # Function to calculate the average acceleration
    try:
        car_name = str(first_name.get())
        initial_velocity = eval(second_number.get())
        final_velocity = eval(third_number.get())

        # If user forgot to calculate the time taken then default time shall be considered
        # as mentioned in the background context of the topic
        try:
            time_taken = eval(fourth_number.get())
            
        except SyntaxError: # If time is empty it will give SyntaxError, thus use default time
            time_taken = DEFAULT_TIME
            
        result_acc = (float(final_velocity) -
                      float(initial_velocity)) / float(time_taken)

        if len(car_name) == 0:  # If car name is empty, show error message
            tmsg.showerror("Error", "Car name cannot be left empty")
            return

    except ZeroDivisionError:   # ZeroDivisionError as user might enter time as 0.
        # Provide user the option to either go with default time
        # or change the time
        a = tmsg.askyesno(
            "Error", "You entered 0s as time taken. Default time of 10s will be considered."
            "\nDo you wish to continue with the default time?")

        if a:
            time_taken = DEFAULT_TIME
        else:
            return

    except NameError:   # NameError as user might enter incorrect values for variables
        tmsg.showerror("Error", "Please input valid values")
        return

    except SyntaxError:     # SyntaxError as there can be error in python syntax
        tmsg.showerror("Error", "Please input valid values")
        return

    # Calculating the average acceleration
    result_acc = ((float(final_velocity) - float(initial_velocity)) / 
        float(time_taken))

    values = (result_acc, car_name) # Creating a tuple of car acceleration and their names

    for i in range(len(ls_acc)):    # Editing the value of acceleration of a car if
        # it has been entered already
        if car_name == ls_acc[i][1]:
            ls_acc.pop(i)
            break

    ls_acc.append(values)

    gui_result.set(
        f"Average Acceleration of Car {car_name} is {result_acc :.3f} m/s\u00b2")


def f_distance():   # Function to calculate the distance covered
    try:
        car_name = str(first_name.get())
        initial_velocity = eval(second_number.get())
        final_velocity = eval(third_number.get())

        # If user forgot to calculate the time taken then default time shall be considered
        # as mentioned in the background context of the topic
        try:    
            time_taken = eval(fourth_number.get())
            
        except SyntaxError: # If time is empty it will give SyntaxError, thus use default time
            time_taken = DEFAULT_TIME
            
        if len(car_name) == 0:  # If car name is empty, show error message
            tmsg.showerror("Error", "Car name cannot be left empty")
            return

        # Calculating the distance covered by the car
        avgAcc = ((float(final_velocity) - float(initial_velocity)) / 
            float(time_taken))
        result_distance = ((float(initial_velocity)*float(time_taken)) + 
            1/2*(float(avgAcc)*float(time_taken)**2))

    except ZeroDivisionError:   # ZeroDivisionError as user might enter time as 0.
        result_distance = 0.0   # If time taken is 0, then distance covered will always be 0

    except NameError:   # NameError as user might enter incorrect values for variables
        tmsg.showerror("Error", "Please input valid values")
        return

    except SyntaxError:    # SyntaxError as there can be error in python syntax
        tmsg.showerror("Error", "Please input valid values")
        return

    gui_result.set(
        f"Distance covered by car {car_name} is {str(result_distance)} m")


def f_max_acceleration():   # Function to find the car with the max average acceleration
    acc_arr = []    # List for all the calculated accelerations only

    try:
        for i in range(len(ls_acc)):

            acc_arr.append(ls_acc[i][0])
            greatest = max(acc_arr)    # Max value of average acceleration
            index_of_greatest = acc_arr.index(
                greatest)    # Index of the max value

    except IndexError:  # IndexError if index out of range
        tmsg.showerror("Error", "Something went wrong, please try again")

    gui_result.set(
        f"Car {(ls_acc[index_of_greatest][1])} has the max average acceleration of{greatest: .3f} m/s\u00b2")


# Showing error message if max average acceleration is calculated for less than 2 cars

def show_warning():
    if len(ls_acc) == 0:
        tmsg.showerror("Error", "Please calculate average acceleration of atleast 2 cars first")
    elif len(ls_acc) == 1:
        tmsg.showerror("Error", "Please calculate average acceleration of atleast 1 more car")
    else:
        f_max_acceleration()


# A function to display the about message

def about():
    tmsg.showinfo("About", "This program helps the user to calculate the"
                  " average acceleration, distance covered and find"
                  " the max average acceleration of a car.")


# A function to change background color of the widgets

def Colors(i):
    color_name = ['palegreen', 'lightpink', 'SystemButtonFace']
    lst_widget = [window, lbl_first, lbl_second, lbl_third,
                  lbl_fourth, dropdown, btn_calculate, btn_max]

    for widget in range(len(lst_widget)):
        lst_widget[widget].config(background=color_name[i])


# A function to display the color palette

def color_palette():
    color_code = colorchooser.askcolor(title="Color Palette")

    lst_widget = [window, lbl_first, lbl_second, lbl_third,
                  lbl_fourth, dropdown, btn_calculate, btn_max]

    for widget in range(len(lst_widget)):
        lst_widget[widget].config(background=color_code[1])


def options(event):
    global choice
    choice = var_options.get()

# A menu to give the user the option to calculate average acceleration or distance covered

def menu():
    try:
        if choice == 'Average Acceleration':
            f_avg_acc()
        elif choice == "Distance Covered":
            f_distance()
    except NameError:
        tmsg.showerror("Error", "Please choose between one from the options")


# Creating object window

window = Tk()
window.title("Car Kinematics")

# Creating a color menu bar
menubar = Menu(window)

color_menu = Menu(menubar, tearoff=0)

color_menu.add_command(label="Pale Green", command=lambda: Colors(0))
color_menu.add_command(label="Light Pink", command=lambda: Colors(1))
color_menu.add_command(label="Default", command=lambda: Colors(2))
color_menu.add_separator()
color_menu.add_command(label="Color Palette", command=color_palette)

menubar.add_cascade(label="Colors", menu=color_menu)

about_menu = Menu(menubar, tearoff=0)

about_menu.add_command(label='About', command=about)
menubar.add_cascade(label="About", menu=about_menu)

window.config(menu=menubar)


# Adding labels
lbl_first = Label(window, text="Car name:",
                  borderwidth=2, relief=SUNKEN, width=15)
lbl_first.grid(row=0, column=0, padx=(10, 0), pady=(10, 5))

lbl_second = Label(window, text="Initial Velocity:", borderwidth=2,
                   relief=SUNKEN, width=15)
lbl_second.grid(row=1, column=0, padx=(10, 0))

lbl_third = Label(window, text="Final Velocity:",
                  borderwidth=2, relief=SUNKEN, width=15)
lbl_third.grid(row=2, column=0, padx=(10, 0), pady=(5))

lbl_fourth = Label(window, text="Time taken:",
                   borderwidth=2, relief=SUNKEN, width=15)
lbl_fourth.grid(row=3, column=0, padx=(10, 0))


# Adding entries
first_name = StringVar()
ent_first = Entry(window, width=5, borderwidth=2, textvariable=first_name)
ent_first.grid(row=0, column=1, padx=(0, 20), pady=(10, 0))

second_number = StringVar()
ent_second = Entry(window, width=5, borderwidth=2, textvariable=second_number)
ent_second.grid(row=1, column=1, padx=(0, 20))

third_number = StringVar()
ent_third = Entry(window, width=5, borderwidth=2, textvariable=third_number)
ent_third.grid(row=2, column=1, padx=(0, 20))

fourth_number = StringVar()
ent_fourth = Entry(window, width=5, borderwidth=2, textvariable=fourth_number)
ent_fourth.grid(row=3, column=1, padx=(0, 20))

# Adding the entry that prints the results
gui_result = StringVar()
ent_fifth = Entry(window, width=49, borderwidth=2,
                  state="readonly", textvariable=gui_result)
ent_fifth.grid(row=6, column=0, columnspan=2, padx=5, pady=10)


# Addind dropdown menu
options_list = ['Average Acceleration', 'Distance Covered']
var_options = StringVar()
var_options.set('Options')
dropdown = OptionMenu(window, var_options, *options_list, command=options)
dropdown.config(width=17)
dropdown.grid(row=4, column=0, padx=(5, 0), ipadx=5, pady=10)


# Adding button
btn_calculate = Button(window, width=12, text="Calculate", command=menu)
btn_calculate.grid(row=4, column=1, padx=10)

btn_max = Button(window, width=18, text="Maximum Acceleration",
                 command=show_warning)
btn_max.grid(row=5, column=0, padx=10)

btn_exit = Button(window, width=8, text="Exit", command=window.destroy,
                  borderwidth=3, bg='light blue')
btn_exit.grid(row=7, column=0, columnspan=2, pady=(0, 20))


window.mainloop()
