import os
from subprocess import Popen, PIPE

def process_output(stdout, stderr):
    sort_time_line_with_empty_strings = stderr.decode('utf-8').split('\n')[3].split(' ')
    sort_time_line = list(filter(None, sort_time_line_with_empty_strings))
    return sort_time_line[2]

inputs = []

# directory were data are located
data_dir = './miss-prediction-and-predication/data'

# get data file paths and line counts
for file_name in os.listdir(data_dir):
    file_path = '{}/{}'.format(data_dir, file_name)
    with open(file_path, 'r') as file:
        inputs.append((file_path, len(file.readlines())))

# print(inputs)

times = {
    'branched': [],
    'predicated': []
}

for file, lines in inputs:
    process = Popen(["./miss-prediction-and-predication/code/sort-branched", str(1000), file], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = process.communicate()
    exit_code = process.wait()
    time = process_output(stdout, stderr)
    times['branched'].append(time)

    process = Popen(["./miss-prediction-and-predication/code/sort-predicated", str(1000), file], stdout=PIPE, stderr=PIPE)
    (stdout, stderr) = process.communicate()
    exit_code = process.wait()
    time = process_output(stdout, stderr)
    times['predicated'].append(time)

print(times)