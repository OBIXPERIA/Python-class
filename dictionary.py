"""
dictionary methods
get - returns value from key
values - returns all values
keys - returns all the key
"""

userProfile = {
    "id" : '1',
    "name":"dragon",
    "work": "developer"
}

userData = [
    {
        "id" :1,
    "name":"dragon",
    "work": "developer" 
    },
     {
        "id" : 2,
    "name":"syntax",
    "work": "teacher" 
    },
     {
        "id" : 3,
    "name":"test",
    "work": "developer" 
    },
]


# print(userProfile["name"])

# print(userProfile.keys())

# print(userProfile.values())

# print(userProfile.get("name"))


# getting key from value
# search_value = input("Enter  value: ")

# for i in userProfile.keys():
#     if userProfile.get(i) == search_value :
#         print(i)
    

# userProfile["id"] = "45"

# print(userData)

# working with arrays of object
for data in userData:
    if data.get('work') == "developer":
        print(data)

# print(userProfile["work"])