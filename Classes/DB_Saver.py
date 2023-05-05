import psycopg2
import configparser


class DB_Saver():
    """Отвечает за сохранение и удаление данных в БД"""

    def connect_to_db(self, config_file="config.ini"):
        """Функция для установления соединения с БД"""
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

    def write_employers(self, data: list):
        """Записывает данные в таблицу employers"""
        #connection, cur = self.connect_to_db()
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                print('Начинаем вставку')
                cur.executemany("insert into employers (id, name, url, description) values (%s, %s, %s, %s)", data)
                connection.commit()
                print('Вставка завершена')
        connection.close()

    def write_vacancies(self, data: list):
        """Записывает данные в таблицу vacancy"""
        #connection, cur = self.connect_to_db()
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                print('Начинаем вставку')
                cur.executemany("insert into vacancy (id, name, salary_from, salary_to, emlployer_id, url, currency, requirement, responsibility) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
                connection.commit()
                print('Вставка завершена')
        connection.close()

    def delete_employers(self):
        """Удаляет данные из таблицы employers"""
        #connection, cur = self.connect_to_db()
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                print('Начинаем удаление')
                cur.execute("delete from employers")
                connection.commit()
                print('Удаление завершено')
        connection.close()

    def delete_vacancy(self):
        """Удаляет данные из таблицы vacancy"""
        #connection, cur = self.connect_to_db()
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                print('Начинаем удаление')
                cur.execute("delete from vacancy")
                connection.commit()
                print('Удаление завершено')
        connection.close()

    def delete_all(self):
        """Удаляет данные из таблиц employers и vacancy"""
        #connection, cur = self.connect_to_db()
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                print('Начинаем удаление')
                cur.execute("delete from employers")
                cur.execute("delete from vacancy")
                connection.commit()
                print('Удаление завершено')
        connection.close()

    def read(self):
        """Чтение данных. Используется для тестов"""
        #connection, cur = self.connect_to_db()
        connection = psycopg2.connect(host="localhost",
            port="5432",
            dbname="course_work_5",
            user="postgres",
            password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                cur.execute("select * from employers")
                vac_info = cur.fetchone()
                print(vac_info)
        connection.close()


