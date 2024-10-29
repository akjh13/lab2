def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    # Calculate BMI using the formula: weight / (height^2)
    bmi = weight / (height * height)
    
    # Determine the weight classification and return corresponding value
    if bmi < 18.5:
        print("Under Weight")
        classification = -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        classification = 0
    else:
        print("Over Weight")
        classification = 1

    # Print the calculated BMI
    print("BMI = " + str(round(bmi, 2)))  # Rounding to 2 decimal places for readability
    
    return classification

# Example usage
result = calculate_bmi(weight=57, height=1.73)
print("Weight Classification Return Value:", result)
