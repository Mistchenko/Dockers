FROM centos/systemd

RUN yum -y install httpd; yum clean all; systemctl enable httpd.service

EXPOSE 80

CMD ["/usr/sbin/init"]

# https://hub.docker.com/r/centos/systemd/

# docker build --rm --no-cache -t httpd .

# docker run --privileged --rm --name httpd -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 8888:80 -d  httpd
