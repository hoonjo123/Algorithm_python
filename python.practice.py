print("hello")
a = 0xABC
print(a)
a = 3
b = 4
print(a ** b)
print('''
hello
      my name is
      hoon
      ''')

# def hello() : {
#   print("this is python")
# } 
# print(hello)


print("=" * 50)
print("My Program")
print("=" * 50)

a = "algorithm test"
print(len(a))
print(a[3])
print(a[-1])
print(a[0:9])
print(a[5:])

a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])

print("I eat %s apples" % "five")
print("I eat %d apples" % 3)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days" %(number, day))

print("I ate %s apples. so I was sick for %s days" %(number, day))
# %s를 사용하면 어떤 형태의 값이든 변환가능

print("Error is %d%%." % 98)
#%d% 하면 에러나옴 

print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
