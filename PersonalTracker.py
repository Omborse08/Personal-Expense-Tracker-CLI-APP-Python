expense_list = []
total_expense = 0

while True:
    print("\n1.Add Expense")
    print("2.View All Expense")
    print("3.Show Total Expense")
    print("4.Category-wise Total")
    print("5.Search by Date")
    print("6.Exit")
    choose_option = input("> Choose Option: ")
    match choose_option:
        case "1":
            add_date = input("- Date (DD-MM-YYYY): ")
            add_category = input("- Enter Category: ").strip()
            add_amount = float(input("- Enter Amount: ₹"))
            expense_list.append([add_date,add_category,add_amount])
            total_expense += add_amount

        case "2":
            if len(expense_list) > 0:
                print("All Expense Is")
                for i in expense_list:
                    print("> Date: ",i[0]," Category: ",i[1]," Amount: ",i[2])
            else:
                print("No List Found.")
        
        case "3":
            if len(expense_list) > 0:
                print("> Total Expense Is: ₹",total_expense)
            else:
                print("No total expense found.")

        case "4":
            if len(expense_list) > 0:
                print("Enter Category To Search")
                category = input("Enter Category: ")
                category_total = 0
                for j in expense_list:
                  if category == j[1]:
                    category_total += j[2]
                if category_total > 0:
                    print("> Total in",category,": ₹",category_total)
                else:
                    print("No expense found in this category.")

        case "5":
            if len(expense_list) > 0:
                date_add = input("Enter Date (DD-MM-YYYY): ")
                print("Expense On",date_add)
                for k in expense_list:
                    if date_add == k[0]:
                        print("> Category: ",k[1],"Amount: ",k[2])
            else:
                print("No Date Matched.")

        case "6":
            print("You're in Existing State")
            print("1.Yes")
            print("2.No")
            Choose_Exit = input("Choose Option: ")
            match Choose_Exit:
                case "2":
                    print("Exit Cancelled.")

                case "1":
                    print("> Thanks For Using Personal Tracker App")
                    break
                case _:
                    print("Invalid Option Try Again.")
        
        case _:
            print("Invalid Option. ")