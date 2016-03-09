FROM centos

EXPOSE 4505 4506
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

RUN yum localinstall -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum update -y
RUN yum install -y python-devel python-pip gcc gcc-c++

RUN install -d /etc/salt/master.d /etc/salt/pki/minion /etc/salt/pki/master/minions

COPY mode.conf /etc/salt/master.d/mode.conf

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
