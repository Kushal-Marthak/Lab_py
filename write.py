#-->write
"""f = open("info.txt", "w")
f.write("Hello Students\n")
f.write("Welcome to Python file handling.\n")
f.write("Learning is fun!\n")
f.close()"""

#-->writeline
"""f = open("info.txt", "w")

f.write("New content only.\n")

f.close()"""

#-->append
"""f = open("info.txt", "a")
f.write("This line is added at the end.\n")
f.close()"""