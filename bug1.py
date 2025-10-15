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

    def shape(aShape):
        print(aShape.draw())

    def draw(self):
        return f"""This is a circle
({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
    , '               ' ,
  ,                      ,
 ,                        ,
,                          ,
,                          ,
,                          ,
 ,                        ,
  ,                      ,
    ,                 , '
      ' - , _ _ _ , '
        """

def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())

main()
