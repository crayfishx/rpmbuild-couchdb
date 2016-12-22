Name:		apache-couchdb
Version:	2.0.0
Release:	1%{?dist}
Summary:	Apache CouchDB Server

Group:		Applications/Servers
License:	Apache 2.0
URL:		http://www.couchdb.org
Source0:	http://www.pirbot.com/mirrors/apache/couchdb/source/2.0.0/apache-couchdb-2.0.0.tar.gz

# These dependencies are for EL based platforms.
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: curl-devel
BuildRequires: erlang-asn1
BuildRequires: erlang-erts
BuildRequires: erlang-eunit
BuildRequires: erlang-os_mon
BuildRequires: erlang-xmerl
BuildRequires: help2man
BuildRequires: js-devel >= 1.8.5
BuildRequires: libicu-devel
BuildRequires: libtool
BuildRequires: perl-Test-Harness
BuildRequires: erlang
BuildRequires: gcc-c++


%description

Apache CouchDB Server


%prep
/bin/rm -rf %{buildroot}

%setup -q


%build
./configure
make release 


%install
mkdir -p %{buildroot}/opt
cp -r rel/couchdb %{buildroot}/opt/couchdb


%files
/opt/couchdb

%post
useradd -s /bin/nologin -d /opt/couchdb couchdb || /bin/true
chown -R couchdb:couchdb /opt/couchdb


IS_SYSTEMD=$((pidof systemd 2>&1 > /dev/null)  && echo "yes" || echo "no")
if [ "$IS_SYSTEMD" == "yes" ]; then
cat <<EOF > /etc/systemd/system/couchdb.service
[Unit]
Description=Apache CouchDB Server

[Service]
ExecStart=/opt/couchdb/bin/couchdb
User=couchdb
Type=simple

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
fi

%doc

%changelog
* Thu Dec 22 2016 Craig Dunn <craig@craigdunn.org>
- Initial couchdb package for CentOS

