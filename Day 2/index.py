#print(type("Hello")) -- String
#print(type(258963))  --int
#print(type(2.5))      --Float
#print(type(True))       --boolean

#subscripting
#print("Hello"[4])  --As in the programming the numbering start with 0,1,2,3,4,5....(So in eg the 4 will print O)

#String
#print("123" + "456")  #concatenation

#Typr Conversion
# name_of_the_user =input("Enter User Name : ")
# Length_of_the_Username = len(name_of_the_user)
# print(type(Length_of_the_Username))
# print("The Length of the Username is:" + str(Length_of_the_Username))

#mathematical
# print(123+456)
# print(741-258)
# print(12*2)
# print(12/2)
# print(12//2)
# print(12%2)
# print(12**2)
# print(3*3+3/3-3)

# height = 1.65
# weight = 84
#
# # Write your code here.
# # Calculate the bmi using weight and height.
# bmi = weight / (height ** 2)
#
# #print(int(bmi))
# #print(bmi)
# print(round(bmi, 2))
# print(round(bmi))



#####TIP CALCULATOR

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like? 10 12 15 20 "))
people = int(input("How many people to split the bill? "))
#bill_with_tip = bill * (1+tip / 100)
#print(bill_with_tip)
tip_as_percent = tip/100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")