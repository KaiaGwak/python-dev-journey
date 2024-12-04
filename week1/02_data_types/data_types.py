# data_types.py

# ===== 1. 숫자형(Numeric) =====
# 정수(Integer)
age = 25
print(f"정수: {age}, 타입: {type(age)}")

# 실수(Float)
height = 175.5
print(f"실수: {height}, 타입: {type(height)}")

# 복소수(Complex)
complex_num = 3 + 4j
print(f"복소수: {complex_num}, 타입: {type(complex_num)}")

# ===== 2. 문자열(String) =====
name = "Python"
multiline = """여러 줄의
문자열을
표현할 수 있습니다."""
print(f"\n문자열: {name}, 타입: {type(name)}")
print(f"여러 줄 문자열:\n{multiline}")

# 문자열 메서드
print(f"대문자: {name.upper()}")
print(f"문자 개수: {len(name)}")
print(f"문자 치환: {name.replace('P', 'J')}")

# ===== 3. 리스트(List) =====
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "Python", 3.14, True]
print(f"\n리스트: {numbers}, 타입: {type(numbers)}")
print(f"혼합 리스트: {mixed_list}")

# 리스트 메서드
numbers.append(6)
print(f"append 후: {numbers}")
numbers.pop()
print(f"pop 후: {numbers}")

# ===== 4. 튜플(Tuple) =====
coordinates = (10, 20)
print(f"\n튜플: {coordinates}, 타입: {type(coordinates)}")
# coordinates[0] = 30  # 에러: 튜플은 변경 불가

# ===== 5. 딕셔너리(Dictionary) =====
person = {
    "name": "Python",
    "age": 30,
    "skills": ["programming", "problem solving"]
}
print(f"\n딕셔너리: {person}, 타입: {type(person)}")
print(f"이름: {person['name']}")
print(f"나이: {person.get('age')}")

# ===== 6. 집합(Set) =====
fruits = {"apple", "banana", "orange"}
print(f"\n집합: {fruits}, 타입: {type(fruits)}")
fruits.add("grape")
print(f"add 후: {fruits}")

# ===== 7. 불리언(Boolean) =====
is_active = True
is_adult = age >= 18
print(f"\n불리언: {is_active}, 타입: {type(is_active)}")
print(f"성인 여부: {is_adult}")

# ===== 실습 예제 =====
def practice_data_types():
    # 1. 리스트에 좋아하는 음식 3개를 넣고 출력해보세요
    # 2. 딕셔너리를 사용해서 자신의 정보를 저장하고 출력해보세요
    # 3. 집합을 사용해서 좋아하는 색깔들을 저장하고 출력해보세요
    pass  # 여기에 코드를 작성하세요