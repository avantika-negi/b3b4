import pickle

#A Python object (dictionary in this case)

data ={"name":"alice","age":"22","occupation":"kuch nhi"}

with open ("data.pickle","wb") as file:
    pickle.dump(data,file)
    
print("data has been searialised and saved to data.pickle")

#open the file in binary read Mode

with open ("data.pickle","rb") as file:
    loaded_data = pickle.load(file)
    
print("deserialized data:",loaded_data)