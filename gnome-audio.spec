Summary:	Sounds for GNOME events
Summary(pl):	DzwiЙki dla zdarzeЯ GNOME
Summary(ru):	Поддержка звуковых событий GNOME
Summary(uk):	П╕дтримка звукових под╕й GNOME
Summary(zh_CN):	GNOMEйб╪ЧкЫпХ╣диЫрТнд╪Ч
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

%description -l pl
Je╤li u©ywasz ╤rodowiska GNOME byФ mo©e bЙdziesz chciaЁ uzupeЁniФ
zdarzenia GNOME efektami d╪wiЙkowymi zawartymi w tym pakiecie.

%description -l ru
Вы можете установить этот пакет звуков, если используете GNOME.

%description -l uk
Ви можете встановити цей пакет звук╕в, якщо використову╓те GNOME.

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
