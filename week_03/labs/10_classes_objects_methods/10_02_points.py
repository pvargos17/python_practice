'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''
import math
class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """


def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))




def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

class Rectangle:
    """Represents a rectangle
    attributes: width, height, corner
    """
def find_center(rect):

    """ Returns a Point at the center of a rectangle

    rect : Rectangle

    return: new Point

    """
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def moved_rectangle(rect, dx, dy):

  """Move the Rectangle by modifying its corner object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).
    """
    rect.corner.x += dx
    rect.corner.y += dy
def move_rectangle_copy(rect, dx, dy):
    """Move the Rectangle and return a new Rectangle object.

    rect: Rectangle object.
    dx: change in x coordinate (can be negative).
    dy: change in y coordinate (can be negative).

    returns: new Rectangle
    """
    new = copy.deepcopy(rect)
    move_rectangle(new, dx, dy)
    return new




def main():
       blank = Point()
    blank.x = 0
    blank.y = 0

    grosse = Point()
    grosse.x = 3
    grosse.y = 4

    print('distance', end=' ')
    print(distance_between_points(grosse, blank))

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)
    print('move')
    move_rectangle(box, 50, 100)
    print(box.corner.x)
    print(box.corner.y)

    new_box = move_rectangle_copy(box, 50, 100)
    print(new_box.corner.x)
    print(new_box.corner.y)
