#operating a file for reding (with'with')

with open("Book1.csv","r") as file:
    content=file.read() #READING THE CONTENT 
    print(content) #DISPLAYING THE CONTENT THE FILE
    
    
    rows=content.split("\n")
    for row in rows:
        print(f"row is {row}")
        cols= row.split(",")
        for col in cols:
            print(col)