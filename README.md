# Python Archive

A collection of small Python exercises and experiments covering calculators,
information systems, validation tools, games, demonstrations, file processing,
and text processing. Each exercise is intentionally self-contained and is
usually run directly as a Python script rather than through a shared build
system.

## Repository layout

```text
calculators/
  BirthdayCalculator/          Birthday and age calculations
  CubesCalculator/             Sum, average, and sum-of-cubes calculator
  EmployeePayCalculator/       Employee wage and pay calculations
  MarkCalculator/              Mark input helpers and validation examples
  ModuleGradeCalculator/       Module marks, pass/fail results, and statistics
  QuadraticRootsCalculator/    Quadratic-equation root calculator
  TemperatureConverter/        Celsius/Fahrenheit converter
  WageCalculatorProgram/       Employee wage and commission calculator
demonstrations/
  ClassesAndObjects/           Notebook on classes, objects, attributes, and methods
  FuctionDemonstrator/         Examples of reusable input functions
  IntroToPandasAndNumpy/        Notebook introducing NumPy arrays and Pandas data frames
  ListFunctionDemonstrator/    Demonstration of list-related helper functions
  StudentsPerformanceClassifications/ Notebook exploring student performance classification
file-based-programs/
  InspirationalQuotes/         Random quote reader using a text file
games/
  RockPaperScissorsGame/       Rock-paper-scissors game against the computer
information-systems/
  GradeInformation/            Student grade lookup by student ID
  HousingOccupancyReport/      House counts and percentages by occupancy
  PartyGuestList/              Guest list management exercise
  ProductDatabase/             Interactive product database exercise
  StudentManagement/           Interactive student list management
text-tools/
  LetterQunatityTool/          Letter-frequency counter for text
  TextAnalysisTool/             Word-frequency analysis for text
validation-tools/
  FruitPickerProgram/           Fruit selection with input-error handling
  ExceptionHandling/           Notebook on Python exceptions and handling patterns
  LeapYearChecker/             Leap year validation example
  StudentIDValidator/          Student ID lookup and validation example
  VariableNameChecker/         Checks whether a variable name is valid
```

## Requirements

- Python 3.6 or newer
- Standalone scripts require no third-party packages
- The Jupyter notebooks require Jupyter and the libraries used in each notebook,
  including Matplotlib, NumPy, Pandas, scikit-learn, and Seaborn

There is no shared package, dependency manifest, or build file, so commands
are run from each exercise's directory.

## Running the examples

### Rock-paper-scissors

```text
cd games/RockPaperScissorsGame
python RockPaperScissorsGame.py
```

Choose `1` for Rock, `2` for Paper, or `3` for Scissors when prompted.

### Module grade calculator

```text
cd calculators/ModuleGradeCalculator
python ModuleGradeCalculator.py
```

Enter a module name, the number of students, and each student's mark to
display a pass/fail report and summary statistics.

### Other calculators

Each calculator can be run directly from its own directory:

```text
cd calculators/BirthdayCalculator
python BirthdayCalculator.py

cd ../CubesCalculator
python CubesCalculator.py

cd ../EmployeePayCalculator
python EmployeePayCalculator.py

cd ../QuadraticRootsCalculator
python QuadraticRootsCalculator.py

cd ../TemperatureConverter
python TemperatureConverter.py

cd ../WageCalculatorProgram
python Wage_Calculator_Program.py
```

The cube calculator reports the sum, average, and sum of cubes for three
numbers. The quadratic-roots calculator uses the quadratic formula, and the
temperature converter accepts values ending in `C` or `F`.

### Validation helpers

```text
cd validation-tools/FruitPickerProgram
python FruitPickerProgram.py

cd validation-tools/LeapYearChecker
python LeapYearChecker.py

cd ../StudentIDValidator
python StudentIDValidator.py

cd ../VariableNameChecker
python VariableNameChecker.py
```

These examples validate common inputs such as leap years, student IDs, and
variable naming rules. The fruit picker demonstrates handling invalid numeric
input and out-of-range list indexes.

### Student management

```text
cd information-systems/StudentManagement
python StudentManagementProgram.py
```

Use the menu to add, list, sort, or clear student names.

### Inspirational quotes

```text
cd file-based-programs/InspirationalQuotes
python InspirationalQuotes.py
```

The program selects a random line from `inspirationalquotes.txt`, so run it
from this directory to keep the relative file path available.

### Grade information

```text
cd information-systems/GradeInformation
python GradeInformationProgram.py
```

This example collects student marks and prints a sorted report with pass/fail
results and summary statistics.

### Housing occupancy report

```text
cd information-systems/HousingOccupancyReport
python HousingOccupancyReport.py
```

Enter the number of houses in each occupancy group to display the count and
percentage for each group.

### Party guest list

```text
cd information-systems/PartyGuestList
python PartyGuestList.py
```

This exercise manages a guest list and demonstrates simple list operations.

### Demonstration scripts

```text
cd demonstrations/FuctionDemonstrator
python FuctionDemonstrator.py

cd ../ListFunctionDemonstrator
python ListFunctionDemonstrator.py
```

These examples highlight reusable input helpers and list-based programming
patterns.

### Demonstration notebooks

Open these notebooks in JupyterLab or VS Code:

```text
demonstrations/ClassesAndObjects/ClassesAndObjects.ipynb
demonstrations/IntroToPandasAndNumpy/IntroToPandasAndNumpy.ipynb
demonstrations/StudentsPerformanceClassifications/StudentsPerformanceClassification.ipynb
validation-tools/ExceptionHandling/ExceptionHandling.ipynb
```

The classes notebook covers classes, objects, attributes, and methods. The
exception-handling notebook demonstrates common exceptions and `try`/`except`
patterns. The NumPy and Pandas notebook introduces arrays and data frames; it
also loads example datasets from the internet and references a local
`california_housing_train.csv` file. The student-performance notebook uses
Seaborn and scikit-learn to explore student scores and train classification
models; it expects a local `StudentsPerformance.csv` dataset.

### Letter quantity tool

```text
cd text-tools/LetterQunatityTool
python LetterQunatityTool.py
```

Enter a word or sentence to display the number of occurrences of each letter
of the alphabet.

### Text analysis tool

```text
cd text-tools/TextAnalysisTool
python TextAnalysisTool.py
```

This exercise defines a text-analysis class that normalizes text and provides
word-frequency counts.

## Supporting examples

The `calculators/MarkCalculator` directory contains `input_functions.py`,
which provides reusable integer and floating-point input helpers. The
`if_test.py` script exercises those helpers:

```text
cd calculators/MarkCalculator
python if_test.py
```

## Project status

These are learning exercises and archives, not a unified production
application. Most programs are interactive scripts, and some examples contain
partial experiments or intentionally simple implementations. Inspect the
relevant directory before assuming that an exercise provides a reusable
library or automated test suite.

## License

This project is released under the [MIT License](LICENSE).
