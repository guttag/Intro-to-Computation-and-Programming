# -*- coding: utf-8 -*-

# # Figure 7-1 on page 136
pi = 3.14159

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius

def sphere_surface(radius):
    return 4.0*area(radius)

def sphere_volume(radius):
    return (4.0/3.0)*pi*(radius**3)

