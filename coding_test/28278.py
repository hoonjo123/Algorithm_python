# #스택2
# import sys
# input = sys.stdin.read

# def process_commands(commands):
#   stack = []
#   result = []

#   for command in commands:
#     if command[0] == '1':
#       stack.append(int(command[1]))
#     elif command[0] == '2':
#       if stack:
#         result.append(stack.pop())
#       else:
#         result.append(-1)
#     elif command[0] == '3':
#       result.append(len(stack))
#     elif command[0] == '4':
#       if stack:
#         result.append(0)
#       else:
#         result.append(1)
#     elif command[0] =='5':
#       if stack:
#         result.append(stack[-1])
#       else:
#         result.append(-1)

#   return result

# commands = input().splitlines()
# commands = [command.split() for command in commands[1:]]

# output = process_commands(commands)
# sys.stdout.write("\n".join(map(str, output)) + "\n")

n = int(input())

stack = []

for _ in range(n):
  command = input().split()

  if command[0] == '1':
    stack.append(int(command[1]))