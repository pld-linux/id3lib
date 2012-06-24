Summary:	A software library for manipulating ID3v1 and ID3v2 tags
Summary(pl):	Biblioteka do zarz�dzania znacznikami ID3v1 oraz ID3v2
Name:		id3lib
Version:	3.7.13
Release:	5
License:	LGPL
Group:		Libraries
Source0:	ftp://download.sourceforge.net/pub/sourceforge/id3lib/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
Patch1:		%{name}-nozlibpopt.patch
URL:		http://id3lib.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities.

%description -l pl
Pakiet dostarcza bibliotek� pozwalaj�c� na manipulacje znacznikami
ID3v1 oraz ID3v2. Dostarcza on przekonywuj�cy interfejs dla
programist�w pozwalaj�c na dodawanie mo�liwo�ci obs�ugi znacznik�w
ID3v1/2 w ich w�asnych aplikacjach. Mo�liwo�ci biblioteki to
identyfikacja prawid�owych znacznik�w, automatyczna konwersja
rozmiaru, synchronizacja ramek, dekompresja itp.

%package devel
Summary:	Headers for developing programs that will use id3lib
Summary(pl):	Pliki nag��wkowe dla programist�w u�ywaj�cych id3lib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the headers that programmers will need to
develop applications which will use id3lib, the software library for
ID3v1 and ID3v2 tag manipulation.

%description devel -l pl
Pakiet zawiera pliki nag��wkowe, kt�re b�d� potrzebne programistom
chc�cych rozwija� aplikacje u�ywaj�ce biblioteki id3lib.

%package static
Summary:	Static id3lib libraies
Summary(pl):	Statyczne biblioteki id3lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static id3lib libraies.

%description static -l pl
Statyczne biblioteki id3lib.

%package utils
Summary:	Simple id3 utils
Summary(pl):	Proste narz�dzia do id3
Group:		Applications/File
Requires:	%{name} = %{version}

%description utils
Few simple utilities to manipulate on ID3 tags: id3convert, id3cp,
id3info, id3tag.

%description utils -l pl
Kilka prostych narz�dzi do obs�ugi tag�w ID3: id3convert, id3cp,
id3info, id3tag.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal -I m4
%{__autoconf}
%{__automake}
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

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
