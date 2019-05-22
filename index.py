import myFunc

print("|{:-^50}|".format(""))
print("|{:^50}|".format("Welcome"))
print("|{:-^50}|".format(""))
print("|{:^50}|".format("Choose one operation: "))
print("|{:50}|".format("  1. Signup"))
print("|{:50}|".format("  2. Signin"))
print("|{:50}|".format("  3. Admin Signin"))
print("|{:50}|".format("  4. Quit"))
print("|{:-^50}|".format(""))

__ch = input("Enter your choice: ")

if __ch == "1":
    myFunc.signup()
elif __ch == "2":
    myFunc.login()
elif __ch == "3":
    myFunc.admin()
elif __ch == "4":
    exit()
else:
    print("You entered an incorrect choice. Please try again!")
