import math
from datetime import datetime

def calculate_tire_volume():
    with open("volumes.txt", "at") as volumes_file:

        width_of_the_tire = int(input("Please enter the width of the tire in mm (e.g. 205): "))
        aspect_ratio_of_the_tire = int(input("Please enter the aspect ratio of the tire (e.g. 60): "))
        the_diameter_of_the_wheel = int(input("Please enter the diameter of the wheel in inches (e.g. 15): "))

        first_part = math.pi * (width_of_the_tire**2)
        second_part = first_part * aspect_ratio_of_the_tire
        third_part = (width_of_the_tire * aspect_ratio_of_the_tire) + (2540 * the_diameter_of_the_wheel)
        fourth_part = (second_part * third_part) / 10000000000
        current_date_and_time = datetime.now()

        # questions about the buy.
        get_choice = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()

        if get_choice == "yes":
            name_client = input("Please write your name: ")
            phone_client = input("Please enter your phone number: ")

            volumes_file.write(f"Name of the client: {name_client}, Phone number: {phone_client}\n")
            print("Thank you! Your information has been stored.")
        else:
            print("Thank you for visiting us.")

        print(f"{current_date_and_time:%Y-%m-%d}, {width_of_the_tire}, {aspect_ratio_of_the_tire}, {the_diameter_of_the_wheel}, {fourth_part:.2f}", sep=", ", flush=True)
        volumes_file.write(f"{current_date_and_time:%Y-%m-%d},{width_of_the_tire}, {aspect_ratio_of_the_tire},{the_diameter_of_the_wheel}, {fourth_part:.2f}\n")

if __name__ == "__main__":
    calculate_tire_volume()
