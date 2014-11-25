#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Exception
%define		pnam	Class-TryCatch
%include	/usr/lib/rpm/macros.perl
Summary:	Exception::Class::TryCatch - syntactic try/catch sugar for use with Exception::Class
Summary(pl.UTF-8):	Exception::Class::TryCatch - składniowe try/catch do używania z Exception::Class
Name:		perl-Exception-Class-TryCatch
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d9943ce5e251437312a11001b9531f43
URL:		http://search.cpan.org/dist/Exception-Class-TryCatch/
BuildRequires:	perl-Exception-Class >= 1.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exception::Class::TryCatch - syntactic try/catch sugar for use with
Exception::Class.

%description -l pl.UTF-8
Exception::Class::TryCatch - składniowe try/catch do używania z
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
