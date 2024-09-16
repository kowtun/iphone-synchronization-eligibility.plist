
# README

## Overview

This Python script modifies specific integer values within the `eligibility.plist` file on macOS. It updates certain settings under the `OS_ELIGIBILITY_DOMAIN_IRON` key. Before making any changes, the script creates a timestamped backup of the original file to ensure you can restore it if needed.

----------

## Prerequisites

-   **Python 3**: Ensure Python 3 is installed on your Mac.
-   **Administrative Privileges**: You need to run the script with `sudo` because it modifies a protected system file.
-   **Backup Directory**: A directory where you have write permissions to store backup files.

----------

## Script Configuration

Before running the script, you need to update two variables in the script:

1.  **`file_path`**: The path to the `eligibility.plist` file you want to modify.
2.  **`backup_directory`**: The path to the directory where you want to store backup files.

### 1. Updating the File Path (`file_path`)

Locate the following line in the script:

`# Path to the protected file
file_path = '/private/var/db/os_eligibility/eligibility.plist'` 

**Action**:

-   **If the `eligibility.plist` file is located at `/private/var/db/os_eligibility/eligibility.plist`, you do not need to change this.**
-   **If the file is located elsewhere**, update the `file_path` variable with the correct path to the plist file.

**Example**:

`file_path = '/path/to/your/eligibility.plist'` 

### 2. Updating the Backup Directory (`backup_directory`)

Locate the following lines in the script:

`# Alternative path to store the backup file
backup_directory = '/Users/yourusername/eligibility_backups'  # Update this path if needed` 

**Action**:

-   Replace `'/Users/yourusername/eligibility_backups'` with the path to a directory where you have write permissions.
-   This directory can be anywhere you prefer, such as a folder in your home directory.

**Example**:

`backup_directory = '/Users/johndoe/eligibility_backups'` 

**Note**:

-   Ensure that the directory exists. If it doesn't, the script will attempt to create it using `os.makedirs(backup_directory, exist_ok=True)`.

----------

## Running the Script

### Step 1: Open Terminal

-   Navigate to the directory where your `modify_eligibility_plist.py` script is saved.

### Step 2: (Optional) Test the Script on a Copy

**It's recommended to test the script on a copy of the plist file before modifying the actual file.**

#### a. Create a Test Copy of the Plist File

`sudo cp /private/var/db/os_eligibility/eligibility.plist ~/Desktop/test_eligibility.plist
sudo chown $(whoami) ~/Desktop/test_eligibility.plist` 

#### b. Update the `file_path` in the Script for Testing

`file_path = '/Users/yourusername/Desktop/test_eligibility.plist'` 

#### c. Run the Script Without `sudo`

`python3 modify_eligibility_plist.py` 

#### d. Verify the Changes

-   Open `~/Desktop/test_eligibility.plist` using a plist editor to confirm that the specified values have been updated.

### Step 3: Run the Script on the Actual File

#### a. Revert `file_path` Back to the Original

`file_path = '/private/var/db/os_eligibility/eligibility.plist'` 

#### b. Run the Script with Administrative Privileges

`sudo python3 modify_eligibility_plist.py` 

-   You will be prompted to enter your administrator password.

### Step 4: Confirm Backup Creation

-   Navigate to your backup directory (e.g., `/Users/johndoe/eligibility_backups`).
-   Verify that a backup file with a timestamped name has been created.

----------

## Important Notes

-   **System Integrity Protection (SIP)**:
    
    -   Be aware that macOS's SIP may prevent modifications to certain system files, even with `sudo`.
    -   Disabling SIP is not recommended due to security risks.
-   **Permissions**:
    
    -   Ensure you have the necessary permissions to read and write to the specified directories and files.
-   **Backups**:
    
    -   Always verify that a backup of the original file is created before making changes.
    -   The backup file will have a name like `eligibility.plist_YYYYMMDD-HHMM.bak`.
-   **Error Handling**:
    
    -   The script includes print statements to inform you if any keys are not found or if there is an unexpected structure.
    -   If you encounter errors, check the structure of your plist file and adjust the script accordingly.

----------

## Script Structure Overview

-   **Backup Creation**:
    
    -   The script creates a timestamped backup of the original plist file in the specified backup directory.
-   **Modifying Values**:
    
    -   The script modifies the following keys under `OS_ELIGIBILITY_DOMAIN_IRON`:
        
        -   `os_eligibility_answer_t`: Updated to `4`.
        -   `OS_ELIGIBILITY_INPUT_COUNTRY_BILLING`: Updated to `3`.
        -   `OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION`: Updated to `3`.
-   **Using `plistlib`**:
    
    -   The script uses Python's `plistlib` module to read and write plist files.
    -   This ensures compatibility with both XML and binary plist formats.

----------

## Troubleshooting

-   **Key Not Found Errors**:
    
    -   If the script reports that a key is not found, it may be due to differences in the plist file's structure.
    -   Use a plist editor to inspect the file and update the script's keys accordingly.
-   **Permission Denied Errors**:
    
    -   Ensure you're running the script with `sudo` when modifying the actual plist file.
    -   Verify that you have the necessary permissions for the backup directory.

----------

## Example of Updating Variables

`# Example updated file_path and backup_directory

file_path = '/private/var/db/os_eligibility/eligibility.plist'
backup_directory = '/Users/johndoe/eligibility_backups'` 

----------

## Disclaimer

-   **Use at Your Own Risk**:
    
    -   Modifying system files can have unintended consequences.
    -   Ensure you have backups and understand the changes you're making.
-   **No Liability**:
    
    -   The author is not responsible for any damage or data loss resulting from the use of this script.