trystack_util
=============

Util script for trystack management

cleanup.py 
-----------------------------------------
Cleanup VMs which lives longer than 1 day

How to use 
setup OpenStack envs
export OS_REGION_NAME=RegionOne
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_AUTH_URL=http://127.0.0.1:5000/v2.0/
export OS_PASSWORD=seacret

python cleanup.py
