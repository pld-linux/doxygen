#
# Conditional build:
# _without_qt	- without doxywizard (qt-based)
#
Summary:	Doxygen is the documentation system for C/C++
Summary(pl):	System dokumentowania dla C/C++
Summary(pt_BR):	Um sistema de documentaГЦo para C/C++
Summary(ru):	Система документирования для C та C++
Summary(uk):	Система документування для C та C++
Name:		doxygen
Version:	1.3.3
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}.src.tar.gz
# Source0-md5:	ce5523a8dc6fd39acf713696e7cc3a3e
Patch0:		%{name}-system-libpng.patch
Patch1:		%{name}-qtstyle.patch
Patch2:		%{name}-qt-dirs.patch
URL:		http://www.doxygen.org/
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{!?_without_qt:BuildRequires:	qt-devel >= 2.1.0}
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-plain-misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# because of qt
%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
Doxygen to system dokumentowania dla C, C++ i IDL. Mo©e generowaФ
dokumentacjЙ klas on-line (w HTML) lub podrЙcznik off-line (w LaTeX-u)
z zestawu udokumentowanych plikСw ╪rСdЁowych. Ma tak©e mo©liwo╤Ф
generowania stron man i konwersji na Postscript, PDF z hiperЁ╠czami
oraz skompresowany HTML. Dokumentacja jest wyci╠gana bezpo╤rednio ze
╪rСdeЁ.

Doxygen mo©e byФ skonfigurowany tak©e do wyci╠gania struktury kodu z
nieudokumentowanych plikСw ╪rСdЁowych. Mo©e byФ to przydatne do
szybkiego odnalezienia siЙ w du©ych ╪rСdЁach.

%description -l pt_BR
Doxygen И uma sistema de documentaГЦo para C e C++ que gera um class
browser on-line (em HTML) e/ou um manual de referencia off-line (em
LaTeX) a partir de um conjunto de fontes documentados. A documentaГЦo
И extraida diretamente a partir dos fontes.

%description -l ru
Doxygen - это система документирования для C, C++ и IDL. Она может
создать онлайновый броузер классов (в HTML) и/или оффлайновый
справочник (в LaTeX) из набора документированных файлов. Есть также
поддержка создания man-страниц и конвертации сгенерированного вывода в
Postscript, PDF с гиперссылками и компрессированный HTML. Документация
извлекается непосредственно из исходных файлов.

Doxygen можно также сконфигурировать для получения структуры кода из
нелокументированных исходных файлов. Это может быть очень полезным для
того, чтобы бысто разобраться в большом проекте.

%description -l uk
Doxygen - це система документування для C, C++ та IDL. Вона може
створити онлайновий броузер клас╕в (в HTML) та/чи оффлайновий дов╕дник
(в LaTeX) з набору документованих вих╕дних файл╕в. ╢ також п╕дтримка
для створення man-стор╕нок та конвертац╕╖ згенерованого виводу в
Postscript, PDF з г╕перл╕нками та компресований HTML. Документац╕я
видобува╓ться безпосердньо з вих╕дних файл╕в.

Doxygen можна також зконф╕гурувати для отримання структури коду з
недокументованих вих╕дних файл╕в. Це може бути дуже корисним для того,
щоб швидко роз╕братися у великому проект╕.

%package doxywizard
Summary:	A GUI front-end for creating and editing configuration files
Summary(pl):	GUI do tworzenia i edycji plikСw konfiguracyjnych
Summary(pt_BR):	Wizard grАfico para o Doxygen
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	qt >= 2.1.0

%description doxywizard
Doxywizard is a GUI front-end for creating and editing configuration
files that are used by doxygen.

%description doxywizard -l pl
Doxywizard to frontend z graficznym interfejsem do tworzenia i edycji
plikСw konfiguracyjnych u©ywanych przez doxygen.

%description doxywizard -l pt_BR
Wizard grАfico para o Doxygen

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf libpng

%build
export QTDIR=%{_prefix}
# don't change it to %%configure, not autoconf-generated!
./configure \
	--prefix %{_prefix} \
	--perl %{_bindir}/perl \
	--install %{_bindir}/install \
	%{!?_without_qt:--with-doxywizard}

%{__make} QTDIR=%{_prefix} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags} \
	-DQT_NO_CODECS -DQT_LITE_UNICODE -fno-rtti -fno-exceptions"

%{__make} docs
#%%{__make} pdf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/doxy* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html examples README LICENSE
%attr(755,root,root) %{_bindir}/doxygen
%attr(755,root,root) %{_bindir}/doxytag
%attr(755,root,root) %{_bindir}/doxysearch

%if 0%{!?_without_qt:1}
%files doxywizard
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/doxywizard
%endif
