def get_requirements() -> str:
    """Returns the project requirements

    Returns:
        requirements(str): the content of the requirements.txt file
    """

    with open('requirements.txt', 'r') as file:
        content = file.read()

    requirements = f'<pre>{content}</pre>' + '<br>'

    return requirements
