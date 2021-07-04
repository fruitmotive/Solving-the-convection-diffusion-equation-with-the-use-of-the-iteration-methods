import numpy as math
import matplotlib.pyplot as plt
nx, nt = map(int, input('net dim: ').split()) 
xs, xe = map(int, input('x set: ').split()) 
ts, te = map(int, input('t set: ').split()) 
eps = float((input('e: ')))
solution = math.zeros((nx, nt), dtype=float)     
netx, nett = math.linspace(xs, xe, nx), math.linspace(ts, te, nt) 
h, tau = float(xe - xs)/(nx - 1), float(te - ts)/(nt - 1) 
solution[0, :], solution[:, 0] = 0, netx 
def itfoo(v, d, l, dl): 
    return (v - d)/(2*tau) + (l - dl)/(2*tau) + (math.arctan(d) - math.arctan(dl))/(2*h) + (math.arctan(v) - math.arctan(l))/(2*h)
def ditfoo(v): 
    return 1/(2*tau) + 1/(2*h*(1 + v**2)) 
def iterator(d, l, dl): 
    e = eps + math.inf
    value = dl
    while e > eps:
        aux = value
        value = aux - itfoo(aux, d, l, dl)/ditfoo(aux)
        e = abs(aux - value)
    return value
for i in range(1, nx): 
    for j in range(1, nt):
        solution[i, j] = iterator(solution[i - 1, j], solution[i, j - 1], solution[i - 1, j - 1])
ax = plt.axes(projection="3d") 
T, X = math.meshgrid(nett, -netx)
ax.plot_surface(X, T, solution, cmap='plasma')
plt.xlabel("X")
plt.ylabel("T")
plt.savefig("graphresh.jpeg", dpi=400)

