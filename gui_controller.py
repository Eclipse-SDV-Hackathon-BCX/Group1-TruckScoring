from PySide2.QtCore import QObject, Property, Signal


class Controller(QObject):
    _driver_name = "Shawn"
    _score = 0
    _task = "Starting..."

    show_positive_change = Signal(int, arguments=['change'])
    show_negative_change = Signal(int, arguments=['change'])

    def get_driver_name(self):
        return self._driver_name

    def set_driver_name(self, new_driver_name: str):
        self.driver_name = new_driver_name
        self.dn_changed.emit()

    @Signal
    def dn_changed(self):
        pass

    def get_score(self):
        return str(self._score).zfill(3)

    def set_score(self, new_score: int):
        self._score = new_score
        self.s_changed.emit()

    @Signal
    def s_changed(self):
        pass

    def get_task(self):
        return self._task

    def set_task(self, new_task: str):
        self._task = new_task
        self.t_changed.emit()

    @Signal
    def t_changed(self):
        pass

    driver_name = Property(str, get_driver_name, set_driver_name, notify=dn_changed)
    score = Property(str, get_score, set_score, notify=s_changed)
    task = Property(str, get_task, set_task, notify=t_changed)
