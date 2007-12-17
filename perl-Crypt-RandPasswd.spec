%define module	Crypt-RandPasswd
%define name	perl-%{module}
%define version 0.02
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Random password generator based on FIPS-181
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch

%description
This code is a Perl language implementation of the Automated Password Generator
standard, like the program described in "A Random Word Generator For
Pronounceable Passwords" (not available on-line). This code is a re-engineering
of the program contained in Appendix A of FIPS Publication 181, "Standard for
Automated Password Generator". In accordance with the standard, the results
obtained from this program are logically equivalent to those produced by the
standard.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*


