from math import prod
from flask import Flask, abort, request
import json
from mock_data import catalog
from config import db
from bson import ObjectId

app = Flask("Server")

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/me")
def about_me():
    return "Guillermo Jimenez"


#######################################################
###############     API ENDPOINTS     #################
###############      RETURN JSONS     #################
#######################################################

@app.route("/api/catalog", methods=["get"])
def get_catalog():

    products = []
    cursor = db.products.find({}) #cursor is collection

    for prod in cursor:
        #fix_id
        prod["_id"] = str(prod["_id"])
        products.append(prod)
    
    return json.dumps(products)

@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json() #return data payload from the request

    db.products.insert_one(product)
    print(product)

    #fix_id
    product["_id"] = str(product["_id"])

    #crash
    return json.dumps(product)

# GET /api/catalog/count -> how many products exist in the catalog
@app.route("/api/catalog/count")
def product_count():
    cursor = db.products.find({})
    count = 0

    for prod in cursor:
        count += 1

    #cnt = len(list(cursor))
    return json.dumps(count)

#get /api/catalog/total -> the sum o all the product's prices
@app.route("/api/catalog/total")
def total_of_catalog():
    cursor = db.products.find({})

    total = 0

    for prod in cursor:
        total += prod["price"]

    return json.dumps(total)

@app.route("/api/product/<id>")
def get_by_id(id):
    #find the product with _id is equal to id

    prod = db.products.find_one({"_id": ObjectId(id)})

    if not prod:
        #not found, return an error 404
        return abort(404, "No product with such id")

    prod["_id"] = str(prod["_id"])
    return json.dumps(prod)
    
    

#GET /api/product/cheapest
#should return the product with the lowest price
@app.route("/api/product/cheapest")
def cheapest_product():
    #create a variable with one of the elements from the list
    #create a for loop to travel catalog
    #if the price of your prod is lower than the price of your solutions
    solution = catalog[0]
    for prod in catalog:
        if prod["price"] < solution["price"]:
            solution = prod

    return json.dumps(solution)

#GET /api/categories
#should return a list of strings representing the unique categories

@app.get("/api/categories")
def unique_categories():
    categories = []
    for prod in catalog:
        category = prod["category"]
        if not category in categories:
            categories.append(category)
    
    return json.dumps(categories)



#ticket 2345
#create an endpoint that allows the client to get all the products
#form an unspecified category
#/api/catalog/fruit where fruit is the category in question
@app.get("/api/catalog/<category>")
def prods_by_pcategory(category):
    products = []
    cursor = db.products.find({"category": category})

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        products.append(prod)

    return json.dumps(products)



@app.get("/api/someNumbers")
def some_numbers():
    #return a list with numbers from 1 to 50 as json
    numbers = []
    for num in range(1, 51):
        numbers.append(num)

    return json.dumps(numbers)



############################################################
################# Coupon Code Endpoints ####################
############################################################

allCoupons = []

@app.route("/api/couponCode", methods=["get"])
def get_coupons():

    coupons = []
    cursor = db.couponCodes.find({})

    for code in cursor:
        code["_id"] = str(code["_id"])
        coupons.append(code)

    return json.dumps(coupons)



#create the post /api/couponCode
#get the coupon from the request
#assign an _id and add it to all coupons
#return the coupon as json

@app.route("/api/couponCode", methods=["post"])
def save_coupon():

    coupon = request.get_json()


    #must contain code, discount
    if not "code" in coupon or not "discount" in coupon:
        abort(400, "Invalid Coupon: No code and discount")

    #code should have at least 5 characters
    if len(coupon["code"]) < 5:
        abort(400, "Invalid Coupon: Coupon code should be at least 5 characters long")

    #discount should not be lower than 5 and not greater than 50
    if len(coupon["code"]) < 5 or len(coupon["code"]) > 50:
        abort(400, "Invalid Coupon: Coupon code should be at least 5 characters long and maximum 50 characters")

    
    db.couponCodes.insert_one(coupon)
    
    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)


@app.route("/api/couponCode/<code>")
def getcouponcode(code):
    coupon = db.couponCodes.find_one({"code", code})

    if not coupon:
        return abort(404, "No coupon with such id")

    coupon["_id"] = str(coupon["_id"])

    return json.dumps(coupon)





############################################################
#################### Users Endpoints #######################
############################################################

@app.route("/api/users", methods=["GET"])
def get_users():
    all_users = []
    cursor = db.users.find({})

    for user in cursor:
        user["_id"] = str(user["_id"])
        all_users.append(user)

    return json.dumps(all_users)


@app.route("/api/users", methods=["POST"])
def save_user():
    user = request.get_json()
    db.users.insert_one(user)

    user["_id"] = str(user["_id"])

    return json.dumps(user)

@app.route("/api/users/<email>")
def get_user_by_email(email):
    user = db.users.find_one({"email": email})
    
    if not user:
        return abort(404, "No user with that email")

    user["_id"] = str(user["_id"])

    return json.dumps(user)


@app.route("/api/login", methods=["POST"])
def login():
    data=request.get_json()
    
    if not "user" in data:
        abort(400, "User is required to login")

    if not "password" in data:
        return abort(400, "Password is required for login")

    user = db.users.find_one({"userName": data["user"], "password": data["password"]})

    if not user:
        abort(401, "Invalid login")

    

    return json.dumps(user)

app.run(debug=True)