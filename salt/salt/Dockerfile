FROM centos

EXPOSE 4505 4506 8000
ENTRYPOINT ["/usr/local/bin/entrypoint"]

RUN yum localinstall -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum update -y
RUN yum install -y python-devel python-pip pyOpenSSL python-cherrypy gcc gcc-c++

RUN install -d /etc/salt/master.d /etc/salt/pki/minion /etc/salt/pki/master/minions

ADD mode.conf /etc/salt/master.d/mode.conf
ADD api.conf /etc/salt/master.d/api.conf

ADD entrypoint.py /usr/local/bin/entrypoint
