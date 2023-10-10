import math

# Constants
g = 9.80665

# Inputs
dry_mass_kg = 15.778
rocket_length_m = 2.73
parachute_cd = 0.97
apogee_m = 3600
launch_alt_m = 1401
inner_diameter_m = 0.123952
inner_area_m2 = math.pi * ((inner_diameter_m/2) ** 2)

main_velocity_ms = 5
drogue_velocity_ms = 30
main_deploy_alt_m = 100
drogue_deploy_alt_m = apogee_m
main_air_density_kgm3 = (-(((((main_deploy_alt_m/2)) + launch_alt_m)/1000)-44.3308)/42.2665) ** (7418/1743)
drogue_air_density_kgm3 = (-((((((drogue_deploy_alt_m + main_deploy_alt_m)/2)) + launch_alt_m)/1000)-44.3308)/42.2665) ** (7418/1743)

main_volume_m3 = 0.011
drogue_volume_m3 = 0.0023

num_shear_pins = 8
shear_pin_force_N = 170.5
rc_mK = 12.16
t_K = 1739

# Parachute size
main_area_ms2 = (2 * g * dry_mass_kg)/(parachute_cd * main_air_density_kgm3 * (main_velocity_ms ** 2))
drogue_area_ms2 = (2 * g * dry_mass_kg)/(parachute_cd * drogue_air_density_kgm3 * (drogue_velocity_ms ** 2))
main_diameter_m = 2 * math.sqrt(main_area_ms2/math.pi)
drogue_diameter_m = 2 * math.sqrt(drogue_area_ms2/math.pi)
main_diameter_ft = main_diameter_m * 3.2084
drogue_diameter_ft = drogue_diameter_m * 3.2084

# Shockcord
shockcord_length_m = rocket_length_m * 3
shockcord_length_ft = shockcord_length_m * 3.2084

# Blackpowder
shear_pin_pressure_Pa = num_shear_pins * shear_pin_force_N / inner_area_m2
main_bp_mass_g = (shear_pin_pressure_Pa * main_volume_m3) / (rc_mK * t_K * g) * 1000
main_bp_mass_oz = main_bp_mass_g / 28.35
drogue_bp_mass_g = (shear_pin_pressure_Pa * drogue_volume_m3) / (rc_mK * t_K * g) * 1000
drogue_bp_mass_oz = drogue_bp_mass_g / 28.35

# Prints
print('\nDimension\t\tMetric\tImperial')
print('----------------------------------------')
print(f'Shockcord length\t{round(shockcord_length_m)} m\t{round(shockcord_length_ft)} ft')
print(f'Main diameter\t\t{round(main_diameter_m)} m\t{round(main_diameter_ft)} ft')
print(f'Drogue diameter\t\t{round(drogue_diameter_m)} m\t{round(drogue_diameter_ft)} ft')
print(f'Main blackpowder\t{round(main_bp_mass_g, 2)} g\t{round(main_bp_mass_oz, 3)} oz')
print(f'Drogue blackpowder\t{round(drogue_bp_mass_g, 2)} g\t{round(drogue_bp_mass_oz, 3)} oz')
print('\n')