# ---------------------------------------------------
#  Mobile Plan Advisor
#  Name: Harmanpreet Kaur
# 
# ---------------------------------------------------

# STEP 1: Define the plans (hard-coded)
plans = [
    { "name": "CellCast", "base_cost": 29.83, "minutes": float("inf"), "data": 25,
      "extra_minute_cost": 0.0, "extra_gb_cost": 4.7, "roaming": False },

    { "name": "PackFinder", "base_cost": 54.47, "minutes": 471, "data": 41,
      "extra_minute_cost": 0.23, "extra_gb_cost": 1.14, "roaming": True },

    { "name": "ByteRadar", "base_cost": 44.30, "minutes": float("inf"), "data": 31,
      "extra_minute_cost": 0.0, "extra_gb_cost": 3.55, "roaming": False },

    { "name": "RoamTune", "base_cost": 27.76, "minutes": 474, "data": 18,
      "extra_minute_cost": 0.12, "extra_gb_cost": 2.38, "roaming": True },

    { "name": "RoamBoost", "base_cost": 55.68, "minutes": float("inf"), "data": 31,
      "extra_minute_cost": 0.0, "extra_gb_cost": 2.47, "roaming": False }
]


# STEP 2: Cost calculation function 
def calculate_cost(plan, minutes_used, data_used):
    extra_minutes = 0
    extra_data = 0

    if plan["minutes"] != float("inf") and minutes_used > plan["minutes"]:
        extra_minutes = minutes_used - plan["minutes"]

    if data_used > plan["data"]:
        extra_data = data_used - plan["data"]

    total_cost = (plan["base_cost"] +
                  extra_minutes * plan["extra_minute_cost"] +
                  extra_data * plan["extra_gb_cost"])
    return total_cost

# STEP 3: Menu function 
def show_menu(): 
    print("\n==============================")
    print("      Mobile Plan Advisor")
    print("==============================")
    print("1) Input your monthly usage")
    print("2) View current usage")
    print("3) Show all plan costs")
    print("4) Suggest the cheapest plan")
    print("5) Exit program")
    print("==============================")

# STEP 4: Main program
def main():
    # Start with no usage entered
    global plans 

    minutes_used = None
    data_used = None
    roaming_needed = None

    print("Welcome to the Mobile Plan Advisor!")
    print("This tool will help you find the most cost-effective plan.")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # Enter usage
            try:
                minutes_used = int(input("How many minutes do you use per month? "))
                data_used = int(input("How many GB of data do you use per month? "))
                roaming = input("Do you need international roaming (yes/no)? ").strip().lower()
                roaming_needed = True if roaming == "yes" else False
            except ValueError:
                print("Please enter numbers for minutes and data.")

        elif choice == "2":
            # Display usage
            print("\n--- Your Current Usage ---")
            if minutes_used is None:
                print("You haven’t entered your usage yet.")
            else:
                print(f"Minutes per month: {minutes_used}")
                print(f"Data per month: {data_used} GB")
                print(f"International roaming: {'Yes' if roaming_needed else 'No'}")

        elif choice == "3":
            print("\n--- Plan Costs ---")
            if minutes_used is None:
                print("Please enter your usage first (Option 1).")
            else:
                for plan in plans:
                    cost = calculate_cost(plan, minutes_used, data_used)
                    print(f"{plan['name']}: ${cost:.2f}")

        elif choice == "4":
            print("\n--- Best Plan Recommendation ---")
            if minutes_used is None:
              print("Please enter your usage first (Option 1).")
            else:
                valid_plans = []

        # Filter plans based on roaming
            for plan in plans: 
                if roaming_needed and not plan["roaming"]:
                  continue
                cost = calculate_cost(plan, minutes_used, data_used)
                valid_plans.append((plan["name"], cost))

            if not valid_plans: 
                print("No plans available that meet your roaming requirement.")
            else:
                cheapest = min(valid_plans, key=lambda x: x[1])
                print(f"The cheapest plan for your usage is: {cheapest[0]} (${cheapest[1]:.2f})")
            

        elif choice == "5":
            print("Thanks for using Mobile Plan Advisor. Goodbye, LEGEND!")
            break
        else:
            print("Invalid selection, try again.")

# STEP 5: Run program
if __name__ == "__main__":
    main()





 


