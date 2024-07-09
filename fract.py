class Fractions:
    def __init__(self , n , d):
        self.num = n
        self.den = d
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self , other):
        temp_den = self.den * other.den
        temp_num = (self.num * other.den) + (self.den * other.num)

        return f"{temp_num}/{temp_den}"
    
    def __sub__(self , other):
        temp_den = self.den * other.den
        temp_num = (self.num * other.den) - (self.den * other.num)

        return f"{temp_num}/{temp_den}"

    def __mul__(self , other):
        temp_den = self.den * other.den
        temp_num = self.num * other.num

        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self , other):
        temp_den = self.den * other.num
        temp_num = self.num * other.den

        return f"{temp_num}/{temp_den}"
    
