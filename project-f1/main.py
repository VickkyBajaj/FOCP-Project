import sys
from tabulate import tabulate

def read_file_lines(file_path):
    """Read the lines of a file into a list."""
    try:
        # Open the file in read mode and read all lines into a list
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]  # Remove any leading/trailing whitespace
    except FileNotFoundError:
        # Handle case where the file does not exist
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)  # Exit the program with an error code

def get_race_name(file_lines):
    """Extract the name of the race from the file content."""
    return file_lines[0]  # The race name is the first line in the file

def extract_driver_data(file_lines):
    """Extract driver information and lap times from file content."""
    driver_codes = [line[:3] for line in file_lines[1:]]  # Extract the driver code (first 3 characters)
    lap_times = [float(line[3:]) for line in file_lines[1:]]  # Extract the lap time (remaining part)
    return driver_codes, lap_times

def get_fastest_time(lap_times):
    """Identify the fastest lap time from a list of times."""
    return min(lap_times)  # Return the smallest value in the list

def find_index_of_fastest_time(lap_times, fastest_time):
    """Find the index of the fastest lap time."""
    return lap_times.index(fastest_time)  # Find the position of the fastest time in the list

def compute_driver_best_times(driver_codes, lap_times):
    """Compute the fastest lap time for each driver."""
    best_lap_times = {}
    for i in range(len(driver_codes)):
        driver = driver_codes[i]
        time = lap_times[i]
        # Update the best lap time for each driver
        if driver in best_lap_times:
            best_lap_times[driver] = min(best_lap_times[driver], time)
        else:
            best_lap_times[driver] = time
    return best_lap_times

def calculate_overall_average_time(lap_times):
    """Calculate the average of all lap times."""
    return sum(lap_times) / len(lap_times)  # Return the mean of all lap times

def compute_driver_average_times(driver_codes, lap_times):
    """Calculate the average lap time for each driver."""
    total_lap_times = {}  # Dictionary to store the total lap times for each driver
    lap_counts = {}  # Dictionary to store the number of laps for each driver
    for i in range(len(driver_codes)):
        driver = driver_codes[i]
        time = lap_times[i]
        total_lap_times[driver] = total_lap_times.get(driver, 0) + time  # Add lap time to the total
        lap_counts[driver] = lap_counts.get(driver, 0) + 1  # Increment lap count

    # Calculate averages by dividing total time by lap count
    average_lap_times = {driver: total / lap_counts[driver] for driver, total in total_lap_times.items()}
    return average_lap_times

def load_driver_info(driver_file):
    """Load driver details into a dictionary."""
    file_data = read_file_lines(driver_file)  # Load file content
    driver_info = {}
    for line in file_data:
        parts = line.split(',')  # Split the line by commas
        driver_info[parts[1]] = {
            'name': parts[2],  # Driver name
            'team': parts[3]   # Driver team
        }
    return driver_info

def sort_driver_statistics(statistics):
    """Sort a dictionary of driver statistics by lap time."""
    return dict(sorted(statistics.items(), key=lambda item: item[1]))  # Sort by the second item (lap time)

def format_table(statistics, driver_info):
    """Format a table for display using the tabulate library."""
    # Prepare table data with driver code, lap time, name, and team
    table_data = [
        [driver, f"{time:.3f}", driver_info[driver]['name'], driver_info[driver]['team']]
        for driver, time in statistics.items()
    ]
    # Format the table using tabulate
    table = tabulate(
        table_data,
        headers=["Driver Code", "Lap Time", "Driver Name", "Race Team"],
        tablefmt="fancy_grid",
        numalign="center",
        stralign="center"
    )
    return table

def show_race_summary(race_name, top_driver, best_time, driver_info, sorted_averages, overall_average):
    """Display the race summary at the beginning."""
    best_average_driver = next(iter(sorted_averages))  # Get the driver with the best average lap time
    summary = f"""
    Formula 1 Grand Prix {race_name} Race Summary:
    ------------------------------------------------------------
    The fastest driver is {driver_info[top_driver]['name']} 
    from {driver_info[top_driver]['team']} with a lap time of {best_time:.3f} seconds.

    The overall average lap time across all drivers is {overall_average:.3f} seconds.
    ------------------------------------------------------------
    """
    print(summary)

def main():
    # Ensure the program is run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py <lap_times_file>")
        sys.exit(1)

    lap_times_file = sys.argv[1]  # First argument is the lap times file
    driver_details_file = "f1_drivers.txt"  # File containing driver details

    # Load and process data
    file_lines = read_file_lines(lap_times_file)  # Read lap times
    driver_codes, lap_times = extract_driver_data(file_lines)  # Extract driver codes and lap times
    race_name = get_race_name(file_lines)  # Get the race name

    # Find fastest and average lap times
    best_time = get_fastest_time(lap_times)  # Identify the fastest time
    fastest_driver_index = find_index_of_fastest_time(lap_times, best_time)  # Find index of fastest lap
    fastest_driver = driver_codes[fastest_driver_index]  # Get the driver with the fastest lap

    # Calculate fastest and average times per driver
    best_lap_times_per_driver = compute_driver_best_times(driver_codes, lap_times)
    average_lap_times_per_driver = compute_driver_average_times(driver_codes, lap_times)
    overall_average_lap_time = calculate_overall_average_time(lap_times)

    # Load driver details and sort data
    driver_info = load_driver_info(driver_details_file)  # Load driver details
    sorted_best_times = sort_driver_statistics(best_lap_times_per_driver)  # Sort fastest times
    sorted_average_times = sort_driver_statistics(average_lap_times_per_driver)  # Sort average times

    # Display summary
    show_race_summary(race_name, fastest_driver, best_time, driver_info, sorted_average_times, overall_average_lap_time)

    # Display detailed tables
    print("Fastest Lap Times Per Driver:")
    print(format_table(sorted_best_times, driver_info))

    print("\nAverage Lap Times Per Driver:")
    print(format_table(sorted_average_times, driver_info))

if __name__ == "__main__":
    main()