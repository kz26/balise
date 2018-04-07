#!/usr/bin/env python

from flask import Flask, Response, abort, request

import geoip2.database
import geoip2.errors
import maxminddb

import ipaddress
import json
import re

__version__ = '2.0.0'

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

_open_mode = getattr(maxminddb, app.config['GEOIP2_OPEN_MODE']) | maxminddb.MODE_AUTO
GI2_CITY = geoip2.database.Reader(app.config['GEOIP2_CITY_DB'], mode=_open_mode) 
GI2_ASN = geoip2.database.Reader(app.config['GEOIP2_ASN_DB'], mode=_open_mode) 

@app.route('/<ip_addr>')
def lookup_ip(ip_addr):
    try: 
        ip = ipaddress.ip_address(ip_addr)
    except ValueError:
        abort(400)
    try:
        rc = GI2_CITY.city(ip.exploded)
        rasn = GI2_ASN.asn(ip.exploded)
    except geoip2.errors.AddressNotFoundError:
        abort(404)
    data = {}
    data['ip'] = ip.exploded
    data['city'] = rc.city.name
    data['country'] = {
        'name': rc.country.name,
        'iso_code': rc.country.iso_code
    }
    data['region'] = {
        'name': rc.subdivisions.most_specific.name,
        'iso_code': rc.subdivisions.most_specific.iso_code
    }
    data['location'] = {
        'latitude': rc.location.latitude,
        'longitude': rc.location.longitude,
        'metro_code': rc.location.metro_code,
        'time_zone': rc.location.time_zone
    }
    data['postal_code'] = rc.postal.code
    data['asn'] = rasn.autonomous_system_number
    data['org'] = rasn.autonomous_system_organization
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/')
def lookup_self():
    return lookup_ip(request.remote_addr)


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
