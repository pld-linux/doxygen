
%bcond_without qt	# without doxywizard (qt-based)

Summary:	Doxygen is the documentation system for C/C++
Summary(es):	Doxygen es el sistema de documentación para C/C++
Summary(pl):	System dokumentowania dla C/C++
Summary(pt_BR):	Um sistema de documentação para C/C++
Summary(ru):	óÉÓÔÅÍÁ ÄÏËÕÍÅÎÔÉÒÏ×ÁÎÉÑ ÄÌÑ C ÔÁ C++
Summary(uk):	óÉÓÔÅÍÁ ÄÏËÕÍÅÎÔÕ×ÁÎÎÑ ÄÌÑ C ÔÁ C++
Name:		doxygen
Version:	1.3.6
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}.src.tar.gz
# Source0-md5:	74d3cfb6463bfd4ed1d051153375156d
Patch0:		%{name}-system-libpng.patch
Patch1:		%{name}-qtstyle.patch
Patch2:		%{name}-qt-dirs.patch
Patch3:		%{name}-lib64.patch
URL:		http://www.doxygen.org/
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{?with_qt:BuildRequires:	qt-devel >= 2.1.0}
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

%description -l es
Doxygen es un sistema de documentación para C, C++ e IDL. Es capaz de
generar un navegador on-line entre clases (en HTML) y-o un manual
off-line de referencia (en LaTeX) a partir de un conjunto de ficheros
de código fuente documentados. También hay soporte para generar
páginas man y para convertir la generada salida an Postscript, PDF con
hiperenlaces o HTML comprimido. La documentación se extrae directamente
de los fuentes.

Doxygen puede también ser configurado a extraer la estructura del
código de código fuente que carece de documentación. Eso puede ser
muy útil para orientarse rápidamente en distribuciones grandes de
código fuente.

%description -l pl
Doxygen to system dokumentowania dla C, C++ i IDL. Mo¿e generowaæ
dokumentacjê klas on-line (w HTML) lub podrêcznik off-line (w LaTeXu)
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

%description -l ru
Doxygen - ÜÔÏ ÓÉÓÔÅÍÁ ÄÏËÕÍÅÎÔÉÒÏ×ÁÎÉÑ ÄÌÑ C, C++ É IDL. ïÎÁ ÍÏÖÅÔ
ÓÏÚÄÁÔØ ÏÎÌÁÊÎÏ×ÙÊ ÂÒÏÕÚÅÒ ËÌÁÓÓÏ× (× HTML) É/ÉÌÉ ÏÆÆÌÁÊÎÏ×ÙÊ
ÓÐÒÁ×ÏÞÎÉË (× LaTeX) ÉÚ ÎÁÂÏÒÁ ÄÏËÕÍÅÎÔÉÒÏ×ÁÎÎÙÈ ÆÁÊÌÏ×. åÓÔØ ÔÁËÖÅ
ÐÏÄÄÅÒÖËÁ ÓÏÚÄÁÎÉÑ man-ÓÔÒÁÎÉÃ É ËÏÎ×ÅÒÔÁÃÉÉ ÓÇÅÎÅÒÉÒÏ×ÁÎÎÏÇÏ ×Ù×ÏÄÁ ×
Postscript, PDF Ó ÇÉÐÅÒÓÓÙÌËÁÍÉ É ËÏÍÐÒÅÓÓÉÒÏ×ÁÎÎÙÊ HTML. äÏËÕÍÅÎÔÁÃÉÑ
ÉÚ×ÌÅËÁÅÔÓÑ ÎÅÐÏÓÒÅÄÓÔ×ÅÎÎÏ ÉÚ ÉÓÈÏÄÎÙÈ ÆÁÊÌÏ×.

Doxygen ÍÏÖÎÏ ÔÁËÖÅ ÓËÏÎÆÉÇÕÒÉÒÏ×ÁÔØ ÄÌÑ ÐÏÌÕÞÅÎÉÑ ÓÔÒÕËÔÕÒÙ ËÏÄÁ ÉÚ
ÎÅÌÏËÕÍÅÎÔÉÒÏ×ÁÎÎÙÈ ÉÓÈÏÄÎÙÈ ÆÁÊÌÏ×. üÔÏ ÍÏÖÅÔ ÂÙÔØ ÏÞÅÎØ ÐÏÌÅÚÎÙÍ ÄÌÑ
ÔÏÇÏ, ÞÔÏÂÙ ÂÙÓÔÏ ÒÁÚÏÂÒÁÔØÓÑ × ÂÏÌØÛÏÍ ÐÒÏÅËÔÅ.

%description -l uk
Doxygen - ÃÅ ÓÉÓÔÅÍÁ ÄÏËÕÍÅÎÔÕ×ÁÎÎÑ ÄÌÑ C, C++ ÔÁ IDL. ÷ÏÎÁ ÍÏÖÅ
ÓÔ×ÏÒÉÔÉ ÏÎÌÁÊÎÏ×ÉÊ ÂÒÏÕÚÅÒ ËÌÁÓ¦× (× HTML) ÔÁ/ÞÉ ÏÆÆÌÁÊÎÏ×ÉÊ ÄÏ×¦ÄÎÉË
(× LaTeX) Ú ÎÁÂÏÒÕ ÄÏËÕÍÅÎÔÏ×ÁÎÉÈ ×ÉÈ¦ÄÎÉÈ ÆÁÊÌ¦×. ´ ÔÁËÏÖ Ð¦ÄÔÒÉÍËÁ
ÄÌÑ ÓÔ×ÏÒÅÎÎÑ man-ÓÔÏÒ¦ÎÏË ÔÁ ËÏÎ×ÅÒÔÁÃ¦§ ÚÇÅÎÅÒÏ×ÁÎÏÇÏ ×É×ÏÄÕ ×
Postscript, PDF Ú Ç¦ÐÅÒÌ¦ÎËÁÍÉ ÔÁ ËÏÍÐÒÅÓÏ×ÁÎÉÊ HTML. äÏËÕÍÅÎÔÁÃ¦Ñ
×ÉÄÏÂÕ×Á¤ÔØÓÑ ÂÅÚÐÏÓÅÒÄÎØÏ Ú ×ÉÈ¦ÄÎÉÈ ÆÁÊÌ¦×.

Doxygen ÍÏÖÎÁ ÔÁËÏÖ ÚËÏÎÆ¦ÇÕÒÕ×ÁÔÉ ÄÌÑ ÏÔÒÉÍÁÎÎÑ ÓÔÒÕËÔÕÒÉ ËÏÄÕ Ú
ÎÅÄÏËÕÍÅÎÔÏ×ÁÎÉÈ ×ÉÈ¦ÄÎÉÈ ÆÁÊÌ¦×. ãÅ ÍÏÖÅ ÂÕÔÉ ÄÕÖÅ ËÏÒÉÓÎÉÍ ÄÌÑ ÔÏÇÏ,
ÝÏÂ Û×ÉÄËÏ ÒÏÚ¦ÂÒÁÔÉÓÑ Õ ×ÅÌÉËÏÍÕ ÐÒÏÅËÔ¦.

%package doxywizard
Summary:	A GUI front-end for creating and editing configuration files
Summary(es):	Un front-end GUI para crear y editar ficheros de configuración
Summary(pl):	GUI do tworzenia i edycji plików konfiguracyjnych
Summary(pt_BR):	Wizard gráfico para o Doxygen
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	qt >= 2.1.0

%description doxywizard
Doxywizard is a GUI front-end for creating and editing configuration
files that are used by doxygen.

%description doxywizard -l es
Doxywizard es un front-end GUI para crear y editar los ficheros de
configuración que son usados por doxygen.

%description doxywizard -l pl
Doxywizard to frontend z graficznym interfejsem do tworzenia i edycji
plików konfiguracyjnych u¿ywanych przez doxygen.

%description doxywizard -l pt_BR
Wizard gráfico para o Doxygen

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%ifarch amd64
%patch3 -p1
%endif

rm -rf libpng src/unistd.h

%build
export QTDIR=%{_prefix}
# don't change it to %%configure, not autoconf-generated!
./configure \
	--prefix %{_prefix} \
	--perl %{_bindir}/perl \
	--install %{_bindir}/install \
	%{?with_qt:--with-doxywizard}

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
%doc html examples README
%attr(755,root,root) %{_bindir}/doxygen
%attr(755,root,root) %{_bindir}/doxytag

%if %{with qt}
%files doxywizard
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/doxywizard
%endif
