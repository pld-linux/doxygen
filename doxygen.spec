#
# Conditional build:
%bcond_without	qt	# without doxywizard (qt-based)
#
Summary:	Doxygen is the documentation system for C/C++
Summary(es.UTF-8):	Doxygen es el sistema de documentación para C/C++
Summary(pl.UTF-8):	System dokumentowania dla C/C++
Summary(pt_BR.UTF-8):	Um sistema de documentação para C/C++
Summary(ru.UTF-8):	Система документирования для C та C++
Summary(uk.UTF-8):	Система документування для C та C++
Name:		doxygen
Version:	1.5.7.1
Release:	3
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}.src.tar.gz
# Source0-md5:	bc35dfd52bdae0247b862e67e0cbe7d7
Patch0:		%{name}-system-libpng.patch
Patch1:		%{name}-qt-dirs.patch
Patch2:		%{name}-lib64.patch
Patch3:		%{name}-qt-thread.patch
Patch4:		%{name}-64bit.patch
URL:		http://www.doxygen.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	python
%{?with_qt:BuildRequires:	qt-devel >= 2.1.0}
BuildRequires:	texlive-latex
BuildRequires:	texlive-pdftex
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

%package doxywizard
Summary:	A GUI front-end for creating and editing configuration files
Summary(es.UTF-8):	Un front-end GUI para crear y editar ficheros de configuración
Summary(pl.UTF-8):	GUI do tworzenia i edycji plików konfiguracyjnych
Summary(pt_BR.UTF-8):	Wizard gráfico para o Doxygen
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	qt >= 2.1.0

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if "%{_lib}" == "lib64"
%patch2 -p1
%endif
%patch3 -p1

rm -rf libpng src/unistd.h addon/doxywizard/Makefile.doxywizard

%build
export QTDIR=%{_prefix}
# don't change it to %%configure, not autoconf-generated!
./configure \
	--prefix %{_prefix} \
	--perl %{__perl} \
	--install %{_bindir}/install \
	%{?with_qt:--with-doxywizard}

%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	LINK="%{__cxx}" \
	QTDIR="%{_prefix}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags} -DQT_NO_CODECS -DQT_LITE_UNICODE -DNODEBUG -fno-rtti -fno-exceptions"

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
%doc html examples README
%attr(755,root,root) %{_bindir}/doxygen
%attr(755,root,root) %{_bindir}/doxytag

%if %{with qt}
%files doxywizard
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/doxywizard
%endif
