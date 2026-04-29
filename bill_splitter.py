# Start with 0 dollars and 4 friends
running_total = 0
num_of_friends = 4

# Costs of everything ordered
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Add all the food and drinks together
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Calculate a 25% tip
tip = running_total * 0.25
print('Tip amount:', tip)

# Add the tip to the total bill
running_total += tip
print('Total with tip:', running_total)

# Split the total bill between 4 friends
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Round the number to 2 decimal places (like real money)
each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)
