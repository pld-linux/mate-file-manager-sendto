Summary:	Caja context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe zarządcy plików Caja do wysyłania plików
Name:		mate-file-manager-sendto
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	6b2d5d6c30ab39ad509ac05692628560
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 1.0.2
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-devel >= 0.13
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-file-manager-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	glib2 >= 1:2.26.0
Requires:	mate-file-manager >= 1.1.0
Suggests:	file-roller
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-file-manager-sendto provides a Caja context menu for sending
files via other desktop applications. It's a fork of nautilus-sendto
from GNOME.

%description -l pl.UTF-8
mate-file-manager-sendto dostarcza menu kontekstowe dla zarządcy
plików Caja do wysyłania plików poprzez inne aplikacje biurkowe. Jest
to odgałęzienie programu nautilus-sendto z GNOME.

%package burn
Summary:	mate-file-manager-sendto CD/DVD Creator plugin
Summary(pl.UTF-8):	Wtyczka mate-file-manager-sendto dla kreatora CD/DVD
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	brasero

%description burn
A mate-file-manager-sendto plugin for sending files to CD/DVD Creator
(Brasero).

%description burn -l pl.UTF-8
Wtyczka mate-file-manager-sendto do wysyłania plików do kreatora
CD/DVD (Brasero).

%package emailclient
Summary:	mate-file-manager-sendto e-mail client plugin
Summary(pl.UTF-8):	Wtyczka mate-file-manager-sendto dla klienta poczty elektronicznej
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description emailclient
A mate-file-manager-sendto plugin for sending files via e-mail client.
Supported e-mail clients are: Evolution 2.0 through 3.0, Balsa,
Thunderbird/Icedove, Seamonkey/Iceape, Sylpheed/Claws Mail, Anjal.

%description emailclient -l pl.UTF-8
Wtyczka mate-file-manager-sendto do wysyłania plików poprzez klienta
poczty elektronicznej. Obsługiwane są: Evolution 2.0 do 3.0, Balsa,
Thunderbird/Icedove, Seamonkey/Iceape, Sylpheed/Claws Mail, Anjal.

%package gajim
Summary:	mate-file-manager-sendto Gajim plugin
Summary(pl.UTF-8):	Wtyczka mate-file-manager-sendto dla Gajima
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	dbus >= 1.0.2
Requires:	gajim >= 0.10.1

%description gajim
A mate-file-manager-sendto plugin for sending files via Gajim.

%description gajim -l pl.UTF-8
Wtyczka mate-file-manager-sentdo do wysyłania plików poprzez Gajima.

%package pidgin
Summary:	mate-file-manager-sendto Pidgin plugin
Summary(pl.UTF-8):	Wtyczka mate-file-manager-sendto dla Pidgina
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	pidgin >= 2.0

%description pidgin
A mate-file-manager-sendto plugin for sending files via Pidgin.

%description pidgin -l pl.UTF-8
Wtyczka mate-file-manager-sentdo do wysyłania plików poprzez Pidgina.

%package upnp
Summary:	mate-file-manager-sendto UPnP media server plugin
Summary(pl.UTF-8):	Wtyczka mate-file-manager-sendto dla serwera multimediów UPnP
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gupnp-tools

%description upnp
A mate-file-manager-sendto plugin for sending files to UPnP media
server.

%description upnp -l pl.UTF-8
Wtyczka mate-file-manager-sendto do wysyłania plików do serwera
multimediów UPnP.

%package devel
Summary:	Header files for caja-sendto extensions
Summary(pl.UTF-8):	Pliki nagłówkowe dla rozszerzeń caja-sendto
Group:		Development/Libraries
# doesn't require base
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+2-devel >= 2:2.18

%description devel
Header files for caja-sendto extensions.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla rozszerzeń caja-sendto.

%package apidocs
Summary:	caja-sendto API documentation
Summary(pl.UTF-8):	Dokumentacja API caja-sendto
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
caja-sendto API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API caja-sendto.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-schemas-compile \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/{caja-sendto/plugins,caja/extensions-2.0}/*.la

# mate < 1.5 did not exist in PLD, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/caja-sendto-convert

%find_lang caja-sendto

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f caja-sendto.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/caja-sendto
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-sendto
%{_mandir}/man1/caja-sendto.1*

%files burn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstburn.so

%files emailclient
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstemailclient.so

%files gajim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstgajim.so

%files pidgin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files upnp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstupnp.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/caja-sendto
%{_pkgconfigdir}/caja-sendto.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/caja-sendto
