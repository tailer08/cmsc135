import json
import subprocess

class Measurement:
    def run_ping(self,hostnames = [], num_packets = 0, raw_ping_output_filename = "", aggregated_ping_output_filename =""):
        for hostname in hostnames:
            ping_call   = subprocess.Popen( [ 'ping', '-c ' + str(num_packets) , hostname ], stdout=subprocess.PIPE )
            ping_result = ping_call.communicate()[0]
            ping_result_array = ping_result.split(' ');
            print (ping_result)
            # retrieve rtts
            ping_time_float = []
            for word in ping_result_array:
                if "time" in word:
                    print (word[5:])
                    if not word[5:]:
                        continue
                    else:
                        ping_time_float.append(float(word[5:]))
            print(ping_time_float)

            json_data = []
            json_data.append({
                hostname : ping_time_float
            })
            with open('my_sample_data.json', 'w') as outfile:
                json.dump(json_data, outfile);

    def create_json(self):
        data = []
        data.append({
            "My" : "sample sample"
        })

        data.append({
            "My" : "sample sample sample"
        })
        with open('my_sample_data.json', 'w') as outfile:
            json.dump(data, outfile);
    #
    # def plot_median_rtt_cdf():
    #
    # def plot_ping_cdf():

instance = Measurement();
instance.run_ping(['www.google.com'], 10);
# instance.create_json();
