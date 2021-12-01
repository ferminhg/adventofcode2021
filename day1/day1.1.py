print("Day 1.1")


def measurement_increases(report):
    increases = 0
    last_measurement = report[0]
    for measurement in report:
        if measurement > last_measurement:
            increases += 1
        last_measurement = measurement
    return increases


def extract_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [int(line) for line in lines]


assert (measurement_increases(extract_data_from_file('day1.1.test.txt')) == 7)
print(measurement_increases(extract_data_from_file('day1.1.txt')))
