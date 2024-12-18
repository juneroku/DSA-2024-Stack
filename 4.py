def is_valid_json(json_string):
  """ตรวจสอบความถูกต้องของ JSON string

  Args:
    json_string: JSON string ที่ต้องการตรวจสอบ

  Returns:
    True ถ้า JSON string ถูกต้อง
    False ถ้า JSON string ไม่ถูกต้อง
  """

  stack = []
  opening_brackets = '{'
  closing_brackets = '}'

  for char in json_string:
    if char in opening_brackets:
      stack.append(char)
    elif char in closing_brackets:
      if not stack:
        return False
      stack.pop()

  return not stack

# รับ JSON string จากผู้ใช้
json_str = input("กรุณากรอก JSON string: ")

# ตรวจสอบความถูกต้อง
if is_valid_json(json_str):
  print("JSON string ถูกต้อง")
else:
  print("JSON string ไม่ถูกต้อง")