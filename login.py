import json
import os
import hashlib
import getpass
import time

DB_FILE = "users.json"


# -----------------------------
# Create database if not exists
# -----------------------------
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)


# -----------------------------
# Database Functions
# -----------------------------
def load_users():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)


# -----------------------------
# Password Hashing
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# -----------------------------
# Register
# -----------------------------
def register():
    users = load_users()

    print("\n=== CREATE ACCOUNT ===")

    username = input("Username: ").strip()

    if username in users:
        print("❌ Username already exists!")
        return

    if len(username) < 3:
        print("❌ Username must be at least 3 characters!")
        return

    password = getpass.getpass("Password: ")
    confirm = getpass.getpass("Confirm Password: ")

    if password != confirm:
        print("❌ Passwords do not match!")
        return

    if len(password) < 6:
        print("❌ Password must be at least 6 characters!")
        return

    users[username] = {
        "password": hash_password(password),
        "created": time.ctime()
    }

    save_users(users)

    print("✅ Account created successfully!")


# -----------------------------
# Login
# -----------------------------
def login():
    users = load_users()

    print("\n=== LOGIN ===")

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    hashed_password = hash_password(password)

    if username in users and users[username]["password"] == hashed_password:
        print(f"\n✅ Welcome back, {username}!")
        dashboard(username)
    else:
        print("❌ Invalid username or password!")


# -----------------------------
# Dashboard
# -----------------------------
def dashboard(username):
    while True:
        print(f"\n===== DASHBOARD ({username}) =====")
        print("1. View Account Info")
        print("2. Change Password")
        print("3. Delete Account")
        print("4. Logout")

        choice = input("Select option: ")

        if choice == "1":
            users = load_users()

            print("\n--- ACCOUNT INFO ---")
            print("Username :", username)
            print("Created  :", users[username]["created"])

        elif choice == "2":
            change_password(username)

        elif choice == "3":
            deleted = delete_account(username)
            if deleted:
                break

        elif choice == "4":
            print("👋 Logged out successfully.")
            break

        else:
            print("❌ Invalid option!")


# -----------------------------
# Change Password
# -----------------------------
def change_password(username):
    users = load_users()

    print("\n=== CHANGE PASSWORD ===")

    old_password = getpass.getpass("Old Password: ")

    if users[username]["password"] != hash_password(old_password):
        print("❌ Wrong password!")
        return

    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm New Password: ")

    if new_password != confirm_password:
        print("❌ Passwords do not match!")
        return

    if len(new_password) < 6:
        print("❌ Password too short!")
        return

    users[username]["password"] = hash_password(new_password)

    save_users(users)

    print("✅ Password updated successfully!")


# -----------------------------
# Delete Account
# -----------------------------
def delete_account(username):
    users = load_users()

    print("\n⚠ DELETE ACCOUNT")
    confirm = input("Type YES to confirm: ")

    if confirm == "YES":
        del users[username]
        save_users(users)

        print("✅ Account deleted successfully.")
        return True

    print("❌ Account deletion cancelled.")
    return False


# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\n========== LOGIN SYSTEM ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice!")


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()