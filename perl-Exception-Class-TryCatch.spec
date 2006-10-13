#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Exception
%define		pnam	Class-TryCatch
Summary:	Exception::Class::TryCatch - syntactic try/catch sugar for use with Exception::Class
Summary(pl):	Exception::Class::TryCatch - sk³adniowe try/catch do u¿ywania z Exception::Class
Name:		perl-Exception-Class-TryCatch
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e77f27aff6e6b6845944bb677127fd79
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Exception-Class >= 1.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exception::Class::TryCatch - syntactic try/catch sugar for use with
Exception::Class.

%description -l pl
Exception::Class::TryCatch - sk³adniowe try/catch do u¿ywania z
Exception::Class.

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
%doc README Changes LICENSE
%{perl_vendorlib}/Exception
%{_mandir}/man3/*
