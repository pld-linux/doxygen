Summary:	Doxygen is the documentation system for C/C++
Summary(pl):	System dokumentowania dla C/C++
Summary(pt_BR):	Um sistema de documentação para C/C++
Name:		doxygen
Version:	1.2.14
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}.src.tar.gz
URL:		http://www.stack.nl/~dimitri/doxygen/
BuildRequires:	qt-devel => 2.1
BuildRequires:	libstdc++-devel
BuildRequires:	tetex
BuildRequires:	tetex-latex
BuildRequires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Doxygen is a documentation system for C, C++ and IDL. It can generate
an on-line class browser (in HTML) and/or an off-line reference manual
(in LaTeX) from a set of documented source files. There is also
support for generating man pages and for converting the generated
output into Postscript, hyperlinked PDF or compressed HTML. The
documentation is extracted directly from the sources.

Doxygen can also be configured to extract the code-structure from
undocumented source files. This can be very useful to quickly find
your way in large source distributions.

%description -l pl
Doxygen to system dokumentowania dla C, C++ i IDL. Mo¿e generowaæ
dokumentacjê klas on-line (w HTML) lub podrêcznik off-line (w LaTeX-u)
z zestawu udokumentowanych plików ¼ród³owych. Ma tak¿e mo¿liwo¶æ
generowania stron man i konwersji na Postscript, PDF z hiper³±czami
oraz skompresowany HTML. Dokumentacja jest wyci±gana bezpo¶rednio ze
¼róde³.

Doxygen mo¿e byæ skonfigurowany tak¿e do wyci±gania struktury kodu z
nieudokumentowanych plików ¼ród³owych. Mo¿e byæ to przydatne do
szybkiego odnalezienia siê w du¿ych ¼ród³ach.

%description -l pt_BR
Doxygen é uma sistema de documentação para C e C++ que gera um class
browser on-line (em HTML) e/ou um manual de referencia off-line (em
LaTeX) a partir de um conjunto de fontes documentados. A documentação
é extraida diretamente a partir dos fontes.

%package doxywizard
Summary:	A GUI front-end for creating and editing configuration files
Summary(pl):	GUI do tworzenia i edycji plików konfiguracyjnych
Group:		X11/Applications
Requires:	%{name} = %{version}
Requires:	qt >= 2.2

%description doxywizard
Doxywizard is a GUI front-end for creating and editing configuration
files that are used by doxygen.

%description doxywizard -l pl
Doxywizard to frontend z graficznym interfejsem do tworzenia i edycji
plików konfiguracyjnych u¿ywanych przez doxygen.

%prep
%setup -q

%build
export QTDIR=%{_prefix}
## don't change it to %%configure!!!
./configure \
	--prefix %{_prefix} \
	--perl %{_bindir}/perl \
#	--with-doxywizard

%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags} \
	-DQT_NO_CODECS -DQT_LITE_UNICODE -fno-rtti -fno-exceptions"

%{__make} docs
%{__make} ps
mkdir ps
mv -f latex/doxygen_manual.ps ps

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}

install bin/doxy* ${RPM_BUILD_ROOT}%{_bindir}

gzip -9nf README LICENSE

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc html examples *.gz
%attr(755,root,root) %{_bindir}/doxygen
%attr(755,root,root) %{_bindir}/doxytag
%attr(755,root,root) %{_bindir}/doxysearch

#%files doxywizard
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/doxywizard
