class BaseRobot:
    def __init__(self, name: str, weight: float, coords: list[int] = [0,0]) -> None:
        self.name = name
        self.weight = weight
        self.coords = coords

    def go_forward(self, step: int = 1) -> None:
        self.coords[1] += step

    def go_back(self, step: int = 1) -> None:
        self.coords[1] -= step

    def go_left(self, step: int = 1) -> None:
        self.coords[0] -= step

    def go_right(self, step: int = 1) -> None:
        self.coords[0] += step

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"