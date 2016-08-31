# Balise

A portable, lightweight, locally-hosted IPv4 and IPv6 geolocation API/server

## Requirements

* Python 3.3+ or 2.x with ipaddress module
* [MaxMind Python GeoIP Legacy module](https://github.com/maxmind/geoip-api-python)
* Flask 0.10.x+
* [MaxMind GeoIP or GeoLite Legacy City and Organization/ASN datasets (both IPv4 and IPv6)](https://dev.maxmind.com/geoip/legacy/geolite/)

## Installation and setup

1. Create a virtualenv (highly recommended)
2. Download datasets (see [data/update.sh](data/update.sh))
3. Adjust configuration in ```settings.cfg``` as appropriate
4. ```python main.py``` or run using your favorite WSGI server

If you will be running balise behind a reverse proxy, use ```main_rp.py``` instead as
a WSGI entry point so that the client IP address is passed along properly.

## API/Usage

Results are returned in JSON format.

```/```: Return GeoIP data for the current IP address    
```/<IPv4 or IPv6 address>```: Return GeoIP data for the specified IP address

Example
```
GET /128.135.100.101

{
  "country_name": "United States",
  "longitude": -87.602699279785,
  "org": "University of Chicago",
  "ip": "128.135.100.101",
  "asn": "AS160",
  "city": "Chicago",
  "postal_code": "60637",
  "country_code3": "USA",
  "time_zone": "America\/Chicago",
  "region_name": "Illinois",
  "latitude": 41.78039932251,
  "dma_code": 602,
  "country_code": "US",
  "metro_code": 602,
  "area_code": 773,
  "region": "IL"
}
```

## License

Balise is made available under the terms of the MIT license. Please refer to [LICENSE.txt](LICENSE.txt)
for more information.
