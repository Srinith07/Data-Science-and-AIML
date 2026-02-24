with open('file_handling.txt', 'r') as file:
    for line in file:
        if line.strip():                 # checks if line is not empty
            cleaned_line = line.strip()  # removes extra spaces
            print(cleaned_line.lower())  # converts text to lowercase
