# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:08:00 2022

@author: hgokc
"""

from dolfin import *
from dolfin_adjoint import *
import moola
import matplotlib.pyplot as plt
import numpy as np
import ufl

img = plt.imread("bert2.PNG")
print(img.shape)
(Nx, Ny, Nz) = img.shape


mesh = UnitSquareMesh(Nx, Ny, "crossed")
V = FunctionSpace(mesh, "DG", 0)

class FE_image(UserExpression):
    def eval_cell(self, value, x, ufc_cell):
        p = Cell(mesh, ufc_cell.index).midpoint()
        i, j, k = int(p[0]*Nx), int(p[1]*Ny), int(p[2]*Nz)
        value[:] = img[-(i+1), j,k]

    def value_shape(self):
        return ()

y = FE_image() # expression
yv = interpolate(y,V)
file = File("png-mesh.pvd");
file << yv

