
# Input from User
str1 = input("Enter the first string : ")
str2 = input("Enter the second string : ")

# Convert Strings to Lowercase
str1 = str1.lower()
str2 = str2.lower()

# Sort Both Strings
print(sorted(str1))
print(sorted(str2))

# Check Anagram Condition
if sorted(str1) == sorted(str2):

    print("These are Anagrams")

else:

    print("These are not Anagrams")