# Problem Statement
# Write a program to check if there is a vowel in a string.

# Input
# The input consists of a string.

# Output
# Output will be the answer whether there is a vowel or not. If there is vowel it will print "The string contains a vowel.", otherwise it will print "The string does not contain any vowel."

# Constraints
# The program will terminate whenever it finds a vowel.
# Example-1:
# Enter a String

# Input:
# Hello
# Output:
# The string contains a vowel.
your_str = input()
for char in your_str:
    if ((char=="a") or (char=="e") or (char=="i") or (char=="o") or (char=="u") or (char=="A") or (char=="E") or (char=="I") or (char=="O") or (char=="U")):
        vowel=True
        break
    else:
        vowel=False
    
    

if vowel == True:
    print("The string contains a vowel.") 
else:
    print("The string does not contain any vowel.")

