import os

# Define the path to the desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Path to the file on the desktop
file_path = os.path.join(desktop_path, 'numbers.txt')

# Open a text file for writing
with open(file_path, 'w') as f:
    # Iterate through all numbers from 0 to 99999999
    for number in range(100000000):
        # Convert the number to a string with a fixed length of 8 characters, padding with leading zeros
        number_str = str(number).zfill(8)
        # Write the number to the file, followed by a new line
        f.write(number_str + '\n')

print("Numbers have been written to 'numbers.txt' on the Desktop.")
