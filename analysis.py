import numpy as np

def calculate_area(image_mask):
    white_pixels = np.sum(image_mask == 255)
    pixel_to_m2 = 0.25  # Estimated conversion factor
    return white_pixels * pixel_to_m2

def estimate_solar_output(area_m2, efficiency=0.18):
    return area_m2 * 1000 * efficiency

def estimate_roi(output_kw, cost_per_kw=60000, tariff=6):
    annual_savings = output_kw * 4 * 365 * (tariff / 1000)
    installation_cost = output_kw * cost_per_kw
    return round(installation_cost / annual_savings, 2)
