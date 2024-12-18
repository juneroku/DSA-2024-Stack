def create_stack():
  stack = []
  return stack

def push(stack, item):
  stack.append(item)
  print("Pushed item: " + item)

def pop(stack):
  if (isEmpty(stack)):
    return("Stack is empty")
  return stack.pop()

def peek(stack):
  if (isEmpty(stack)):
    return("Stack is empty")
  return stack[len(stack)-1]

def isEmpty(stack):
  return len(stack) == 0

# สร้าง Stack
stack = create_stack()

# 1. สร้าง Stack และทดสอบการ push ข้อมูล 5 ตัว
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))

# 2. แสดงข้อมูลบนสุดโดยใช้ peek
print("\nItems in stack after push operations:")
print(stack)

# 3. ทดสอบ pop ข้อมูลออก 3 ตัว
print("\nPopped item: " + pop(stack))
print(pop(stack))
print(pop(stack))

print("\nStack after pop operations:")
print(stack)

# 4. แสดงข้อมูลที่เหลือใน Stack
print("\nTop item is: " + peek(stack))