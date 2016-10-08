""" Access the current gold price from a site """

import urllib
import urllib.request

#  This URL contains tables of the gold price in the HTML
url = 'https://www.bullionbypost.co.uk/gold-price/'

request = urllib.request.Request(url)

# The site checks User-Agent header to foil scripters
request.add_header("User-Agent", "Mozilla/5.0 Firefox/48.0")
#print("Request is: ", request.get_method(), " ",request.header_items())

response = urllib.request.urlopen(request)

# Read data back in the response
data = response.read()

# Decode to a string
resp_str = data.decode()

# The first table is the one we want
startIdx = resp_str.find("<table")
endIdx = resp_str.find("</table")

#print("startIdx: ", startIdx, " endIdx: ", endIdx)
table = resp_str[startIdx: endIdx]
#print("Table: ", table)

# First price is the gold price in ounces
goldStartIdx = table.find("£")
goldEndIdx = table.find("</span")

price = table[goldStartIdx:goldEndIdx]

print("Gold price is: ", price)
