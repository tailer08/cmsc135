def run_ping(hostnames, num_packets, raw_ping_output_filename, aggregated_ping_output_filename):
    subprocess.call('ping -c ' + num_packets + ' ' + hostnames)

def plot_median_rtt_cdf():

def plot_ping_cdf():
