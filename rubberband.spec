Summary:	Audio time-stretching and pitch-shifting library
Name:		rubberband
Version:	1.8.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://code.breakfastquay.com/attachments/download/23/%{name}-%{version}.tar.bz2
# Source0-md5:	6c2b4e18a714bcc297d0db81a10f9348
BuildRequires:	fftw3-devel
BuildRequires:	ladspa-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkg-config
BuildRequires:	vamp-plugin-sdk-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rubber Band is a block-based phase vocoder with phase resets
on percussive transients, an adaptive stretch ratio between phase
reset points, and a "lamination" method to improve vertical phase
coherence.

%package libs
Summary:	rubberband library
Group:		Libraries

%description libs
This is the package containing rubberband library.

%package devel
Summary:	Header files for rubberband library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for rubberband
library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT			\
	INSTALL_LADSPADIR="%{_libdir}/ladspa"	\
	INSTALL_LIBDIR="%{_libdir}"		\
	INSTALL_PKGDIR="%{_pkgconfigdir}"	\
	INSTALL_VAMPDIR="%{_libdir}/vamp"

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/rubberband

%attr(755,root,root) %{_libdir}/ladspa/ladspa-rubberband.so
%{_libdir}/ladspa/ladspa-rubberband.cat
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf

%attr(755,root,root) %{_libdir}/vamp/vamp-rubberband.so
%{_libdir}/vamp/vamp-rubberband.cat

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/librubberband.so.2
%attr(755,root,root) %{_libdir}/librubberband.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librubberband.so
%{_includedir}/rubberband
%{_pkgconfigdir}/*.pc

