#!/bin/sh

#for i in $(cat ./yum_install.txt); do [ ${i:0:1} = "#" ] || yum -y install $i ; done
yum -y update
yum -y install epel-release 
yum -y install python-pip


# yum -y install mariadb101u-devel
# yum -y install libxslt-devel
# yum -y install libffi-devel
# yum -y install openldap-devel

yum -y clean all

pip install -U pip
pip install -r /var/ap/requirements/pip_base.txt
yum -y install mc