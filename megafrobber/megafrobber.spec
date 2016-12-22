Name:           megafrobber
Version:        0.1
Release:        1%{?dist}
Summary:        Megafrob ur downloads.

License:        MIT
URL:            http://github.com/boosted-chimps/boosted-examples/megafrobber
Source0:        %{name}-%{version}.tar.gz



%description
Megafrob ur downloads for fun and profit.

%prep
%setup -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp megafrobber $RPM_BUILD_ROOT/usr/bin

%files
/usr/bin/megafrobber

%changelog
* Wed Dec 21 2016 Andrew Butcher <abutcher@redhat.com>
- First build.
