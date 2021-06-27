#In programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it’s easier for users to read.
print("Nice pages!") #This is a regular statement
print("\tNice pages!") #This is a statement but tabbed to the right using the \t command

print("Languages:\nPython\nC\nJavaScript") #\n adds the string to a new line

print("Languages:\n\tPython\n\tC\n\tJavaScript")#combination of the above \t and the \n tags

##Whitespace Stripping

#To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
t = "Emery "
print(t.rstrip())#this output will delete any spaces the string had to the right.
t =" Emery"
print(t.lstrip())#this output will delete any spaces the string had to the left.