#!/usr/bin/make

VERSION := $(shell grep "Version" megafrobber.spec | cut -d: -f2 | tr -d '[:space:]')

rpm:
	tar -czf megafrobber-$(VERSION).tar.gz megafrobber
	mv megafrobber-$(VERSION).tar.gz ~/rpmbuild/SOURCES/
	rpmbuild -bb megafrobber.spec
