# File Read & Write Challenge

# Read from input file
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (convert to uppercase)
modified_content = content.upper()

# Write to output file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read and modified content written to output.txt")
