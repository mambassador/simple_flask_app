from flask import request

from faker import Faker


fake = Faker()


def generate_users() -> str:
    """Returns a string with list of mock users.

    Returns:
        mock_users(str): generated mock users

    By default, it returns 100 users.
    The query parameter 'count' specifies the total number of users.
    """

    users_request = request.args.get('count', default=100)
    response = [f'{fake.name()} {fake.email()}' for _ in range(int(users_request))]

    mock_users = f'<pre>{"<br>".join(response)}</pre>'

    return mock_users
