
from app.business_logic.extraction_data_log import ExtractionDataLog

fake_logs = [
        "20140616 05:42:52 vm5 [4f8a7f94:533e226f] sshd transport algorithms: direction=client->server cipher=aes128-ctr mac=hmac-sha1 compression=none 10.10.10.1",
        "20140616 05:42:54 vm5 [4f8a7f94:533e226f] ag_userd Looking for account source for 'root'",
        "20140616 05:42:54 vm5 [4f8a7f94:533e226f] ag_userd User 'root' was not found"
    ]

def test_extraction_data():
    log = fake_logs[0]

    log_instance = ExtractionDataLog.get_Log_intance(log)

    print (log_instance)



