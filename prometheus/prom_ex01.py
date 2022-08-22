#
# Prometheus demo app
#
# This is an example based on code from the client_python repo
#

from prometheus_client import start_http_server, Summary, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    num_datapoints_metric = Gauge('orca_cdf_datapoints_inserted', 'ORCA netsolution vessel datapoints ingested',
                           labelnames=['vessel', 'cdf_datapoint_type'])
    while True:
        # process_request(random.random())
        num_datapoints_metric.labels(vessel='VAN', cdf_datapoint_type='orca_netsolution_vessel')
        num_datapoints_metric.set(random.randint(1000, 5000))
        # Sleep 30 seconds before setting next datapoint
        time.sleep(30)
