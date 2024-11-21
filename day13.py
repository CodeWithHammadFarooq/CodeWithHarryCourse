#Strings are immutable
a = "!!!Hammad !!!!!!!! !!!!!!! Hammad"
print(len(a))
print(a.upper())
print(a.lower())
print(a)
print(a.rstrip("!"))
print(a.replace("Hammad","Ammar"))
print(a.split(" "))
blogHeading = "intRoduction tO pYtHoN"
print(blogHeading.capitalize())

str = "Welcome to the Console!!!!!!!"
print(str.center(50))
print(len(str))
print(len(str.center(50)))

print(a.count("Hammad"))

str1 = "Welcome to the console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the console !!!"
print(str1.endswith("to", 4, 10))

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))
print(str2.find("ishh"))
#print(str2.findex("is"))
str3 = "WelcomeTotheConsole"
print(str3.isalnum())

str4 = "welcome"
print(str4.islower())

str5 = "welcome\n"
print(str5.isprintable())

print(str5.isspace())
str5 = "            " #using spacebar
print(str4.isspace())
str4 = "            " #using spacebar

str6 = "World Health Organization"
print(str6.istitle())

str6 = "world health organization"
print(str6.istitle())

str7 = "Python is a high level language"
print(str7.startswith("Python"))

str8 = "Python is a high level language"
print(str8.swapcase())

str9 = "He is harry and harry is honest man"
print(str9.title())