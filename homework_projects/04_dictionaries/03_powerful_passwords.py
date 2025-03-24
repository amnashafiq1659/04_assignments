# import sha256 from hashlib for hashing the password
from hashlib import sha256


# function to check password
def login(email, stored_logins, password_to_check):

    # check if email is not in stored_logins
    if email not in stored_logins:

        # return False if email is not in stored_logins
        return False

    # check if password_to_check is equal to stored_logins[email]
    return stored_logins[email] == hash_password(password_to_check)


# function to hash the password
def hash_password(password):

    # hash the password using sha256 algorithm
    return sha256(password.encode()).hexdigest()


def main():
    # store hashed passwords in a dictionary for easy lookup
    stored_logins = {
        "user@example.com": "6e659deaa85842cdabb5c6305fcc40033ba43772ec00d45c2a3c921741a5e377",
        "example.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "hello@website.com": "fbb4a8a163ffa958b4f02bf9cabb30cfefb40de803f2c4c346a9d39b3be1b544",
    }

    # test the login function
    print(login("user@example.com", stored_logins, "mypassword123"))
    print(login("user@example.com", stored_logins, "myword123"))

    print(login("example.com", stored_logins, "password"))
    print(login("example.com", stored_logins, "word"))

    print(login("hello@website.com", stored_logins, "securepass"))
    print(login("hello@website.com", stored_logins, "SecurePass"))


if __name__ == "__main__":
    main()
