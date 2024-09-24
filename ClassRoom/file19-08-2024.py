#create file handle

file = open("example.txt","w")

# write data in file
file.write("hello ,this is a test.")
#save and close file
file.close()


file = open("example.txt","a")
file.write("\nnew line".upper())
file.close

#for reading the data 
filename="example.txt"
file=open(filename,"r")
filecontent=file.readlines()
file.close()

print(filecontent)

