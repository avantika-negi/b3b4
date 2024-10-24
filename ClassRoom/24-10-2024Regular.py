import re

pattern = r"hello"
text = "hello world "
match = re.search (pattern , text)
print("Match found:",match.group() if match else "No match")

pattern = r"cat"
text1 = "the cat sat on the mat."
match2=re.search(pattern ,text1)
print("Match found:",match2.group() if match2 else "No match")


pattern = r"[a-z]+"
text2 = "Hello World 123"
match3=re.findall(pattern ,text2)
print("Match found:",match3)

pattern = r"[A-Z]+"
text3 = "Hello World 123"
match4=re.findall(pattern ,text2)
print("Match found:",match4)


pattern = r"\d"
text4 = "Hello World 123"
match5=re.findall(pattern ,text2)
print("Match found:",match5)


pattern = r"\d+"
text5 = "Hello World 123 456 890 128 44444 666666"
match6=re.findall(pattern ,text5)
print("Match found:",match6)


pattern = r"[\w]"
text6 = "Hello World 123 456 890 128 44444 666666"
match7=re.findall(pattern ,text6)
print("Match found:",match7)


pattern = r"\d{3}"  # 3 digit pair
text7 = "Hello World 123 456 890 128 44444 666666"
match8=re.findall(pattern ,text7)
print("Match found:",match8)

pattern = r"h.llo"
text8 = "helllo"
match9=re.findall(pattern ,text8)
print("Match found:",match.group() if match9 else "no ,match")


pattern1= r".*"
text9 = "content"
match10=re.search(pattern1,text9)
print("Greedy match:",match10.group())


pattern2= r".?"
text10 = "content"
match11=re.search(pattern2,text10)
print("lazy match:",match11.group())


# pattern3= r"(\d{3})-(\d{2})"
# text11 = "Phone number : 123-456"
# match12=re.search(pattern2,text11)
# print("Area code:", match12.group(1))
# print("local code:", match12.group(2))

pattern3=r"cat"
text11="The cat sat on the mat"
result = re.sub(pattern3,"dog",text11)
print("After substitution:",result)

pattern4=r"\s+"
text12="The split this sentence by spaces"
result1 = re.split(pattern4,text12)
print("split result:",result1)

pattern5=r" "
text13="The  too   split this sentence    by spaces  youu"
result2 = re.split(pattern5,text13)
print("split result:",result2)

pattern6=re.compile(r"\d+")
text14="123 apples,456 bananas"
matche12 = pattern6.findall(text14)
print("Matches:",matche12)


pattern6=re.compile(r"\d+")
text14="123 apples,456 bananas"
matche12 = pattern6.findall(text14)
print("Matches:",matche12)

pattern7 = r"hello"
text15 = "Hello"
match13 = re.search(pattern7, text, re.IGNORECASE)
print("Case-insensitive match:", match13.group() if match13 else "No match")



