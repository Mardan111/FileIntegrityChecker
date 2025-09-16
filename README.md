# FileIntegrityChecker

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : MOHAMMED MARDAN ALI

*INTERN ID* : CT04DY1075

*DOMAIN* : CYBER SECURITY AND ETHICAL HACKING 

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR

This repository contains a Python script `fileIntegrityChecker.py` for monitoring the integrity of files in a specified directory. The script helps identify unauthorized modifications, deletions, or additions to files by generating and comparing cryptographic hashes.

## Features

- **Generate Baseline:** Create a baseline of file hashes for all files in a directory.
- **Check File Integrity:** Compare current file hashes against the baseline to detect changes.
- **Detect Changes:** Report newly added, modified, or deleted files since the baseline was created.
- **User-Friendly CLI:** Simple command-line interface for ease of use.

## How It Works

1. **Baseline Generation:** The script scans the chosen directory and calculates a SHA-256 hash for each file. The results are saved in `file_hashes_baseline.json`.
2. **Integrity Check:** On demand, the script recalculates hashes for the files and compares them to the baseline. It reports any files that have been modified, deleted, or newly added.

## Usage

### Prerequisites

- Python 3.8 or newer

### Running the Script

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mardan111/FileIntegrityChecker.git
   cd FileIntegrityChecker
   ```

2. **Run the script:**
   ```bash
   python fileIntegrityChecker.py
   ```

3. **Follow the prompts:**
   - Enter the directory path you want to monitor.
   - Choose an option:
     - `1` to generate a baseline
     - `2` to check file integrity
     - `3` to exit

### Example

```text
Enter the directory to monitor: /home/user/documents

Choose an option:
1. Generate Baseline
2. Check File Integrity
3. Exit
Enter your choice (1-3): 1
Baseline generated and saved to file_hashes_baseline.json

Choose an option:
1. Generate Baseline
2. Check File Integrity
3. Exit
Enter your choice (1-3): 2
MODIFIED: /home/user/documents/report.txt
DELETED: /home/user/documents/old_notes.txt
NEW: /home/user/documents/new_file.txt
```

## How It Works: Internals

- Uses `hashlib` to compute SHA-256 hashes for each file.
- Stores baseline hashes as a JSON file.
- Compares current hashes to baseline and reports differences.

## Notes

- The script checks all files recursively in the specified directory.
- The baseline file (`file_hashes_baseline.json`) is created in the current working directory.
- For large directories, hash calculation may take some time.

## Output

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/28d71ed5-83c6-417c-b7fd-beb5e9ef4af4" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/24fae27f-f322-4ef6-bc80-8f1ef7392748" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/78b2d6a6-b190-440a-b036-1d5659ea652b" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/9df3382a-0847-4347-9e2d-4e84c2f10b02" />
