"""
from PIL import Image

img = Image.open("요원.png")
print(img.size)
print(img.format)

img.show()
"""

"""
django 설치 방법
1. 설치 확인하기
cmd에 가서 pip-V를 입력하고 
'pip 19.0.3 from c:\users\admin\appdata\local\programs\python\python37-32\lib\site-packages\pip (python 3.7)'
이 출력이 되었다면 파이썬이 정상적으로 설치가 되었음을 알 수있다.
2. django 설치하기
커맨드창에 pip install django를 입력하고 잠시 기다리면 설치가 진행된다.
그리고 successfully...라는 메시지가 출력이 되면 django는 설치가 완료가 되었다.

설치가 잘못되어서 다시 지우고 설치를 하거나 삭제를 하여야할 경우에는 pip uninstall django를 입력
하면 삭제가 가능하고 언제든 다시 설치가 가능하다.
"""

import cv2

cap = cv2.VideoCapture('sample_video.mp4')

while True:
    ret,img_color = cap.read()

    if ret == False:
        break
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Color",img_color) # 컬러 화면으로 동영상을 출력한다.
 #  cv2.imshow("Gray",img_gray) 흑백 화면으로 동영상을 출력한다.

    if cv2.waitKey(1)&0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()