# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

list_for_function =[1,2,3,4,5]

### FUNCTION ###
def list_doubled(list_simple):
    new_list = []
    ### CHECK THE TYPE ###
    if isinstance(list_simple, list):
        ### DOUBLE EVERY ELEMENT ###
        for i in range(len(list_simple)):
            if i%2 == 1:
                new_list.append(list_simple[i])
        return new_list
    else:
        ### ERROR FOR NOT LIST ###
        raise TypeError("it's not a list")

### CALL THE FUNCTION ###
list_doubled(list_for_function)
# list_doubled(5)
