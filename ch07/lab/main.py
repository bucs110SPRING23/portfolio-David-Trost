from Rectangle import Rectangle
from Surface import Surface

def main():
    self = Rectangle(10, 10, 10, 10)
    assert((self.x, self.y, self.height, self.width) == (10,10,10,10))
    
    self = Rectangle(-1, 1, 1, 1)
    assert((self.x, self.y, self.height, self.width) == (1,1,1,1))
    
    self= Rectangle(1, -5, 1, 1)
    assert((self.x, self.y, self.height, self.width) == (1,5,1,1))
    
    self= Rectangle(1, 1, -10, 1)
    assert((self.x, self.y, self.height, self.width) == (1,1,10,1))
    
    self = Rectangle(1, 1, 1, -1000)
    assert((self.x, self.y, self.height, self.width) == (1,1,1,1000))

    print("Rectangle tests passed")

if __name__ == '__main__':
    main()




s=Surface("Saul.jpg",10,10,10,10)
assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
srect = s.getRect()
assert((srect.x,  s.getRect().y, srect.height,  srect.width) == (10,10,10,10))
print("Test Complete!")