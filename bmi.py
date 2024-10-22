def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    # Calculate BMI using the formula: weight / (height^2)
    bmi = weight / (height * height)
    if bmi <18.5:
        print("Under Weight")
    elif 18.5<=bmi<=25.0:
        print("Normal Weight")
    else:
        print("Over Weight")

    # Print the calculated BMI
    print("BMI = " + str(round(bmi, 2)))  # Rounding to 2 decimal places for readability

calculate_bmi(weight=57, height=1.73)
