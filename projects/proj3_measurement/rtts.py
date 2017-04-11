import json
import subprocess

class Measurement:
    def run_ping(self,hostnames = [], num_packets = 0, raw_ping_output_filename = "", aggregated_ping_output_filename =""):
        for hostname in hostnames:
            ping_call   = subprocess.Popen( [ 'ping', '-c ' + str(num_packets) , hostname ], stdout=subprocess.PIPE )
            ping_result = ping_call.communicate()[0]
            print "*************************************"
            print (ping_result)
            print "*************************************"
    def create_json():
        data = {
            "My" : "sample"
        }
        with open('my_sample_data.json', 'w') as outfile:
            json.dump(data, outfile);
    #
    # def plot_median_rtt_cdf():
    #
    # def plot_ping_cdf():

instance = Measurement();
instance.run_ping(['www.google.com', 'www.facebook.com'], 10);
