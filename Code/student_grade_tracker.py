#Phase 1
def show_menu():
    print("--------------------------------")
    print("     Student Grade Tracker Program     ")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Check Pass OR Fail")
    print("4. Exit")
    print("--------------------------------")
  



#Phase 2:
def main():
  while True:
    show_menu()
    
    choice= input("Enter a Choice: ")
    

    if(choice == "1"):
      #placeholder for add_student()
      pass
    elif (choice == "2"):
      #placeholder for view_student()
      pass
    elif (choice == "3"):
      #placeholder for check_pass_fail()
      pass
    elif (choice == "4"):
      print("Bye Bye!")
      break
    else:
      print("Invalid Number, Try again!")
main()

      