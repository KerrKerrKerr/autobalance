if __name__ == '__main__':
    pass
from math import cos,degrees,sqrt
from numpy import square,arccos
class vec:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def mul(self,other):
        return [self.x*other.x,self.y*other.y,self.z*other.z]
    def __add__(self,other):
        return(f'{self.x+other.x} ; {self.y+other.y} ; {self.z+other.z}')
    def __sub__(self,other):
        return(f'{self.x-other.x} ; {self.y-other.y} ; {self.z+-other.z}')
    def __mul__(self,other):
        return (f'{self.x*other.x} ; {self.y*other.y} ; {self.z*other.z}')
    def __truediv__(self, other):
        return (f'{self.x/other.x} ; {self.y/other.y} ; {self.z/other.z}')
    def mod(self):
        return (round(sqrt(square(self.x)+square(self.y)+square(self.z)),9))
    def angle(self, other):
        return round(degrees(  arccos(  (sum(self.mul(other)))  /  (self.mod()*other.mod())  )),6)


v1=vec(-(sqrt(3)),-1,2*(sqrt(2)))
v2=vec(sqrt(3),-1,2*(sqrt(2)))
print(v1.angle(v2))