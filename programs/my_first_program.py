# Simple Calculator
from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    operation = Input(name="operation", party=party1)  # Operation input (add, subtract, multiply, divide)

    # Perform the calculation based on the operation input
    result = SecretInteger()

    with If(operation == "add"):
        result = my_int1 + my_int2
    with ElseIf(operation == "subtract"):
        result = my_int1 - my_int2
    with ElseIf(operation == "multiply"):
        result = my_int1 * my_int2
    with ElseIf(operation == "divide"):
        result = my_int1 / my_int2
    with Else():
        result = SecretInteger(0)  # Default to 0 if the operation is not recognized

    # Output the result
    return [Output(result, "result", party1)]
