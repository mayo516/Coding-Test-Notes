# 크기가 n이고 1차원 리스트를 초기화 하는 코드
n = 10
a = [0] *n
print(a)

# 리스트 컴프리헨션
# 리스트를 초기화 하는 방법 중 하다. 리스트 안에 반복문을 통해서 만들기 때문에 한 줄의 소스코드로 초기화 가능

array = [ i for i in range(20) if i %2 ==1]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array2 = [[0] * m for _ in range(n)]
print(array2)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]