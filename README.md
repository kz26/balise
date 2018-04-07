# Balise

A portable, lightweight, locally-hosted IPv4 and IPv6 geolocation API/server

***balise 2.x is designed to operate with MaxMind's GeoIP2/GeoLite 2 databases.
For GeoIP Legacy/GeoLite Legacy support, use the balise 1.x branch.***

## Requirements

* Python 3.3+ or 2.x with ipaddress module
* [MaxMind Python GeoIP2 module](https://geoip2.readthedocs.io/en/latest/)
* [MaxMind GeoLite2 or GeoIP2 City and ASN databases](https://dev.maxmind.com/geoip/geoip2/geolite2/)
* Flask 0.12.2+

## Installation and setup

1. Create a virtualenv (highly recommended)
2. Adjust configuration in ```settings.cfg``` as appropriate
3. ```python main.py``` or run using your favorite WSGI server

If you will be running balise behind a reverse proxy, use ```main_rp.py``` instead as
a WSGI entry point so that the client IP address is passed along properly.

## API/Usage

Results are returned in JSON format.

```/```: Return GeoIP data for the IP address that made the request 
```/<IPv4 or IPv6 address>```: Return data for the specified IP address

Example

```
GET /128.135.100.101

{
  "region": {
    "iso_code": "IL",
    "name": "Illinois"
  },
  "org": "University of Chicago",
  "city": "Chicago",
  "country": {
    "iso_code": "US",
    "name": "United States"
  },
  "postal_code": "60637",
  "location": {
    "latitude": 41.7804,
    "longitude": -87.6027,
    "time_zone": "America\/Chicago",
    "metro_code": 602
  },
  "asn": 160,
  "ip": "128.135.100.101"
}

```

## License

Balise is made available under the terms of the MIT license. Please refer to [LICENSE.txt](LICENSE.txt)
for more information.
