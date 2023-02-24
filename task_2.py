class Road:
    mass = 50
    thickness = 0.1

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * self.mass * self.thickness
        if mass >= 1000:
            return f"Road mass = {mass / 1000} t."
        return f"Road mass = {mass} kg."


new_road = Road(500, 30)
print(new_road.calc_mass())

new_road2 = Road(10, 10)
print(new_road2.calc_mass())
