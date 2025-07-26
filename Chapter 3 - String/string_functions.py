name ="niteesh kumar patel"

# len () function – 
# This function returns the length of the strings including space.

print(len(name))

# String.endswith("tel") –
# This function_ tells whether the variable string ends with the string "tel" or not. 
# If string is "niteesh kumar patel", it returns true for "tel" since Niteesh Kumar patel ends with tel.

print(name.endswith("tel"))

# string.count("a") 
# counts the total number of occurrences of any character.

print(name.count("a"))

#string.find(word) – 
#This function friends a word and returns the index of first occurrence of that word in the string.

print(name.find("l"))


# string.captilize() -
# First letter will be capital in string

print(name.capitalize())

# string.replace (old word, new word ) – 
# This function replace the old word with new word in the entire string.

replacestr = name.replace("patel","King Patel")
print(replacestr)