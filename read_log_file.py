import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse

def find_unique_id_number(file_path, keyword):
    unique_ids = set()

    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                temp = line.split()
                # print(temp)
                unique_ids = [temp[2]]
    return unique_ids


def strip_off_extra(timestamp):
    ts = timestamp.strip("[']")
    ts = float(ts)
    # print(ts)
    return ts


def filter_log_file(file_path, keyword):
    ts = []
    rssi = []
    ant_num = []
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line and 'Err' not in line:
            #if keyword and not 'Err' in line:
                temp = line.split()
                print(temp)
                ts.append(strip_off_extra(temp[0]))
                rssi.append(int(temp[3]))
                ant_num.append(int(temp[4]))

    return {'ts': ts, 'id': keyword, 'RSSI': rssi, 'Antenna':  ant_num}


# Plot time vs RSSI disregarding antenna
def plot_all_antenna(all_info):
    for i, d in enumerate(all_info):
        print(i)

        ts_start = d['ts'][0]

        ts = np.array(d['ts'][:]) - ts_start
        plt.figure()
        plt.plot(ts, d['RSSI'])
        plt.xlabel('Time(s)')
        plt.ylabel('RSSI(dB)')


def plot_antenna(tag_info):
    ts = [[], [], [], []]
    rssi = [[], [], [], []]
    for n in range(0, 4):
        for i in range(0, len(tag_info['Antenna'])):
            if tag_info['Antenna'][i] == n:
                # ts[n].append(tag_info['ts'][i])
                rssi[n].append(tag_info['RSSI'][i])

    print(rssi)
    plt.figure()
    for n in range(0, 4):
        plt.plot(rssi[n], label="Ant {}".format(n))


    plt.xlabel('Time(s)')
    plt.ylabel('RSSI(dB)')
    plt.legend()

# -------------------------------------------------------------
# Start
# -------------------------------------------------------------

# Configure parser
parser = argparse.ArgumentParser(
        description="BLE Antenna Diversity",
        usage="%(prog)s [options] mode ...",)
        # formatter_class=argparse.RawDescriptionHelpFormatter)
        # epilog=""")

parser.add_argument( "-f", "--file", dest="filename",
    nargs='+',
    help="Input file")
parser.add_argument( "-k", "--keyword", dest="keyword",
    nargs='+',
    help="Search Keyword")


options = parser.parse_args(sys.argv[1:])
print(options)

#log_file = './log_example/friday_test.txt'
#log_file = './log_files/test_1.txt'
log_file = options.filename[0]

#search_keyword = 'BLE'
#search_keyword = '72308628870207035'
search_keyword = options.keyword[0]

ids = find_unique_id_number(log_file, search_keyword)
print(ids)
input("Press to continue...")
# Info list has a seperate entry (member) for each tag ID
info = []
for i, id in enumerate(ids):
    print(i)
    info.append(filter_log_file(log_file, id))

plot_all_antenna(info)

selected_info_idx = 0
plot_antenna(info[selected_info_idx])

plt.show()

