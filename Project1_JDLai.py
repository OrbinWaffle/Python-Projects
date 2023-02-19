# Name: Joshua Lai
# Project 1
# Completed 2/20/2022

import math

# Task One
def TaskOne():
   while(True):
      selection = input("Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): ")
      if(selection == "q"):
         quit()
      selection = selection.upper()
      weight = str(input("Please input your weight in {0}: ".format("pounds" if selection == "I" else "kilograms")))
      if (not weight.replace(".", "").isnumeric() or float(weight) <= 0):
         print("ERROR: Weight must be a positive, non-zero number.")
         quit()
      height = str(input("Please input your height in {0}: ".format("inches" if selection == "I" else "meters")))
      if (not height.replace(".", "").isnumeric() or float(height) <= 0):
         print("ERROR: Height must be a positive, non-zero number.")
         quit()
      bmi = float(weight)/(float(height) ** 2)
      if (selection == "I"):
         bmi *= 703
      print("Your BMI is {0:.2f}.".format(bmi))
      if (bmi <= 18):
         print("Your BMI is below average. This is considered underweight.")
      elif (bmi > 18 and bmi < 25):
         print("Your BMI is within the average range.")
      if (bmi >= 25):
         print("Your BMI is above average. This is considered overweight.")

# OUTPUT:
   # Which task would you like to run? Type 1 or 2: 1
   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): I
   # Please input your weight in pounds: 155
   # Please input your height in inches: 70
   # Your BMI is 22.24.
   # Your BMI is within the average range.

   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): I
   # Please input your weight in pounds: 172
   # Please input your height in inches: 68
   # Your BMI is 26.15.
   # Your BMI is above average. This is considered overweight.

   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): M  
   # Please input your weight in kilograms: 75
   # Please input your height in meters: 1.83
   # Your BMI is 22.40.
   # Your BMI is within the average range.

   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): M  
   # Please input your weight in kilograms: 51.5
   # Please input your height in meters: 1.68
   # Your BMI is 18.25.
   # Your BMI is within the average range.

   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): I  
   # Please input your weight in pounds: 100
   # Please input your height in inches: 76
   # Your BMI is 12.17.
   # Your BMI is below average. This is considered underweight.

   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): M  
   # Please input your weight in kilograms: 205
   # Your BMI is 197.04.
   # Your BMI is above average. This is considered overweight.
   
   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): I  
   # Please input your weight in pounds: 999
   # Please input your height in inches: 0
   # ERROR: Height must be a positive, non-zero number.

   # Would you like to use Metric or Imperial? Type M for Metric or I for imperial (q to quit): M
   # Please input your weight in kilograms: -100 
   # ERROR: Weight must be a positive, non-zero number.

# Task Two
def TaskTwo():
   min_error = 0.000001
   while(True):
      input_exp = input("Please input the number to find the sine of, or \"q\" to quit: ")
      if(input_exp == "q"):
         quit()
      input_exp = input_exp.replace("pi", "math.pi")
      input_num = eval(input_exp)
      real_solution = math.sin(input_num)
      solution = 0
      last_fac = 1
      last_exp = input_num
      for i in range(1, 1000000):
         if (i == 1):
            current_exp = input_num
            solution += current_exp
            continue
         fac_demoninator = (i*2) - 1
         current_exp = last_exp * ((input_num ** 2) / (fac_demoninator * (fac_demoninator - 1)))
         print(current_exp)
         last_exp = current_exp
         current_exp *= -((-1) ** i)
         solution += current_exp
         if(math.fabs(solution - real_solution) < min_error):
            print ("It took {0} iterations to reach the minimum required error of {1}.".format(i, min_error))
            break
         last_fac += 2
      print("Final solution: {0}\nReal solution: {1}\n".format(solution, real_solution))

# OUTPUT:
   # Which task would you like to run? Type 1 or 2: 2
   # Please input the number to find the sine of, or "q" to quit: pi/3
   # It took 5 iterations to reach the minimum required error of 1e-06.
   # Final solution: 0.8660254450997811
   # Real solution: 0.8660254037844386

   # Please input the number to find the sine of, or "q" to quit: -pi/6
   # It took 4 iterations to reach the minimum required error of 1e-06.
   # Final solution: -0.4999999918690232
   # Real solution: -0.49999999999999994

   # Please input the number to find the sine of, or "q" to quit: 0.112
   # It took 2 iterations to reach the minimum required error of 1e-06.
   # Final solution: 0.11176584533333334
   # Real solution: 0.11176599215128519

   # Please input the number to find the sine of, or "q" to quit: pi
   # It took 8 iterations to reach the minimum required error of 1e-06.
   # Final solution: -7.727858895155385e-07
   # Real solution: 1.2246467991473532e-16

   # Please input the number to find the sine of, or "q" to quit: pi/2
   # It took 6 iterations to reach the minimum required error of 1e-06.
   # Final solution: 0.999999943741051
   # Real solution: 1.0

   # Please input the number to find the sine of, or "q" to quit: pi/9
   # It took 3 iterations to reach the minimum required error of 1e-06.
   # Final solution: 0.3420202684051968
   # Real solution: 0.3420201433256687

   # Please input the number to find the sine of, or "q" to quit: (2*pi) / 100 + (3 ** 2) 
   # It took 17 iterations to reach the minimum required error of 1e-06.
   # Final solution: 0.3540952120305122
   # Real solution: 0.35409492104802737

   # Please input the number to find the sine of, or "q" to quit: 10
   # It took 18 iterations to reach the minimum required error of 1e-06.
   # Final solution: -0.5440217912424486
   # Real solution: -0.5440211108893698

# Task selector
selection = int(
   input("Which task would you like to run? Type 1 or 2: "))
if (selection == 1):
   TaskOne()
elif (selection == 2):
   TaskTwo()