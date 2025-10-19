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

    def shape(self, header=False):
        # Include header only if header=True
        if header:
            return "This is a circle\n" + self.draw()
        else:
            return self.draw()
    def draw(self):
        return f"""({self.x}, {self.y})
{self.size}
         , - ~ ~ ~ - ,
     , '               ' ,
   ,                       ,
  ,                         ,
 ,                           ,
 ,                           ,
 ,                           ,
  ,                         ,
   ,                       ,
     ,                  , '
       ' - , _ _ _ ,  '
               """

def main():
    c = Circle(1, 2, 3)
    print(c.shape(header=True))

main()