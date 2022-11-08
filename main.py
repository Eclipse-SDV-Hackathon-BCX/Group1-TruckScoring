import sys
from threading import Thread
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from gui_controller import Controller

from ecal_api import *

app = QGuiApplication(sys.argv)

controller = Controller()

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.rootContext().setContextProperty("main_controller", controller)
engine.load('qml/main.qml')

window = engine.rootObjects()[0]
controller.show_positive_change.connect(window.show_positive_change)
controller.show_negative_change.connect(window.show_negative_change)


def ms_to_score(time):
    time_ms = time / 1000.
    return int(50 - (time_ms / 100))


def do_stuff():
    ecal_core.initialize(sys.argv, "reaction-test")
    truck = TruckAPI()

    total_score = 0
    max_timeout = 8 # seconds
    max_wait = 3 # seconds
    min_wait = 1 # seconds
    print("Starting game in 3 seconds!")
    time.sleep(3)
    while True:
        print("Total Score: {}\n\n".format(total_score))
        test = random.randint(0, 5)
        wait = random.random() * max_wait
        # wait = max(min_wait, wait)

        time.sleep(wait)

        score = max_timeout
        test_name = "Error"
        print(test)
        if test == 0:
            controller.set_task("Brake!")
            score = ms_to_score(truck.reaction_test_brake(max_timeout))
            test_name = "Braking Test"
        elif test == 1:
            controller.set_task("Steer Right!")
            score = ms_to_score(truck.reaction_right_steering(max_timeout))
            test_name = "Right Steering Test"
        elif test == 2:
            controller.set_task("Steer Left!")
            score = ms_to_score(truck.reaction_left_steering(max_timeout))
            test_name = "Left Steering Test"
        elif test > 2 and test <= 6:
            button_index = random.randint(0, 11)
            task_string = "Press Button: {}".format(button_index+1)
            controller.set_task(task_string)
            test_name = "Button test!"
            score = ms_to_score(truck.reaction_button(button_index, max_timeout))
        print("{} - Score: {}".format(test_name, score))
        if score >= 0:
            controller.show_positive_change.emit(score)
        else:
            controller.show_negative_change.emit(abs(score))
        total_score += score
        controller.set_score(total_score)
        controller.set_task("Wait")

        truck.lightbar_front(500)
        time.sleep(0.5)
        truck.lightbar_front(500)
        time.sleep(0.5)
        truck.lightbar_front(500)
        time.sleep(0.5)
        truck.lightbar_front(500)
        time.sleep(0.5)
        print("Lightbar")

worker_thread = Thread(target=do_stuff)
worker_thread.start()

sys.exit(app.exec_())
