print("Registration Application")
print("---------------------------------")
usern=input("enter username  ")
email=input("enter email  ")
password=input("enter password  ")
cpassword=input("enter again ")


if usern and email and password and cpassword:
    if usern.isalnum():
        if "@" in email and email.endswith(".com"):
            if password== cpassword:
                if len(password)>=8:
                    print("COMPLETE")
                else:
                    print("size too small")
            else:
                print("password doesnt match")
        else:
            print("invalid email")
    else:
        print("invalid username")
else:
    print("incomplete")