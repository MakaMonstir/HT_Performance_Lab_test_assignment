# HT Performance Lab Test Assignment

This repository contains solutions to tasks assigned by NT Performance Lab. The tasks are implemented in pure Python and organized in separate directories. Each task directory contains a single source code file and any necessary resources.

## Task 1: Circular Array Path

**Description**: This task involves creating a circular array of numbers from 1 to n and finding the path of starting elements by moving m steps in the array.

**Usage**:

```sh
python <path-to-repo>/task1/task1.py <n> <m>
```

where n, m - positive integer numbers and m > 1.

## Task 2: Point Position Relative to Circle

**Description**: This task calculates the position of points relative to a circle based on coordinates read from two input files.

**Usage**:

```sh
python <path-to-repo>/task2/task2.py <circle_file> <points_file>
```

circle_file structure:

```
1 1 # Coordinates of circle center
2 # Radius of circle
```

points_file structure:

```
1 1 # Each line contains coordinates of points
2 2
4 6
...
```

## Task 3: Generate Report from Test Results

**Description**: This task generates a report file `report.json` based on the structure in `tests.json` and values from `values.json`.

**Usage**:

```sh
python <path-to-repo>/task3/task3.py <values_file> <tests_file> <report_file>
```

## Task4: Minimum Moves to Equal Array Elements

**Description**: This task calculates the minimum number of moves required to make all elements of an array equal. The elements are read from a file.

**Usage**:

```sh
python <path-to-repo>/task4/task4.py <nums_file>
```
