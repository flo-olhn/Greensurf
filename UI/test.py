import psutil
import time


def networkTrafficEmissions(val_list, val_init):
    vals = psutil.net_io_counters()
    bytes_sent = vals[0]
    bytes_received = vals[1]
    total_bytes = bytes_sent + bytes_received
    total_emission = ((total_bytes * 1.52E-10) * 0.055) - val_init
    val_list.append(total_emission)
    print(total_emission)
    print(val_list)
    val_init = val_list[-1]
    return total_emission


if __name__ == '__main__':
    values_start = psutil.net_io_counters()
    b = values_start[0] + values_start[1]
    values = []
    val = (b * 1.52E-10) * 0.055
    for i in range(10):
        networkTrafficEmissions(values, val)
        time.sleep(1)