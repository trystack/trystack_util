import datetime
import os
import sys
import time

# Clenup scirpt which will delete VM which is living longer than 1day

from novaclient.v1_1 import client

USER = os.environ.get('OS_USERNAME', '')
PASS = os.environ.get('OS_PASSWORD', '')
TENANT = os.environ.get('OS_TENANT_NAME', '')
AUTH_URL = os.environ.get('OS_AUTH_URL', '')
REGION_NAME = os.environ.get('OS_REGION_NAME', '')

client = client.Client(USER, PASS, TENANT, AUTH_URL, 
                       endpoint_type="adminURL",
                       region_name=REGION_NAME)
now = datetime.datetime.now()
oneday = datetime.timedelta(days=1)
for server in client.servers.list(True, {'all_tenants':True}):
    delta = now - datetime.datetime.strptime(server.created, 
                                             "%Y-%m-%dT%H:%M:%SZ") 
    if delta > oneday:
	print "server_id:%s\ttenant_id:%s deleted" % (server.id,
                                                      server.tenant_id)
	try:
	    server.delete() 
	    time.sleep(1)
	    print "server_id:%s\ttenant_id:%s deleted" % (server.id,
                                                          server.tenant_id)
        except:
	    print "[ERROR] failed to delete server_id:%s\ttenant_id:%s" % (
                server.id,
                server.tenant_id)
