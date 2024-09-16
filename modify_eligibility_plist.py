import os
import shutil
import plistlib
from datetime import datetime

# Path to the protected eligibility.plist file 
file_path = '/private/var/db/os_eligibility/eligibility.plist'

# Alternative path to store the backup file
backup_directory = '/Users/USERNAME/eligibility_backups'  # Update this path if needed

# Ensure the backup directory exists
os.makedirs(backup_directory, exist_ok=True)

# Generate a datetime stamp in the format YYYYMMDD-HHmm
timestamp = datetime.now().strftime('%Y%m%d-%H%M')

# Create a backup of the original file in the alternative directory with a timestamp
backup_filename = f"{os.path.basename(file_path)}_{timestamp}.bak"
backup_path = os.path.join(backup_directory, backup_filename)
shutil.copyfile(file_path, backup_path)
print(f"Backup created at {backup_path}")

# Read the plist file using plistlib
with open(file_path, 'rb') as fp:
    plist_data = plistlib.load(fp)

# Navigate and modify the plist data
try:
    # Access the 'OS_ELIGIBILITY_DOMAIN_IRON' dictionary
    iron_dict = plist_data['OS_ELIGIBILITY_DOMAIN_IRON']

    # Update 'os_eligibility_answer_t' to 4
    if 'os_eligibility_answer_t' in iron_dict:
        print(f"Original os_eligibility_answer_t value: {iron_dict['os_eligibility_answer_t']}")
        iron_dict['os_eligibility_answer_t'] = 4
        print(f"Updated os_eligibility_answer_t value to: {iron_dict['os_eligibility_answer_t']}")
    else:
        print("os_eligibility_answer_t not found in OS_ELIGIBILITY_DOMAIN_IRON")

    # Access the 'status' dictionary within 'OS_ELIGIBILITY_DOMAIN_IRON'
    status_dict = iron_dict['status']

    # Update 'OS_ELIGIBILITY_INPUT_COUNTRY_BILLING' to 3
    if 'OS_ELIGIBILITY_INPUT_COUNTRY_BILLING' in status_dict:
        print(f"Original OS_ELIGIBILITY_INPUT_COUNTRY_BILLING value: {status_dict['OS_ELIGIBILITY_INPUT_COUNTRY_BILLING']}")
        status_dict['OS_ELIGIBILITY_INPUT_COUNTRY_BILLING'] = 3
        print(f"Updated OS_ELIGIBILITY_INPUT_COUNTRY_BILLING value to: {status_dict['OS_ELIGIBILITY_INPUT_COUNTRY_BILLING']}")
    else:
        print("OS_ELIGIBILITY_INPUT_COUNTRY_BILLING not found in status")

    # Update 'OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION' to 3
    if 'OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION' in status_dict:
        print(f"Original OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION value: {status_dict['OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION']}")
        status_dict['OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION'] = 3
        print(f"Updated OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION value to: {status_dict['OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION']}")
    else:
        print("OS_ELIGIBILITY_INPUT_COUNTRY_LOCATION not found in status")

    # Write the modified plist data back to the file
    with open(file_path, 'wb') as fp:
        plistlib.dump(plist_data, fp)
    print(f"Modifications have been written to {file_path}")

except KeyError as e:
    print(f"Key not found: {e}")