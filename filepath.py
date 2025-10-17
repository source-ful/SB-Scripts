import os

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Script directory: {script_dir}")

# Get the absolute path of this script file
script_path = os.path.abspath(__file__)
print(f"Script path: {script_path}")
