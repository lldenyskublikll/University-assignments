import numpy as np

# Correct order for operations:
#      x1 --- OR  ------------\
#          x                   >  AND ----- result    
#      x2 --- AND --- NAND ---/
#                  (AND + NOT)

# Activation function
def activation(x): 
    if x <= 0: 
        return 0 
    else: 
        return 1 

class Perceptron:
    def model(x, w, b): # x-inputs, w-weights, b-bias
        weighted_sum = np.dot(w, x) + b
        result = activation(weighted_sum)
        return result  

class Logical_operations:     
    def AND(x):
        AND_weights = np.array([1, 1])
        AND_bias = -1.5
        return Perceptron.model(x, AND_weights, AND_bias)
    
    def OR(x):
        OR_weights = np.array([1, 1])
        OR_bias = -0.5
        return Perceptron.model(x, OR_weights, OR_bias)
    
    def NOT(x):
        NOT_weights = -1
        NOT_bias = 0.5
        return Perceptron.model(x, NOT_weights, NOT_bias)
    
    def NAND(x):
        return Logical_operations.NOT(Logical_operations.AND(x))
    
    def XOR(x): 
        OR_out = Logical_operations.OR(x)
        AND_out = Logical_operations.AND(x)
        NAND_out = Logical_operations.NOT(AND_out)
        
        XOR_inputs = np.array([NAND_out, OR_out])
        XOR_out = Logical_operations.AND(XOR_inputs)
        return XOR_out

# Testing Perceptron for XOR logical operation
test_input_sample = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print("\nXOR logical function:")
for i, inputs in enumerate(test_input_sample):
    operation_result = Logical_operations.XOR(inputs)
    print(f"Result for {inputs[0]} ⊕  {inputs[1]}: {operation_result}")


print("\nOther LO that took part in XOR (just to be sure):")
print("AND logical function:")
for i, inputs in enumerate(test_input_sample):
    operation_result = Logical_operations.AND(inputs)
    print(f"Result for {inputs[0]} + {inputs[1]}: {operation_result}")

print("\nNAND logical function:")
for i, inputs in enumerate(test_input_sample):
    operation_result = Logical_operations.NAND(inputs)
    print(f"Result for !({inputs[0]} + {inputs[1]}): {operation_result}")

print("\nOR logical function:")
for i, inputs in enumerate(test_input_sample):
    operation_result = Logical_operations.OR(inputs)
    print(f"Result for {inputs[0]} * {inputs[1]}: {operation_result}")