import numpy as np

def scale_values(old_value, new_max=1.0, new_min=0.2):
    """Scales old values to fit between a new range """
    
    old_min = np.min(old_value)
    old_range = np.max(old_value) - np.min(old_value)
    new_range = new_max - new_min

    return (((old_value - old_min) * new_range) / old_range) + new_min
    