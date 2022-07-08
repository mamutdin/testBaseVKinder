import psycopg2
from psycopg2 import OperationalError


class Postgresql:
    def __init__(self):
        self.con = psycopg2.connect(
            database='vkinder',
            user='postgres',
            password='A84db68d',
            host='localhost',
            port='5432',
        )
        self.cursor = self.con.cursor()

    def query(self, query_text):
        self.cursor.execute(query_text)

    def __del__(self):
        self.con.close()


create_table1 = """CREATE TABLE initiators (id INTEGER PRIMARY KEY, first_name VARCHAR(40), last_name VARCHAR(40),
                    birthday INTEGER, id_sex INTEGER, city VARCHAR(40),);"""
create_table2 = """CREATE TABLE founds (id INTEGER PRIMARY KEY, first_name VARCHAR(40), last_name VARCHAR(40),
                    birthday VARCHAR(40), id_sex INTEGER, city VARCHAR(40),);"""
create_table3 = """CREATE TABLE initiators_founds (initiator_id INTEGER REFERENCES initiators(id), 
                    found_id INTEGER REFERENCES founds(id), 
                    CONSTRAINT pk2 PRIMARY KEY (initiator_id, found_id));"""

insert_data1 = """INSERT INTO initiators VALUES (13526, "ramil", "mamytov", 29, 1, "Moscow")"""
insert_data2 = """INSERT INTO founds VALUES (22896, "alfa", "mamytova", 26, 2, "Kazan")"""
insert_data3 = """INSERT INTO initiators_founds VALUES (13526, 22896)"""

query_select = """SELECT * FROM founds JOIN initiators_founds if ON founds.id = if.found_id 
                    WHERE if.initiator_id = 13526"""
