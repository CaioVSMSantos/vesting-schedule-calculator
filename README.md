[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# Vesting Schedule Calculator

This application can read a file with Vesting Events and generate a cumulative Vesting Schedule up to a given date, providing a concise and easy to understand table.

## Installation

1. The system which will run the application should have a version of Python installed. It is strongly recommended that version 3.8 or higher is installed
    - Python can be downloaded and installed through its main website: https://www.python.org/downloads/
    - It is also required that the Python package manager 'pip' is also installed. If Python was installed from its main website, then pip is probably already installed. More information can be obtained on its main website: https://pypi.org/project/pip/
    - Python version can be checked with the following terminal command:
        - > python --version
    - pip version and assurance of installation can be checked with the following terminal command:
        - > pip --version
2. An experienced developer may wish to use a Python Virtual Environment to install this application dependencies and run it. More information on https://docs.python.org/3/library/venv.html
3. With Python and pip properly installed, the following command should be used to install application dependencies:
    - > pip install -r requirements.txt
    - The final argument 'requirements.txt' is a path to the file of the same name inside the application root directory
4. If for some reason the installation through requirements.txt fail, the 'pandas' library should be enough:
    - > pip install pandas

## Usage example

The Standard implementation of this application can be called from a terminal, passing as arguments a Vesting Events .csv file and a target date in the format 'yyyy-MM-dd'. It will calculate the total Vesting Quantities to each Employee and Award type up to and including the provided date. Some examples of standard Vesting Events files are inside the 'data' directory.

Example:
> vesting_schedule_calculator.py data\example1.csv 2021-01-01

Should return:
> E001,AliceSmith,ISO-001,2000 \
> E001,Alice Smith,ISO-002,800 \
> E002,Bobby Jones,NSO-001,600 \
> E003,Cat Helms,NSO-002,0  

A third Precision argument may be passed to set the number of decimals in the quantities, specially if they have fractional values on the Events file, like example3.csv.

Example:
> vesting_schedule_calculator.py data\example3.csv 2021-01-01 3

Should return:
> E001,Alice Smith,ISO-001,299.750 \
> E002,Bobby Jones,ISO-002,234.000

## Design and Implementation Decisions

It was assumed that the layout of the Vesting Events file, its extension and even the output could be changed. Maybe instead of printing to console, someone might like to have a .txt or .json file of the Schedule. The Events layout could include a new column after some update. With that assumption, the application was built using four distinct modules:
1. An ArgParser, responsible to parse the arguments
2. An Events File Parser, responsible to read the events file and output a pandas DataFrame with a layout easily readable for the third module
3. A Schedule, which includes all the important calculation rules and is responsible to read the Events DataFrame and return a Schedule DataFrame
4. A Schedule Presenter, responsible to read the Schedule DataFrame and output it in the desired format

The main class 'VestingScheduleCalculator' receives the described modules on its constructor, allowing a developer to easily switch any of them for another implementation if desirable.

## License

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
