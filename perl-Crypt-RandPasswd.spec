%define upstream_name	 Crypt-RandPasswd
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Random password generator based on FIPS-181

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*



