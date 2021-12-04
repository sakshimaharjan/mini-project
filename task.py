f = open("data.txt", "w+")
while(True):

    uName = input("Enter customer name: ")

    if uName == "quit":
        exit()
    uAge = input("Enter customer age: ")
    uGender = input("Enter customer gender: ")

    f.write("Customer name: " f"{uName} \n")
    f.write("Customer age: " f"{uAge} \n")
    f.write("Customer gender: " f"{uGender} \n")
    print("\n The data is saved. \n")

