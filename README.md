# Keepass csv export to MacOS csv import

Is a Python script that helps reorganize password data from a CSV file to the standard format for importing passwords into Apple devices. It provides a convenient utility for users who want to migrate their password data from a different password manager or system to Apple's native password management system.

## Features

- Converts a CSV file containing password data to the standard format for Apple password imports.
- Handles reorganization of columns to match the required fields: Title, URL, Username, Password, Notes, and OTPAuth.
- Works with CSV files that may have columns in different orders or with varying column names.
- Supports macOS and can be run directly on your system.

## Requirements

- Python 3.x
- Dependencies: csv, tkinter (automatically installed if not present)

## Usage

1. Clone the repository or download the script file.
2. Run the script using the command `python csv_keepass_to_apple.py`.
3. Select the input CSV file when prompted.
4. The script will generate the reorganized CSV file with the suffix "-ForMacOS.csv" in the same directory as the input file.

## Note

- Make sure your input CSV file follows the structure of the standard format for Apple password imports.

## Acknowledgements

This script was developed to simplify the process of migrating passwords to Apple devices.
