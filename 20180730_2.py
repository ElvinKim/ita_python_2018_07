# 문자열
a = 1234
b = "1234"


# 문자열을 만드는 방법
print("abc")
c = 'test'
print(c)

d = '''python is
very good!'''

print(d)

# 따옴표 넣기
print('I\'m a python programmer')

# 줄바꿈
print("python is\nvery good")

# 문자열 연산자
print("-" * 20)
print("ABC" + "DEF")
print("abcd" * 3)

# 문자열 인덱싱
print("=" * 20)
a = "ABCDEFG"
print(a[2])
print(a[-1])
print("ABCDEFGHI"[-2])

# 문자열 슬라이싱
print("=" * 20)
b = "ABCDEFGHI"
print(b[1:3])
print(b[3:-1])


# 문자열 포맷팅
print("=" * 20)
name_format = "나의 이름은 %s입니다."
age_format = "나의 나이는 %d살 입니다."
my_format = "나의 이름은 %s이고 나이는 %d살 입니다."
print(name_format % "김상묵")
a = name_format % "김상묵"
print(a)

print(age_format % 20)
print(my_format % ("김영희", 25))


my_format_ver2 = "나의 이름은 %s이고 나이는 %s살 입니다."
print(my_format_ver2 % ("김영희", str(25)))

print(int("1234") + 1000)
print(float("2.345") + 1000)


# 문자열 포맷팅 2
print("=" * 20)
name_format = "나의 이름은 {}입니다."
age_format = "나의 나이는 {}살 입니다."
my_format = "나의 이름은 {}이고 나이는 {}살 입니다."
my_format_ver2 = "나의 이름은 {name}이고 나이는 {age}살 입니다."

print(name_format.format("김상묵"))
print(my_format.format("김상묵", 20))
print(my_format_ver2.format(name="김상묵", age=20))




