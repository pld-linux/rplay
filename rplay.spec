Summary:	Flexible network audio system
Summary(pl):	Elastyczny sieciowy system d¼wiêku
Name:		rplay
Version:	3.3.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://rplay.doit.org/dist/%{name}-%{version}.tar.gz
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

%description -l pl
rplay to elastyczny sieciowy system d¼wiêku pozwalaj±cy na odtwarzanie
d¼wiêku na i z lokalnych i zdalnych systemów. D¼wiêki mog± byæ
odtwarzane z lub bez przesy³ania danych po sieci przy u¿yciu UDP lub
TCP. Serwery d¼wiêku rplay mog± byæ skonfigurowane tak, by dzieli³y
pliki d¼wiêkowe miêdzy siebie. Obs³ugê rplay ma kilka aplikacji, w tym
xpilot, xlockmore, xboing, fvwm i ctwm.

%package devel
Summary:	rplay header file
Summary(pl):	Plik nag³ówkowy rplay
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
rplay header file.

%description devel -l pl
Plik nag³ówkowy rplay.

%package static
Summary:	rplay static library
Summary(pl):	Statyczna biblioteka rplay
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
rplay static library.

%description static -l pl
Statyczna biblioteka rplay.

%prep
%setup -q

%build
#cd rx
#%{__autoconf}
#cd ..
%{__autoconf}
CFLAGS="%{rpmcflags} -D_GNU_SOURCE"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix} \
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
