#!/bin/sh

yum -y update
yum -y install epel-release 
yum -y install python34
yum -y install python34-pip


yum -y install gcc
yum -y install python34-devel

yum -y install mc

yum -y clean all

pip3 install -U pip

echo '

		▄■▀■▄■▀■▄■▀■▄☼ pIp InStAlL ☼▀■▄■▀■▄■▀■▄■▀

'

pip install -r /var/install/pip3.txt

echo '

		▄■▀■▄■▀■▄■▀■▄☼ InStAlLaTiOn CoMpLeTe ☼▀■▄■▀■▄■▀■▄■▀

'


