# NOTE: on upgrades, beware of texlive features available in PLD
#
# Conditional build:
%bcond_without	qt	# without doxywizard (qt-based)
%bcond_without	xapian	# without doxysearch (xapian based)
#
Summary:	Doxygen is the documentation system for C/C++
Summary(es.UTF-8):	Doxygen es el sistema de documentación para C/C++
Summary(pl.UTF-8):	System dokumentowania dla C/C++
Summary(pt_BR.UTF-8):	Um sistema de documentação para C/C++
Summary(ru.UTF-8):	Система документирования для C та C++
Summary(uk.UTF-8):	Система документування для C та C++
Name:		doxygen
Version:	1.8.10
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Tools
# only latest
#Source0Download: https://www.doxygen.nl/download.html
#Source0:	https://www.doxygen.nl/files/%{name}-%{version}.src.tar.gz
Source0:	http://downloads.sourceforge.net/doxygen/%{name}-%{version}.src.tar.gz
# Source0-md5:	79767ccd986f12a0f949015efb5f058f
Patch0:		%{name}-doc.patch
Patch1:		flex2.6.patch
URL:		https://www.doxygen.nl/
%{?with_qt:BuildRequires:	QtGui-devel >= 4.3}
%{?with_qt:BuildRequires:	QtXml-devel >= 4.3}
BuildRequires:	bison
BuildRequires:	cmake >= 2.8.12
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	python >= 2
%{?with_qt:BuildRequires:	qt4-build >= 4.3}
%{?with_qt:BuildRequires:	qt4-qmake >= 4.3}
BuildRequires:	texlive-latex
BuildRequires:	texlive-pdftex
%{?with_xapian:BuildRequires:	xapian-core-devel}
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

%description -l es.UTF-8
Doxygen es un sistema de documentación para C, C++ e IDL. Es capaz de
generar un navegador on-line entre clases (en HTML) y-o un manual
off-line de referencia (en LaTeX) a partir de un conjunto de ficheros
de código fuente documentados. También hay soporte para generar
páginas man y para convertir la generada salida an Postscript, PDF con
hiperenlaces o HTML comprimido. La documentación se extrae
directamente de los fuentes.

Doxygen puede también ser configurado a extraer la estructura del
código de código fuente que carece de documentación. Eso puede ser muy
útil para orientarse rápidamente en distribuciones grandes de código
fuente.

%description -l pl.UTF-8
Doxygen to system dokumentowania dla C, C++ i IDL. Może generować
dokumentację klas on-line (w HTML-u) lub podręcznik off-line (w
LaTeXu) z zestawu udokumentowanych plików źródłowych. Ma także
możliwość generowania stron man i konwersji na Postscript, PDF z
hiperłączami oraz skompresowany HTML. Dokumentacja jest wyciągana
bezpośrednio ze źródeł.

Doxygen może być skonfigurowany także do wyciągania struktury kodu z
nieudokumentowanych plików źródłowych. Może być to przydatne do
szybkiego odnalezienia się w dużych źródłach.

%description -l pt_BR.UTF-8
Doxygen é uma sistema de documentação para C e C++ que gera um class
browser on-line (em HTML) e/ou um manual de referencia off-line (em
LaTeX) a partir de um conjunto de fontes documentados. A documentação
é extraida diretamente a partir dos fontes.

%description -l ru.UTF-8
Doxygen - это система документирования для C, C++ и IDL. Она может
создать онлайновый броузер классов (в HTML) и/или оффлайновый
справочник (в LaTeX) из набора документированных файлов. Есть также
поддержка создания man-страниц и конвертации сгенерированного вывода в
Postscript, PDF с гиперссылками и компрессированный HTML. Документация
извлекается непосредственно из исходных файлов.

Doxygen можно также сконфигурировать для получения структуры кода из
нелокументированных исходных файлов. Это может быть очень полезным для
того, чтобы бысто разобраться в большом проекте.

%description -l uk.UTF-8
Doxygen - це система документування для C, C++ та IDL. Вона може
створити онлайновий броузер класів (в HTML) та/чи оффлайновий довідник
(в LaTeX) з набору документованих вихідних файлів. Є також підтримка
для створення man-сторінок та конвертації згенерованого виводу в
Postscript, PDF з гіперлінками та компресований HTML. Документація
видобувається безпосердньо з вихідних файлів.

Doxygen можна також зконфігурувати для отримання структури коду з
недокументованих вихідних файлів. Це може бути дуже корисним для того,
щоб швидко розібратися у великому проекті.

%package search
Summary:	Search tools for Doxygen
Summary(pl.UTF-8):	Narzędzia do przeszukiwania dla Doxygena
Group:		Development/Tools
Conflicts:	doxygen < 1:1.3.4

%description search
Search tools for Doxygen.

%description search -l pl.UTF-8
Narzędzia do przeszukiwania dla Doxygena.

%package doxywizard
Summary:	A GUI front-end for creating and editing configuration files
Summary(es.UTF-8):	Un front-end GUI para crear y editar ficheros de configuración
Summary(pl.UTF-8):	GUI do tworzenia i edycji plików konfiguracyjnych
Summary(pt_BR.UTF-8):	Wizard gráfico para o Doxygen
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doxywizard
Doxywizard is a GUI front-end for creating and editing configuration
files that are used by doxygen.

%description doxywizard -l es.UTF-8
Doxywizard es un front-end GUI para crear y editar los ficheros de
configuración que son usados por doxygen.

%description doxywizard -l pl.UTF-8
Doxywizard to frontend z graficznym interfejsem do tworzenia i edycji
plików konfiguracyjnych używanych przez doxygen.

%description doxywizard -l pt_BR.UTF-8
Wizard gráfico para o Doxygen.

%package latex
Summary:	LaTeX packages to support Doxygen-generated files compilation
Summary(pl.UTF-8):	Pakiety LaTeXa pozwalające na kompilowanie plików wygenerowanych przez Doxygena
Group:		Applications/Publishing
Requires:	/usr/bin/pdflatex
Requires:	/usr/bin/makeindex
Requires:	tex(adjustbox)
# TODO: generic dependencies instead of texlive-specific:
#Requires:	tex(psnfss)
#Requires:	tex(wasysym)
# TODO: generic dependencies instead of texlive-specific:
Requires:	texlive-fonts-larm
# alltt array calc fancyhdr fixltx2e float fontenc geometry hyperref ifpdf ifthen inputenc makeidx multirow natbib sectsty textcomp tocloft verbatim xcolor xtab
Requires:	texlive-latex
# amssymb
Requires:	texlive-latex-ams
# ??? obsolete?
Requires:	texlive-latex-cyrillic
# ??? obsolete?
Requires:	texlive-latex-extend
# courier helvet
Requires:	texlive-latex-psnfss
Requires:	texlive-latex-wasysym
Requires:	texlive-makeindex

%description latex
This metapackage installs all LaTeX packages required to compile PDF
documentation from Doxygen-generated LaTeX files.

%description latex -l pl.UTF-8
Ten metapakiet instaluje wszystkie pakiety LaTeXa otrzebne do
skompilowania dokumentacji w formacie PDF z plików LaTeXa
wygenerowanych przez Doxygena.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF \
	-Dbuild_doc=ON \
	%{?with_xapian:-Dbuild_search=ON} \
	%{?with_qt:-Dbuild_wizard=ON}

%{__make}

%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md build/html
%attr(755,root,root) %{_bindir}/doxygen
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/doxygen.1*

%if %{with xapian}
%files search
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/doxyindexer
%attr(755,root,root) %{_bindir}/doxysearch.cgi
%{_mandir}/man1/doxyindexer.1*
%{_mandir}/man1/doxysearch.1*
%endif

%if %{with qt}
%files doxywizard
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/doxywizard
%{_mandir}/man1/doxywizard.1*
%endif

%files latex
%defattr(644,root,root,755)
