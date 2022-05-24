from dolfin import *

img = plt.imread("bertoldi.PNG")
print(img.shape)
(Nx, Ny, Nz) = img.shape

mesh = UnitSquareMesh(Nx, Ny, "crossed")
V = FunctionSpace(mesh, "DG", 0)


class FE_image(UserExpression):
    def eval_cell(self, value, x, ufc_cell):
        p = Cell(mesh, ufc_cell.index).midpoint()
        i, j, k = int(p[0] * Nx), int(p[1] * Ny), int(p[2] * Nz)
        value[:] = img[-(i + 1), j, k]

    def value_shape(self):
        return ()


def H(a):
    return 0.5 * (1 + a / (0.1 + abs(a)))


y = FE_image()  # expression 
yv = project(H(y - 0.5), V)
file = File("png-mesh.pvd");
file << yv
