# from gui import *

# def main():
#     question1()

# if __name__ == "__main__":
#     main()


def ask_opener_question():
    opener_question = "What is your primary purpose for the vehicle?\n1. Daily commuting and running errands\n2. Family transportation\n3. Adventure and off-road activities\n4. Luxury and comfort\n5. Business use"
    possible_purposes = ["1", "2", "3", "4", "5"]
    while True:
        response = input(
            opener_question + "\nEnter the number corresponding to your choice: "
        )
        if response in possible_purposes:
            break
        print("Invalid input Please try again.")
    return response


def ask_followup_questions(purpose):
    allowed_responses = ["1", "2"]
    if purpose == "1":
        commute_question = "How long is your average commute?\nEnter '1' for under 30 minutes or '2' for over 30 minutes: "
        commute_response = input(commute_question)
        if (
            not commute_response
            in allowed_responses
            # or not size_question in allowed_responses
        ):
            print("Invalid input. Please try again.")
            return None
        else:
            if commute_response == "1":
                size_question = "Do you prefer a compact or a larger vehicle for your daily needs?\nEnter '1' for compact or '2' for larger: "
                size_response = input(size_question)
                if size_response == "1":
                    return "Hatchback or Sedan"
                else:
                    return "Crossover SUV"
            elif commute_response == "2":
                cargo_question = "Do you require additional cargo space for goods, equipment or other items?\nEnter '1' for yes or '2' for no: "
                cargo_response = input(cargo_question)
                if cargo_response == "1":
                    return "Minivan or Pickup Truck"
                else:
                    return "Mid-size Sedan or SUV"

    elif purpose == "2":
        family_question = "How many family members do you need to accommodate?\nEnter '1' for up to 4 members or '2' for more than 4 members: "
        family_response = input(family_question)
        if (
            not family_response
            in allowed_responses
            # or not storage_question in allowed_responses
        ):
            print("Invalid input Please try again.")
            return None
        else:
            if family_response == "1":
                storage_question = "Do you require extra storage space for strollers, sports equipment, or other items?\nEnter '1' for yes or '2' for no: "
                storage_response = input(storage_question)
                if storage_response == "1":
                    return "Compact SUV"
                else:
                    return "Compact SUV with extra storage space on the roof or Minivan"
            elif family_response == 2:
                luxury_question = "Do you want your vehicle to feel luxurious?\nEnter '1' for yes or '2' for no: "
                luxury_response = input(luxury_question)
                if luxury_response == "1":
                    return "Full-size SUV"
                else:
                    return "Station wagon or Minivan"

    elif purpose == "3":
        frequency_question = "How frequently do you go off-road?\nEnter '1' for occasional or '2' for frequent: "
        frequency_response = input(frequency_question)
        if (
            not frequency_response
            in allowed_responses
            # or not storage_question in allowed_responses
        ):
            print("Invalid input Please try again.")
            return None
        else:
            if frequency_response == "1":
                terrain_question = "What type of terrain do you plan to encounter?\nEnter '1' for light terrain or '2' for rugged terrain: "
                terrain_response = input(terrain_question)
                if terrain_response == "1":
                    return "Crossover or Compact SUV"
                else:
                    return "Crossover or Pickup Truck or Off-road SUV"
            elif frequency_response == "2":
                passenger_question = "Are you looking for a compact vehicle for solo journeys or are you going to transport passengers?\nEnter '1' for compact or '2' for passenger transport: "
                passenger_response = input(passenger_question)
                if passenger_response == "1":
                    return "Compact SUV or Crossover"
                else:
                    return "Full-Size SUV or Off-road SUV"

    elif purpose == "4":
        ride_question = "Do you prioritize a smooth and quiet ride or sporty performance?\nEnter '1' for smooth and quiet, or '2' for sporty: "
        ride_response = input(ride_question)
        if (
            not ride_response
            in allowed_responses
            # or not storage_question in allowed_responses
        ):
            print("Invalid input Please try again.")
            return None
        else:
            if ride_response == "1":
                people_question = "How many people would you like to accommodate in the vehicle?\nEnter '1' for up to 4 people or '2' for more than 4 people: "
                people_response = input(people_question)
                if people_response == "1":
                    return "Luxury Sedan"
                else:
                    return "Luxury Coupe"
            elif ride_response == "2":
                weather_question = "Does it rain often in your region or is your is it usually dry?\nEnter '1' for often or '2' for dry: "
                weather_response = input(weather_question)
                if weather_response == "1":
                    return "Luxury Coupe or Luxury Sedan"
                else:
                    return "Luxury Coupe or Convertible"

    elif purpose == "5":
        image_question = "Will you be meeting clients or attending events where a more upscale appearance is preferred?\nEnter '1' for yes or '2' for no: "
        image_response = input(image_question)
        if (
            not image_response
            in allowed_responses
            # or not storage_question in allowed_responses
        ):
            print("Invalid input Please try again.")
            return None
        else:
            if image_response == "1":
                cargo_question = "Do you require a vehicle with cargo space for business-related items?\nEnter '1' for yes or '2' for no: "
                cargo_response = input(cargo_question)
                if cargo_response == "1":
                    return "Luxury Sedan or Luxury Coupe"
                else:
                    return "Luxury SUV"
            elif image_response == "2":
                fuel_question = "How much daily driving will you be doing and are you primarly looking for a fuel-efficient car?\nEnter '1' for yes or '2' for no: "
                fuel_response = input(fuel_question)
                if fuel_response == "1":
                    return "Sedan or Coupe"
                else:
                    return "Compact SUV or Crossover"


def main():
    print("Welcome to the Car Body Type Expert System!")
    purpose = ask_opener_question()
    while True:
        body_type = ask_followup_questions(purpose)
        if body_type != None:
            break
    print(
        f"Based on your answers, we recommend the following car body type(s): {body_type}",
    )


if __name__ == "__main__":
    main()


#
# Sedan - Sedans are a great choice for commuters who prioritize fuel efficiency and comfort. They are typically affordable and come in a range of sizes,
# from compact to full-size. Sedans generally have good safety ratings and a sleek, classic look. However, they may not have as much cargo space as other
# body styles, and they are not designed for off-road driving or heavy towing.

# SUV - SUVs are versatile vehicles that can handle a range of driving conditions, from city streets to rugged terrain. They offer ample cargo space and
# passenger room, making them a great choice for families or those who prioritize practicality. SUVs can also be equipped with advanced safety features
# and often have good crash-test ratings. However, they may not be as fuel-efficient as sedans, and they can be expensive to purchase and maintain.

# Crossover - Crossovers are a popular choice for those who want the practicality of an SUV but with better fuel efficiency and handling. They are often
# smaller and lighter than SUVs, making them easier to maneuver in city driving. Crossovers typically have good cargo space and can be equipped with
# advanced safety features. However, they may not have the same off-road capabilities as SUVs, and they can be more expensive than some sedans.

# Coupe - Coupes are a sportier option for those who prioritize handling and performance over practicality. They are typically smaller and lighter than
# sedans and have a sleek, stylish look. Coupes can be fun to drive and offer good handling, but they may not be as comfortable or spacious as other body
# styles. They also often have higher price tags than sedans.

# Convertible - Convertibles offer the fun of open-air driving and are a great choice for those who prioritize style and leisure activities. They can be
# sporty and fun to drive, but they may not be as practical or comfortable as other body styles. Convertibles also often have higher price tags than other
# cars.

# Pickup Truck - Pickup trucks are a great choice for those who need off-road capabilities or towing capacity. They are versatile vehicles that can
# handle a range of driving conditions and offer plenty of cargo space. Pickup trucks can be equipped with advanced safety features and often have good
# crash-test ratings. However, they may not be as fuel-efficient as other body styles, and they can be expensive to purchase and maintain.

# Hatchback - Hatchbacks are a practical and affordable choice for those who prioritize cargo space and fuel efficiency. They are typically smaller than
# sedans and can be more fuel-efficient. Hatchbacks also often have good safety ratings and can be equipped with advanced safety features. However, they
# may not have as much passenger room as other body styles.

# Wagon - Wagons offer the practicality of an SUV or crossover but with a more classic, understated look. They are great for families or those who
# prioritize cargo space and passenger comfort. Wagons can be equipped with advanced safety features and often have good crash-test ratings. However,
#  they may not be as fuel-efficient as some sedans or crossovers.

# Sports Car - Sports cars are designed for performance and handling and are a great choice for those who prioritize style and driving experience. They
# can be fun to drive and offer good handling, but they may not be as practical or comfortable as other body styles. Sports cars also often have higher
# price tags than other cars.

# Electric Vehicle (EV) - EVs are a great choice for those who prioritize fuel efficiency and sustainability. They are typically smaller than sedans and
# can be more fuel-efficient. EVs can also be equipped with advanced safety features and often have good crash-test
