# A user can create and view 2D Coordinates
# A user can find out the distance between 2 coordinates
# A user can find the distannce of a Coordinate from Origin
# A user can check if apoint lies on a given line
# A user can find the distance between a given 2D point and a given line


class Point:

    def __init__(self,x,y):
        self.xCod = x
        self.yCod = y

    def __str__(self):
        return '<{},{}>'.format(self.xCod,self.yCod)


#    |`````````2```````````2````````````
#   \| (x2 -x1) +  (y2 -y1)

    def euclidean_distance(self,other):
        return ((self.xCod - other.xCod)**2 + (self.yCod - other.yCod)**2)*0.5

    def distance_from_origin(self):
        #return (self.xCod**2 + self.yCod**2)**0.5
        return self.euclidean_distance(Point(0,0))  # we can use the euclidean_distance method to find the distance from origin



#  Ax + By + C = 0

class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
    # def distance_from_point(self,point):
    #     return self.A* point.xCod + self.B*point.yCod + self.C

    def point_on_line(line,point):
        if line.A * point.xCod + line.B * point.yCod * line.C == 0:
            return 'lies on the line'
        else:
            return 'Does not lie on the line'

    # Calculate the shortest Distance between Line and point
    #     | Ax1 +By1 +C|
    #  d= ---------------
    #     |--------------
    #    \| A**2 + B**2
    # 

    def shortest_distance(line,point):
        return abs(line.A * point.xCod + line.B * point.yCod + line.C) / (line.A **2 + line.B**2)*0.5


    # Line intersect each other

    def line_intersect(line1,line2):
        x = (line1.B * line2.C - line2.B * line1.C)/(line1.A*line2.B - line2.A*line1.B)
        y = (line1.C * line2.A - line2.C * line1.A)/(line1.A*line2.B - line2.A*line1.B)
        return '{}/{}'.format(x,y)

# obj = Point(0,0)
# obj2 = Point(3,4)
# print(obj)   # with the help of __str__ we are able to see the o/p format  
#              # otherwise it will show the memory location         
# print(obj2)
# print(obj.euclidean_distance(obj2))   # first obj is the current object which is auto send as 1st parameter and
#                                       # obj2 is the other object which is passed as an argument that can send as a 2nd parameter

# print(obj.distance_from_origin())

# obj3 = Line(2,2,-4)
# obj4 = Point(1,1)

# obj5 = Point(2,3)
# print(obj3)
# print(obj4)

# print(obj3.point_on_line(obj4))

# print(obj3.shortest_distance(obj4))

# print(obj3.shortest_distance(obj5))

obj11 = Line(5,1,1)
obj12 = Line(2,6,2)

print(obj11.line_intersect(obj12))