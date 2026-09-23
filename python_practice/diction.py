login_details = {
    "name": "sunday",
    "email": "sundayattah77@gmail.com",
    "number": 4
}
print(login_details)
print(login_details["name"])
print(login_details.get("number", "Not provided"))
p = login_details["name"]= "john"
print(p)
name = login_details.pop("name")
print(name)
