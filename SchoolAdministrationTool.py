import csv
def update_into_csv(info_list):
    with open("student_info.csv",'a') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact No.","Email ID"])
        writer.writerow(info_list)




if __name__ =="__main__":
    condition= True
    student_no=1
    while (condition):
        student_info=input("Enter the student #{} details in the following format:-\n[Name Age Contact_Number Email_ID]:-".format(student_no))

        student_info_list=student_info.split()

        print("Check the entered information of the student:-\nName:- {}\nAge:- {}\nContact No.:- {}\nEmail ID:- {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        check=input("Enter (yes/no) whether the details of student are correct or not:-")

        if check=="yes":
            choice=input("Enter (yes/no) whether you want to enter more student details:-")
            if choice=="yes":
                student_no=student_no+1
                condition=True
            elif choice=="no":
                condition=False
                update_into_csv(student_info_list)
        elif check=="no":
            print("Please re-enter the details!")


    
