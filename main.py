# Sample used car inventory
used_cars = [
    {"make": "Toyota", "model": "Camry", "year": 2018, "mileage": 30000, "price": 18000},
    {"make": "Honda", "model": "Civic", "year": 2017, "mileage": 25000, "price": 16000},
    {"make": "Ford", "model": "Escape", "year": 2019, "mileage": 20000, "price": 20000},
    {"make": "Chevrolet", "model": "Malibu", "year": 2016, "mileage": 35000, "price": 15000},
    {"make": "Nissan", "model": "Altima", "year": 2020, "mileage": 18000, "price": 22000},
    {"make": "Hyundai", "model": "Sonata", "year": 2017, "mileage": 28000, "price": 17000},
    {"make": "Volkswagen", "model": "Jetta", "year": 2018, "mileage": 22000, "price": 19000},
    {"make": "Ford", "model": "Fusion", "year": 2016, "mileage": 32000, "price": 16000},
    {"make": "Chevrolet", "model": "Equinox", "year": 2019, "mileage": 23000, "price": 22000},
    {"make": "Toyota", "model": "Rav4", "year": 2017, "mileage": 27000, "price": 21000},
    {"make": "Honda", "model": "Accord", "year": 2018, "mileage": 24000, "price": 19000},
    {"make": "Subaru", "model": "Outback", "year": 2017, "mileage": 26000, "price": 20000},
    {"make": "Kia", "model": "Sorento", "year": 2019, "mileage": 18000, "price": 23000},
    {"make": "Mazda", "model": "CX-5", "year": 2018, "mileage": 21000, "price": 20000},
    {"make": "Ford", "model": "Explorer", "year": 2017, "mileage": 30000, "price": 25000},
    {"make": "Chevrolet", "model": "Traverse", "year": 2016, "mileage": 32000, "price": 22000},
    {"make": "Toyota", "model": "Highlander", "year": 2020, "mileage": 15000, "price": 28000},
    {"make": "Honda", "model": "Pilot", "year": 2019, "mileage": 22000, "price": 26000},
    {"make": "Nissan", "model": "Rogue", "year": 2018, "mileage": 20000, "price": 21000},
    {"make": "Hyundai", "model": "Tucson", "year": 2020, "mileage": 17000, "price": 24000},
    {"make": "Volkswagen", "model": "Tiguan", "year": 2017, "mileage": 25000, "price": 20000},
    {"make": "Ford", "model": "Edge", "year": 2018, "mileage": 19000, "price": 23000},
    {"make": "Chevrolet", "model": "Cruze", "year": 2019, "mileage": 22000, "price": 18000},
    {"make": "Toyota", "model": "Corolla", "year": 2016, "mileage": 30000, "price": 15000},
    {"make": "Honda", "model": "Fit", "year": 2017, "mileage": 18000, "price": 14000},
    {"make": "Subaru", "model": "Impreza", "year": 2018, "mileage": 22000, "price": 17000},
    {"make": "Kia", "model": "Sportage", "year": 2019, "mileage": 20000, "price": 21000},
    {"make": "Mazda", "model": "Mazda3", "year": 2017, "mileage": 24000, "price": 16000},
    {"make": "Ford", "model": "F-150", "year": 2016, "mileage": 35000, "price": 28000},
    {"make": "Chevrolet", "model": "Silverado", "year": 2018, "mileage": 32000, "price": 30000},
    {"make": "Toyota", "model": "Tacoma", "year": 2019, "mileage": 18000, "price": 26000},
    {"make": "Honda", "model": "Ridgeline", "year": 2017, "mileage": 25000, "price": 27000},
    {"make": "Nissan", "model": "Titan", "year": 2020, "mileage": 22000, "price": 29000},
    {"make": "Hyundai", "model": "Santa Fe", "year": 2018, "mileage": 21000, "price": 24000},
    {"make": "Volkswagen", "model": "Atlas", "year": 2019, "mileage": 20000, "price": 28000},
    {"make": "Ford", "model": "Expedition", "year": 2017, "mileage": 28000, "price": 32000},
    {"make": "Chevrolet", "model": "Tahoe", "year": 2018, "mileage": 25000, "price": 34000},
    {"make": "Toyota", "model": "4Runner", "year": 2019, "mileage": 22000, "price": 35000},
    {"make": "Honda", "model": "Prelude", "year": 2020, "mileage": 18000, "price": 32000},
    {"make": "Subaru", "model": "WRX", "year": 2018, "mileage": 20000, "price": 28000},
]

def search_inventory(make, model, max_price):
    results = []
    for car in used_cars:
        if car["make"].lower() == make.lower() and car["model"].lower() == model.lower() and car["price"] <= max_price:
            results.append(car)
    return results


def display_car_details(car):
    print("Make:", car["make"])
    print("Model:", car["model"])
    print("Year:", car["year"])
    print("Mileage:", car["mileage"])
    print("Price:", car["price"])
    print("-" * 20)

# Main menu
while True:
    print("Used Car Inventory Search Menu:")
    print("1. Search for a Car")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        make_input = input("Enter the make of the car: ")
        model_input = input("Enter the model of the car: ")
        max_price_input = float(input("Enter the maximum price: "))

        search_results = search_inventory(make_input, model_input, max_price_input)

        if search_results:
            print("Search Results:")
            for result in search_results:
                display_car_details(result)
        else:
            print("No matching cars found.")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")