#!/bin/sh

yum -y update
yum -y install epel-release 
yum -y install python-pip


#yum -y install mariadb101u-devel
yum -y install mariadb-devel
yum -y install libxslt-devel
yum -y install libffi-devel
yum -y install openldap-devel

yum -y install rsyslog

yum -y install git
yum -y install numpy

yum -y clean all

pip install -U pip

echo ''
echo '  ******  *   **'
echo '  **   *  *   **'
echo '  **   *  *   **'
echo '  ******  ******'
echo '  **          **'
echo '  **      ******'
echo ''

# pip install -r /var/ap/install/pip_base.txt
pip install -r /var/ap/install/dev7.txt

systemctl enable rsyslog

#yum -y install mc