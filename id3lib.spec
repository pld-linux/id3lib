Summary:	A software library for manipulating ID3v1 and ID3v2 tags
Summary(pl):	Biblioteka do zarz±dzania znacznikami ID3v1 oraz ID3v2
Name:		id3lib
Version:	3.7.13
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://download.sourceforge.net/pub/sourceforge/id3lib/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
URL:		http://id3lib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities.

%description -l pl
Pakiet dostarcza bibliotekÍ pozwalaj±c± na manipulacje znacznikami
ID3v1 oraz ID3v2. Dostarcza on przekonywuj±cy interfejs dla
programistÛw pozwalaj±c na dodawanie moøliwo∂ci obs≥ugi znacznikÛw
ID3v1/2 w ich w≥asnych aplikacjach. Moøliwo∂ci biblioteki to
identyfikacja prawid≥owych znacznikÛw, automatyczna konwersja
rozmiaru, synchronizacja ramek, dekompresja itp.

%package devel
Summary:	Headers for developing programs that will use id3lib
Summary(pl):	Pliki nag≥Ûwkowe dla programistÛw uøywaj±cych id3lib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package contains the headers that programmers will need to
develop applications which will use id3lib, the software library for
ID3v1 and ID3v2 tag manipulation.

%description -l pl devel
Pakiet zawiera pliki nag≥Ûwkowe, ktÛre bÍd± potrzebne programistom
chc±cych rozwijaÊ aplikacje uøywaj±ce biblioteki id3lib.

%package static
Summary:	Static id3lib libraies
Summary(pl):	Statyczne biblioteki id3lib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static id3lib libraies.

%description -l pl static
Statyczne biblioteki id3lib.

%prep
%setup -q
%patch0 -p1

%build
cd zlib
	aclocal
	autoconf
cd ..
cd popt
	aclocal
	autoconf
cd ..
rm -f missing
libtoolize --copy --force
aclocal -I m4
autoconf
automake -a -c
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog HISTORY NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {A*,H*,N*,R*,T*}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
