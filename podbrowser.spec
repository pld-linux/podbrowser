%include 	/usr/lib/rpm/macros.perl
Summary:	A full-featured Perl Documentation Browser
Summary(pl.UTF-8):	W pełni funkcjonalna przeglądarka dokumentacji perlowej
Name:		podbrowser
Version:	0.09
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://jodrell.net/files/podbrowser/%{name}-%{version}.tar.gz
# Source0-md5:	240e1a31df328ee4029724b2d4acecfe
Patch0:		%{name}-desktop.patch
URL:		http://jodrell.net/projects/podbrowser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodBrowser is a documentation browser for Perl. You can view the
documentation for Perl's builtin functions, its "perldoc" pages,
pragmatic modules and the default and user-installed modules.

%description -l pl.UTF-8
PodBrowser to przeglądarka dokumentacji do Perla. Pozwala przeglądać
dokumentację do funkcji wbudowanych Perla, strony "perldoc", modułów
pragmatycznych oraz modułów domyślnych i zainstalowanych przez
użytkownika.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/podbrowser.desktop
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*
%{_datadir}/podbrowser
