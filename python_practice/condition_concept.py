bad_words = ["scam", "fake", "bad"]
product_type = "this product is very bad"
'''if "bad" in product_type:
    print("the product is very bad")
else:
    print("Invalid Item")
    
if any(text in product_type for text in bad_words):
    print("the product is bad")
else:
    print("the product is good")
    '''
for text in bad_words:
    if text in product_type:

        print(f"we found the {text} product")
        break

    else:
        print("product is good")