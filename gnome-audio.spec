Summary:	Sounds for GNOME events
Summary(pl):	Dzwiêki dla zdarzeñ GNOME
Name:		gnome-audio
Version:	1.4.0
Release:	2
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-audio/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://www.gnome.org/
Obsoletes:	gnome-audio-extra
BuildArch:	noarch

%define		_prefix		/usr/X11R6

%description
If you use the GNOME desktop environment, you may want to install this
package of complementary sounds.

%description -l pl
Je¶li u¿ywasz ¶rodowiska GNOME byæ mo¿e bêdziesz chcia³ uzupe³niæ
zdarzenia GNOME efektami d¼wiêkowymi zawartymi w tym pakiecie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/sounds/*
