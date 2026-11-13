
class Rectangle:
    """A class representing a Rectangle with width and height."""
    
    def __init__(format_self_placeholder, width, height):
        # سنستخدم self بدلاً من format_self_placeholder للتوضيح القياسي
        pass

class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Returns True if width equals height, False otherwise."""
        return self.width == self.height

    def __str__(self):
        """Returns string representation like 'Rectangle 4 x 3'."""
        return f"Rectangle {self.width} x {self.height}"


if __name__ == "__main__":
    print("=== Testing Rectangle Class ===")
    
    # 1. إنشاء كائنات صحيحة وتجربة الدوال
    r1 = Rectangle(4, 3)
    r2 = Rectangle(5, 5)
    
    print(r1)  # Rectangle 4 x 3
    print("Area of r1:", r1.area())
    print("Perimeter of r1:", r1.perimeter())
    print("Is r1 a square?:", r1.is_square())
    
    print("-" * 30)
    
    print(r2)  # Rectangle 5 x 5
    print("Is r2 a square?:", r2.is_square())

    print("-" * 30)

    # 2. تجربة إجراء خاطئ داخل try / except ValueError
    try:
        r_invalid = Rectangle(-2, 4)
    except ValueError as e:
        print("Caught expected ValueError:", e)