# Megafrobber RPM

## Setup

Install `rpmdevtools` and generate an `rpmbuild` tree within your home directory.

```
sudo dnf install -y rpmdevtools
cd && rpmdev-setuptree
```

## Building

Use the Makefile to build an rpm package. The final package will be created as `~/rpmbuild/RPMS/x86_64/megafrobber-0.1-1.fc24.x86_64.rpm`.

```
make rpm
```

## Installing

```
sudo dnf install -y ~/rpmbuild/RPMS/x86_64/megafrobber-0.1-1.fc24.x86_64.rpm
```
