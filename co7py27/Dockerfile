FROM centos:7
ENV container docker

# RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
# systemd-tmpfiles-setup.service ] || rm -f $i; done); \

# RUN (cd /lib/systemd/system/sysinit.target.wants/; \
# 	for i in *; do [ $i == systemd-tmpfiles-setup.service -o $i == systemd-journald.service ] || rm -f $i; done);

# RUN rm -f /lib/systemd/system/multi-user.target.wants/*;\
# rm -f /etc/systemd/system/*.wants/*;\
# rm -f /lib/systemd/system/local-fs.target.wants/*; \
# rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
# rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
# rm -f /lib/systemd/system/basic.target.wants/*;\
# rm -f /lib/systemd/system/anaconda.target.wants/*;

CMD ["/usr/sbin/init"]

#VOLUME [ "/sys/fs/cgroup" ]

RUN yum -y install epel-release
RUN yum -y update
RUN yum -y install python-pip 
RUN yum -y install systemd-python

RUN pip install --upgrade pip

RUN yum -y install mc

RUN yum -y clean all

ENV APP_DIR=/var/app/

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

#ADD ./app $APP_DIR/

