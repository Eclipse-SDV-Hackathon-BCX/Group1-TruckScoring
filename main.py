import sys
from threading import Thread
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from gui_controller import Controller

from truck_api import *

app = QGuiApplication(sys.argv)

controller = Controller()

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.rootContext().setContextProperty("main_controller", controller)
engine.load('qml/main.qml')

window = engine.rootObjects()[0]


# Lets do this here, so we can access the GUI elements

import ecal.core.core as ecal_core
from ecal.core.subscriber import StringSubscriber


ecal_core.initialize(sys.argv, "reaction-test")


def callback_carla(_topic, msg, _time):
    print("Carla Callback: {}".format(msg))
    if msg == "Crashed":
        controller.show_negative_change.emit(100)
        controller.set_score(-100)
        controller.set_task("Collision!")
    if msg == "Crossed line Solid":
        controller.show_negative_change.emit(20)
        controller.set_score(-20)
        controller.set_task("Crossed Solid Line!")


sub = StringSubscriber("Carla")
sub.set_callback(callback_carla)


# We don't want to share the controller, so we will set a callback to the
# eCAL brake topic, as it gets polled every 10ms.

points_per_duration = 50 # points per duration
duration_for_points = 5 # seconds
last_point_time = ecal_core.getmicroseconds()[1]
def give_points_over_time_cb(topic, msg, time):
    global last_point_time
    global points_per_duration
    global duration_for_points
    if last_point_time + duration_for_points * 1000 * 1000 < ecal_core.getmicroseconds()[1]:
        controller.set_score(points_per_duration)
        controller.show_positive_change.emit(points_per_duration)
        last_point_time = ecal_core.getmicroseconds()[1]


point_brake_sub = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)
point_brake_sub.set_callback(give_points_over_time_cb)

def ms_to_score(time):
    time_ms = time / 1000.
    return int(50 - (time_ms / 100))


def challenge_loop():
    truck = TruckAPI()

    total_score = 420 # Starting score
    max_timeout = 8 # seconds, max wait for a challenge
    max_wait = 10 # seconds, max wait for a new challenge

    print("Starting game in {} seconds!".format(max_wait))
    time.sleep(max_wait)
    while True:
        print("Total Score: {}\n\n".format(total_score))
        wait = random.random() * max_wait
        # wait = max(min_wait, wait)

        time.sleep(wait)

        test_decision = random.randint(0,1)

        score = 0
        test_name = ""
        if test_decision == 0:
            task_string = "Press Button"
            controller.set_task(task_string)
            test_name = "Button test!"
            score = ms_to_score(truck.reaction_button(max_timeout))
        elif truck.can_slow_down(1) and test_decision == 1:
            controller.set_task("Slow Down")
            test_name = "Slow Down"
            score = ms_to_score(truck.reaction_slow_down(max_timeout))
        elif test_decision == 1:
            print("Too slow for stop challenge")

        print("{} - Score: {}".format(test_name, score))

        if score > 0:
            controller.show_positive_change.emit(score)
        elif score < 0:
            controller.show_negative_change.emit(abs(score))


        total_score += score
        controller.set_score(score)
        controller.set_task("Wait")

        worst_possible_score = ms_to_score(max_timeout)

        if score > worst_possible_score:
            truck.lightbar_front(500)
            time.sleep(0.5)
            truck.lightbar_front(500)
            time.sleep(0.5)
            truck.lightbar_front(500)
            time.sleep(0.5)
            truck.lightbar_front(500)
            time.sleep(0.5)
        else:
            truck.lightbar_red_time(2.0)


worker_thread = Thread(target=challenge_loop)
worker_thread.start()

sys.exit(app.exec_())
