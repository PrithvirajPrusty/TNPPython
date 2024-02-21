def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

user_input = input("Enter an expression:")
calculated_result = evaluate_expression(user_input)

print(f"Result: {calculated_result}")
