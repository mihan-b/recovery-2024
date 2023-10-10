import math

# Constants
g = 9.80665

# Inputs
dry_mass_kg = 15.778
rocket_length_m = 2.73
parachute_cd = 0.97
apogee_m = 3600
launch_alt_m = 1401

main_velocity_ms = 5
drogue_velocity_ms = 30
main_deploy_alt_m = 100
drogue_deploy_alt_m = apogee_m
main_air_density_kgm3 = (-(((((main_deploy_alt_m/2)) + launch_alt_m)/1000)-44.3308)/42.2665) ** (7418/1743)
drogue_air_density_kgm3 = (-((((((drogue_deploy_alt_m + main_deploy_alt_m)/2)) + launch_alt_m)/1000)-44.3308)/42.2665) ** (7418/1743)

#main_volume_m3 = 
#drogue_volume_m3 = 

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

# Prints
print(f'Shockcord length\t{round(shockcord_length_ft)} ft')
print(f'Main diameter\t\t{round(main_diameter_ft)} ft')
print(f'Drogue diameter\t\t{round(drogue_diameter_ft)} ft')