FROM centos

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

RUN yum localinstall -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum update -y
RUN yum install -y python-devel python-pip gcc gcc-c++

RUN install -d /etc/salt/pki/minion

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
