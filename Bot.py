import time
print("WELCOME! "*3)
time.sleep(2.0)
print("WELCOME TO THE TALKING MACHINE!")
time.sleep(2.0)
print("PLEASE RATE US IN STARS!")
time.sleep(2.0)
print("PRESS 1 TO CREATE AN ACCOUNT")
print("PRESS 2 TO LOGIN")
option =int(input("Choose Your Option Here: "))
time.sleep(2.0)
def inputs():
    if option==1:
        print("To Create An Account Type Your Name And Create A New Password As Below:")
        time.sleep(2.0)
        name=(input("Enter Your Name: "))
        password=(input("Create Your password: "))
        time.sleep(2.0)
        print(f"Hello! {name} Congratulation!You Have Successfully Created Your Account!")
        time.sleep(2.0)
        print("Nice To Meet You!")
        time.sleep(2.0)
    if option==2:
        print("To Login Type Your Name And Password: ")
        time.sleep(2.0)
        user_name=(input("Please Enter Your Name: "))
        password=(input("Please Enter Your Password: "))
        time.sleep(2.0)
        print(f"Hey!{user_name}")
        time.sleep(2.0)
        print("WELCOME BACK!")
        time.sleep(2.0)
inputs()
def choices():
    print("Press 1 To Random Talk With Bot")
    print("Press 2 To Talk about Your Favourite")
    print("Press 3 To Open Calculator")
    print("Press 4 To LogOut")
    option2 = int(input("Choose Your Option Here: "))
    if option2==1:
        print("LETS START A RANDOM TALK WITH ME!")
        time.sleep(2.0)
        name=(input("What Is Your Name: "))
        time.sleep(2.0)
        print(f"Ohh {name} Nice! My Name Is RoBo")
        time.sleep(2.0)
        study=(input("What Is Your Qualification: "))
        time.sleep(2.0)
        print(f"Ohh {study} Great! I M A PROGRAMMER..")
        time.sleep(2.0)
        print(f"Okay {name} I have To Leave Now")
        time.sleep(2.0)
        print("HAVE A GOOD DAY")
        time.sleep(2.0)
        def again():
            choices()
        again()
    if option2==2:
        print("LETS TALK ABOUT YOUR FAVORITES!")
        time.sleep(2.0)
        color=(input("What Is Your Favorite Color: "))
        time.sleep(2.0)
        print(f"Ohh {color} Great! My Favorite Color Is Black")
        time.sleep(2.0)
        actor=(input("What is Your Favorite Actor: "))
        time.sleep(2.0)
        print(f"Ohh {actor} Amazing! My Favorite Actor Is SRK")
        time.sleep(2.0)
        print(f"Okay {name} I have To Leave Now")
        time.sleep(2.0)
        print("HAVE A GOOD DAY")
        time.sleep(2.0)
        def again2():
            choices()
        again2()
    if option2==3:
        print("STARTING....CALCULATOR")
        time.sleep(2.0)
        num1=int(input("Enter Your First Number: "))
        num2=int(input("Enter Your Second Number: "))
        time.sleep(2.0)
        print("Press 1 For ADDING")
        print("Press 2 For SUBSTRACT")
        print("Press 3 For MULTIPLY")
        print("Press 4 For DIVIDE")
        option3=int(input("CHOOSE AN OPTION HERE: "))
        if option3==1:
            print("CALCULATING........")
            time.sleep(2.0)
            sum=num1+num2
            print(sum)
        if option3==2:
            print("CALCULATING........")
            time.sleep(2.0)
            sum=num1-num2
            print(sum)
        if option3==3:
            print("CALCULATING........")
            time.sleep(2.0)
            sum=num1*num2
            print(sum)
        if option3==4:
            print("CALCULATING........")
            time.sleep(2.0)
            sum=num1/num2
            print(sum)
            def again3():
                choices()
            again3()
    if option2==4:
        print("THANK YOU FOR USING OUR APP")
        time.sleep(2.0)
        print("DON'T FORGOT TO RATE US!!!")
        time.sleep(2.0)
        def again4():
            choices()
        again4()
choices()