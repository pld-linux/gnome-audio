%define  ver     1.0.0
%define  rel     6
%define  prefix  /usr

Summary: Sounds for GNOME events.
Name: gnome-audio
Version: %ver
Release: %rel
Copyright: LGPL
Group: Applications/Multimedia
Source: ftp://ftp.gnome.org/pub/GNOME/sources/gnome-audio-%{ver}rh.tar.gz
BuildRoot:/var/tmp/gnome-audio-%{PACKAGE_VERSION}-root
URL: http://www.gnome.org
Docdir: %{prefix}/doc
BuildArchitectures: noarch

%description
If you use the GNOME desktop environment, you may want to
install this package of complementary sounds.

%prep
%setup -q

%package extra
Summary: Optional Sounds for GNOME events.
Group: System Environment/Libraries

%description extra
This package contains extra sound files useful for customizing the
sounds that the GNOME desktop environment makes.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{prefix} install 

#
# cleanout some stuff we'd rather not have as default
#
rm -f $RPM_BUILD_ROOT/%{prefix}/share/sounds/login.wav
rm -f $RPM_BUILD_ROOT/%{prefix}/share/sounds/logout.wav

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%{prefix}/share/sounds/info.wav
%{prefix}/share/sounds/error.wav
%{prefix}/share/sounds/warning.wav
%{prefix}/share/sounds/generic.wav
%{prefix}/share/sounds/question.wav
%{prefix}/share/sounds/shutdown1.wav
%{prefix}/share/sounds/startup3.wav
%{prefix}/share/sounds/panel
%{prefix}/share/sounds/gtk-events

#symlinks
#%{prefix}/share/sounds/login.wav
#%{prefix}/share/sounds/logout.wav

%files extra
%{prefix}/share/sounds/card_shuffle.wav
%{prefix}/share/sounds/phone.wav
%{prefix}/share/sounds/startup1.wav
%{prefix}/share/sounds/startup2.wav
