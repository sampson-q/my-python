# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:37:59 2021

@author: Hash
"""
import numpy as npy

# fetching L from user
beamLength = input('Enter Beam of Lenght in Meters: ')
# typecasting L into an integer
beamLength = int(beamLength)
# fetching w from user :: and typecasted into integer straight forward
loadIntensity = int(input('Enter Load Intensity in kN/m: '))
print()

# Bending moment at x = 0
def M_at_x0():
    x = 0
    bendMoment = (loadIntensity * (-6 * x ** 2) + (6 * beamLength * x) - (beamLength ** 2)) / 12
    print('Bending Moment at x = 0: {}'.format(bendMoment))
    print()

# bending moment at x = L
def M_at_xL():
    x = beamLength
    bendMoment = (loadIntensity * (-6 * x ** 2) + (6 * beamLength * x) - (beamLength ** 2)) / 12
    print('Bending Moment at x = L: {}'.format(bendMoment))
    print()
    
# shear force at x = 0
def V_at_x0():
    x = 0
    shearForce = loadIntensity * ((beamLength / 2) - x)
    print('Shear Force at x = 0: {}'.format(shearForce))
    print()
    
# shear force at x = L
def V_at_xL():
    x = loadIntensity
    shearForce = loadIntensity * ((beamLength / 2) - x)
    print('Shear Force at x = L: {}'.format(shearForce))
    print()

def M0_distance():
    bendMoment = 0
    distance0 = (beamLength / 2) - npy.sqrt()
    distance3 = 'hello'