class Car:
    def __init__(self, color, vin):
        self.color = color
        self._is_on = False
        self.__vin_number = vin
    @property
    def is_off(self):
        print('call the is_on getter')
        return not self._is_on

    @is_off.setter
    def is_off(self, off_value):
        if not isinstance(off_value, bool):
            raise ValueError("value should be boolean")
        print('call the is_on setter')
        self._is_on = not off_value

    @is_off.deleter
    def is_off(self):
        print("call the is_on deleter")
        self._is_on = None
        
    def set_vin(self, vin_num):
        self.__vin_number = vin_num
    def get_vin(self):
        print(self.__vin_number)
    def set_is_on(self, is_on):
        self._is_on = is_on
    def start(self):
        self._is_on = True
    def on_status(self):
        return self._is_on

