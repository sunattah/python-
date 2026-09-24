'''login_details = {
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
student_details = {
    "student1":{
        "name" : "sunday",
        "age" : 34,
        "class" : "primary 4"
    },

    "student 2" :{
        "name": "gideon",
        "age": 56,
        "class": "jss 4"
    }
}
print(student_details)
'''
def word_frequency(text):
    # Step 1: split the text into a list of words
    # (hint: convert to lowercase first so "The" and "the" count the same)
    words = ["Monkey", "baboo", "kong", "hunter", "dog"]
    
 
    # Step 2: create an empty dictionary to hold the counts
    counts = {}

    # Step 3: loop through each word
    for word in words:
        # Step 4: if the word is already a key in counts, increment it
        # if it's not, add it with a value of 1
        # (try doing this WITHOUT using .get() first, using an if/else)
        ___

    return counts


# Test it
sentence = "the cat sat on the mat the cat ran"
result = word_frequency(sentence)
print(result)
# Expected: {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'ran': 1}