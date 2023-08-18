# Assignment 4a Exception handling
# Author : Parth Goyal
# Date created : September 30, 2021
# Date last changed : October 9, 2021
# Input : car_data.txt, Output : results.txt
# This program calculates the average acceleration of cars, distance covered
# and the max average acceleration with proper exception handling


import os
import os.path

INPUT_PATH = 'car_data.txt'     # Input file
OUTPUT_PATH = 'results.txt'     # Output file

# Remove the ouput file if it exists already
try:
    os.remove(OUTPUT_PATH)
except FileNotFoundError:   # FileNotFoundError if the file does not exist and then pass
    pass

print()

# Creating a menu


def menu():
    print("Enter 1 to calculate average acceleration of cars")
    print("Enter 2 to calculate the distance covered by the cars")
    print("Enter 3 for car with greatest acceleration")
    print("Enter 0 to exit")


menu()
print()

# Constant
DEFAULT_TIME = int(10)      # Set default time = 10s

# Creating empty lists to store the content of the input file
name_list = []
v0_list = []
v1_list = []
time_list = []

# Reading from the input file and storing it in the lists
while True:
    try:
        # Check if file exists and is empty or not
        if os.path.exists(INPUT_PATH) == True:
            if (os.stat(INPUT_PATH).st_size == 0):
                print("File is empty")
                exit()

        with open(INPUT_PATH, "r") as f:
            next(f)     # Ignoring the header of the input file
            for line in f:
                line = line.split(',')

                # If time is null use default time
                try:
                    t = line[3]
                except IndexError:  # IndexError used if no time is provided by the user
                    t = DEFAULT_TIME

                # All entries added to the corresponding lists
                try:
                    name_list.append(line[0])
                    v0_list.append(line[1])
                    v1_list.append(line[2])
                    time_list.append(t)

                except NameError:   # NameError as user might have entered incorrect values for variables
                    print("Incorrect data in file")
                    exit()
        break

    except FileNotFoundError:   # FileNotFoundError used if there in no input file
        print(f"The file {INPUT_PATH} does not exist.")
        x = int(input("Press 1 to enter correct file name or press any key to exit: "))

        if x == 1:
            INPUT_PATH = input("Please enter correct input file name: ")
            print()
        else:
            print("Thank You")
            exit()

avg_acc_list = []
distance_list = []
computed_values_list = []


def compute():  # Creating a compute function to calculate average acceleration and
    # distance covered
    for i in range(len(name_list)):

        try:
            # Using formula a = (v1 - v0) / t
            avg_acc = ((float(v1_list[i]) - float(v0_list[i])) /
                       float(time_list[i]))

            # Using formula distance = (v0*t) + (1/2 * a * t^2)
            distance = ((float(v0_list[i]) * (float(time_list[i]))) +
                        (1/2)*(avg_acc)*(float(time_list[i])**2))

        except ZeroDivisionError:   # ZeroDivisionError as user might enter time as 0.
            print("Time cannot be zero. Default time of 10s has been considered.")

            avg_acc = ((float(v1_list[i]) - float(v0_list[i])) /
                       float(DEFAULT_TIME))

            distance = ((float(v0_list[i]) * (float(DEFAULT_TIME))) +
                        (1/2)*(avg_acc)*(float(DEFAULT_TIME)**2))

        except ValueError:  # ValueError as user might enter invalid value in the file
            print(
                f"You have entered incorrect information in the file {INPUT_PATH}.")
            exit()

        avg_acc_list.append(avg_acc)

        distance_list.append(distance)

        computed_values = (avg_acc, distance)   # Using a tuple here
        computed_values_list.append(computed_values)


def f_avg_acc():    # A function to write average acceleration in the output file
    compute()       # Calling the compute function
    try:
        for i in range(len(name_list)):

            with open(OUTPUT_PATH, 'a') as wf:
                wf.write("{} {} {} {} {}\n".format("Average acceleration of car",
                                                   name_list[i], "is", str(computed_values_list[i][0]), 'm/s\u00b2'))
                # eg: m/s\u00b2 = m/s^2

        with open(OUTPUT_PATH, 'a') as wf:
            wf.write('\n')

    except IOError:    # IOError used if in case of input/output issue
        print("Unable to write to file")


def f_distance():   # A function to write distance covered in the output file
    compute()       # Calling the compute function
    try:
        for i in range(len(name_list)):
            with open(OUTPUT_PATH, 'a') as wf:
                wf.write("{} {} {} {} {}\n".format("Distance covered by car",
                                                   name_list[i], "is", str(computed_values_list[i][1]), 'm'))

        with open(OUTPUT_PATH, 'a') as wf:
            wf.write('\n')

    except IOError:    # IOError used if in case input/output issue
        print("Unable to write to file")


def greatest_acceleration():    # A function to write greatest acceleration in the output file
    compute()       # Calling the compute function
    greatest = max(avg_acc_list)    # Max value of average acceleration
    indexOfGreatest = avg_acc_list.index(greatest)    # Index of the max value

    try:
        with open(OUTPUT_PATH, 'a') as wf:
            wf.write("{} {} {}".format("Car", name_list[indexOfGreatest],
                                       "has the greatest average acceleration."))

        with open(OUTPUT_PATH, 'a') as wf:
            wf.write('\n')

    except IOError:    # IOError used if in case of input/output issue
        print("Unable to write to file")

# Choice function


def choice():
    global options
    while True:
        try:
            options = int(input("Enter the options: "))
            break
        except ValueError:  # ValueError used if user enters a value other than integer
            print("Please enter a number!!")
            print()

# Main function


def main():
    choice()    # Calling the choice function
    while True:
        if options == 1:    # Option 1 to calculate average acceleration of the cars
            f_avg_acc()
            print("\nAverage acceleration has been calculated and printed to the"
                  f" {OUTPUT_PATH} file")
        elif options == 2:  # Option 2 to calculate the distance covered by the cars
            f_distance()
            print("\nDistance covered has been calculated and printed to the"
                  f" {OUTPUT_PATH} file")
        elif options == 3:  # Option 3 to calculate the max average acceleration of the car
            greatest_acceleration()
            print("\nMaximum average acceleration has been calculated and printed to the"
                  f" {OUTPUT_PATH} file")
        elif options == 0:  # Option 0 to exit the program
            print('Thank You')
            exit()

        else:   # If user enters an integer other than 0,1,2,3 print invalid input
            print("Invalid input. Please enter a number from 0-3")

        print()
        menu()
        print()

        choice()


main()  # Calling the main function
