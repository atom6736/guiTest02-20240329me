import sys

from PyQt5.QtWidgets import *
from  PyQt5.QtGui import *
from PyQt5 import uic #  Qt designer에서 제작한 ui를 불러오는 클래스. 이것이 없으면 못 불러오기 때문에 매우 중요.

form_class = uic.loadUiType("ui/test.ui")[0]  # 쓰기 전에 미리 uic를 불러와야 함. ui폴더에 넣었으니 그곳에서 가져와야 함. 그리고 인덱스 첫번째. 꼭 써주어야.
# 큐티디자이너에서 만든 ui를 불러오는 명령문이 바로 위의 문장. 이것이 클래스 전에 위치해야 함. 그리고 클래스가 이것도 상속받아야 함. 다중상속. 부모가 여럿. 파이썬은 가능함.

class MyWindow(QMainWindow, form_class): #여기서는 큐메인윈도우에서 상속받아야 함. 그리고 하나 더
    def __init__(self):
        super().__init__() # 부모클래스 생성자 호출
        self.setupUi(self) # 그리고 이 부분이 반드시 있어야 함. 위에서 불러온 test.ui를 연결하는 것임.
        self.setWindowTitle("연습 프로그램")




if __name__ == "__main__":  # 다른 파일에서 불러왔을 때 자동실행이 안 되도록 하는 기능.
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

    # 이상과 같이 하여 실행하면 판때기가 뜸. 그것은 계속 기본임. # 이상이 모두 ui불러오기를 하는 코딩.


