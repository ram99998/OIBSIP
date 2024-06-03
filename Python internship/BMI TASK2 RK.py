#PROMPT THE USER FOR INPUT
height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))


#BMI CALCULATION LOGIC
BMI=weight/(height/100)**2

print(f"your BMI is {BMI}")

#BMI CLASSIFICATION LEVELS
if BMI<=18.4:
    print("you're underweight.\n you sholud do something aboout it.")
elif BMI<=24.9:
    print("Hey buddy you're healthy")
elif BMI<=29.9:
    print("you're overweight.\n Go and hit the GYM!")
elif BMI<=34.9:
    print("you're severely overweight.\n You should cut some Calories..!")
elif BMI<=39.9:
    print("you're obese.")
else :
    print("you are severely obese.")


