def display_main_menu():
    """Display the main menu options."""
    print("\nPlease choose an option:")
    print("1. Enter temperatures")
    print("2. Calculate average temperature")
    print("3. Find minimum and maximum temperature")
    print("4. Sort temperatures in ascending order")
    print("5. Calculate median temperature")
    print("6. Exit")

def get_user_input():
    """Get a list of temperatures from the user."""
    temperatures = input("Enter temperatures separated by commas: ").split(',')
    # Convert the input to a list of floats
    temperatures = [float(temp) for temp in temperatures]
    return temperatures

def calc_average(temperatures):
    """Calculate the average of the list of temperatures."""
    if len(temperatures) == 0:
        return 0
    average = sum(temperatures) / len(temperatures)
    return average

def find_min_max(temperatures):
    """Find the minimum and maximum temperatures in the list."""
    if len(temperatures) == 0:
        return [None, None]
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return [min_temp, max_temp]

def sort_temperature(temperatures):
    """Sort the list of temperatures in ascending order."""
    return sorted(temperatures)

def calc_median_temperature(temperatures):
    """Calculate the median temperature from the list."""
    if len(temperatures) == 0:
        return None  # Handle the case of an empty list
    
    # Sort the list in ascending order
    sorted_temps = sorted(temperatures)
    
    # Calculate the median
    n = len(sorted_temps)
    mid = n // 2
    
    # If the number of temperatures is even, average the two middle elements
    if n % 2 == 0:
        median = (sorted_temps[mid - 1] + sorted_temps[mid]) / 2
    else:
        # If odd, the median is the middle element
        median = sorted_temps[mid]
    
    return median

# Example usage in the main program
def main():
    temperatures = []
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            # Get user input for temperatures
            temperatures = get_user_input()
            print("Temperatures recorded successfully.")
        elif choice == '2':
            # Calculate and display average temperature
            average = calc_average(temperatures)
            print(f"The average temperature is: {average:.2f}")
        elif choice == '3':
            # Find and display minimum and maximum temperatures
            min_max = find_min_max(temperatures)
            print(f"The minimum temperature is: {min_max[0]}")
            print(f"The maximum temperature is: {min_max[1]}")
        elif choice == '4':
            # Sort and display temperatures in ascending order
            sorted_temps = sort_temperature(temperatures)
            print("Temperatures in ascending order:", sorted_temps)
        elif choice == '5':
            # Calculate and display median temperature
            median = calc_median_temperature(temperatures)
            if median is not None:
                print(f"The median temperature is: {median:.2f}")
            else:
                print("No temperatures available to calculate the median.")
        elif choice == '6':
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # Invalid input handling
            print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()
