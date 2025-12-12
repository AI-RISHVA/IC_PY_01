import math

def calculate(tokens):
    try:
        if not tokens:
            return None

        # Square root as unary operator
        if tokens[0] == "sqrt":
            if len(tokens) != 2:
                return "Error"
            x = float(tokens[1])
            if x < 0:
                return "Error"
            return math.sqrt(x)

        # Only one token (just a number)
        if len(tokens) == 1:
            return float(tokens[0])

        # Multi-number calculation
        result = float(tokens[0])
        i = 1
        while i < len(tokens):
            op = tokens[i]
            if i+1 >= len(tokens):
                return "Error"
            num = float(tokens[i+1])

            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                if num == 0:
                    return "Error: division by zero"
                result /= num
            elif op == "^":
                result **= num
            elif op == "%":
                result = (result / 100) * num
            else:
                return "Error: unsupported operator"

            i += 2

        return result

    except:
        return "Error"

print("Calculator ready. Type 'exit' to stop.")
while True:
    line = input("calc> ").strip()
    if line == "exit":
        break
    result = calculate(line.split())
    print(result)
