import pyodbc

def get_word_list(username, password):
    SERVER = "sql8010.site4now.net"
    DATABASE = "db_aa9650_hangman"
    USERNAME = "db_aa9650_hangman_admin"
    PASSWORD = "TeamBRules123"

    ##connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Integrated Security=True;

    connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    conn = pyodbc.connect(connectionString)

    cursor = conn.cursor()

    cursor.execute("SELECT Word FROM tWords")

    records = cursor.fetchall()

    word_list = [record.Word for record in records]

    conn.close()

    return word_list

    #for r in records:
    #    rec = []
    #    for col in r:
    #        rec.append(col)
    #    print(rec)