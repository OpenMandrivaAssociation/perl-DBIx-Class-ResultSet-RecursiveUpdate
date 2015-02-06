%define upstream_name    DBIx-Class-ResultSet-RecursiveUpdate
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	DBIx-Class extension for providing recursive updates
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp::Clan) >= 6.40
BuildRequires:	perl(DBD::SQLite) >= 1.210
BuildRequires:	perl(DBIx::Class) >= 0.81.30
BuildRequires:	perl(DBIx::Class::IntrospectableM2M)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Readonly) >= 1.30
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(SQL::Translator) >= 0.110.60
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildArch:	noarch

%description
You can feed the ->create method of DBIx::Class with a recursive datastructure
and have the related records created. Unfortunately you cannot do a similar
thing with update_or_create. This module tries to fill that void until
DBIx::Class has an api itself.

The functional interface can be used without modifications of the model, for
example by form processors like HTML::FormHandler::Model::DBIC.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 677431
- update to new version 0.24

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.230.0-2
+ Revision: 657404
- rebuild for updated spec-helper

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.230.0-1
+ Revision: 643374
- update to new version 0.23

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.210.0-2mdv2011.0
+ Revision: 624770
- Add the missing SQL::Abstract dependency
- import perl-DBIx-Class-ResultSet-RecursiveUpdate

