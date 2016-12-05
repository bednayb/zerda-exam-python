# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def count_a_in_text_file(file_name,string):
    try:
        ### OPEN THE FILE ###
        f = open(file_name)
        file_lines = f.readlines()
        number_of_a = 0
        ### COUNT "A" ###
        for word in range(len(file_lines)):
            for char in file_lines[word]:
                if char == "a":
                    number_of_a +=1
        print(number_of_a)
    ### NOT EXIST FILE ###
    except FileNotFoundError:
        return 0
