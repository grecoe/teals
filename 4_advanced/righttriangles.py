'''
    Right triangles have some unique properties. You can calculate quite a bit using 
    the pythagorean theorem. 

    1. Determine if a triangle is a right triangle given the length of 
       the three sides.
    2. Find the hypotenuse
    3. Find the length of any missing side 
    4. Calculate the any of the angles that are not the right angle using sin,cos,tan. 

    Calculating angles in a right triangle follows a particular pattern:

    PATTERN: Sohcahtoa

        Soh...      = Sine = Opposite / Hypotenuse
        ...cah...   = Cosine = Adjacent / Hypotenuse
        ...toa      = Tangent = Opposite / Adjacent

              /|<-- 1
           C / | 
            /  |  A
           /   |
      3-->/----- <-- 2
             B

    * C is the hypotenuse

    For this example let B = 2.5 and C(H) = 5
        Expected Angles:
            1 = 30
            2 = 90
            3 = 60
'''
import math

def getHypotenuse(a, b):
    '''
        Theorum says c^2 = a^2 + b^2

        Calculate the hypotenuse with that formula
    '''
    a_squared = a**2
    b_squared = b**2
    hypotenuse_squared = a_squared + b_squared  
    return math.sqrt(hypotenuse_squared)

def getMissingSide(h, a):
    '''
        Also using the theorum, if we know the hypotenuse and one 
        of the sides lengths we can calculate the missing side. 

        c^2 - a^2 = b^2
    '''
    a_squared = a**2
    h_squared = h**2
    missing_side_squared = h_squared - a_squared  
    return math.sqrt(missing_side_squared)

def verifyRightTriangle(side1, side2, side3):
    '''
        Given the three sides of a triangle we can use the 
        theorum to determine if it's a right triangle by calculating
        the hypotenuse and checking if it matches the expected side. 
    '''
    return_value = False
    hypotenuse = None
    if side1 == getHypotenuse(side2, side3):
        return_value = True
        hypotenuse = side1
    elif side2 == getHypotenuse(side1, side3):
        return_value = True
        hypotenuse = side2
    elif side3 == getHypotenuse(side2, side1):
        return_value = True
        hypotenuse = side3
    return {"is_rt" : return_value, "hyp" : hypotenuse }

def _correctDegrees(calc_degrees):
    '''
        Getting odd rounding on angles in floats. So, if angle is 
            XX.000000000
            or
            XX.999999999
        We need to floor or ceil the value
    '''
    return_value = calc_degrees
    int_degrees = int(calc_degrees)
    remainder = calc_degrees - int_degrees
    if remainder > 0.999999999:
        return_value = float(int_degrees + 1)
    elif remainder < 0.000000002:
        return_value = float(int_degrees)
    return return_value

def getAngle(numerator,denominator,angle_function):
    '''
        Calculates the angle. Based on the numerator and denominator
        we calculate either the sin, cos, or tan. 

        Then using the angle_function we can calculate radians. That will be 
        either 
            math.asin, math.acos, math.atan
        
        Then we convert the radians into degrees
    '''
    angle_calc = numerator/denominator
    radians = angle_function(angle_calc)
    degrees = math.degrees(radians)
    return _correctDegrees(degrees)

def getSOH(opposite,hypoteneuse):
    # sin = opp/hypot
    # asin of that gives us radians
    return getAngle(opposite,hypoteneuse,math.asin)

def getCAH(adjacent,hypoteneuse):
    # cos = adj/hypot
    # acos of that gives us radians
    return getAngle(adjacent,hypoteneuse,math.acos)

def getTOA(opposite,adjacent):
    # tan = o/a
    # atan of that gives us radians
    return getAngle(opposite,adjacent,math.atan)

'''
    Lets get our sides sorted
'''
hypotenuse = 5
b = 2.5
a = None

# Get the missing side and verify it
a = getMissingSide(hypotenuse, b)
print("Missing side = ", a)
print("Hypotenuse, expect ", hypotenuse, "got", getHypotenuse(a, b))

# We already know the answer for this set, but is it a right triange?
answer = verifyRightTriangle(a,b,hypotenuse)
print("Is right triange? ", answer["is_rt"], "Hypotenuse = ", answer["hyp"])

# Calculate angle 1 and 3 with sin, cos, tan
print("Calculating Angle 1 = SOH = O/H = b/hypotenuse = ", getSOH(b,hypotenuse))
print("Calulating  Angle 3 = SOH = O/H = a/hypotenuse = ", getSOH(a, hypotenuse))

print("Calulating  Angle 1 = CAH = A/H = a/hypoteneuse = ", getCAH(a, hypotenuse)) 
print("Calulating  Angle 3 = CAH = A/H = b/hypoteneuse = ", getCAH(b, hypotenuse)) 

print("Calulating  Angle 1 = TOA = O/A = b/a = ", getTOA(b, a)) 
print("Calulating  Angle 3 = TOA = O/A = a/b = ",  getTOA(a, b)) 
