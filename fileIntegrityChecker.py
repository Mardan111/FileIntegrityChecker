import hashlib
import os
import json

# Define the file to store the baseline hashes
BASELINE_FILE = 'file_hashes_baseline.json'

def calculate_file_hash(filepath, hash_algorithm='sha256'):
    """Calculates the hash of a given file."""
    hasher = hashlib.new(hash_algorithm)
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):  # Read file in chunks for large files
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error calculating hash for {filepath}: {e}")
        return None

def generate_baseline(directory_to_monitor):
    """Generates a baseline of file hashes in a given directory."""
    baseline_hashes = {}
    for root, _, files in os.walk(directory_to_monitor):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                baseline_hashes[filepath] = file_hash
    
    with open(BASELINE_FILE, 'w') as f:
        json.dump(baseline_hashes, f, indent=4)
    print(f"Baseline generated and saved to {BASELINE_FILE}")

def check_file_integrity(directory_to_monitor):
    """Checks the integrity of files against the stored baseline."""
    try:
        with open(BASELINE_FILE, 'r') as f:
            baseline_hashes = json.load(f)
    except FileNotFoundError:
        print("Baseline file not found. Please generate a baseline first.")
        return

    current_hashes = {}
    for root, _, files in os.walk(directory_to_monitor):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = calculate_file_hash(filepath)
            if file_hash:
                current_hashes[filepath] = file_hash

    # Check for modified or deleted files
    for filepath, baseline_hash in baseline_hashes.items():
        if filepath not in current_hashes:
            print(f"DELETED: {filepath}")
        elif current_hashes[filepath] != baseline_hash:
            print(f"MODIFIED: {filepath}")

    # Check for new files
    for filepath, current_hash in current_hashes.items():
        if filepath not in baseline_hashes:
            print(f"NEW: {filepath}")

def main():
    """Main function to run the file integrity monitor."""
    directory = input("Enter the directory to monitor: ")
    if not os.path.isdir(directory):
        print("Invalid directory path.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Generate Baseline")
        print("2. Check File Integrity")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            generate_baseline(directory)
        elif choice == '2':
            check_file_integrity(directory)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
