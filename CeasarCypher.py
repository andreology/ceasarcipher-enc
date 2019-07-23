alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter Message: ")
shift = int(input("Shift Value By?: "))

n = len(str_in)
str_out = ""

for i in range(n):
	c = str_in[i]
	loc = alpha.find(c)
	newloc= (loc + shift)%26
	str_out += alpha[newloc]

print("obfuscated version: " + str_out)