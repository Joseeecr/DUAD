import psycopg2
import psycopg2.extras
class PgManager:
  def __init__(self, dbname, user, password, host, port=5432):
    self.dbname = dbname
    self.user = user
    self.password = password
    self.host = host
    self.port = port


  def _connect(self):
    try:
      connection = psycopg2.connect(
      dbname = self.dbname,
      user = self.user,
      password = self.password,
      host = self.host,
      port = self.port
    )
      cursor =  connection.cursor()
      return connection, cursor
    except Exception as error:
      print("Error connecting to the database:", error)
      return None, None


  def execute_query(self, query, *args):
    connection, cursor = self._connect()
    if not connection or not cursor:
      return None

    try:
      cursor.execute(query, *args)
      connection.commit()

      if cursor.description:
          results = cursor.fetchall()
          return results
    except Exception as error:
      print("Error executing query:", error)

    finally:
      cursor.close()
      connection.close()
  

  def execute_query_dict_result(self, query, *args):
    connection, cursor = self._connect()
    if not connection:
        return None

    try:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query, *args)
        connection.commit()
        
        if cursor.description:
            return cursor.fetchall()
    except Exception as error:
        print("Error executing query with dict result:", error)
    finally:
        cursor.close()
        connection.close()
