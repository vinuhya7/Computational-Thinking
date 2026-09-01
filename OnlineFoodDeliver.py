import random

# -----------------------------
# CUSTOMER DATA
# -----------------------------

customers = {
    1: {
        "name": "vinuhya",
        "location": (16.5062, 80.6480)
    }
}

# -----------------------------
# DELIVERY PERSON DATA
# -----------------------------

delivery_persons = {
    101: {
        "name": "sai",
        "location": (16.5100, 80.6400),
        "available": True
    },
    102: {
        "name": "vani",
        "location": (16.5200, 80.6500),
        "available": True
    },
    103: {
        "name": "ram",
        "location": (16.5000, 80.6600),
        "available": True
    }
}

# -----------------------------
# ORDERS
# -----------------------------

orders = {}


# -----------------------------
# 1. RECEIVE ORDER
# -----------------------------

def receive_order(customer_id, food_item, restaurant):

    order_id = random.randint(1000, 9999)

    orders[order_id] = {
        "customer_id": customer_id,
        "food": food_item,
        "restaurant": restaurant,
        "status": "Order Received",
        "delivery_person": None,
        "delivery_location": None
    }

    print("\n==============================")
    print("       ORDER RECEIVED")
    print("==============================")

    print("Order ID:", order_id)
    print("Customer:", customers[customer_id]["name"])
    print("Food:", food_item)
    print("Restaurant:", restaurant)
    print("Status:", orders[order_id]["status"])

    return order_id


# -----------------------------
# 2. ASSIGN DELIVERY PERSON
# -----------------------------

def assign_delivery_person(order_id):

    for person_id, person in delivery_persons.items():

        if person["available"]:

            orders[order_id]["delivery_person"] = person_id
            orders[order_id]["status"] = "Delivery Person Assigned"

            # Mark delivery person as unavailable
            person["available"] = False

            print("\n==============================")
            print("   DELIVERY PERSON ASSIGNED")
            print("==============================")

            print("Delivery Person:", person["name"])
            print("Order ID:", order_id)
            print("Status:", orders[order_id]["status"])

            return person_id

    print("\nNo delivery person available.")
    return None


# -----------------------------
# 3. TRACK DELIVERY LOCATION
# -----------------------------

def track_delivery(order_id):

    person_id = orders[order_id]["delivery_person"]

    if person_id is None:

        print("\nDelivery person has not been assigned.")
        return

    person = delivery_persons[person_id]

    customer_id = orders[order_id]["customer_id"]
    customer_location = customers[customer_id]["location"]

    orders[order_id]["status"] = "Out for Delivery"

    print("\n==============================")
    print("       DELIVERY STARTED")
    print("==============================")

    # Simulate movement
    for i in range(5):

        current_lat = person["location"][0]
        current_lon = person["location"][1]

        # Move delivery person closer to customer
        new_lat = current_lat + (
            customer_location[0] - current_lat
        ) * 0.25

        new_lon = current_lon + (
            customer_location[1] - current_lon
        ) * 0.25

        # Update delivery person's location
        person["location"] = (new_lat, new_lon)

        # Update order's delivery location
        orders[order_id]["delivery_location"] = person["location"]

        print("\nStep", i + 1)
        print("Latitude:", round(new_lat, 6))
        print("Longitude:", round(new_lon, 6))

    # Delivery completed
    orders[order_id]["status"] = "Delivered"

    # Make delivery person available again
    person["available"] = True

    print("\n==============================")
    print("       DELIVERY COMPLETED")
    print("==============================")

    print("Order ID:", order_id)
    print("Status:", orders[order_id]["status"])


# -----------------------------
# 4. UPDATE CUSTOMER
# -----------------------------

def update_customer(order_id):

    order = orders[order_id]

    person_id = order["delivery_person"]

    if person_id is not None:
        person_name = delivery_persons[person_id]["name"]
    else:
        person_name = "Not Assigned"

    print("\n==============================")
    print("       CUSTOMER UPDATE")
    print("==============================")

    print("Order ID:", order_id)
    print("Food:", order["food"])
    print("Restaurant:", order["restaurant"])
    print("Delivery Person:", person_name)
    print("Status:", order["status"])

    if order["delivery_location"] is not None:

        latitude = order["delivery_location"][0]
        longitude = order["delivery_location"][1]

        print("\nCurrent Location:")
        print("Latitude:", round(latitude, 6))
        print("Longitude:", round(longitude, 6))

    print("==============================")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("\n")
print("==============================")
print("   ONLINE FOOD DELIVERY SYSTEM")
print("==============================")


# Customer places order
order_id = receive_order(
    customer_id=1,
    food_item="Chicken Biryani",
    restaurant="Spice Restaurant"
)


# Assign delivery person
delivery_person_id = assign_delivery_person(order_id)


# Track delivery
if delivery_person_id is not None:

    track_delivery(order_id)

    # Update customer
    update_customer(order_id)