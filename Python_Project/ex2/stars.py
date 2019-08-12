"""
i = 0 # 변수를 설정
while i < 5: #n번 반복하기 위한 조건식
    print('*'*(i+1))
    i = i+1 # i+=1으로 바꾸어 사용을 할 수 있다.


a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0 # 총합의 변수를 설정
count = 0 # 종 개수의 변수를 설정
for i in a:
    total +=i
    count +=1
print(total/count)


n = int(input("n을 입력 하세요 : ")) # 정수 값을 입력 받도록 설정
def pivolist(n):
    pivonumber = [0 , 1] # 초기 리스트를 설정
    if n == 1:
        print(0)
    elif n == 2:
        print([0, 1])
    else:
        while pivonumber[-1]+pivonumber[-2]<n:
            pivonumber.append(pivonumber[-1]+pivonumber[-2])
        print(pivonumber)
    pivonumber(n)

"""
"""
score=[70,60,55,75,95,90,80,100]
textfile=open('./sample.txt','w') #읽기 모드 전환
for i in score:
    textfile.write(str(i)+'\n') #text 파일 쓸 때는 무조건 string 형식!
textfile.close() #파일 닫기는 생활화
newtextfile=open('./sample.txt','r')
total=0
number=0
for line in newtextfile:
    total+=int(line)
    number+=1
average=total/number
newtextfile.close()
resulttext=open('./result.txt','w')
resulttext.write(str(average))
resulttext.close()
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1) Numpy의 난수를 발생시키는 random 모듈에서 N개의 난수를
# 발생시키는 rand() 함수를 활용하여 50개의 난수를 발생시켜보자.
list = np.random.rand(50)
# 2) 이렇게 발생된 데이터를 Pandas의 시리즈형 데이터로 변환해보자.
data = pd.Series(list)
plt.plot(data)
# 3) Pandas 시리즈형 데이터를 선형 그래프로 그려 보자.
plt.show()
plt.hist(data)
# 4) 동일한 데이터를 가지고 막대 그래프를 그려 보자.
plt.show
