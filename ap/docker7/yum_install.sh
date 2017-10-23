#!/bin/sh

yum -y update
yum -y install epel-release 
yum -y install python-pip


#yum -y install mariadb101u-devel
yum -y install gcc
yum -y install python-devel
# yum -y install mariadb-devel
# yum -y install libxslt-devel
# yum -y install libffi-devel
# yum -y install openldap-devel

# yum -y install rsyslog

# yum -y install git
# yum -y install numpy

yum -y install mc
yum -y clean all

pip install -U pip

echo '

		▄■▀■▄■▀■▄■▀■▄☼ pIp InStAlL ☼▀■▄■▀■▄■▀■▄■▀

'

# pip install -r /var/ap/install/dev7.txt
pip install -r /var/ap/install/pip_base.txt

# systemctl enable rsyslog

# echo '#' > /var/log/ap/dev/ws.log
# echo '#' > /var/log/ap/dev/ping.log
# echo '#' > /var/log/ap/dev/saml.log


echo '

		▄■▀■▄■▀■▄■▀■▄☼ InStAlLaTiOn CoMpLeTe ☼▀■▄■▀■▄■▀■▄■▀

'
