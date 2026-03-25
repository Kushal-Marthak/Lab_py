#-->read
"""f = open("myfile.txt", "r")
data = f.read() # reads the whole file
print("File content:", data)
f.close()"""

#-->readline
"""f = open("myfile.txt", "r")

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

print("Line 1:", line1)
print("Line 2:", line2)
print("Line 3:", line3)

f.close()"""

#-->readlines
"""f = open("myfile.txt", "r")

lines = f.readlines()

print("List of lines:", lines)
print("Number of lines:", len(lines))

f.close()"""

#-->strip
"""f = open("myfile.txt", "r")

lines = f.readlines()

print(lines[1].strip())

f.close()"""
