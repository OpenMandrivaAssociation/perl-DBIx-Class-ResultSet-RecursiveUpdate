%define upstream_name    DBIx-Class-ResultSet-RecursiveUpdate
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    DBIx-Class extension for providing recursive updates
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp::Clan) >= 6.40
BuildRequires: perl(DBD::SQLite) >= 1.210
BuildRequires: perl(DBIx::Class) >= 0.81.30
BuildRequires: perl(DBIx::Class::IntrospectableM2M)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(DateTime)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Readonly) >= 1.30
BuildRequires: perl(SQL::Abstract)
BuildRequires: perl(SQL::Translator) >= 0.110.60
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

