#!/usr/bin/env python

from flask import Flask, Response, abort, request

import GeoIP

import ipaddress
import json
import re

__version__ = '1.0.3'

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

_open_mode = getattr(GeoIP, app.config['GEOIP_OPEN_MODE'])
GI_CITY = GeoIP.open(app.config['GEOIP_CITY_PATH'], _open_mode) 
GI_CITY_V6 = GeoIP.open(app.config['GEOIP_CITY_V6_PATH'], _open_mode) 
GI_ORG = GeoIP.open(app.config['GEOIP_ORG_PATH'], _open_mode) 
GI_ORG_V6 = GeoIP.open(app.config['GEOIP_ORG_V6_PATH'], _open_mode) 

for x in (GI_CITY, GI_CITY_V6, GI_ORG, GI_ORG_V6):
	x.set_charset(GeoIP.GEOIP_CHARSET_UTF8)

@app.route('/<ip_addr>')
def lookup_ip(ip_addr):
	try: 
		ip = ipaddress.ip_address(ip_addr)
	except ValueError:
		abort(400)
	if ip.version == 4:
		gi_city = GI_CITY
		gi_org = GI_ORG
		r = gi_city.record_by_addr(ip.exploded)
		org = gi_org.name_by_addr(ip.exploded)	
	else:
		gi_city = GI_CITY_V6
		gi_org = GI_ORG_V6
		r = gi_city.record_by_addr_v6(ip.exploded)
		org = gi_org.name_by_addr_v6(ip.exploded)	
	if org:
		m = re.search(r'^(AS[0-9]+) (.+)$', org)
		if m and isinstance(r, dict):
			r['asn'] = m.group(1)
			r['org'] = m.group(2)
	r['ip'] = ip_addr
	return Response(json.dumps(r), mimetype='application/json')


@app.route('/')
def lookup_self():
	return lookup_ip(request.remote_addr)


if __name__ == '__main__':
	app.run(host=app.config['HOST'], port=app.config['PORT'])
