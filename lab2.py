def display_main_menu():
    """Display the main menu options."""
    print("Please choose an option:")
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
        return None
    sorted_temps = sort_temperature(temperatures)
    n = len(sorted_temps)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_temps[mid - 1] + sorted_temps[mid]) / 2
    else:
        median = sorted_temps[mid]
    return median

# Example usage in the main program
def main():
    temperatures = []
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            temperatures = get_user_input()
        elif choice == '2':
            average = calc_average(temperatures)
            print(f"The average temperature is: {average:.2f}")
        elif choice == '3':
            min_max = find_min_max(temperatures)
            print(f"The minimum temperature is: {min_max[0]}")
            print(f"The maximum temperature is: {min_max[1]}")
        elif choice == '4':
            sorted_temps = sort_temperature(temperatures)
            print("Temperatures in ascending order:", sorted_temps)
        elif choice == '5':
            median = calc_median_temperature(temperatures)
            print(f"The median temperature is: {median:.2f}")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    display_main_menu()
