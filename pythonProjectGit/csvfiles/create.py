#import csv
#import json
import os


# Prompt the user for information
run_pro = True
while run_pro:
   print(f"\nCSV Project!\n \t 1) Write to CSV File \n\t 2) View the CSV File\n\t 3) Convert the CSV File to JSON \n\t "
         f"4) View JSON\n\t 5) Exit")
   user_menu_option = int(input("Make your choice: "))

    #ask the user if they would like to create a csv file
   if user_menu_option == 1:
       #prompt first name
       user_first_name = input(f"What is your first name? ")

        #prompt last name
       user_last_name = input(f"What is your last name? ")

        #prompt phone number
       user_phone_number = input(f"What is your phone number? ")

        #this creates the file name


       user_file_name = str(user_first_name+user_last_name+user_phone_number).lower()


       print(f"Your file name is: {user_file_name}.csv")
       # Open the file for writing
       d = open(f"{user_file_name}.csv", "w")
       d.write(f"Information: \n First Name: {user_first_name} \n Last Name: {user_last_name} \n Phone Number: {user_phone_number}")
       d.close()

    #reads the csv file
   elif user_menu_option == 2:
       # Open the file for reading
       user_file_name_input= input(f"enter your file name in \'filename\' format: ")
       file_path =(f"{user_file_name_input}.csv")
       #checks if file exists, if so then read information
       if os.path.exists(file_path):
           with open(file_path, "r") as d:
               content = d.read()
           print(content)
       else:
           #if file is not found then give error and repromt
           print("File not found. Please make sure the file exists and try again.")

    # this will end the program
   elif user_menu_option ==5 :
       print("Done")
       run_pro = False
    #if the user inputs a false number this will display then will repromt for a new number
   else:
       print("UNKNOWN!!! ERROR!!!!")
