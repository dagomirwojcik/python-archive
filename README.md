# Python Archive

A collection of small Python exercises and experiments covering calculators,
information systems, validation tools, games, demonstrations, file processing,
and text processing. Each exercise is intentionally self-contained and is
usually run directly as a Python script rather than through a shared build
system.

## Repository layout

```text
calculators/
  CubesCalculator/             Sum, average, and sum-of-cubes calculator
  MarkCalculator/              Mark input helpers and validation examples
  ModuleGradeCalculator/       Module marks, pass/fail results, and statistics
  QuadraticRootsCalculator/    Quadratic-equation root calculator
  TemperatureConverter/        Celsius/Fahrenheit converter
  WageCalculatorProgram/       Employee wage and commission calculator
demonstrations/
  FuctionDemonstrator/         Examples of reusable input functions
file-based-programs/
  InspirationalQuotes/         Random quote reader using a text file
games/
  RockPaperScissorsGame/       Rock-paper-scissors game against the computer
information-systems/
  GradeInformation/            Student grade lookup by student ID
  ProductDatabase/             Interactive product database exercise
  StudentManagement/           Interactive student list management
text-tools/
  LetterQunatityTool/          Letter-frequency counter for text
validation-tools/
  StudentIDValidator/          Student ID lookup and validation example
  VariableNameChecker/         Checks whether a variable name is valid
```

## Requirements

- Python 3.6 or newer
- No third-party packages are required

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
cd calculators/CubesCalculator
python CubesCalculator.py

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

### Letter quantity tool

```text
cd text-tools/LetterQunatityTool
python LetterQunatityTool.py
```

Enter a word or sentence to display the number of occurrences of each letter
of the alphabet.

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
