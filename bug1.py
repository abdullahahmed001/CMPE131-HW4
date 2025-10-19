# TODO: there's code missing in one or more lines below
class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        return ""

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def shape(self):
        return "This is a circle\n" + self.draw()

    def draw(self):
        lines = [
            f"({self.x}, {self.y})",
            f"{self.size}",
            "         , - ~ ~ ~ - ,",
            "     , '               ' ,",
            "   ,                       ,",
            "  ,                         ,",
            " ,                           ,",
            " ,                           ,",
            " ,                           ,",
            "  ,                         ,",
            "   ,                       ,",
            "     ,                  , '",
            "       ' - , _ _ _ ,  '"
        ]
        return "\n".join(lines).rstrip()


def main():
    c = Circle(1, 2, 3)
    print(c.shape())

main()