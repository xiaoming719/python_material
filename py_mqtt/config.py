# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:53:13 2018

@author: test
"""
VERSION = '1.0.0'

#mqtt_configure

mqtt_ip = '192.168.100.174'
mqtt_port = 1883
mqtt_user = 'ehigh'
mqtt_password = 'Abc123'

#redis_configure
redis_cache_enable = 1
redis_ip = 'localhost'
redis_port = 6379
redis_db = 2

#mysql_configure

mysql_configure = {
        'db_user' : 'root',
        'db_password' : 'eHIGH2014',
        'db_host' : '192.168.100.139',
        'db_port' : 3306,
        'db_name' : 'test',
        'dbcharset' : 'utf8',
        'db_unicode' : True,
        'throw_alarm' : True
        }

#rpc_configure

rpc_port = 2018
rpc_process = 1


