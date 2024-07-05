set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
#home work2

users = {}

def add_user(id, first_name, last_name, email, password, phone_number):
    users[id] = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone_number": phone_number
    }

def user_name(first_name, last_name):
    for user_data in users.values():
        if user_data["first_name"] == first_name and user_data["last_name"] == last_name:
            return user_data
    return "Not found"

def user_email(email):
    for user_data in users.values():
        if user_data["email"] == email:
            return user_data
    return "Not found"

def find_user_by_id(id):
    return users.get(id, "Not found")

add_user(1, "Aram", "Gevorgyan", "aram.@example.com", "password123", "+1234567890")
add_user(2, "Armen", "Abrahamyan", "ar.@example.com", "qwerty456", "+9876543210")

name = user_name("John", "Doe")
print("User name:", name if name != "Not found" else "User not found by name")

email = user_email("jane.smith@example.com")
print("User email:", email if email != "Not found" else "User not found by email")