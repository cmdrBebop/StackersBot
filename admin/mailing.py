import datetime
import psycopg2


def publish(data):
    def get_event_id(data):
        return data['type_of_event_id']

    def get_mailing_user_id(id):
        con = psycopg2.connect(
            dbname="stackers_db",
            user="postgres",
            password="Millioner1000000",
            host="localhost",
            port=5432
        )
        type = {1: 'hackathon_subscribe', 2: 'meet_up_subscribe', 3: 'lecture_subscribe', 4: 'vacancy_subscribe'}
        cur = con.cursor()
        select_query = f"select user_id from web_subscribe where {type[id]} = 't';"
        cur.execute(select_query)
        con.commit()
        ids = [data[0] for data in cur.fetchall()]
        return ids

    def get_post(data):
        return str(data['title']) + '\nДата: ' + str(data['event_date']) + '\nОписание: ' + str(
            data['post_about_event'])

    ids = get_mailing_user_id(get_event_id(data))
    post = get_post(data)

    return (ids, post)
