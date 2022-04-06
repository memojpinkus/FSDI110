from mock_data import catalog


#count the product whose title contains the text
def find_prod():
    text="y"

    #1 for loop and print the titles
    count = 0
    for prod in catalog:
        title = prod["title"]
        if text.lower() in title.lower():
            print(f"{title} ${prod['price']}")



def unique_categories():
    results = []
    for prod in catalog:
        cat = prod["category"]
        if not cat in results:
            results.append(cat)

    print(results)



find_prod()
unique_categories()