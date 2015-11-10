# Balise

A portable, lightweight IP geolocation API/server

## Requirements

* Python 3.3+ or 2.x with ipaddress module
* MaxMind Python GeoIP module
* Flask 0.10.x+

## Installation and setup

1. Create a virtualenv (highly recommended)
2. Download datasets
3. Adjust configuration in ```settings.cfg``` as appropriate
4. ```python main.py``` or run using your favorite WSGI server

## API/Usage

```/ip```: Return GeoIP data for the current IP address
```/ip/<IPv4 or IPv6 address>```: Return GeoIP data for the specified IP address

## License

Balise is made available under the terms of the MIT license. Please refer to [LICENSE.txt](LICENSE.txt)
for more information.
