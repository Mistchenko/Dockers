#!/bin/sh

yum -y update
yum -y install epel-release 
yum -y install python-pip
yum -y install mc

yum -y clean all

pip install -U pip

echo '

		▄■▀■▄■▀■▄■▀■▄☼ pIp InStAlL ☼▀■▄■▀■▄■▀■▄■▀

'

pip install -r /var/ap/install/pip_install.txt


echo '

		▄■▀■▄■▀■▄■▀■▄☼ InStAlLaTiOn CoMpLeTe ☼▀■▄■▀■▄■▀■▄■▀

'