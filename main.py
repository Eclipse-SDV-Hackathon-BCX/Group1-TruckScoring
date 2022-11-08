import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from gui_controller import Controller

app = QGuiApplication(sys.argv)

controller = Controller()

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.rootContext().setContextProperty("main_controller", controller)
engine.load('qml/main.qml')

window = engine.rootObjects()[0]
controller.show_positive_change.connect(window.show_positive_change)
controller.show_negative_change.connect(window.show_negative_change)

sys.exit(app.exec_())