class Expense_Tracker:

    def welcome(self):
        print("=============================")
        print("WELCOME TO EXPENSE TRACKER")
        print("=============================")

    def track(self):
        pocket_money = int(input("ENTER YOUR POCKET MONEY: "))

        total_expense = 0
        expense_list = []

        file_name = "Expense_tracker.txt"

        while True:
            print("""
----------
Category
----------
1. Food
2. Travel
3. Recharge
4. Other
5. Stop
""")

            try:
                cat = int(input("ENTER CATEGORY (1-5): "))
            except:
                print("Invalid input! Enter number only.")
                continue

            if cat == 5:
                break

            if cat not in [1, 2, 3, 4]:
                print("Invalid category! Try again.")
                continue

            try:
                ex = int(input("ENTER EXPENSE: "))
            except:
                print("Invalid amount!")
                continue

            if cat == 1:
                category = "Food"
            elif cat == 2:
                category = "Travel"
            elif cat == 3:
                category = "Recharge"
            else:
                category = "Other"

            expense_list.append((category, ex))
            total_expense += ex

      
            with open("Expense_tracker.txt","a") as f:
                f.write(f"{category} - {ex}\n")

            print(f"Added → {category}: {ex}")

        # SUMMARY
        saving = pocket_money - total_expense

        print("\n================ SUMMARY ================")
        print("POCKET MONEY:", pocket_money)
        print("TOTAL EXPENSE:", total_expense)
        print("SAVING:", saving)
        print("NUMBER OF ENTRIES:", len(expense_list))

        if expense_list:
            highest = max(expense_list, key=lambda x: x[1])
            print("HIGHEST EXPENSE:", highest)

        # READ FILE
        print("\n========== FILE DATA ==========")
        with open("Expense_tracker.txt", "r") as f:
            print(f.read())


m1 = Expense_Tracker()
m1.welcome()
m1.track()