import sys

from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5 import uic #  Qt designer에서 제작한 ui를 불러오는 클래스. 이것이 없으면 못 불러오기 때문에 매우 중요.


form_class = uic.loadUiType("ui/test.ui")[0]  # 쓰기 전에 미리 uic를 불러와야 함. ui폴더에 넣었으니 그곳에서 가져와야 함. 그리고 인덱스 첫번째. 꼭 써주어야.
# 큐티디자이너에서 만든 ui를 불러오는 명령문이 바로 위의 문장. 이것이 클래스 전에 위치해야 함. 그리고 클래스가 이것도 상속받아야 함. 다중상속. 부모가 여럿. 파이썬은 가능함.

class MyWindow(QMainWindow, form_class): #여기서는 큐메인윈도우에서 상속받아야 함. 그리고 하나 더 form_class도 상속받아야 함.
    def __init__(self):
        super().__init__() # 부모클래스 생성자 호출
        self.setupUi(self) # 그리고 이 부분이 반드시 있어야 함. 위에서 불러온 test.ui를 연결하는 것임.
        self.setWindowTitle("연습 프로그램")
        self.button1.clicked.connect(self.button1_click) ## button1 click 끝에 자동완성으로 나타나는 함수괄호 두개는 지워야 에러가 나지 않음.
        # 버튼 1이 클릭되면 button1_click 메서드 호출 connect 안에는 이름만 들어가야 하기 때문에 ()가 들어가면 안됨.
        self.button2.clicked.connect(self.button2_click)
        self.setWindowIcon(QIcon("img/Image20240326124631.png"))
        self.statusBar().showMessage("made by Koreanumberone 2023-03-29") # 판때기 아래에 출처 같은 줄을 표시하는 방법


    def button1_click(self):
        self.label1.setText("HelloWorld!!!") # 이 이름과 큐티디자이너의 이름이 오타로 인해 다르면 콘솔창에 에러가 찍히면 고치면 되는데 이 이름을 잘못 써서 에러가 나면 에러통지가 없고 그냥 프로그램이 튕겨버린다고. 프로그램이 간단하지만 에러가 안 뜨고
        # 멀쩡하다가 그냥 튕겨버림. 위젯의 양이 많아지면 이름을 틀리게 쓰는 경우가 많음. 그러니까 
        # 차라리 큐티디자이너의 이름을 복붙하는 것이 최선이다. 제일 에러가 많이 나는 이유다. 이게 다른 클래스를 불러 온 것이라 연동도 안되고 무조건 타이핑해야 하기때문에 더욱 주의.
#함수를 먼저 만들고 이벤트 처리하는 것이 순서. 이와 같이 함수를 만든 후에 위로 돌아가 이벤트(클릭하면 함수로 연결되도록 하는)를 만들도록 한다.

    def button2_click(self):
        self.label1.setText("안녕하세요!!!")



if __name__ == "__main__":  # 다른 파일에서 불러왔을 때 자동실행이 안 되도록 하는 기능.
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

    # 이상과 같이 하여 실행하면 판때기가 뜸. 그것은 계속 기본임. # 이상이 모두 ui불러오기를 하는 코딩.


