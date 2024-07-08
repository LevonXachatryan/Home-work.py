def user_data():
    user_name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    repeat_password = input("Repeat your password: ")
    
    if len(user_name) < 3:
        return False
    elif not user_name.isalnum():
        return False
    
    if "@" not in email:
        print("lease enter a valid email")
        return False
    if not phone.isdigit() or len(phone) != 8:
        print("Phone number should be 10 digits long and contain only digits.")
        return False
    if password != repeat_password:
        print("Please try again.")
        return False
    
    print("Registration data is valid.")
    return True
    
if user_data():
    print("Fine")
else:
    print("Failed")