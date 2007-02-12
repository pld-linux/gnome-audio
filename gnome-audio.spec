Summary:	Sounds for GNOME events
Summary(pl.UTF-8):   Dźwięki dla zdarzeń GNOME
Summary(ru.UTF-8):   Поддержка звуковых событий GNOME
Summary(uk.UTF-8):   Підтримка звукових подій GNOME
Summary(zh_CN.UTF-8):   GNOME事件所需的声音文件
Name:		gnome-audio
Version:	2.0.0
Release:	2
License:	LGPL
Group:		X11/Applications/Sound
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	cd14b84af59fb2ec673527d32f4e379f
URL:		http://www.gnome.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gnome-audio-extra

%description
If you use the GNOME desktop environment, you may want to install this
package of complementary sounds.

%description -l pl.UTF-8
Jeśli używasz środowiska GNOME być może będziesz chciał uzupełnić
zdarzenia GNOME efektami dźwiękowymi zawartymi w tym pakiecie.

%description -l ru.UTF-8
Вы можете установить этот пакет звуков, если используете GNOME.

%description -l uk.UTF-8
Ви можете встановити цей пакет звуків, якщо використовуєте GNOME.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/sounds/*
