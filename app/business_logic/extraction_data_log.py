import re
from datetime import datetime

from app.models.log import Log

class ExtractionDataLog:

    @staticmethod
    def get_Log_intance(log_string):

        date = re.findall(r'^\d+\s\d{1,2}:\d{1,2}:\d{1,2}', log_string)
        
        identificador_server =log_string[18:21]

        mac_addres = re.findall(r'(?:[0-9a-fA-F]:?){16}', log_string)

        description = log_string[42:]

        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', description)

        date_str = str(date[0])
        date_tmp = date_str[0:4] + "-" + date_str[4:6] + "-" + date_str[6:]

        date = datetime.strptime(date_tmp, '%Y-%m-%d %H:%M:%S')

        
        log = Log(
            date=date,
            username="test",
            ip_address=ip[0],
            mac_address=mac_addres[0],
            description=description
        )

        return log 
