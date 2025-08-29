# Error Handling Lab

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as f:
        print("File content:\n")
        print(f.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)
