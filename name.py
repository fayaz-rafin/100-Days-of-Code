name = "ada lovelace"
print(name.title()) #The title() method changes each word to title case, where each word begins with a capital letter.
print(name.upper()) #Prints every letter into upper cases.
print(name.lower()) #Prints every name into lower cases.

first_name = "ada"
last_name = "lovelace"

# this is an f string. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.

full_name = f"{first_name} {last_name}" 
print(f"Hello, {full_name.title()}!")
