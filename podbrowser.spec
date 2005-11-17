%include 	/usr/lib/rpm/macros.perl
Summary:	A full-featured Perl Documentation Browser
Summary(pl):	W pe³ni funkcjonalna przegl±darka dokumentacji perlowej
Name:		podbrowser
Version:	0.08
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://jodrell.net/files/podbrowser/%{name}-%{version}.tar.gz
# Source0-md5:	59f11c50e03f348e41de8058d0a30e0b
Patch0:		%{name}-desktop.patch
URL:		http://jodrell.net/projects/podbrowser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodBrowser is a documentation browser for Perl. You can view the
documentation for Perl's builtin functions, its "perldoc" pages,
pragmatic modules and the default and user-installed modules.

%description -l pl
PodBrowser to przegl±darka dokumentacji do Perla. Pozwala przegl±daæ
dokumentacjê do funkcji wbudowanych Perla, strony "perldoc", modu³ów
pragmatycznych oraz modu³ów domy¶lnych i zainstalowanych przez
u¿ytkownika.

%prep
%setup -q
%patch0 -p1

%build
%{__make} PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix}

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
