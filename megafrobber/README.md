# Megafrobber RPM

In this example we will create an rpm package that installs a single python script `/usr/bin/megafrobber`.

## Setup

Install `rpmdevtools` and generate an `rpmbuild` tree within your home directory.

```
$ sudo dnf install -y rpmdevtools
$ cd && rpmdev-setuptree
```

This will generate an `rpmbuild` directory with the following subdirectories.

```
rpmbuild
├── BUILD
├── RPMS
├── SOURCES
├── SPECS
└── SRPMS
```

## Building

Use the Makefile to build an rpm package. The final package will be created as `~/rpmbuild/RPMS/x86_64/megafrobber-0.1-1.fc24.x86_64.rpm`.

```
$ make rpm
```

## Installing

```
$ sudo dnf install -y ~/rpmbuild/RPMS/x86_64/megafrobber-0.1-1.fc24.x86_64.rpm
```

## Running

Once installed, simply run `megafrobber`.

```
$ megafrobber --help
Usage: megafrobber [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
    --name TEXT      The person to greet.
      --help           Show this message and exit.
```
