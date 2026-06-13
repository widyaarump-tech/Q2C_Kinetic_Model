import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
Vmax = 5.0
Km = 2.0
Ki = 3.0
X = 10
k2 = 1.0
k3 = 0.8
k4 = 0.3

def model(y, t):
    A, B, P = y

    # Flux equations
    v1 = (Vmax * X) / ((Km + X) * (1 + P / Ki))
    v2 = k2 * A
    v3 = k3 * B
    v4 = k4 * A

    # ODEs
    dAdt = v1 - v2 - v4
    dBdt = v2 - v3
    dPdt = v3

    return [dAdt, dBdt, dPdt]

# Initial conditions: [A, B, P]
y0 = [0, 0, 0]

# Time points
t = np.linspace(0, 20, 200)

# Solve ODEs
solution = odeint(model, y0, t)

A = solution[:, 0]
B = solution[:, 1]
P = solution[:, 2]

# Plot simulation result
plt.figure(figsize=(8, 5))
plt.plot(t, A, label="A")
plt.plot(t, B, label="B")
plt.plot(t, P, label="P")

plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("Simulation of Metabolic Pathway with Feedback Inhibition")
plt.legend()
plt.grid(True)

plt.savefig("q2c_simulation_plot.png", dpi=300, bbox_inches="tight")
plt.show()
