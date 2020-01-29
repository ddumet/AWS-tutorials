import pymysql
import pandas as pd

if __name__ == '__main__':

    # Read from local .csv file
    meteo_dataset = "./sunlab-faro-meteo-2017-extract-100-obs.csv"
    df_meteo = pd.read_csv(meteo_dataset,sep=";")

    # Configure our DB connection
    # Change the value below according to your data
    host="database-1.chpvivqevrkc.us-east-1.rds.amazonaws.com"
    port=3306
    dbname="db1"
    user="didier"
    password="didier"

    # Connect to the DB
    connection = pymysql.connect(host,
        user=user,
        port=port,
        passwd=password,
        db=dbname)
    cursor=connection.cursor()

    for i,row in df_meteo.iterrows():

        # Loop through all rows of the df_meteo DataFrame and insert all
        # rows in DB
        sql1 = "INSERT INTO observations (obs_date,temperature, global_rad, diffuse_rad, ultraviolet, wind_velocity, wind_direction, precipitation, atm_pressure) VALUES ('{0}',{1},{2},{3},{4},{5},{6},{7},{8})".format(row["Datetime"],
            row["Ambient Temperature [ºC]"],row["Global Radiation [W/m2]"],row["Diffuse Radiation [W/m2]"],row["Ultraviolet [W/m2]"],
            row["Wind Velocity [m/s]"],row["Wind Direction [º]"], row["Precipitation [mm]"], row["Atmospheric pressure [hPa]"])
        cursor.execute(sql1)
    
        # the connection is not autocommitted by default, so we must commit to save our changes
        connection.commit()

    # Closing connection to DB
    connection.close()
