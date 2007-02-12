Summary:	Flexible network audio system
Summary(pl.UTF-8):   Elastyczny sieciowy system dźwięku
Name:		rplay
Version:	3.3.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://rplay.doit.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	e39888f6bea32e1c8cf4a8880b416e56
Patch0:		%{name}-errno.patch
URL:		http://rplay.doit.org/
BuildRequires:	autoconf
BuildRequires:	libgsm-devel
BuildRequires:	readline-devel
BuildRequires:	rx
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rplay is a flexible network audio system that allows sounds to be
played to and from local and remote Unix systems. Sounds can be
played with or without sending audio data over the network using
either UDP or TCP. rplay audio servers can be configured to share
sound files with each other. Support for rplay is included in several
applications. These include xpilot, xlockmore, xboing, fvwm, and ctwm.

%description -l pl.UTF-8
rplay to elastyczny sieciowy system dźwięku pozwalający na odtwarzanie
dźwięku na i z lokalnych i zdalnych systemów. Dźwięki mogą być
odtwarzane z lub bez przesyłania danych po sieci przy użyciu UDP lub
TCP. Serwery dźwięku rplay mogą być skonfigurowane tak, by dzieliły
pliki dźwiękowe między siebie. Obsługę rplay ma kilka aplikacji, w tym
xpilot, xlockmore, xboing, fvwm i ctwm.

%package devel
Summary:	rplay header file
Summary(pl.UTF-8):   Plik nagłówkowy rplay
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
rplay header file.

%description devel -l pl.UTF-8
Plik nagłówkowy rplay.

%package static
Summary:	rplay static library
Summary(pl.UTF-8):   Statyczna biblioteka rplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
rplay static library.

%description static -l pl.UTF-8
Statyczna biblioteka rplay.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL NEWS README README.linux TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/librplay.so
%attr(755,root,root) %{_libdir}/devrplay.so
%{_mandir}/man[158]/*
%{_infodir}/rplay.info*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rplay.h
%{_infodir}/RPLAY.info*
%{_infodir}/RPTP.info*
%{_infodir}/librplay.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/librplay.a
