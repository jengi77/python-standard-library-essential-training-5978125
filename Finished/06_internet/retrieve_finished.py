# retrieve data from the internet
import urllib.request


sample_url = "http://httpbin.org/xml"

# Create a request to retrieve data using urllib.request
response = urllib.request.urlopen(sample_url, timeout=5)

# Check the status
status_code = response.status
print(status_code)

# if no error, then read the response contents
if status_code >= 200 and status_code < 300:
    # work with response headers
    print(response.getheaders())
    print(response.getheader('Content-length'))
    print(response.headers['Content-Type'])

    # read the data from the URL
    data = response.read().decode('utf-8')
    print(data)

    # close the response
    response.close()
