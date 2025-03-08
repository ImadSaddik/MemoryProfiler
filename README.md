# Memory profiling in Python

This repository demonstrates how to use Python's `memory_profiler` package to analyze memory consumption of Python code. The project compares two different methods for extracting content from Excel files and analyzes their memory usage patterns.

## Project overview

Memory profiling is essential for optimizing Python applications, especially when dealing with large datasets or memory-intensive operations. This project serves as a practical guide to memory profiling in Python. Also, there is an accompanying video [tutorial](yet_to_be_added) on the subject.

## Methods comparison

The repository contains two implementations for extracting content from Excel files:

1. **Method 1** (`method_1.py`): Uses the `UnstructuredExcelLoader` from LangChain
2. **Method 2** (`method_2.py`): Uses the `openpyxl` library with read-only optimization

## Memory profiling results

### Method 1 (UnstructuredExcelLoader)

| Line # | Mem usage | Increment | Occurrences | Line contents |
|--------|-----------|-----------|------------|---------------|
| 5      | 74.1 MiB  | 74.1 MiB  | 1          | @profile |
| 6      |           |           |            | def extract_content_from_excel_file(file_path: str) -> str: |
| 7      | 74.3 MiB  | 0.2 MiB   | 1          | loader = UnstructuredExcelLoader(file_path) |
| 8      | 438.2 MiB | 363.9 MiB | 1          | documents = loader.load() |
| 9      | 438.2 MiB | 0.0 MiB   | 1          | file_content = "" |
| 10     | 438.2 MiB | 0.0 MiB   | 2          | for doc in documents: |
| 11     | 438.2 MiB | 0.0 MiB   | 1          | file_content += doc.page_content + "\n" |
| 12     |           |           |            | |
| 13     | 438.2 MiB | 0.0 MiB   | 1          | return file_content.strip() |

### Method 2 (openpyxl)

| Line # | Mem usage | Increment | Occurrences | Line contents |
|--------|-----------|-----------|------------|---------------|
| 6      | 73.2 MiB  | 73.2 MiB  | 1          | @profile |
| 7      |           |           |            | def extract_content_from_excel_file(file_path: str) -> str: |
| 8      | 73.8 MiB  | 0.6 MiB   | 2          | workbook = openpyxl.load_workbook( |
| 9      | 73.2 MiB  | 0.0 MiB   | 1          | file_path, read_only=True, data_only=True) |
| 10     | 73.8 MiB  | 0.0 MiB   | 1          | file_content = "" |
| 11     | 75.4 MiB  | 0.0 MiB   | 2          | for sheet_name in workbook.sheetnames: |
| 12     | 73.8 MiB  | 0.0 MiB   | 1          | sheet = workbook[sheet_name] |
| 13     | 75.4 MiB  | 0.9 MiB   | 10002      | for row in sheet.iter_rows(): |
| 14     | 75.4 MiB  | 0.0 MiB   | 10001      | row_values = [] |
| 15     | 75.4 MiB  | 0.0 MiB   | 110011     | for cell in row: |
| 16     | 75.4 MiB  | 0.0 MiB   | 100010     | cell_value = str(cell.value).strip( |
| 17     | 75.4 MiB  | 0.0 MiB   | 100010     | ) if cell.value is not None else '' |
| 18     | 75.4 MiB  | 0.0 MiB   | 100010     | cleaned_value = " ".join(cell_value.split()) |
| 19     |           |           |            | |
| 20     | 75.4 MiB  | 0.0 MiB   | 100010     | if cleaned_value: |
| 21     | 75.4 MiB  | 0.0 MiB   | 100010     | row_values.append(cleaned_value) |
| 22     |           |           |            | |
| 23     | 75.4 MiB  | 0.0 MiB   | 10001      | row_text = " ".join(row_values) |
| 24     | 75.4 MiB  | 0.0 MiB   | 10001      | if row_text: |
| 25     | 75.4 MiB  | 0.6 MiB   | 10001      | file_content += row_text + "\n" |
| 26     |           |           |            | |
| 27     | 75.4 MiB  | 0.0 MiB   | 1          | return file_content.strip() |

## Analysis

- **Method 1** (LangChain UnstructuredExcelLoader):
  - Peak memory usage: 438.2 MiB
  - Most memory-intensive operation: Loading documents (363.9 MiB increment)
  - Simple implementation but significantly higher memory footprint

- **Method 2** (openpyxl):
  - Peak memory usage: 75.4 MiB
  - Most memory-intensive operations: Iterating rows (0.9 MiB) and building content (0.6 MiB)
  - More code but ~83% lower memory usage

Method 2 is substantially more memory-efficient, requiring only about 1/6th of the memory needed by Method 1.

## Installation

```bash
# Clone the repository
git clone git@github.com:ImadSaddik/MemoryProfiler.git

# Install dependencies
cd MemoryProfiler
pip install -r requirements.txt
```

## Usage

1. Generate the Excel file with the help of [generate_excel_file](generate_excel_file.ipynb)
2. Run the profiling for each method:

```bash
python method_1.py
python method_2.py
```

## How to use memory_profiler

1. Install the `memory_profiler` package:

```bash
pip install memory_profiler
```

2. Import and add the @profile decorator:

```python
from memory_profiler import profile

@profile
def your_function():
    # Your code here
    pass
```

3. Run your script:

```bash
python -m your_script.py
```
