# #이게 왜 안 돌아가? 이건 왜 돌아가? 글쎄

# 왼쪽에서 오른쪽으로 문자열을 탐색하며 소문자는 그대로 출력
# (를 만나면 그냥 다음 문자로 넘어가기
# )를 만나면 가장 가까운 (로 돌아가기/ 문장 반복
               
# 읽을거 없으면 종료

# (의 위치 기억해뒀다가 )나오면 가장 가까운 (로 돌아가서 다시 읽기
                          


def Process(n, code):
  result = []
  stack = []
  i = 0

  while i < n:
    if code[i].isalpha():
      result.append(code[i])
      i += 1
    elif code[i] == '(':
      stack.append(i)
      i += 1

    elif code[i] == ')':
      if stack:
        start = stack.pop() + 1
        for j in range(start,i):
          if code[j].isalpha():
            result.append(code[j])
        i += 1
      else:
        raise ValueError("error")


  return len(result)

n = int(input())
code = input()

answer = Process(n, code)
print(answer)