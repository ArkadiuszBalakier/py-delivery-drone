from app.drone.base_robot import BaseRobot


class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords = None):
        if coords is None:
            coords = [0,0,0]
        if len(coords) == 2:
            coords.append(0)
        super().__init__(name, weight, coords)

    def go_up(self, step: int = 1) -> None:
        self.coords[2] += step

    def go_down(self, step: int = 1) -> None:
        self.coords[2] = self.coords[2] - step