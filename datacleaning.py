import pandas as pd
import csv

df = pd.read_csv("final..csv")
del df["hyperlink"]
del df["temp_planet_date"]
del df["temp_planet_mass"]
del df["pl_planet_type"]
del df["pl_planet_radius"]
del df["pl_orbital_period"]
del df["pl_eccentricity"]
del df["pl_name"]
del df["pl_nameerr1"]
del df["pl_nameerr2"]
del df["pl_namelim"]
del df["pl_light_years_from_earth"]
del df["pl_light_years_from_eartherr1"]
del df["pl_light_years_from_eartherr2"]
del df["pl_light_years_from_earthlim"]

df = df.rename({
                'pl_hostname': "solar_system_name", 
                'pl_discmethod': "planet_discovery_method", 
                'pl_orbincl': "planet_orbital_inclination", 
                'pl_dens': "planet_type", 
                'ra_str': "planet_radius", 
                'dec_str': "orbital_period", 
                "st_teff": "eccentricity", 
                'st_mass': "name", 
                'st_rad': "light_years_from_earth"
            }, axis='columns')

df.to_csv('main.csv')

