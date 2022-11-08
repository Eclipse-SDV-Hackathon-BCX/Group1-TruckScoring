import sys
import random
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher

from PB.SensorNearData import Brake_pb2
from PB.SensorNearData import VehicleDynamics_pb2
from PB.HMI import HMICanKeyboard_pb2
from PB import W3Lightbar_pb2


def lightbar_left_time(sleep_time_ms: int):
    pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
    pb_msg = W3Lightbar_pb2.W3LightbarRequest()
    pb_msg.Clear()
    pb_msg.alley_light_left = True
    pb_msg.turn_signal_left = True
    pub.send(pb_msg)
    time.sleep(sleep_time_ms * 1000)
    lightbar_off()

def lightbar_right_time(sleep_time_ms: int):
    pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
    pb_msg = W3Lightbar_pb2.W3LightbarRequest()
    pb_msg.Clear()
    pb_msg.alley_light_right = True
    pb_msg.turn_signal_right = True
    pub.send(pb_msg)
    time.sleep(sleep_time_ms * 1000)
    lightbar_off()


def lightbar_left():
    pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
    pb_msg = W3Lightbar_pb2.W3LightbarRequest()
    pb_msg.Clear()
    pb_msg.alley_light_left = True
    pb_msg.turn_signal_left = True
    pub.send(pb_msg)

def lightbar_right():
    pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
    pb_msg = W3Lightbar_pb2.W3LightbarRequest()
    pb_msg.Clear()
    pb_msg.alley_light_right = True
    pb_msg.turn_signal_right = True
    pub.send(pb_msg)


def lightbar_front(sleep_time_ms: int):
    pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
    pb_msg = W3Lightbar_pb2.W3LightbarRequest()
    pb_msg.Clear()
    pb_msg.take_down = True
    pb_msg.front_colour_2 = True
    pub.send(pb_msg)
    time.sleep(sleep_time_ms / 1000.)
    lightbar_off()

def lightbar_off():
    pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
    pb_msg = W3Lightbar_pb2.W3LightbarRequest()
    pb_msg.Clear()
    pub.send(pb_msg)



def reaction_test_brake(timeout: int):
    print("Press Brake!")
    sub = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        if msg.signals.is_brake_applied:
            end_time = ecal_core.getmicroseconds()[1]
            break
    score = end_time - start_time
    return score

def reaction_left_steering(timeout: int):
    lightbar_left()
    print("Steer left!")
    sub = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        if msg.signals.steering_wheel_angle > 0.2:
            end_time = ecal_core.getmicroseconds()[1]
            break
    score = end_time - start_time
    lightbar_off()
    return score


def reaction_right_steering(timeout: int):
    lightbar_right()
    print("Steer right!")
    sub = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        if msg.signals.steering_wheel_angle < -0.2:
            end_time = ecal_core.getmicroseconds()[1]
            break
    score = end_time - start_time
    lightbar_off()
    return score

def reaction_button(index:int , timeout: int):
    if index >= 12 or index < 0:
        print("Error, button index wrong")
        return 0

    sub = ProtoSubscriber("HmiCanKeyboardStatePb", HMICanKeyboard_pb2.HmiCanKeyboardState)

    print("Press Button: {}".format(index+1))

    start_time = ecal_core.getmicroseconds()[1]
    end_time = start_time + 1000*1000 * timeout

    while ecal_core.ok():
        if ecal_core.getmicroseconds()[1] > end_time:
            break
        ret, msg, time = sub.receive(500)
        finish = False

        if index == 0 and msg.CanKeyboard_Button_01 == 2:
            finish = True
        elif index == 1 and msg.CanKeyboard_Button_02 == 2:
            finish = True
        elif index == 2 and msg.CanKeyboard_Button_03 == 2:
            finish = True
        elif index == 3 and msg.CanKeyboard_Button_04 == 2:
            finish = True
        elif index == 4 and msg.CanKeyboard_Button_05 == 2:
            finish = True
        elif index == 5 and msg.CanKeyboard_Button_06 == 2:
            finish = True
        elif index == 6 and msg.CanKeyboard_Button_07 == 2:
            finish = True
        elif index == 7 and msg.CanKeyboard_Button_08 == 2:
            finish = True
        elif index == 8 and msg.CanKeyboard_Button_09 == 2:
            finish = True
        elif index == 9 and msg.CanKeyboard_Button_10 == 2:
            finish = True
        elif index == 10 and msg.CanKeyboard_Button_11 == 2:
            finish = True
        elif index == 11 and msg.CanKeyboard_Button_12 == 2:
            finish = True

        if finish:
            print("Button pressed!")
            end_time = ecal_core.getmicroseconds()[1]
            break


    score = end_time - start_time
    return score