from src.models.UserModel import User

class AuthService():

    @classmethod
    def login_user(cls, user):

        try:
            connection = get_connection()
            autheticated_user= None
            with connection.cursor() as cursor:
                cursor.execuse('call sp_verifyIdentity(%s, %s)', (user.username, user.password))
                row = cursor.fetchone()
                if row != None:
                    authenticated_user = User(int(row[0]), row[1], None, row[2])
            connection.close()
            return authenticated_user
        except Exception as ex:
            print(ex)

