from requests import get


def count_astros() -> str:
    """Returns the number of astronauts at the actual moment

    Returns:
        message(str): the informational message about the number
                      of astronauts
    """

    api_request = get('http://api.open-notify.org/astros')
    response = api_request.json()

    astros_number = str(response['number'])
    message = f'<pre>Total astronauts at the moment: {astros_number}</pre>'

    return message
