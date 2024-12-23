import numpy as np

def dynamic_equations(lift, drag, side_force, mass, u, v, w, p, q, r):
    """
    Compute the translational accelerations of the UAV based on the dynamic equations of motion.
    
    Parameters:
    - lift: NumPy array of lift forces (N)
    - drag: NumPy array of drag forces (N)
    - side_force: NumPy array of side forces (N)
    - mass: Mass of the UAV (kg)
    - u, v, w: Body-frame velocity components (m/s) along the x, y, and z axes (scalars or arrays)
    - p, q, r: Angular rates (rad/s) around the x, y, and z axes (scalars or arrays)
    
    Returns:
    - accel_x: Acceleration along the x-axis (forward) in body frame (m/s^2)
    - accel_y: Acceleration along the y-axis (lateral) in body frame (m/s^2)
    - accel_z: Acceleration along the z-axis (vertical) in body frame (m/s^2)
    """
    
    # Translational dynamics (forces):
    # F_x = m * (du/dt + qw - rv)  -> acceleration along x-axis
    # F_y = m * (dv/dt + ru - pw)  -> acceleration along y-axis
    # F_z = m * (dw/dt + pv - qu)  -> acceleration along z-axis
    
    # Compute the accelerations in the body frame using the forces
    accel_x = (lift - drag) / mass + (q * w - r * v)
    accel_y = side_force / mass + (r * u - p * w)
    accel_z = -lift / mass + (p * v - q * u)
    
    return accel_x, accel_y, accel_z
