#!/bin/sh

yum -y update
yum -y install epel-release 
yum -y install python-pip
# yum -y install mc
yum -y install /var/ap/install/rabbitmq-server-3.6.14-1.el7.noarch.rpm
yum -y clean all

pip install -U pip

systemctl enable rabbitmq-server

echo '

		▄■▀■▄■▀■▄■▀■▄☼ pIp InStAlL ☼▀■▄■▀■▄■▀■▄■▀

'

pip install -r /var/ap/install/pip_install.txt


echo '

		▄■▀■▄■▀■▄■▀■▄☼ InStAlLaTiOn CoMpLeTe ☼▀■▄■▀■▄■▀■▄■▀

'