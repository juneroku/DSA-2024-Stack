def evaluate_postfix(expression):
  """
  ฟังก์ชันคำนวณค่าของนิพจน์ Postfix

  Args:
    expression: นิพจน์ในรูปแบบ Postfix

  Returns:
    ค่าของนิพจน์
  """

  stack = []
  operators = "+-*/"

  for char in expression:
    if char.isdigit():
      stack.append(int(char))
    elif char in operators:
      operand2 = stack.pop()
      operand1 = stack.pop()
      if char == '+':
        result = operand1 + operand2
      elif char == '-':
        result = operand1 - operand2
      elif char == '*':
        result = operand1 * operand2
      elif char == '/':
        result = operand1 / operand2
      stack.append(result)

  return stack.pop()

# ตัวอย่างการใช้งาน
postfix_expression = "68+4*"
result = evaluate_postfix(postfix_expression)
print("ผลลัพธ์:", result)