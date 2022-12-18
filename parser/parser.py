import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'stackerbot-0837b544dc61.json'  # Имя файла с закрытым ключом, вы должны подставить свое
spreadsheet_id = '1uuK2NqKI1D_59nSZQn4U0n6s0b_bqUTAxk0Uwk1HaJg'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E10',
    majorDimension='ROWS'
).execute()

table_values = values['values']


def column_data(column, values):
    def column_index(name, values):
        return values[0].index(name)

    def users_data(values):
        return values[1:]

    def elem_users(column, users):
        return [user[column] for user in users]

    index = column_index(column, values)
    return elem_users(index, users_data(values))

#column_data('tg', table_values)

