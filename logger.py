from influxdb import InfluxDBClient
from settings import *
import pandas as pd
class Logger:
    def __init__(self):
        self.ip = ip_adress
        self.port = port
        self.name_db = name_data_base
        self.log = InfluxDBClient(host = self.ip, port = self.port)
        self.path_log = path_log
    def create_data_frame(self, columns=['time', 'player_x', 'player_y', 'ball_id', 'ball_x', 'ball_y']):
        self.df = pd.DataFrame(columns=columns)
    def create_data_base(self):
        self.log.create_database(self.name_db)
        self.log.switch_database(self.name_db)
    def log_to_excel(self):
        self.df.to_excel(self.path_log)
    def log_to_data_frame(self, time, player, ball):
        try:
            self.df.loc[len(self.df)] = [time, player.x, player.y, ball.id, ball.x, ball.y]
        except ValueError:
            self.df.loc[len(self.df)] = [time, player.x, player.y, 0, 0, 0]
    def log_to_data_base(self, player_pos, time ):
        data_body = [
            {
                "measurement": "coordinates on the field",
                "tags": {
                    "Id": 1#camera_id
                },
                "time": time,
                "fields": {
                    "x": player_pos[0],
                    "y": player_pos[1]
                }
            }
        ]
        self.log.write_points(data_body)