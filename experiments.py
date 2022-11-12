import os
import numpy as np
from subprocess import Popen, PIPE

def process_output(stdout, stderr):
    sort_time_line_with_empty_strings = stderr.decode('utf-8').split('\n')[3].split(' ')
    sort_time_line = list(filter(None, sort_time_line_with_empty_strings))
    return sort_time_line[2]

inputs = []

# directory were data are located
data_dir = './data'

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

runs = 5

for file, lines in inputs:
    print(file)
    time = 0
    for run in range(runs):
        process = Popen(["./sort-branched", str(100000), file], stdout=PIPE, stderr=PIPE)
        (stdout, stderr) = process.communicate()
        exit_code = process.wait()
        time += int(process_output(stdout, stderr))
    times['branched'].append(time/runs)

    time = 0
    for run in range(runs):
        process = Popen(["./sort-predicated", str(100000), file], stdout=PIPE, stderr=PIPE)
        (stdout, stderr) = process.communicate()
        exit_code = process.wait()
        time += int(process_output(stdout, stderr))
    times['predicated'].append(time/runs)

for key, value in times.items():
    print('Mode: {}'.format(key))
    print('Times: {}'.format(value))
    print('Average: {}'.format(np.mean(value)))
    print('Standard deviation: {}'.format(np.std(value)))
