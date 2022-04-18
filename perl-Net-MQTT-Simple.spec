#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	MQTT-Simple
Summary:	Net::MQTT::Simple - Minimal MQTT version 3 interface
Summary(pl.UTF-8):	Net::MQTT::Simple - minimalistyczny interfejs do MQTT w wersji 3
Name:		perl-Net-MQTT-Simple
Version:	1.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2c6fa5b0f4eba18da80b8d68f798768
URL:		http://search.cpan.org/dist/Net-MQTT-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module consists of only one file and has no dependencies except
core Perl modules, making it suitable for embedded installations where
CPAN installers are unavailable and resources are limited.

Only basic MQTT functionality is provided; if you need more, you'll
have to use the full-featured Net::MQTT instead.

Connections are set up on demand, automatically reconnecting to the
server if a previous connection had been lost.

Because sensor scripts often run unattended, connection failures will
result in warnings (on STDERR if you didn't override that) without
throwing an exception.

Please refer to Net::MQTT::Simple::SSL for more information about
encrypted and authenticated connections.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Net/MQTT/Simple
%{perl_vendorlib}/Net/MQTT/Simple.pm
%{perl_vendorlib}/Net/MQTT/Simple/SSL.pm
%attr(755,root,root) %{_bindir}/mqtt-simple
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
