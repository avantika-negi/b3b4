# Write a program to save python list And read that save  file and recover original list 
import pickle

list1 =[1,2,3,4,5]

filepath = "data.txt"

with open(filepath,"w") as fileHandle:
    fileHandle.write(str(list1))
    
with open(filepath,"r") as fileHandle:
    readData = fileHandle.read()
    readData = readData[1:len(readData)-1].replace("","").split(",")
    print(f"read data is {readData} \n its type is {type(readData)}")
    
#A Python object (dictionary in this case)



with open ("readData.pickle","wb") as file:
    pickle.dump(readData,file)
    
print("data has been searialised and saved to data.pickle")

#open the file in binary read Mode

with open ("readData.pickle","rb") as file:
    loaded_data = pickle.load(file)
    
print("deserialized data:",loaded_data)
