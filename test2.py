def test_dict():
    me={
        "first": "Memo",
        "last": "Pinkus",
        "age": 22,
        "hobbies": [],
        "address": {
            "street": "Via Ixtapa",
            "city": "Tijuana"
        },
        "another": 12,
    }

    print(me["first"] +" " + me["last"])

    #print age
    print(f"My age is: " + str(me['age']))

    #print age alternative
    print(f"My age is: {me['age']}")

    #print street address
    address= me["address"]
    print(address["street"])

    #print street address alternative
    print(me["address"]["street"])

    #add bew keys
    me["color"] = "red"

    #modify existing keys
    me["age"] = 36

    #check if a key exist in the dict
    if "age" in me:
        print("Age exist")



print("--------Dictionary Test---------")
test_dict()