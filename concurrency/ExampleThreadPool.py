##########################################################################################
#
# See: https://docs.python.org/3/library/concurrent.futures.html?highlight=concurrency%20future#concurrent.futures.ThreadPoolExecutor
#
##########################################################################################

import concurrent.futures
import urllib.request

URLS = [
    "https://www.vg.no/",
    "http://www.cnn.com/",
    "http://europe.wsj.com/",
    "http://www.bbc.co.uk/",
    "http://some-made-up-domain.com/",
]


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    # NOTE
    # future_to_url is dictionary of:
    # {Future object: str object with the URL}
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    #
    # as_completed() (module function) returns and iterator over Future
    # instances - see reference to doc at top of file.
    # In this case the
    # dictionary future_to_url is an Iterable
    # Iterable can be lists, str, tuple, dict, file objects...
    for future in concurrent.futures.as_completed(future_to_url):
        # Note the mapping key is the future object, very generic... Usually we use things
        # like strings and numbers as the key...
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print("%r generated an exception: %s" % (url, exc))
        else:
            print("%r page is %d bytes" % (url, len(data)))
