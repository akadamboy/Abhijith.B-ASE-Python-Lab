from graphics import circle, rectangle
from graphics.threeDgraphics import cuboid
from graphics.threeDgraphics.sphere import area as sphere_area
from graphics.threeDgraphics.sphere import perimeter as sphere_perimeter

print(rectangle.area(10, 50))
print(rectangle.perimeter(10, 50))

print(circle.area(10))
print(circle.perimeter(10))

print(cuboid.area(2, 3, 5))
print(cuboid.perimeter(2, 3, 5))

print(sphere_area(25))
print(sphere_perimeter(25))