class Base:
    def _init_(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        return ""

class Circle(Base):
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        super()._init_(x, y, size)

    def shape(self):
        # EXACTLY one newline after "This is a circle"
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
        # No trailing newline
        return "\n".join(lines)

def main():
    c = Circle(1, 2, 3)
    print(c.shape())
main()