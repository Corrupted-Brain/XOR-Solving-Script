import binascii
print("enter your hexcode here")
input_string = raw_input()
str1 = binascii.unhexlify(input_string)
for i in range(0,255):
	str2=""
	for j in range(len(str1)):
		str2 += chr(ord( str1[j] ) ^ i)
		if "flag_format_here{" in str2:
			print(str2)
