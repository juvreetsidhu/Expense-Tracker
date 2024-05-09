"""
-----------------------------------------------------------------------------------------------
Programmer: Juvreet Sidhu
Date: February 18, 2024
Description: Rather than making a silly game, I decided to make a program that has 
practical use. This program records user expenses and then summarzies them by category. 
After this it indicates total money spent and budget (user inputted value) remaining.
------------------------------------------------------------------------------------------------
"""

def main():
  print("------------------------------------------------------------\nWelcome to Monthly Expense Tracker!\n------------------------------------------------------------")

  #Runs the function that asks the user for their budget and sets that equal to a variable
  budget = get_valid_budget()
  
  #Empty lisst to store expense amounts and categories
  tot_xpnse_amount = []
  all_xpnse_categories = []

  #Continues getting expenses until user enters 0
  while True:
    xpnse_amount = get_xpnse_amount()
    if xpnse_amount == 0:
      break

    #Adds the expense amounts and categories to the list
    xpnse_category = get_xpnse_category()
    tot_xpnse_amount = tot_xpnse_amount + [xpnse_amount]
    all_xpnse_categories = all_xpnse_categories + [xpnse_category]

  #Runs the function that summarizes the expenses
  summarize_xpnses(tot_xpnse_amount, all_xpnse_categories, budget)

#Ensures valid budget is inputted
def get_valid_budget():
  while True:
    budget = input("Please enter your budget for the next 30 days (Exclude $ sign): ")
    if budget.isdigit():
      return float(budget)
    else:
      print("Please enter a valid number")

#Ensures valid expense amount is inputted
def get_xpnse_amount():
  while True:
    xpnse_amount = (input("Please enter the amount for your expense or enter 0 to stop (Exclude $ sign): "))
    if xpnse_amount.isdigit():
      return float(xpnse_amount)
    else:
      print("Please enter a valid number")

#Ensures valid expense category is selected
def get_xpnse_category():
  print("Please select a category for this expense: ")
  categories = [
    "🍔Food",
    "🚗Transportation",
    "🏡Housing",
    "🎪Entertainment",
    "✨Miscellaneous",
  ]

  #Numbers categories 1-5
  for x in range(len(categories)):
    print(f"{x+1}. {categories[x]}")

  category_range = f"[1-{len(categories)}]"
  selec_category = int(input(f"Now enter a category number {category_range}: "))
  if selec_category in range (1, len(categories)+1):
    return categories[selec_category-1]
  else:
    print("Invalid category number, setting category to 'Miscellaenous'")
    return "✨Miscellaneous"

def summarize_xpnses(tot_xpnse_amount, all_xpnse_categories, budget):
  print("------------------------------------------------------------\nSummarizing Your Expenses...\n------------------------------------------------------------")

  #Calculates total expenses by category
  tot_spent = 0
  for x in range(len(all_xpnse_categories)):
    xpnse_amount = tot_xpnse_amount[x]
    xpnse_category = all_xpnse_categories[x]
    print(f"{xpnse_category}: ${xpnse_amount}")

    #Calculates & prints total spent, budget remaining and daily budget
    tot_spent = tot_spent + xpnse_amount
  print(f"----> Total Spent: ${tot_spent}")
  rmng_budget = budget - tot_spent
  dly_budget = round(rmng_budget / 30, 2)
  if rmng_budget < 0:
    print(f"It looks like you are ${abs(rmng_budget)} over your budget :(")
  else: 
    print(f"----> Budget Remaining: ${rmng_budget}")
    print(f"----> Daily Budget: ${dly_budget}")

main()
