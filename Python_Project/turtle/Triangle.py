# 터틀 그래픽을 import 해온다.
import turtle as t

"""
터틀 그래픽을 실행하려면 run -> run module 을 선택을 하거나
F5키를 누른다.
idea 는 ctrl + shift + f10을 누르면 터틀 그래픽이 실행이 된다.
"""

#거부기 모양으로 변경
t.shape("turtle")

'''
#삼각형 그리기
t.forward(100) #거북이가 100만큼 앞으로 이동한다.
t.left(120) #거북이가 왼쪽으로 120도 회전
t.forward(100) # 상기의 내용을 2번 반복시킨다.
t.left(120)
t.forward(120)
t.left(120)
'''
'''
#원 그리기
t.circle(50) # 반지름의 크기가 50인 원을 그린다. (원의 크기도 변경 가능하다)

#사각형 그리기
t.color("blue") # 펜의 색상을 파란색으로 변경(색상 자유)
t.pensize(2) # 펜의 굵기를 조절 가능하다(여기서는 굵기를 2로 지정하였다.)

for i in range(5) : #하기의 로직을 5번 반복시킨다.
    t.forward(100)
    t.left(90)
'''
#오각형 그리기
n = 5
t.color("blue")
t.begin.fill() # 색칠을 하는 영역을 지정한다.

for x in range(n):
    t.forward(50)
    t.left(360/n) # 거북이가 왼쪽으로 360/n만큼 왼쪽으로 회전 한다.

t.end_fill() # 색칠을 하는 영역을 마무리
t.hideturtle(); # 거북이를 화면에 보이지 않도록 숨긴다.