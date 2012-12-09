Summary:	A software library for manipulating ID3v1 and ID3v2 tags
Summary(pl.UTF-8):	Biblioteka do zarządzania znacznikami ID3v1 oraz ID3v2
Name:		id3lib
Version:	3.8.3
Release:	10
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/id3lib/%{name}-%{version}.tar.gz
# Source0-md5:	19f27ddd2dda4b2d26a559a4f0f402a7
Patch0:		%{name}-nozlibpopt.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-iconv-in-libc.patch
Patch3:		http://downloads.sourceforge.net/easytag/patch_id3lib_3.8.3_UTF16_writing_bug.diff
Patch4:		%{name}-CVE-2007-4460.patch
Patch5:		%{name}-gcc43.patch
URL:		http://id3lib.sourceforge.net/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake >= 1.5
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, (re)synchronisation of tag frames, seamless tag
(de)compression, and optional padding facilities.

%description -l pl.UTF-8
Pakiet dostarcza bibliotekę pozwalającą na manipulacje znacznikami
ID3v1 oraz ID3v2. Dostarcza on wygodny interfejs dla programistów
pozwalając na dodawanie możliwości obsługi znaczników ID3v1/2 w ich
własnych aplikacjach. Możliwości biblioteki to identyfikacja
prawidłowych znaczników, automatyczna konwersja rozmiaru,
synchronizacja ramek, dekompresja itp.

%package devel
Summary:	Headers for developing programs that will use id3lib
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających id3lib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use id3lib, the software library for
ID3v1 and ID3v2 tag manipulation.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe, które będą potrzebne programistom
chcących rozwijać aplikacje używające biblioteki id3lib.

%package static
Summary:	Static id3lib libraries
Summary(pl.UTF-8):	Statyczne biblioteki id3lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static id3lib libraries.

%description static -l pl.UTF-8
Statyczne biblioteki id3lib.

%package utils
Summary:	Simple id3 utils
Summary(pl.UTF-8):	Proste narzędzia do id3
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description utils
Few simple utilities to manipulate on ID3 tags: id3convert, id3cp,
id3info, id3tag.

%description utils -l pl.UTF-8
Kilka prostych narzędzi do obsługi znaczników ID3: id3convert, id3cp,
id3info, id3tag.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}
cd doc
doxygen

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS HISTORY NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libid3-3.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libid3-3.8.so.3

%files devel
%defattr(644,root,root,755)
%doc ChangeLog doc/
%attr(755,root,root) %{_libdir}/libid3.so
%{_libdir}/libid3.la
%{_includedir}/id3
%{_includedir}/id3.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libid3.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/id3convert
%attr(755,root,root) %{_bindir}/id3cp
%attr(755,root,root) %{_bindir}/id3info
%attr(755,root,root) %{_bindir}/id3tag
