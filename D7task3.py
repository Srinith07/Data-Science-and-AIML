filename = input("Enter the filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
    print("\nOops! That file doesn't exist yet.")
