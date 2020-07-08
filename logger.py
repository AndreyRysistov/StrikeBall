from influxdb import InfluxDBClient
from settings import *
import pandas as pd


class Logger:
    """
    Class that implements the logging mechanism. Supports two ways of logging data: saving data to the influexdb database
    and saving data to the pandas dataframe and then saving it to an xslx file
    The class has the following attributes:
        ip-the IP address or url of the database
        port-port for connecting to the database
        name_db-name of the database
        client-an object of the InfluexDBClient class that implements mechanisms for interacting with the database
        path_log-path to save the xlsx file
    The class has the following methods:
        create_data_frame-creates a data frame for storing coordinates and time
        create_data_base-creates a database for storing coordinates and time
        log_to_excel-saves data to an xslx file at the specified path
        log_to_data_frame-saves data to a data frame
        log_to_data_base-saves data to the database
    """

    def __init__(self):
        self.ip = ip_adress
        self.port = port
        self.name_db = name_data_base
        self.client = InfluxDBClient(host=self.ip, port=self.port)
        self.path_log = path_log

    def create_data_frame(self, columns=['time', 'player_x', 'player_y', 'ball_id', 'ball_x', 'ball_y']):
        self.df = pd.DataFrame(columns=columns)

    def create_data_base(self):
        try:
            self.client.create_database(self.name_db)
            self.client.switch_database(self.name_db)
        except:
            print(f'Database {self.name_db} can not be created')

    def log_to_excel(self):
        try:
            self.df.to_excel(self.path_log)
        except:
            print(f'Path {self.path_log} is not exist')

    def log_to_data_frame(self, time, player, ball):
        try:
            self.df.loc[len(self.df)] = [time, player.x, player.y, str(ball.id) + 'id', ball.x, ball.y]
        except ValueError:
            self.df.loc[len(self.df)] = [time, player.x, player.y, 0, 0, 0]

    def log_to_data_base(self, player_pos, time):
        data_body = [
            {
                "measurement": "coordinates on the field",
                "tags": {
                    "Id": 1  # camera_id
                },
                "time": time,
                "fields": {
                    "x": player_pos[0],
                    "y": player_pos[1]
                }
            }
        ]
        try:
            self.client.write_points(data_body)
        except:
            print(f'Can not write data in database')
