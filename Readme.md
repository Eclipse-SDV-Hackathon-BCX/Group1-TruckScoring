# Gamification Backend + Frontend for eCAL

This is one of our repos for the first challenge. The application uses eCAL to receive data from the truck, the Carla
simulation backend and the gas pedal sensor. Points are then rewarded, or deducted, based on the driving behaviour.
The score is displayed through a QT GUI.

## Files

`gui_controller.py` contains most of the python GUI logic. `truck_api.py` contains most of the eCAL integration to read
data from the truck, the Carla backend and write to the lightbar. The `main.py` contains most of the decision making
and instantiation.