# capital_cities.py
"""
Program that manages a dictionary of countries and their capital cities.
Handles case-insensitive country names.
"""

def run_capital_cities_manager():
    # Initialize dictionary with some countries
    capitals = {
        "england": "London",
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid"
    }
    
    while True:
        # Get country name and normalize
        country = input("\nEnter a country name (or 'quit' to exit): ").strip().lower()
        
        # Check for exit condition
        if country == 'quit':
            break
            
        # Check if country exists in dictionary
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}")
        else:
            # Ask for new capital
            capital = input(f"I don't know the capital of {country.title()}. What is it? ")
            capitals[country] = capital.strip()
            print(f"Thanks, I've learned that {capital} is the capital of {country.title()}")

if __name__ == "__main__":
    print("Welcome to the Capital Cities Manager!")
    print("You can enter a country name to learn its capital.")
    print("If I don't know the capital, you can teach me.")
    print("Enter 'quit' to exit the program.")
    run_capital_cities_manager()
