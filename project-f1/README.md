# Formula 1 Race Analysis

This program analyzes Formula 1 race lap times and provides detailed statistics and summaries for drivers' performances in a given race.

## Features
- Reads race lap times from a file and extracts key information.
- Identifies the fastest lap time and the driver associated with it.
- Calculates the fastest lap time and average lap time for each driver.
- Computes the overall average lap time across all drivers.
- Loads driver details (name and team) from a separate file for enhanced reporting.
- Displays race summaries and statistics in a formatted table using the `tabulate` library.

## File Structure
### Input Files
1. **Lap Times File**:
   - Contains race data in the following format:
     - First line: Race name.
     - Subsequent lines: Driver code (first 3 characters) and lap time (remaining part).
   - Example:
     ```
     Monaco Grand Prix
     HAM78.324
     VER78.290
     LEC78.450
     ```

2. **Driver Details File** (default: `f1_drivers.txt`):
   - Contains driver details in the format: `ID,Code,Name,Team`.
   - Example:
     ```
     1,HAM,Lewis Hamilton,Mercedes
     2,VER,Max Verstappen,Red Bull Racing
     3,LEC,Charles Leclerc,Ferrari
     ```

### Output
- Console output includes:
  - Race summary highlighting the fastest driver and overall average lap time.
  - Detailed tables of fastest and average lap times for all drivers.

## Prerequisites
- Python 3.x
- `tabulate` library (install using `pip install tabulate`)

## Usage
### Running the Program
Run the program from the command line with the following syntax:
```bash
python main.py <lap_times_file>
```

Example:
```bash
python main.py monaco_lap_times.txt
```

### Expected Output
1. **Race Summary**:
   - Highlights the fastest driver and their lap time.
   - Shows the overall average lap time across all drivers.

2. **Detailed Tables**:
   - Fastest lap times for each driver.
   - Average lap times for each driver.

## Program Functions
### Main Functions
1. **`read_file_lines(file_path)`**:
   - Reads all lines from a file and removes leading/trailing whitespace.

2. **`get_race_name(file_lines)`**:
   - Extracts the race name (first line of the lap times file).

3. **`extract_driver_data(file_lines)`**:
   - Extracts driver codes and lap times from the lap times file.

4. **`get_fastest_time(lap_times)`**:
   - Returns the fastest lap time from a list.

5. **`compute_driver_best_times(driver_codes, lap_times)`**:
   - Computes the fastest lap time for each driver.

6. **`calculate_overall_average_time(lap_times)`**:
   - Calculates the overall average lap time.

7. **`compute_driver_average_times(driver_codes, lap_times)`**:
   - Calculates the average lap time for each driver.

8. **`load_driver_info(driver_file)`**:
   - Loads driver details (name and team) from a file.

9. **`format_table(statistics, driver_info)`**:
   - Formats statistics into a table using `tabulate`.

10. **`show_race_summary(race_name, top_driver, best_time, driver_info, sorted_averages, overall_average)`**:
    - Displays the race summary.

### Utility Functions
- **`find_index_of_fastest_time(lap_times, fastest_time)`**:
  - Finds the index of the fastest lap time.
- **`sort_driver_statistics(statistics)`**:
  - Sorts driver statistics by lap time.

## Example Input and Output
### Example Input Files
**Lap Times File (monaco_lap_times.txt):**
```
Monaco Grand Prix
HAM78.324
VER78.290
LEC78.450
```

**Driver Details File (f1_drivers.txt):**
```
1,HAM,Lewis Hamilton,Mercedes
2,VER,Max Verstappen,Red Bull Racing
3,LEC,Charles Leclerc,Ferrari
```

### Example Console Output
```
Formula 1 Grand Prix Monaco Grand Prix Race Summary:
------------------------------------------------------------
The fastest driver is Max Verstappen from Red Bull Racing with a lap time of 78.290 seconds.

The overall average lap time across all drivers is 78.355 seconds.
------------------------------------------------------------

Fastest Lap Times Per Driver:
╒═══════════════╤════════════╤═══════════════════╤════════════════════╕
│ Driver Code   │ Lap Time  │ Driver Name       │ Race Team          │
╞═══════════════╪════════════╪═══════════════════╪════════════════════╡
│ VER           │ 78.290    │ Max Verstappen    │ Red Bull Racing    │
│ HAM           │ 78.324    │ Lewis Hamilton    │ Mercedes           │
│ LEC           │ 78.450    │ Charles Leclerc   │ Ferrari            │
╘═══════════════╧════════════╧═══════════════════╧════════════════════╛

Average Lap Times Per Driver:
╒═══════════════╤════════════╤═══════════════════╤════════════════════╕
│ Driver Code   │ Lap Time  │ Driver Name       │ Race Team          │
╞═══════════════╪════════════╪═══════════════════╪════════════════════╡
│ VER           │ 78.290    │ Max Verstappen    │ Red Bull Racing    │
│ HAM           │ 78.324    │ Lewis Hamilton    │ Mercedes           │
│ LEC           │ 78.450    │ Charles Leclerc   │ Ferrari            │
╘═══════════════╧════════════╧═══════════════════╧════════════════════╛
```

