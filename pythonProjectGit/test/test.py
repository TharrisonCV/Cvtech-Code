
import csv
import json
import os

def write_to_csv(file_name, first_name, last_name, phone_number):
    # Check if the file exists; if not, create and write the header
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['First Name', 'Last Name', 'Phone Number'])
        writer.writerow([first_name, last_name, phone_number])
    print(f"Data written to {file_name}")

def view_csv(file_name):
    if not os.path.isfile(file_name):
        print("The CSV file does not exist.")
        return

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15}")

def convert_csv_to_json(csv_file, json_file):
    if not os.path.isfile(csv_file):
        print("The CSV file does not exist.")
        return

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    with open(json_file, mode='w') as file:
        json.dump(data, file,        indent=4)

    print(f"Data converted to {json_file}")

def view_json(json_file):
    if not os.path.isfile(json_file):
        print("The JSON file does not exist.")
        return

    with open(json_file, mode='r') as file:
        data = json.load(file)
        for entry in data:
            print(f"First Name: {entry['First Name']}, Last Name: {entry['Last Name']}, Phone Number: {entry['Phone Number']}")

def main():
    while True:
        print("\nMenu:")
        print("1) Write to CSV File")
        print("2) View the CSV File")
        print("3) Convert the CSV File to JSON")
        print("4) View JSON")
        print("5) Exit")

        choice = input("Please enter your choice: ")

        if choice == '1':
            first_name = input("What is your first name? ")
            last_name = input("What is your last name? ")
            phone_number = input("What is your phone number? ")
            file_name = f"{first_name.lower()}{last_name.lower()}{phone_number}.csv"
            write_to_csv(file_name, first_name, last_name, phone_number)

        elif choice == '2':
            file_name = input("Enter the CSV file name to view (e.g., firstname_lastname_phonenumber.csv): ")
            view_csv(file_name)

        elif choice == '3':
            csv_file = input("Enter the CSV file name to convert (e.g., firstname_lastname_phonenumber.csv): ")
            json_file = input("Enter the JSON file name to save as (e.g., output.json): ")
            convert_csv_to_json(csv_file, json_file)

        elif choice == '4':
            json_file = input("Enter the JSON file name to view (e.g., output.json): ")
            view_json(json_file)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

