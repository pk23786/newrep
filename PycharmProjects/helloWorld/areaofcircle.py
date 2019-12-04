from math import pi
class circle():
    def __init__(self,radius):
        self.radius=radius

    def display(self):
        print("radius is :{0}".format(self.radius))
        area=2*pi*self.radius
        parameter=pi*self.radius**2
        print("the area of circle is :{0}".format(area))
        print("the parameter of circle is :{0}".format(parameter))

def main():
    print("enter the radius:")
    radius=int(input())
    obj=circle(radius)
    obj.display()
if __name__ == '__main__':
    main()

