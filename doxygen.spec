
%bcond_without qt	# without doxywizard (qt-based)

Summary:	Doxygen is the documentation system for C/C++
Summary(es):	Doxygen es el sistema de documentaci�n para C/C++
Summary(pl):	System dokumentowania dla C/C++
Summary(pt_BR):	Um sistema de documenta��o para C/C++
Summary(ru):	������� ���������������� ��� C �� C++
Summary(uk):	������� �������������� ��� C �� C++
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
Doxygen es un sistema de documentaci�n para C, C++ e IDL. Es capaz de
generar un navegador on-line entre clases (en HTML) y-o un manual
off-line de referencia (en LaTeX) a partir de un conjunto de ficheros
de c�digo fuente documentados. Tambi�n hay soporte para generar
p�ginas man y para convertir la generada salida an Postscript, PDF con
hiperenlaces o HTML comprimido. La documentaci�n se extrae directamente
de los fuentes.

Doxygen puede tambi�n ser configurado a extraer la estructura del
c�digo de c�digo fuente que carece de documentaci�n. Eso puede ser
muy �til para orientarse r�pidamente en distribuciones grandes de
c�digo fuente.

%description -l pl
Doxygen to system dokumentowania dla C, C++ i IDL. Mo�e generowa�
dokumentacj� klas on-line (w HTML) lub podr�cznik off-line (w LaTeXu)
z zestawu udokumentowanych plik�w �r�d�owych. Ma tak�e mo�liwo��
generowania stron man i konwersji na Postscript, PDF z hiper��czami
oraz skompresowany HTML. Dokumentacja jest wyci�gana bezpo�rednio ze
�r�de�.

Doxygen mo�e by� skonfigurowany tak�e do wyci�gania struktury kodu z
nieudokumentowanych plik�w �r�d�owych. Mo�e by� to przydatne do
szybkiego odnalezienia si� w du�ych �r�d�ach.

%description -l pt_BR
Doxygen � uma sistema de documenta��o para C e C++ que gera um class
browser on-line (em HTML) e/ou um manual de referencia off-line (em
LaTeX) a partir de um conjunto de fontes documentados. A documenta��o
� extraida diretamente a partir dos fontes.

%description -l ru
Doxygen - ��� ������� ���������������� ��� C, C++ � IDL. ��� �����
������� ���������� ������� ������� (� HTML) �/��� �����������
���������� (� LaTeX) �� ������ ����������������� ������. ���� �����
��������� �������� man-������� � ����������� ���������������� ������ �
Postscript, PDF � ������������� � ����������������� HTML. ������������
����������� ��������������� �� �������� ������.

Doxygen ����� ����� ���������������� ��� ��������� ��������� ���� ��
������������������� �������� ������. ��� ����� ���� ����� �������� ���
����, ����� ����� ����������� � ������� �������.

%description -l uk
Doxygen - �� ������� �������������� ��� C, C++ �� IDL. ���� ����
�������� ���������� ������� ���Ӧ� (� HTML) ��/�� ����������� ��צ����
(� LaTeX) � ������ �������������� ��Ȧ���� ���̦�. � ����� Ц�������
��� ��������� man-���Ҧ��� �� ��������æ� ������������� ������ �
Postscript, PDF � Ǧ���̦����� �� ������������� HTML. ���������æ�
������������� ������������ � ��Ȧ���� ���̦�.

Doxygen ����� ����� ����Ʀ�������� ��� ��������� ��������� ���� �
���������������� ��Ȧ���� ���̦�. �� ���� ���� ���� �������� ��� ����,
��� ������ ��ڦ������� � �������� �����Ԧ.

%package doxywizard
Summary:	A GUI front-end for creating and editing configuration files
Summary(es):	Un front-end GUI para crear y editar ficheros de configuraci�n
Summary(pl):	GUI do tworzenia i edycji plik�w konfiguracyjnych
Summary(pt_BR):	Wizard gr�fico para o Doxygen
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	qt >= 2.1.0

%description doxywizard
Doxywizard is a GUI front-end for creating and editing configuration
files that are used by doxygen.

%description doxywizard -l es
Doxywizard es un front-end GUI para crear y editar los ficheros de
configuraci�n que son usados por doxygen.

%description doxywizard -l pl
Doxywizard to frontend z graficznym interfejsem do tworzenia i edycji
plik�w konfiguracyjnych u�ywanych przez doxygen.

%description doxywizard -l pt_BR
Wizard gr�fico para o Doxygen

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
