def convertToBase(num, base):
  """
  ฟังก์ชันแปลงเลขฐาน 10 เป็นฐานอื่นๆ โดยใช้ Stack

  Args:
    num: เลขฐาน 10 ที่ต้องการแปลง
    base: ฐานที่ต้องการแปลง (เช่น 2, 16)

  Returns:
    สตริงแสดงเลขในฐานที่ต้องการ
  """

  stack = []

  while num > 0:
    remainder = num % base
    stack.append(remainder)
    num //= base

  result = ""
  while stack:
    result += str(stack.pop())

  return result

# รับค่า input จากผู้ใช้
decimal_num = int(input("กรุณากรอกเลขฐาน 10: "))

# แปลงเป็นฐาน 2
binary_num = convertToBase(decimal_num, 2)
print("เลขฐาน 2:", binary_num)

# แปลงเป็นฐาน 16
hexadecimal_num = convertToBase(decimal_num, 16)
print("เลขฐาน 16:", hexadecimal_num)