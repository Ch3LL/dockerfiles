FROM centos

EXPOSE 4505 4506 8000
ENTRYPOINT ["/usr/local/bin/entrypoint"]

RUN yum localinstall -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum update -y
RUN yum install -y gcc gcc-c++ readline-devel openssl-devel bzip2-devel sqlite-devel libffi-devel make git 

RUN git clone git://github.com/yyuu/pyenv.git /usr/local/share/pyenv
RUN ln -s /usr/local/share/pyenv/bin/pyenv /usr/local/bin/pyenv
RUN ln -s /usr/local/share/pyenv/plugins/python-build/bin/pyenv-install /usr/local/bin/pyenv-install
RUN ln -s /usr/local/share/pyenv/plugins/python-build/bin/pyenv-uninstall /usr/local/bin/pyenv-uninstall
RUN ln -s /usr/local/share/pyenv/plugins/python-build/bin/python-build /usr/local/bin/python-build
RUN pyenv install 2.7.11
RUN pyenv global 2.7.11
ADD pyenv.sh /etc/profile.d/pyenv.sh
RUN bash -l -c 'pip install pyOpenSSl cherrypy'


RUN install -d /etc/salt/master.d /etc/salt/minion.d /etc/salt/proxy.d /etc/salt/pki/minion /etc/salt/pki/master/minions

ADD mode.conf /etc/salt/master.d/mode.conf
ADD api.conf /etc/salt/master.d/api.conf
ADD hash_type.conf /etc/salt/master.d/hash_type.conf
ADD hash_type.conf /etc/salt/minion.d/hash_type.conf
ADD proxy /etc/salt/proxy

ADD entrypoint.py /usr/local/bin/entrypoint
