%define upstream_name	 Crypt-RandPasswd
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Random password generator based on FIPS-181
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/Crypt-RandPasswd-%{upstream_version}.tar.gz

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 680868
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 403036
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.02-8mdv2009.0
+ Revision: 256321
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.02-6mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-6mdv2007.0
+ Revision: 107905
- rebuild
- Import perl-Crypt-RandPasswd

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-5mdk
- spec cleanup
- better URL
- enable tests
- %%mkrel

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-4mdk
- fix buildrequires in a backward compatible way

* Thu Aug 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-3mdk 
- rpmbuildupdate aware

* Mon Mar 01 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-2mdk
- fixed dir ownership (distlint)

* Sun Feb 01 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-1mdk
- first mdk release




