import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def kinematic_wave(L, dx, dt, h0, q0, h_boundary, q_boundary):
    n = int(L / dx)  # Number of grid cells
    q = np.zeros(n)  # Discharge (m3/s)
    h = np.zeros(n)  # Water depth (m)
    z = np.linspace(0, L, n)  # Elevation (m)

    # Define initial conditions
    h[0] = h0  # Water depth at upstream boundary (m)
    q[0] = q0  # Discharge at upstream boundary (m3/s)

    # Define kinematic wave equation
    for i in range(1, n):
        q[i] = q[i-1] + dt/dx * (h[i-1]**(5/3) - h[i]**(5/3))
        h[i] = h[i-1] + dt/dx * (q[i-1] - q[i])

        # Apply boundary conditions
        if i == n-1:
            q[i] = q_boundary
            h[i] = h_boundary

    # Plot results
    plt.plot(z, h)
    plt.xlabel('Distance (m)')
    plt.ylabel('Water depth (m)')
    plt.title('Kinematic Wave Equation')
    st.pyplot()

# Define the Streamlit app
st.title('Kinematic Wave Equation')

# Define input parameters
L = st.slider('Length of river (m)', 1000, 10000, 5000, step=100)
dx = st.slider('Grid spacing (m)', 10, 500, 100, step=10)
dt = st.slider('Time step (s)', 60, 3600, 600, step=60)
h0 = st.slider('Initial water depth at upstream boundary (m)', 0.0, 2.0, 1.0, step=0.1)
q0 = st.slider('Initial discharge at upstream boundary (m3/s)', 0.0, 2000.0, 10.0, step=1.0)
h_boundary = st.slider('Water depth at downstream boundary (m)', 0.0, 2.0, 0.5, step=0.1)
q_boundary = st.slider('Discharge at downstream boundary (m3/s)', 0.0, 1000.0, 0.0, step=1.0)

# Run the kinematic wave equation and display the results
if st.button('Run Kinematic Wave Equation'):
    kinematic_wave(L, dx, dt, h0, q0, h_boundary, q_boundary)
