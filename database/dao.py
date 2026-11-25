from database.DB_connect import DBConnect
from model.bonifico import Bonifico
from model.filiale import Filiale

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    @staticmethod
    def get_bonifico():
        try:
            cnx = DBConnect.get_connection()
            try:
                cursor = cnx.cursor(dictionary=True)


                query = """SELECT *
                FROM bonifico
                """

                cursor.execute(query)

                result = []
                for row in cursor:
                    oggetto = Bonifico(**row)
                    result.append(oggetto)
            finally:
                cursor.close()
        finally:
            cnx.close()

        return result

    @staticmethod
    def get_filiale():
        try:
            cnx = DBConnect.get_connection()
            try:
                cursor = cnx.cursor(dictionary=True)

                query = """SELECT *
                    FROM filiale
                    """

                cursor.execute(query)

                result = {}
                for row in cursor:
                    result[row["id"]] = row["nome"]
            finally:
                cursor.close()
        finally:
            cnx.close()

        return result