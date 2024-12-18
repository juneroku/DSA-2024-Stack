def infix_to_postfix(infix):
    """แปลงนิพจน์ Infix เป็น Postfix

    Args:
        infix (str): นิพจน์ Infix

    Returns:
        str: นิพจน์ Postfix
    """

    stack = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix = []

    for char in infix:
        if char.isdigit():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

def evaluate_postfix(postfix):
    """ประเมินค่าของนิพจน์ Postfix

    Args:
        postfix (str): นิพจน์ Postfix

    Returns:
        int: ค่าของนิพจน์
    """

    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
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

def evaluate_infix(infix):
    """ประเมินค่าของนิพจน์ Infix

    Args:
        infix (str): นิพจน์ Infix

    Returns:
        int: ค่าของนิพจน์
    """

    postfix = infix_to_postfix(infix)
    return evaluate_postfix(postfix)

# ตัวอย่างการใช้งาน
infix_expression = "2+3*(4-2)"
result = evaluate_infix(infix_expression)
print("ผลลัพธ์:", result)