# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def count_a_in_text_file(file_name, string):
    if isinstance(string, str):
        with open(file_name, "a") as myfile:
            myfile.write(string*10)
        return True
    else:
        return False

count_a_in_text_file("text_for_second.txt","apple")
