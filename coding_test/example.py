fruits = ["apple","banana","strawberry"]
for i in range(len(fruits)):
  print(f"index{i}:{fruits[i]}")

total = 0
for i in range(1,11):
  total += i

print(f"10까지의 총합은 : {total}")
# print("10까지의 총합은 : %d"  % total)

number = [str([i]) for i in range(1, 11)]
print(",".join(number))
# print("[]".join(number))

numbers = [f"[{i}]" for i in range(1, 11)]
print(",".join(numbers))


# for j in range(5):
#   if j == 3:
#     pass
#   else:
#     print(f"[{j}]", end="")
#     if j != 4:
#       print(",", end="")

numbers = [f"[{j}]" for j in range(5) if j != 3]
print(",".join(numbers))


def divide(x,y):
  try:
    result = x / y
  except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
  except TypeError as e:
    print(f"Caught an exception: {e}")
  else:
    print(f"Result is: {result}")
  # finally:
    # print("Executing finally block")

divide(10, 2)
divide(10, 0)
divide(10, 'a')

