# Display welcome message
print("Welcome to the cable cost program\n")

# Requesting user name and cable amount
company_name = input("Enter the name of the company: ")
feet_of_cable = float(input("\nEnter the cable amount (in feet): "))

#Convert string to float
#feet_of_cable = float(feet_of_cable)

#Calculate the cost of cable
cost_of_cable = feet_of_cable * .87

if feet_of_cable >= 100:
  cost_of_cable = cost_of_cable * 0.80
if feet_of_cable >= 250:
  cost_of_cable = cost_of_cable * 0.70
if feet_of_cable >= 500:
  cost_of_cable = cost_of_cable * 0.50


# cost_of_cable = round(cost_of_cable, 2)
 
#Display name of the company and cost of fiber optic cable
print(f"\nThe name of the company is {company_name}")
print(f"\nThe cost of the cable is $ {cost_of_cable}")