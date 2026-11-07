dicto={"rahul":50,"sita":30,"virat":10,"jahnvi":20,"tia":80}
temp=0
for i in dicto.values():
    temp+=i
    ave=temp/len(dicto)
print(f"The average is {ave}")
print(f"The highteset score is {max(dicto.values())}")
print(f"The lowest score is {min(dicto.values())}")
searchinp=str(input("who do u want to search? ")).lower()
search=dicto.get(searchinp)
if search == None:
    print("not found")
else:
    print(search)