def measurement_increases(report):
    increases = 0
    last_measurement = None
    for measurement in report.items():
        value = measurement[1]
        if last_measurement is not None and value > last_measurement:
            increases += 1
        last_measurement = value
    return increases


def extract_data_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    data = {}
    line_number = 0
    for line in lines:
        data[line_number] = int(line)
        if line_number+2 >= len(lines):
            break
        data[line_number] += int(lines[line_number+1]) + int(lines[line_number+2])
        line_number += 1
    return data


assert(measurement_increases(extract_data_from_file('day1.1.test.txt')) == 5)
assert(measurement_increases(extract_data_from_file('day1.1.txt')) == 1597)
