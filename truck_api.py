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


class TruckAPI:

    def __init__(self):
        self.light_pub = ProtoPublisher("W3LightbarRequestPb", W3Lightbar_pb2.W3LightbarRequest)
        self.brake_sub = ProtoSubscriber("BrakeInPb", Brake_pb2.Brake)
        self.sub_steering = ProtoSubscriber("VehicleDynamicsInPb", VehicleDynamics_pb2.VehicleDynamics)
        self.sub_keyboard = ProtoSubscriber("HmiCanKeyboardStatePb", HMICanKeyboard_pb2.HmiCanKeyboardState)

    def lightbar_left_time(self, sleep_time_ms: int):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        pb_msg.turn_signal_left = True
        self.light_pub.send(pb_msg)
        time.sleep(sleep_time_ms / 1000)
        self.lightbar_off()

    def lightbar_right_time(self, sleep_time_ms: int):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        pb_msg.turn_signal_right = True
        self.light_pub.send(pb_msg)
        time.sleep(sleep_time_ms / 1000)
        self.lightbar_off()


    def lightbar_left(self):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        #pb_msg.alley_light_left = True
        pb_msg.turn_signal_left = True
        self.light_pub.send(pb_msg)

    def lightbar_right(self):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        #pb_msg.alley_light_right = True
        pb_msg.turn_signal_right = True
        self.light_pub.send(pb_msg)


    def lightbar_front(self, sleep_time_ms: int):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        pb_msg.take_down = True
        #pb_msg.front_colour_2 = True
        self.light_pub.send(pb_msg)
        time.sleep(sleep_time_ms / 1000)
        self.lightbar_off()

    def lightbar_off(self):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        self.light_pub.send(pb_msg)

    def lightbar_yellow_time(self, time_s: int):
        self.lightbar_yellow()
        time.sleep(time_s)
        self.lightbar_off()

    def lightbar_yellow(self):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        pb_msg.three_sixty_degree_colour_2 = True
        pb_msg.front_colour_2 = True
        self.light_pub.send(pb_msg)

    def lightbar_red_time(self, time_s: int):
        self.lightbar_red()
        time.sleep(time_s)
        self.lightbar_off()
    def lightbar_red(self):
        pb_msg = W3Lightbar_pb2.W3LightbarRequest()
        pb_msg.Clear()
        pb_msg.red_warning_light = True
        self.light_pub.send(pb_msg)



    def reaction_test_brake(self, timeout: int):
        print("Press Brake!")

        start_time = ecal_core.getmicroseconds()[1]
        end_time = start_time + 1000*1000 * timeout

        while ecal_core.ok():
            if ecal_core.getmicroseconds()[1] > end_time:
                break
            ret, msg, time = self.brake_sub.receive(500)
            if msg.signals.is_brake_applied:
                end_time = ecal_core.getmicroseconds()[1]
                break
        score = end_time - start_time
        return score

    def reaction_left_steering(self, timeout: int):
        self.lightbar_left()
        print("Steer left!")

        start_time = ecal_core.getmicroseconds()[1]
        end_time = start_time + 1000*1000 * timeout

        while ecal_core.ok():
            if ecal_core.getmicroseconds()[1] > end_time:
                break
            ret, msg, time = self.sub_steering.receive(500)
            if msg.signals.steering_wheel_angle > 0.2:
                end_time = ecal_core.getmicroseconds()[1]
                break
        score = end_time - start_time
        self.lightbar_off()
        return score


    def reaction_right_steering(self, timeout: int):
        self.lightbar_right()
        print("Steer right!")

        start_time = ecal_core.getmicroseconds()[1]
        end_time = start_time + 1000*1000 * timeout

        while ecal_core.ok():
            if ecal_core.getmicroseconds()[1] > end_time:
                break
            ret, msg, time = self.sub_steering.receive(500)
            if msg.signals.steering_wheel_angle < -0.2:
                end_time = ecal_core.getmicroseconds()[1]
                break
        score = end_time - start_time
        self.lightbar_off()
        return score

    def reaction_button(self, timeout: int):
        print("Press Button")

        start_time = ecal_core.getmicroseconds()[1]
        end_time = start_time + 1000*1000 * timeout

        while ecal_core.ok():
            if ecal_core.getmicroseconds()[1] > end_time:
                break
            ret, msg, time = self.sub_keyboard.receive(500)
            finish = False

            if msg.CanKeyboard_Button_01 == 2:
                finish = True
            elif msg.CanKeyboard_Button_02 == 2:
                finish = True
            elif msg.CanKeyboard_Button_03 == 2:
                finish = True
            elif msg.CanKeyboard_Button_04 == 2:
                finish = True
            elif msg.CanKeyboard_Button_05 == 2:
                finish = True
            elif msg.CanKeyboard_Button_06 == 2:
                finish = True
            elif msg.CanKeyboard_Button_07 == 2:
                finish = True
            elif msg.CanKeyboard_Button_08 == 2:
                finish = True
            elif msg.CanKeyboard_Button_09 == 2:
                finish = True
            elif msg.CanKeyboard_Button_10 == 2:
                finish = True
            elif msg.CanKeyboard_Button_11 == 2:
                finish = True
            elif msg.CanKeyboard_Button_12 == 2:
                finish = True

            if finish:
                print("Button pressed!")
                end_time = ecal_core.getmicroseconds()[1]
                break


        score = end_time - start_time
        return score