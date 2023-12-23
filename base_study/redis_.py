import multiprocessing

from redis import StrictRedis


class RedisTool():

    def __init__(self, host, port, db):
        self.conn = None
        self.port = port
        self.host = host
        self.db = db
        self.connet()

    def connet(self):
        self.conn = StrictRedis(host=self.host, port=self.port, db=self.db, password='')
        return self.conn

    def set(self, key, value):
        self.conn.set(key, value)

    def get(self, key, ):
        return self.conn.get(key)


def run():
    db_0 = RedisTool(host='localhost', port=6379, db=0)
    for i in range(9999999999999999999):
        db_0.set(f"第{i}个数", f"==={i}")
        print(db_0.get(f"第{i}个数"))


if __name__ == "__main__":
    run()
