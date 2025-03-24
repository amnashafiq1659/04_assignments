import random
import string


def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation

    password = (
        random.choice(string.ascii_uppercase)
        + random.choice(string.ascii_lowercase)
        + random.choice(string.digits)
        + random.choice(string.punctuation)
        + "".join(random.choice(characters) for i in range(length - 4))
    )

    return password


def main():

    print("🔐 Random Password Generator 🔐")

    while True:

        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length >= 8:
                break
            print("❌ Password length must be at least 8!")
        except ValueError:
            print("❌ Please enter a valid number!")

    password = generate_password(length)

    print(f"\n✅ Generated Password: {password}")


if __name__ == "__main__":
    main()
