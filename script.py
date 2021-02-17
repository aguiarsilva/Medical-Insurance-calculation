# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi,num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = "The estimated insurance cost for "+ name +" is " + str(estimated_cost) + " dollars."
  return (output_message, estimated_cost)

def calculate_difference(output_message1, estimated_cost1, output_message2, estimated_cost2):
  print(output_message1)
  print(output_message2)
  print ("The difference in insurance cost is "+ str(abs(estimated_cost1-estimated_cost2)) + " dollars.") 
# Initial variables for Maria  
# Estimate Maria's insurance cost
maria_output_message, estimated_cost_maria = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

# Initial variables for Omar

# Estimate Omar's insurance cost 
omar_output_message, estimated_cost_omar = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

bruno_output_message, estimated_cost_bruno = calculate_insurance_cost(name = "Bruno", age = 41, sex = 1, bmi = 28.2, num_of_children = 2, smoker = 0)

print(estimated_cost_bruno)
print(estimated_cost_omar)
print(calculate_difference(omar_output_message, estimated_cost_omar, bruno_output_message, estimated_cost_bruno))