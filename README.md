## rpmbuild-couchdb

This is a simple spec file to build couchdb as a CentOS/RedHat RPM which includes systemd unit scripts.

Tested on RedHat 7.0 building Apache CouchDB 2.0

## Quick usage

### Clone the repo to your homedir

```
cd ~
git clone https://github.com/crayfishx/rpmbuild-couchdb
cd rpmbuild-couchdb
```

### Set up an rpmbuild env

```
echo '%_topdir %(echo $HOME)/rpmbuild-couchdb' > ~/.rpmmacros
```

### Install build dependencies

```
sudo yum install yum-utils
sudo yum-builddep SPECS/couchdb.spec
```

### Get the source

```
sudo yum install rpmdevtools
spectool -g -R SPECS/couchdb.spec
```

### Build the RPM

```
rpmbuild -ba SPECS/couchdb.spec
```


## Author

* Written and maintained by Craig Dunn <craig@craigdunn.org> (@crayfishx)

## License

Licensed under the Apache 2.0 License, please see README for details.


