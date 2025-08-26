import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from scipy.signal import savgol_filter


data = pd.read_csv("Raw_Test_Flight_Data_25.csv", skiprows=1)
time = data["time"].to_numpy()
pressure= data["Pressure(Pa)"].to_numpy()


SEA_LEVEL_PRESSURE = 101325      
SEA_LEVEL_TEMP = 288.15         
GRAVITY = 9.80665               
MOLAR_MASS = 0.0289644          
GAS_CONST = 8.3144598            


# Pressure -> Altitude 
alt = (SEA_LEVEL_TEMP / (GRAVITY * MOLAR_MASS / GAS_CONST)) * np.log(SEA_LEVEL_PRESSURE / p)

# Smooth altitude 
altitude_smooth = savgol_filter(alt, window_length=11, polyorder=3)

vel = np.gradient(altitude_smooth, t)

#Plot
fig, (ax_alt, ax_vel) = plt.subplots(2, 1, figsize=(8, 8))

ax_alt.set(title="Altitude vs Time", xlabel="Time (s)", ylabel="Altitude (m)")
ax_vel.set(title="Velocity vs Time", xlabel="Time (s)", ylabel="Velocity (m/s)")

alt_line, = ax_alt.plot([], [], "b-", lw=2)
vel_line, = ax_vel.plot([], [], "r-", lw=2)

# Limits
ax_alt.set_xlim(t.min(), t.max())
ax_alt.set_ylim(altitude_smooth.min() - 10, altitude_smooth.max() + 10)
ax_vel.set_xlim(t.min(), t.max())
ax_vel.set_ylim(vel.min() - 5, vel.max() + 5)

# Animate
def animate(i):
    alt_line.set_data(t[:i], altitude_smooth[:i])
    vel_line.set_data(t[:i], vel[:i])
    return alt_line, vel_line

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=False)

plt.tight_layout()
plt.show()