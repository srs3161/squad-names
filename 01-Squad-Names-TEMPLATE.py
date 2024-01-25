#####################################################################
# author:Satyendra Raj Singh
# date:12/06/2023
# description:A program that calculates the frequency(substrings) of names in a
#             provided squad list file.
####################################################################

# A function to read the contents of a text file. It receives a string
# representing the name of the file, and returns a list containing all
# the names in the file. This function is also in charge of ensuring
# that the filename provided actually exists. If the file does not
# exist, the function prints an error message and prompts the user for a
# new file name.
def readContentsFromFile(file_name):
    try:
        file = open(file_name, "r")
        read = file.readlines()
        file.close()
        return read
    except FileNotFoundError:
        print("The file you entered does not exist")
        return None 
  
# A function that receives two string arguments and returns a boolean
# that represents whether the first string begins with the second
# string.
def startsWith(string1, string2):
    return string1.startswith(string2)

# A function that receives two string arguments and returns a boolean
# that represents whether the first string ends with the second string.
def endsWith(string_a, string_b):
    return string_a.endswith(string_b)


# A function that receives two string arguments and returns a boolean
# that represents whether the first string contains the second string.
def containString(stringA, stringB):
    return stringB in stringA

# A function that receives two arguments i.e. a list of names, and a
# substring. It then creates a short 3 element list that contains the
# number of times that the substring appears in the list. The first
# element is the number of names in which the substring appears at the 
# beginning. The second element in the number of names in which the 
# substring appears at the end. The third element in the number of
# names that contain the substring.
def substringCounting(nameslist1, substring):
    count = [0,0,0]
    for name in nameslist1:
        if startsWith(name.lower(), substring.lower()):
            count[0] +=1
        if endsWith(name.lower().rstrip(), substring.lower()):
            count[1] += 1
        if containString(name.lower(), substring.lower()):
            count[2] += 1
    return count


######################## MAIN #####################################
# prompt the user for the file name
filename = input("Enter the filename: ")


# store the names in the file in a list
namesList = readContentsFromFile(filename)
while namesList is None:
    filename=input("Enter in the file again: ")
    namesList = readContentsFromFile(filename)

# print out the number of names in the list
print(f"The file has {len(namesList)} names in it")


# prompt the user for the substring they want to search for
substringInput = input("What name (or substring) are you interested in searching? ")

print(f"----------------------------------------------------------------------")
# calculate the search statistics
counts = substringCounting(namesList, substringInput)
print(f"{counts[0]} names start with this string")
print(f"{counts[1]} names end  with this string")
# print out the results of the search.
print(f"{counts[2]} names conatains the string ")
print(f"---------------------------------------------------------------------")