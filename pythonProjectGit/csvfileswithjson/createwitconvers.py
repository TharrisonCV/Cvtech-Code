import csv
import json
import os

from pyexpat.errors import codes

# Prompt the user for information
run_pro = True
while run_pro:
    print(f"\nCSV Project!\n\t1) Write to CSV File\n\t2) View the CSV File\n\t3) Convert the CSV File to JSON\n\t"
          f"4) View JSON\n\t5) Exit")
    user_menu_option = int(input("Make your choice: "))

    if user_menu_option == 1:
        user_first_name = input("What is your first name? ")
        user_last_name = input("What is your last name? ")
        user_phone_number = input("What is your phone number? ")

        user_file_name = str(user_first_name + user_last_name + user_phone_number).lower()
        print(f"Your file name is: {user_file_name}.csv")

        # Open the file for writing
        with open(f"{user_file_name}.csv", "w") as d:
            d.write(f"Information: \nFirst Name: {user_first_name} \nLast Name: {user_last_name} \nPhone Number: {user_phone_number}")

    elif user_menu_option == 2:
        # Open the file for reading
        user_file_name_input = input("Enter your file name in 'filename' format: ")
        file_path = f"{user_file_name_input}.csv"
        if os.path.exists(file_path):
            with open(file_path, "r") as d:
                content = d.read()
            print(content)
        else:
            print("File not found. Please make sure the file exists and try again.")
        #this converts the csv file path into a JSON path
    elif user_menu_option == 3:
        user_file_name_input = input("Enter your file name in 'filename' format: ")
        csv_file_path = f"{user_file_name_input}.csv"
        json_file_path = f"{user_file_name_input}.json"
        if os.path.exists(csv_file_path):
            with open(csv_file_path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                data = list(csv_reader)
            with open(json_file_path, mode='w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"CSV data has been converted to JSON and saved as {json_file_path}.")
        else:
            #if there is no path it will return error
            print("CSV file not found. Please make sure the file exists and try again.")
    #opens the json file
    elif user_menu_option == 4:
        user_file_name_input = input("Enter your file name in 'filename' format: ")
        json_file_path = f"{user_file_name_input}.json"
        if os.path.exists(json_file_path):
            with open(json_file_path, mode='r') as json_file:
                data = json.load(json_file)
            print(json.dumps(data, indent=4))
        else:
            print("JSON file not found. Please make sure the file exists and try again.")
    # this will remove files or end the program
    elif user_menu_option == 5:
        exit_code_user = input(f"would you like to remove files? \nYes or No? ")
        if exit_code_user == "Yes":
            file_name_remover = input("Enter your file name in 'filename' format: ")
            user_file_remover = int(
                input(f"What file would you like to remove? \ncsv = 1 \njson = 2 \nMake your choice: "))
            if user_file_remover == 1:
                os.remove(f"{file_name_remover}.csv")
                print(f"{file_name_remover}.csv was removed")
            elif user_file_remover == 2:
                os.remove(f"{file_name_remover}.json")
                print(f"{file_name_remover}.json was removed")
            else:
                print("error cannot process")
        elif exit_code_user == "No":
            print("Done")
            break

        else:
            print("UnKnown variable check the word bank and try again.")

    #if the user inputs anything except 1-5 error will pop up and repromt
    else:
        print("UNKNOWN!!! ERROR!!!!")
        break
