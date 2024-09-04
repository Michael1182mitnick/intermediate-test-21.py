# Create a basic calculator that can evaluate simple arithmetic expressions (e.g., "3 + 5 / 2").

def basic_calculator(expression):
    def evaluate(tokens):
        stack = []
        num = 0
        sign = '+'

        while len(tokens) > 0:
            token = tokens.pop(0)

            if token.isdigit():
                num = int(token)

            if token == '(':
                num = evaluate(tokens)

            if (not token.isdigit() and token != ' ') or len(tokens) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)

                sign = token
                num = 0

            if token == ')':
                break

        return sum(stack)

    # Tokenize the input expression
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num_str = ''
            while i < len(expression) and expression[i].isdigit():
                num_str += expression[i]
                i += 1
            tokens.append(num_str)
        else:
            tokens.append(expression[i])
            i += 1

    return evaluate(tokens)


# Example usage
expression = "3 + 5 / 2"
result = basic_calculator(expression)
print(f"The result of '{expression}' is: {result}")
