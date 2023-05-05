import psycopg2

class DB_Manager():

    def get_companies_and_vacancies_count(self):
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                cur.execute("select e.name, count(*) from vacancy v "
                            "join employers e on v.emlployer_id = e.id " 
                            "group by e.name ")
                info = cur.fetchall()
        connection.close()
        return info

    def get_all_vacancies(self):
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                cur.execute("select e.name, v.name, salary_from, salary_to, currency, v.url  from vacancy v "
                            "join employers e on e.id = v.emlployer_id "
                            "order by e.name")
                info = cur.fetchall()
        connection.close()
        return info

    def get_avg_salary(self):
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                cur.execute("select round(avg(salary_from)) as salary_from, round(avg(salary_to)) as salary_to from vacancy v ")
                info = cur.fetchone()
        connection.close()
        return info

    def get_vacancies_with_higher_salary(self):
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "select * from vacancy v "
                    "where salary_from > (select avg(salary_from) from vacancy v2) "
                    "order by salary_from desc ")
                info = cur.fetchall()
        connection.close()
        return info

    def get_vacancies_with_keyword(self, keyword):
        connection = psycopg2.connect(host="localhost",
                                      port="5432",
                                      dbname="course_work_5",
                                      user="postgres",
                                      password="cnmeses")
        with connection:
            with connection.cursor() as cur:
                cur.execute(
                    "select * from vacancy v "
                    f"where name ilike '%{keyword}%'")
                info = cur.fetchall()
        connection.close()
        return info



