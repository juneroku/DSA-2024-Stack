def reverse_string(s):
  """
  ฟังก์ชันกลับลำดับตัวอักษรในสตริง โดยใช้ Stack

  Args:
    s: สตริงที่จะกลับลำดับ

  Returns:
    สตริงที่กลับลำดับแล้ว
  """

  stack = []
  for char in s:
    stack.append(char)

  reversed_string = ""
  while stack:
    reversed_string += stack.pop()

  return reversed_string

# รับข้อความจากผู้ใช้
input_string = input("กรุณากรอกข้อความ: ")

# เรียกใช้ฟังก์ชันเพื่อกลับลำดับและแสดงผลลัพธ์
result = reverse_string(input_string)
print("ข้อความหลังจากกลับลำดับ:", result)