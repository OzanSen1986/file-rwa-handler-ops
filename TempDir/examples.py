from pathlib import Path
from os import chdir
from dataclasses import dataclass, field

OS_FILE = Path('config.yaml')
DEST_FILE = Path("vector.csv")

@dataclass
class Vector:
    x: float
    y: float
    z: float

    def __truediv__(self, other: int):
        return Vector(self.x / other, self.y / other, self.z / other)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
def read_file(path: Path, vector: Vector) -> None:
    with path.open("a") as f:
        f.write(f"{vector.x}, {vector.y}, {vector.z}\n")

def main() -> None:
    point1 = Vector(6, 8, 19)
    point2 = Vector(33, 99, 72)
    new_point = (point1 + point2) / 2

    read_file(DEST_FILE, vector=point2)
    read_file(DEST_FILE, vector=new_point)

if __name__ == "__main__":
    main()





