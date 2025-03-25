# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2052776 (UOW Student ID)
#           : 20221224 (IIT Student ID)
# Date:2023/12/07
# Part 2 & Part 3
#Importing date and time
print("                             University Grading Calculator.                            ")
print("\n")
# Initializing Variables
Pass_Credit=0
Defer_Credit=0
Fail_Credit=0
Attempt=0
add_credits=0

main_list=[]   #This is the main list all each validated lists are stored in this 
message_list=[]  # Each condition of gradings are appending to this list


from graphics import*
def staff_logging():
    """When a stuff member loged into the programe this function will work"""
    Progress_count=0
    progress_module_trailer_count=0
    Exclude_count=0
    Do_not_Progress_module_retriever_count=0
    #File Handeling
   
    #Giving a while true for user to give another chance if the final out come is not equal to 120
    while True:
    #Making the list to store credits
        List_for_grade=[]   
# Pass Credit
        def pass_credits() :
            ''' This function is used to enter the pass credit and validate the value  '''
            while True:
                # Exceptional Handeling for Pass Credits
                try:
                    Pass_Credit=int(input("Enter your credit in Pass :- "))
                    if Pass_Credit!=0 and Pass_Credit!=20 and Pass_Credit!=40 and Pass_Credit!=60 and Pass_Credit!=80 and Pass_Credit!=100 and Pass_Credit!=120:
                        print("Out Of Range.\n")
                        
                    else:
                        List_for_grade.append(Pass_Credit)
                        break
                except ValueError:
                    print("Not an Integer.\n")
            return Pass_Credit
# Defer Credit
        def defer_credits():
            ''' This function is used to enter the defer credit and validate the value '''
            while True:
                # Exceptional Handeling for Defer Credits
                try:
                    Defer_Credit=int(input("Enter your credit in Defer :- "))
                    if Defer_Credit!=0 and Defer_Credit!=20 and Defer_Credit!=40 and Defer_Credit!=60 and Defer_Credit!=80 and Defer_Credit!=100 and Defer_Credit!=120:
                        print("Out Of Range.\n")
                    else:
                        List_for_grade.append(Defer_Credit)
                        break
                except ValueError:
                    print("Not an Integer.\n")
            return Defer_Credit
# Fail Credit
        def fail_credits():
            ''' This function is used to enter the fail credit and validate the value '''
            while True:
            # Exceptional Handeling for Fail Credits 
                try:
                    Fail_Credit=int(input("Enter your credit in Fail :- "))
                    if Fail_Credit!=0 and Fail_Credit!=20 and Fail_Credit!=40 and Fail_Credit!=60 and Fail_Credit!=80 and Fail_Credit!=100 and Fail_Credit!=120:
                        print("Out Of Range.\n")
                    else:
                        List_for_grade.append(Fail_Credit)
                        break
                except ValueError:
                    print("Not an Integer.\n")
            return  Fail_Credit
# Calling the functions 
        Pass_Credit=pass_credits()
        Defer_Credit=defer_credits()
        Fail_Credit=fail_credits()
        
    # Checking the total is equal to 120
        def total_credits():
            '''This function is to add those pass ,defer and fail credits '''
    # Exceptional Handeling for Total Incorrections
            add_credits=Pass_Credit+Defer_Credit+Fail_Credit
            return add_credits
    # Calling the function
        total=total_credits()
    # Checking whether the total credits are equal to 120
        if(total!=120):
            print("Total Incorrect.\n")
        
    # Giving the user to enter more cerdits or quit
            while True:
                print("Would you like to enter another data set ? ") 
                Attempt=str(input("Enter 'y' to continue or Enter 'q' to quit :- "))
    # Exceptional Handeling for the wrong attempts which user enterd
                if Attempt=="q" or Attempt=="y":
                    break
                else:
                    print("Wrong Character.")
                    print("Please Enter 'y' or 'q'.\n")
            if Attempt=="y":
                print("\n")
                continue
            elif(Attempt=="q"):
                    break
        else:
            main_list.append(List_for_grade)
# Grading Conditions
        if(List_for_grade[0]==120 and List_for_grade[1]==0 and List_for_grade[2]==0):
            message_list.append("Progress")
            print("Progress.\n")
            Progress_count=Progress_count+1
        elif(List_for_grade[0]==100 and (List_for_grade[1]==20 or List_for_grade[2]==20)):
            message_list.append("Progress (module trailer)")
            print("Progress (module trailer).\n")
            progress_module_trailer_count=progress_module_trailer_count+1
        elif(List_for_grade[2]==120 or List_for_grade[2]==80 or List_for_grade[2]==100):
            message_list.append("Exclude")
            print("Exclude.\n")
            Exclude_count=Exclude_count+1
        else:
            message_list.append("Do not Progress - module retriever")
            print("Do not Progress - module retriever.\n")
            Do_not_Progress_module_retriever_count=Do_not_Progress_module_retriever_count+1
# Giving the user to enter more cerdits or quit 
        while True:
            print("Would you like to enter another data set ? ")
            Attempt=str(input("Enter 'y' to continue or Enter 'q' to quit :- "))
# Exceptional Handeling for the wrong attempts which user enterd
            if Attempt=="q" or Attempt=="y":
                break
            else:
                print("Wrong Character.")
                print("Please Enter 'y' or 'q'.\n")
        if Attempt=="y":
            print("\n")
            continue
        elif(Attempt=="q"):
           
            File_Name="records.txt"
            with open(File_Name, "w") as file:
                j=0
                for i in main_list:
                    print(f"{message_list[j]} -",i[0],",",i[1],",",i[2])
                    file.write(f"{message_list[j]} - {i[0]} , {i[1]} , {i[2]}\n")
                    j=j+1
                print("\n")
            with open ('records.txt','r') as f:
                data=f.read()
            print(data)
                    
            break
#Making the histogram

    

    win = GraphWin("Histogram", 600, 400)
    win.setBackground("white")

    # Making the rectangles and the graph bottom line
    bar_for_progress = Rectangle(Point(30, 250), Point(100, 250-(Progress_count*10)))
    bar_for_trailer = Rectangle(Point(130, 250), Point(200, 250-(progress_module_trailer_count*10)))
    bar_for_retriever= Rectangle(Point(230, 250), Point(300, 250-(Do_not_Progress_module_retriever_count*10)))
    bar_for_exclude= Rectangle(Point(330, 250), Point(400, 250-(Exclude_count*10)))
    line = Line(Point(0,250), Point(430,250))

    # Giving colours.

    bar_for_progress.setFill("#38A793")
    bar_for_trailer.setFill("#B3584F")
    bar_for_retriever.setFill("#DEA640")
    bar_for_exclude.setFill("#09AB3D")

# Text formating

    text_histogram=Text(Point(145,30), "Histogram Results")
    text_progress=Text(Point(70,50), "Progress")
    text_trailer=Text(Point(70,50), "Trailer")
    text_retriever=Text(Point(70,50), "Retriever")
    text_exclude=Text(Point(70,50), "Excluded")

# Outputs counting and texting 
    text_progress_count=Text(Point(134,250-(Progress_count*10-40)), f"{Progress_count}")
    text_trailer_count=Text(Point(230,250-(progress_module_trailer_count*10-40)), f"{progress_module_trailer_count}")
    text_retriever_count=Text(Point(320,250-(Do_not_Progress_module_retriever_count*10-40)), f"{Do_not_Progress_module_retriever_count}")
    text_exclude_count=Text(Point(415,250-(Exclude_count*10-40)), f"{Exclude_count}")
    text_total_count=Text(Point(205,350), f"{Progress_count+progress_module_trailer_count+Do_not_Progress_module_retriever_count+Exclude_count} outcomes in the total")

# Moves for the graph and texting them

    bar_for_exclude.move(50,49)
    bar_for_retriever.move(55,49)
    bar_for_trailer.move(65,49)
    bar_for_progress.move(70,49)
    line.move(70,50)
    text_progress.move(63,262)
    text_trailer.move(160,262)
    text_retriever.move(250,262)
    text_exclude.move(345,262)

#styling the texts

    text_histogram.setStyle("bold")
    text_histogram.setSize(20)


    text_progress.setStyle("bold")
    text_progress.setTextColor("#4E6E83")



    text_trailer.setStyle("bold")
    text_trailer.setTextColor("#4E6E83")

    text_retriever.setStyle("bold")
    text_retriever.setTextColor("#4E6E83")


    text_exclude.setStyle("bold")
    text_exclude.setTextColor("#4E6E83")


    text_progress_count.setStyle("bold")
    text_progress_count.setTextColor("#4E6E83")

    text_trailer_count.setStyle("bold")
    text_trailer_count.setTextColor("#4E6E83")

    text_retriever_count.setStyle("bold")
    text_retriever_count.setTextColor("#4E6E83")

    text_exclude_count.setStyle("bold")
    text_exclude_count.setTextColor("#4E6E83")

    text_total_count.setStyle("bold")
    text_total_count.setTextColor("#4E6E83")
    text_total_count.setSize(16)

    # Drawing the objects on the canvas

    bar_for_progress.draw(win)
    bar_for_trailer.draw(win)
    bar_for_retriever.draw(win)
    bar_for_exclude.draw(win)
    line.draw(win)
    text_progress.draw(win)
    text_trailer.draw(win)
    text_retriever.draw(win)
    text_exclude.draw(win)
    text_histogram.draw(win)
    text_progress_count.draw(win)
    text_trailer_count.draw(win)
    text_retriever_count.draw(win)
    text_exclude_count.draw(win)
    text_total_count.draw(win)

    # closing the histogram window

    win.getMouse()  
    win.close()
    

def student_logging():
    """ When a student loged into the programe this function will work"""
# Giving a while true for user to give another chance if the final out come is not equal to 120
    while True:
# Making the list to store credits
        List_for_grade=[]   
# Pass Credit
        def pass_credits() :
            ''' This function is used to enter the pass credit and validate the value  '''
            while True:
# Exceptional Handeling for Pass Credits
                try:
                    Pass_Credit=int(input("Enter your credit in Pass :- "))
                    if Pass_Credit!=0 and Pass_Credit!=20 and Pass_Credit!=40 and Pass_Credit!=60 and Pass_Credit!=80 and Pass_Credit!=100 and Pass_Credit!=120:
                        print("Out Of Range.\n")
                        
                    else:
                        List_for_grade.append(Pass_Credit)
                        break
                except ValueError:
                    print("Not an Integer.\n")
            return Pass_Credit
# Defer Credit
        def defer_credits():
            ''' This function is used to enter the defer credit and validate the value '''
            while True:
# Exceptional Handeling for Defer Credits
                try:
                    Defer_Credit=int(input("Enter your credit in Defer :- "))
                    if Defer_Credit!=0 and Defer_Credit!=20 and Defer_Credit!=40 and Defer_Credit!=60 and Defer_Credit!=80 and Defer_Credit!=100 and Defer_Credit!=120:
                        print("Out Of Range.\n")
                    else:
                        List_for_grade.append(Defer_Credit)
                        break
                except ValueError:
                    print("Not an Integer.\n")
            return Defer_Credit
    #Fail Credit
        def fail_credits():
            ''' This function is used to enter the fail credit and validate the value '''
            while True:
            # Exceptional Handeling for Fail Credits 
                try:
                    Fail_Credit=int(input("Enter your credit in Fail :- "))
                    if Fail_Credit!=0 and Fail_Credit!=20 and Fail_Credit!=40 and Fail_Credit!=60 and Fail_Credit!=80 and Fail_Credit!=100 and Fail_Credit!=120:
                        print("Out Of Range.\n")
                    else:
                        List_for_grade.append(Fail_Credit)
                        break
                except ValueError:
                    print("Not an Integer.\n")
            return  Fail_Credit
# Calling the functions 
        Pass_Credit=pass_credits()
        Defer_Credit=defer_credits()
        Fail_Credit=fail_credits()
        
    # Checking the total is equal to 120
        def total_credits():
            '''This function is to add those pass ,defer and fail credits '''
    # Exceptional Handeling for Total Incorrections
            add_credits=Pass_Credit+Defer_Credit+Fail_Credit
            return add_credits
    # Calling the function
        total=total_credits()
    # Checking whether the total credits are equal to 120
        if(total!=120):
            print("Total Incorrect.\n")
        
    # Giving the user to enter more cerdits or quit
            while True:
                print("Would you like to enter another data set ? ") 
                Attempt=str(input("Enter 'y' to continue or Enter 'q' to quit :- "))
    # Exceptional Handeling for the wrong attempts which user enterd
                if Attempt=="q" or Attempt=="y":
                    break
                else:
                    print("Wrong Character.")
                    print("Please Enter 'y' or 'q'.\n")
            if Attempt=="y":
                print("\n")
                continue
            elif(Attempt=="q"):
                break
    # Grading Conditions
        if(List_for_grade[0]==120 and List_for_grade[1]==0 and List_for_grade[2]==0):
            print("Progress.\n")
            break
        elif(List_for_grade[0]==100 and (List_for_grade[1]==20 or List_for_grade[2]==20)):
            
            print("Progress (module trailer).\n")
            break
        elif(List_for_grade[2]==120 or List_for_grade[2]==80 or List_for_grade[2]==100):
            print("Exclude.\n")
            break
        else:
            
            print("Do not Progress - module retriever.\n")
            break
# loggings    
while True:
    logging=str(input("Enter 'student' for student logging or enter 'staff' for staff logging :- "))
    print("\n")
    if logging=="student" or logging=="staff":
        break
    else:
        print("Wrong Character.")
        print("Please Enter 'student' or 'staff'.\n")
if logging=="student":
    student_logging()
elif logging=="staff":
    staff_logging()
    

        
        
