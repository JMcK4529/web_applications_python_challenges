from lib.user import User
from lib.user_repository import UserRepository
from unittest.mock import Mock

def test_user_repo_constructs():
    try:
        connection = Mock()
        repo = UserRepository(connection)
    except:
        raise AssertionError("UserRepository class does not construct properly")
    
def test_user_repo_all(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repo = UserRepository(db_connection)
    assert repo.all() == [
        'User(JMcK4529)'
    ]

