Summary:	Sounds for GNOME events.
Name:		gnome-audio
Version:	1.0.0
Release:	8
License:	LGPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source:		ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-audio/%{name}-%{version}rh.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
URL:		http://www.gnome.org/
BuildArch:	noarch

%define		_prefix		/usr/X11R6

%description
If you use the GNOME desktop environment, you may want to
install this package of complementary sounds.

%prep
%setup -q

%package extra
Summary:	Optional Sounds for GNOME events.
Group:		Applications/Multimedia

%description extra
This package contains extra sound files useful for customizing the
sounds that the GNOME desktop environment makes.

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/sounds/info.wav
%{_datadir}/sounds/error.wav
%{_datadir}/sounds/warning.wav
%{_datadir}/sounds/generic.wav
%{_datadir}/sounds/question.wav
%{_datadir}/sounds/shutdown1.wav
%{_datadir}/sounds/startup3.wav
%{_datadir}/sounds/panel
%{_datadir}/sounds/gtk-events

#symlinks
%{_datadir}/sounds/login.wav
%{_datadir}/sounds/logout.wav

%files extra
%{_datadir}/sounds/card_shuffle.wav
%{_datadir}/sounds/phone.wav
%{_datadir}/sounds/startup1.wav
%{_datadir}/sounds/startup2.wav
