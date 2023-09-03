# Cron Expression Parser

This Python program is a simple cron expression parser that converts a cron expression into a human-readable table format. 
It takes a standard cron string with five time fields (minute, hour, day of month, month, and day of week) and a command, 
and it formats the cron expression as a table with field names in the first 14 columns and the corresponding times as 
space-separated lists.

## System Requirements

- Python >=3.6
- `pipenv` Python package manager

## Usage

To use this program, follow these steps:

1. Clone the repository to your local machine.

2. Open a terminal or command prompt in the root folder.

3. Install all dependencies and active the virtual environment:
   ```shell
   pipenv install
   pipenv shell
   ```

4. Install the package as a binary.
   ```shell
   pip install --editable .
   ```

5. Now you have access to `cron-parser` binary. Run the program with a cron expression as an argument. For example:

   ```shell
   cron-parser "*/15 0 1,15 * 1-5 /usr/bin/find"
   ```

   Replace `"*/15 0 1,15 * 1-5 /usr/bin/find"` with your own cron expression.

6. The program will output the formatted cron expression as a table, like this:

   ```
   minute        0 15 30 45
   hour          0
   day of month  1 15
   month         1 2 3 4 5 6 7 8 9 10 11 12
   day of week   1 2 3 4 5
   command       /usr/bin/find
   ```

7. You can run the tests to see if the code works correctly:
   ```shell
   pytest
   ```

## Features

- Handles step values, range of values, any value (`*`), and lists of values for each cron field.
- Provides clear and human-readable output with field names and corresponding time values.

## Contributing

If you would like to contribute to this project, please feel free to submit issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
