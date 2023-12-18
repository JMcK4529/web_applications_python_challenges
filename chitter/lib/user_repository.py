from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        """Returns all users without associated peeps."""
        users = []
        rows = self.connection.execute(
            """SELECT * FROM users"""
            )
        for row in rows:
            users.append(
                User(row['id'], row['username'])
            )