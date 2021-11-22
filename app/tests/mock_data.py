from ..models.register_log import RegisterFormat
class MockDataDb:

    def query_data_metrics_log():
        query = [
            {
                "id": 1,
                "date": "2021-10-01",
                "username": "joed",
                "mac_address": "mac1",
                "ip_address": "192.0.0.1",
                "description": "error consult server",
            },
            {
                "id": 2,
                "date": "2021-10-01",
                "username": "joed",
                "mac_address": "mac1",
                "ip_address": "192.0.0.1",
                "description": "loguin test consult server",
            },
            {
                "id": 3,
                "date": "2021-10-02",
                "username": "guad",
                "mac_address": "mac2",
                "ip_address": "192.0.0.10",
                "description": "loguin test consult server",
            },
            {
                "id": 4,
                "date": "2021-10-03",
                "username": "guad",
                "mac_address": "mac2",
                "ip_address": "192.0.0.10",
                "description": "loguin test consult server",
            }
        ]

        result =[RegisterFormat(**x)for x in query]

        return result

    def data_test_db():

        result = [
            {
                "id": 1,
                "IsUserKnown": False,
                "IsClientKnown": False,
                "IsIPKnown": False,
                "IsIPInternal": False,
                "LastSuccessfulLoginDate": "2021-10-10",
                "LastFailedLoginDate": "2021-10-10",
                "FailedLoginCountLastWeek": 10,
            }
        ]
        return result