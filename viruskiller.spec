Summary:	An arcade shoot 'em up
Summary(pl.UTF-8):	Zręcznościowa strzelanka
Name:		viruskiller
Version:	1.03
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.parallelrealities.co.uk/download/viruskiller/%{name}-%{version}-1.tar.gz
# Source0-md5:	ac74f8a49d249a87e3e77cadd9aa6fa9
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.parallelrealities.co.uk/projects/virusKiller.php
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viruses are flooding into your machine via security holes in an OS
vendor's products. The little buggers are making their way towards
some of your file directories and it's up to you to blast them before
they can destroy your files!

%description -l pl.UTF-8
Wirusy zalewają komputer gracza omijając zabezpieczenia systemu
operacyjnego. Małe robaki przedzierają się do kilku plików i katalogów
i zadaniam gracza jest ich zniszczenie zapobiegając niszczeniu plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/viruskiller
%dir %{_datadir}/games/viruskiller
%{_datadir}/games/viruskiller/viruskiller.pak
%{_desktopdir}/viruskiller.desktop
%{_iconsdir}/hicolor/*/apps/viruskiller.png
