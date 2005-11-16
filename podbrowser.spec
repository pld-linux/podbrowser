%include 	/usr/lib/rpm/macros.perl
Name:		podbrowser
Summary:	A full-featured Perl Documentation Browser.
Version:	0.08
Release:	0.1
Group:		Development/Tools
License:	GPL
Source0:	http://jodrell.net/files/podbrowser/%{name}-%{version}.tar.gz
# Source0-md5:	59f11c50e03f348e41de8058d0a30e0b
URL:		http://jodrell.net/projects/podbrowser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PodBrowser is a documentation browser for Perl. You can view the
documentation for Perl's builtin functions, its "perldoc" pages,
pragmatic modules and the default and user-installed modules.

%prep
%setup -q

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
%{_datadir}/applications/podbrowser.desktop
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*
%{_datadir}/podbrowser
