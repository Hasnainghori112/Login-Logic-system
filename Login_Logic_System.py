username: str = "admin"
password: str = "112233"
attempt: int = 3

while True:
    user_input: str = input("Enter username: ")
    pass_input: str = input("Enter password: ")

    if user_input != "admin" or pass_input != "112233":
        attempt -= 1
        print(f"Incorrect credentials \nYou have {attempt} attempts left")
    else:
        print("Login successful")
        break

    if attempt == 0:
        print("You have no more attempts. Try again later.")
        break
