                            #Program For BOOK Mangment System
String_1 = "1: For Add Books\t\t\t\t"
String_2 = "2: For Edit Books (Note: You Must Add Some Record In Order to Search Edit Or View Records)\n"
String_3 = "3: For View Books Record\t\t\t\t4: For Search Books\t\t\t\t5:Exit"
X = 1
B = 1
A = 1
print("{}{}{}".format(String_1,String_2,String_3)) #format function is  used for better output
print ("==="*40)

Choice = eval (input("Enter Your Choice: "))       #We will Get Input From the user
t="|\t\t"
condition = False
while Choice!= 5:    #condition

    if Choice == 1:#Condition for Checking the User Input
        #Getting Ist Book Record From the User
        condition == True
        print()
        print ("||ENTER FIRST BOOK DETAILS|")
        print ("==="*22)
        Frist_Book_ID = eval(input("Enter First Book ID No: "))            #Getting Book ID From User
        First_Book_Name = input("Enter First Book Name: ")                 #Getting Book Name From User
        First_Book_Author = input("Enter First Book Author Name: ")        #Getting Book Author Name From User
        First_Book_Pub_Date = input("Enter First Book Publish Date: ")     #Getting Book Publish Date From User
        First_Book_Price = input("Enter First Book Price: ")               #Getting Book Price From the User
        print()                                                            #Print New Line

        #Getting 2nd Book Record From The User
        print()
        print ("||ENTER SECOND BOOK DETAILS|")
        print ("==="*22)
        Second_Book_ID = eval(input("Enter Second Book ID No: "))        #Getting Book ID From User
        Second_Book_Name = input("Enter Second Book Name: ")             #Getting Book Name From User
        Second_Book_Author = input("Enter Second Book Author Name: ")    #Getting Book Author Name From User
        Second_Book_Pub_Date = input("Enter Second Book Publish Date: ") #Getting Book Publish Date From User
        Second_Book_Price = input("Enter Second Book Price: ")           #Getting Book Price From the User
        print()                                                          #Will Print New Line

        #Getting Third Book Record From The User
        print()
        print ("||ENTER THIRD BOOK DETAILS|")
        print ("==="*22)
        Third_Book_ID = eval(input("Enter Third Book ID No: "))          #Getting Book ID From User
        Third_Book_Name = input("Enter Third Book Name: ")               #Getting Book Name From User
        Third_Book_Author = input("Enter Third Book Author Name: ")      #Getting Book Author Name From User
        Third_Book_Pub_Date = input("Enter Third Book Publish Date: ")   #Getting Book Publish Date From User
        Third_Book_Price = input("Enter Third Book Price: ")             #Getting Book Price From the User
        print()                                                          #Print New Line

        #Getting Fourth Book Record From The User
        print()
        print ("||ENTER FOURTH BOOK DETAILS|")
        print ("==="*22)
        Fourth_Book_ID = eval(input("Enter Fourth Book ID No: "))        #Getting Book ID From User
        Fourth_Book_Name = input("Enter Fourth Book Name: ")             #Getting Book Name From User
        Fourth_Book_Author = input("Enter Fourth Book Author Name: ")    #Getting Book Author Name From User
        Fourth_Book_Pub_Date = input("Enter Fourth Book Publish Date: ") #Getting Book Publish Date From User
        Fourth_Book_Price = input("Enter Fourth Book Price: ")           #Getting Book Price From the User
        print()                                                          #Print New Line

        #Getting Fifth Book Record From The User
        print()
        print ("||ENTER FIFTH BOOK DETAILS|")
        print ("==="*22)
        Fifth_Book_ID = eval(input("Enter Fifth Book ID No: "))        #Getting Book ID From User
        Fifth_Book_Name = input("Enter Fifth Book Name: ")             #Getting Book Name From User
        Fifth_Book_Author = input("Enter Fifth Book Author Name: ")    #Getting Book Author Name From User
        Fifth_Book_Pub_Date = input("Enter Fifth Book Publish Date: ") #Getting Book Publish Date From User
        Fifth_Book_Price =  input("Enter Fifth Book Price: ")          #Getting Book Price From the User
        print()
        #BOOK RECORDS
        Choice_1 = eval (input("Enter 1 To View Newly Added Book Record or Enter any number to proceed: "))  #getting input From user to show record
        print()
        if Choice_1 == 1:
            print ("||FIRST BOOK DETAILS|")
            print ("==="*40)
            print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Frist_Book_ID,t,First_Book_Name,t,First_Book_Author,t,First_Book_Pub_Date,t,First_Book_Price))
            print ()

            print ("||Second BOOK DETAILS||")
            print ("==="*40)                            #it will print == 40 times
            print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Second_Book_ID,t,Second_Book_Name,t,Second_Book_Author,t,Second_Book_Pub_Date,t,Second_Book_Price))
            print ()

            print ("||Third BOOK DETAILS||")
            print ("==="*40)                            #it will print == 40 times
            print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Third_Book_ID,t,Third_Book_Name,t,Third_Book_Author,t,Third_Book_Pub_Date,t,Third_Book_Price))
            print ()

            print ("||Fourth BOOK DETAILS||")
            print ("==="*40)                            #it will print == 40 times
            print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Fourth_Book_ID,t,Fourth_Book_Name,t,Fourth_Book_Author,t,Fourth_Book_Pub_Date,t,Fourth_Book_Price))
            print ()

            print ("||Fifth BOOK DETAILS||")
            print ("==="*40)                            #it will print == 40 times
            print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Fifth_Book_ID,t,Fifth_Book_Name,t,Fifth_Book_Author,t,Fifth_Book_Pub_Date,t,Fifth_Book_Price))
            print ()

            #A = 1                                            #Initialize

            #EDIT RECORD
        else:
            if Choice_1!= 1:
                print("Ok")
        print("1: For Add Books",t,"2: For Edit Books",t,"3: For View Books Record",t,"4: For Search Books",t,"5:Exit")
        print ("==="*37)
        print()
        Choice = eval (input("Enter Your Choice: "))
        print()

    elif Choice == 2:                                        #condition For edit record
        while A == 1:
            BOOK_ID = eval(input("Enter The Book Id You Want to Edit:"))
            print ("==="*12)
            print()

            if BOOK_ID == Frist_Book_ID:
                print("||UPDATING FIRST BOOK RECORD||")
                print ("==="*12)
                Ist_Book_ID = eval(input("Enter Book ID No: "))            #Getting Book ID From User
                Ist_Book_Name = input("Enter Book Name: ")                 #Getting Book Name From User
                Ist_Book_Author = input("Enter Book Author Name: ")        #Getting Book Author Name From User
                Ist_Book_Pub_Date = input("Enter Book Publish Date: ")     #Getting Book Publish Date From User
                Ist_Book_Price = input("Enter Book Price: ")               #Getting Book Price From the User
                print()
                A = input("Enter 1 to Edit More Records Or 0 To Exit: ")
                print()



            elif BOOK_ID == Second_Book_ID:
                print("||UPDATING SECOND BOOK RECORD||")
                print ("==="*12)
                Second_Book_ID = eval(input("Enter Book ID No: "))        #Getting Book ID From User
                Second_Book_Name = input("Enter Book Name: ")             #Getting Book Name From User
                Second_Book_Author = input("Enter Book Author Name: ")    #Getting Book Author Name From User
                Second_Book_Pub_Date = input("Enter Book Publish Date: ") #Getting Book Publish Date From User
                Second_Book_Price =  input("Enter Book Price: ")          #Getting Book Price From the User
                print()
                A = eval(input("Enter 1 to Edit More Records Or 0 To Exit: "))
                print()

            elif BOOK_ID == Third_Book_ID:
                print("||UPDATING THIRD BOOK RECORD||")
                print ("==="*12)
                Third_Book_ID = eval(input("Enter Book ID No: "))          #Getting Book ID From User
                Third_Book_Name = input("Enter Book Name: ")               #Getting Book Name From User
                Third_Book_Author = input("Enter Book Author Name: ")      #Getting Book Author Name From User
                Third_Book_Pub_Date = input("Enter Book Publish Date: ")   #Getting Book Publish Date From User
                Third_Book_Price = input("Enter Book Price: ")             #Getting Book Price From the User
                print()
                A = eval(input("Enter 1 to Edit More Records Or 0 To Exit: "))
                print()


            elif BOOK_ID == Fourth_Book_ID:
                print("||UPDATING FOURTH BOOK RECORD||")
                print ("==="*12)
                Fourth_Book_ID = eval(input("Enter Book ID No: "))        #Getting Book ID From User
                Fourth_Book_Name = input("Enter Book Name: ")             #Getting Book Name From User
                Fourth_Book_Author = input("Enter Book Author Name: ")    #Getting Book Author Name From User
                Fourth_Book_Pub_Date = input("Enter Book Publish Date: ") #Getting Book Publish Date From User
                Fourth_Book_Price = input("Enter Book Price: ")           #Getting Book Price From the User
                print()                                                   #Print New Line
                A = eval(input("Enter 1 to Edit More Records Or 0 To Exit: "))
                print()


            elif BOOK_ID == Fifth_Book_ID:
                print("||UPDATING FIFTH BOOK RECORD||")
                print ("==="*12)
                Fifth_Book_ID = eval(input("Enter Book ID No: "))        #Getting Book ID From User
                Fifth_Book_Name = input("Enter Book Name: ")             #Getting Book Name From User
                Fifth_Book_Author = input("Enter Book Author Name: ")    #Getting Book Author Name From User
                Fifth_Book_Pub_Date = input("Enter Book Publish Date: ") #Getting Book Publish Date From User
                Fifth_Book_Price = input("Enter Book Price: ")           #Getting Book Price From the User
                print()
                A = eval(input("Enter 1 to Edit More Records Or 0 To Exit: "))
                print()


            elif BOOK_ID != Frist_Book_ID or BOOK_ID != Second_Book_ID or BOOK_ID != Third_Book_ID or BOOK_ID != Fourth_Book_ID or BOOK_ID != Fifth_Book_ID :
                print("Sorry!!  No Record To be Edit For This Book ID\nTRY AGAIN")

        print("1: For Add Books",t,"2: For Edit Books",t,"3: For View Books Record",t,"4: For Search Books",t,"5:Exit")
        print ("==="*37)
        print()
        Choice = eval (input("Enter Your Choice: "))
        print ("==="*37)
        print()
        print()

    elif Choice == 3:
      if condition == True:
        print ("||FIRST BOOK DETAILS|")
        print ("==="*40)
        print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Frist_Book_ID,t,First_Book_Name,t,First_Book_Author,t,First_Book_Pub_Date,t,First_Book_Price))
        print ()

        print ("||Second BOOK DETAILS||")
        print ("==="*40)                            #it will print == 40 times
        print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Second_Book_ID,t,Second_Book_Name,t,Second_Book_Author,t,Second_Book_Pub_Date,t,Second_Book_Price))
        print ()

        print ("||Third BOOK DETAILS||")
        print ("==="*40)                            #it will print == 40 times
        print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Third_Book_ID,t,Third_Book_Name,t,Third_Book_Author,t,Third_Book_Pub_Date,t,Third_Book_Price))
        print ()

        print ("||Fourth BOOK DETAILS||")
        print ("==="*40)                            #it will print == 40 times
        print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Fourth_Book_ID,t,Fourth_Book_Name,t,Fourth_Book_Author,t,Fourth_Book_Pub_Date,t,Fourth_Book_Price))
        print ()

        print ("||Fifth BOOK DETAILS||")
        print ("==="*40)                            #it will print == 40 times
        print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Fifth_Book_ID,t,Fifth_Book_Name,t,Fifth_Book_Author,t,Fifth_Book_Pub_Date,t,Fifth_Book_Price))
        print ()
        print("1: For Add Books",t,"2: For Edit Books",t,"3: For View Books Record",t,"4: For Search Books",t,"5:Exit")
        print ("==="*37)
        print()
        Choice = eval (input("Enter Your Choice: "))
        print ("==="*37)
        print()
        print()

        #SEARCH BOOKS IN RECORD

    elif Choice == 4:
      if condition == True:
        while B == 1:
            Search_ID = eval(input("Enter The Book Id You Want to Search:"))
            print ("==="*12)
            print()

            if Search_ID == Frist_Book_ID:
                print("||BOOK RECORD FOUND SUCCESSFULLY||")
                print ("||FIRST BOOK DETAILS|")
                print ("==="*40)
                print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Frist_Book_ID,t,First_Book_Name,t,First_Book_Author,t,First_Book_Pub_Date,t,First_Book_Price))
                print ()
                #B = eval(input("Enter 1 to Search More Records Or 0 To Exit: "))



            elif Search_ID == Second_Book_ID:
                print("||SECOND BOOK RECORD FOUND SUCCESSFULLY||")
                print ("||Second BOOK DETAILS||")
                print ("==="*40)                            #it will print "==" 40 times
                print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Second_Book_ID,t,Second_Book_Name,t,Second_Book_Author,t,Second_Book_Pub_Date,t,Second_Book_Price))
                print ()
                #B = eval(input("Enter 1 to Search More Records Or 0 To Exit: "))
                #if B<1 or B>1:
                 #   print("Loop Conitnue")
                 #   break

            elif Search_ID == Third_Book_ID:
                print("||BOOK RECORD FOUND SUCCESSFULLY||")
                print ("||THIRD BOOK DETAILS||")
                print ("==="*40)                            #it will print == 40 times
                print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Third_Book_ID,t,Third_Book_Name,t,Third_Book_Author,t,Third_Book_Pub_Date,t,Third_Book_Price))
                print ()
                #B = eval(input("Enter 1 to Search More Records Or 0 To Exit: "))
                #break


            elif Search_ID == Fourth_Book_ID:
                print("||BOOK RECORD FOUND SUCCESSFULLY||")
                print ("||FOURTH BOOK DETAILS||")
                print ("==="*40)                            #it will print == 40 times
                print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Fourth_Book_ID,t,Fourth_Book_Name,t,Fourth_Book_Author,t,Fourth_Book_Pub_Date,t,Fourth_Book_Price))
                print ()
                print()
                #B = eval(input("Enter 1 to Search More Records Or 0 To Exit: "))
                #break


            elif Search_ID == Fifth_Book_ID:
                print("||BOOK RECORD FOUND SUCCESSFULLY||")
                print ("||Fifth BOOK DETAILS||")
                print ("==="*40)                            #it will print == 40 times
                print ("||Book ID:{}{}Book Name:{}{}Book Author Name:{}{}Book Publish Date:{}{}Book Price:{} ||".format(Fifth_Book_ID,t,Fifth_Book_Name,t,Fifth_Book_Author,t,Fifth_Book_Pub_Date,t,Fifth_Book_Price))
                print ()


            elif Search_ID != Frist_Book_ID or BOOK_ID != Second_Book_ID or BOOK_ID != Third_Book_ID or BOOK_ID != Fourth_Book_ID or BOOK_ID != Fifth_Book_ID :
                print("Sorry!!  No Record Found For This Book ID\nTRY AGAIN\n")
                B = eval(input("Enter 1 to Search More Records Or 0 To Exit: "))
        print("1: For Add Books",t,"2: For Edit Books",t,"3: For View Books Record",t,"4: For Search Books",t,"5:Exit")
        print ("==="*37)
        print()
        Choice = eval (input("Enter Your Choice: "))
        print ("==="*37)
        print()
        print()
    else:
        print("Wrong Input ")
        break
print ("Program Terminated")
