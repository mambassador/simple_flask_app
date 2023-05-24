from csv import DictReader
from statistics import mean


def get_average_measurement() -> str:
    """Returns average height and weight converted to metric units
    from files/hw.csv file

    Returns:
        result(str): the average height and weight
    """

    with open('files/hw.csv', 'r') as file:
        reader = list(DictReader(file))

        heights = [float(row[' "Height(Inches)"']) for row in reader]
        weights = [float(row[' "Weight(Pounds)"']) for row in reader]

    avg_height = mean(heights) * 2.539999962
    avg_weight = mean(weights) * 0.45359237

    result = f'<pre>Average Height: {avg_height} cm<br>Average Weight: {avg_weight} kg</pre>'

    return result
