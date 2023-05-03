import psycopg2
import configparser


class DB_Saver():
    """Отвечает за сохранение и удаление данных в БД"""

    def connect_to_db(self, config_file="config.ini"):
        config = configparser.ConfigParser()
        config.read(config_file)
        host = config['postgresql']['host']
        port = config['postgresql']['port']
        database = config['postgresql']['database']
        user = config['postgresql']['user']
        password = config['postgresql']['password']

        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=database,
            user=user,
            password=password
        )
        cur = conn.cursor()

        return conn, cur

    def write(self, data: dict):
        pass

    def delete(self, data: dict):
        pass

    def read(self):
        connection, cur = self.connect_to_db()
        with connection:
            with connection.cursor() as cur:
                cur.execute("select * from vacancy")
                vac_info = cur.fetchone()
                print(vac_info)
        connection.close()


test_db_read = DB_Saver().read()


