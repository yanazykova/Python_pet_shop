# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount


def get_pets_sold(shop):  
    return shop["admin"]["pets_sold"]


def increase_pets_sold(shop, number):
     shop["admin"]["pets_sold"] += number


def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    found = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            found.append(pet)
    return found

def find_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)


def add_pet_to_stock(shop, new_pet):
    return shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, amount):
    customers["cash"] -= amount

