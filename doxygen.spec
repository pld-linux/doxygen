
%define relc rc3

Summary:	Doxygen is the documentation system for C/C++
Summary(pl):	System dokumentowania dla C/C++
Summary(pt_BR):	Um sistema de documenta��o para C/C++
Summary(ru):	������� ���������������� ��� C �� C++
Summary(uk):	������� �������������� ��� C �� C++
Name:		doxygen
Version:	1.3
Release:	0.%{relc}
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.stack.nl/pub/users/dimitri/%{name}-%{version}-%{relc}.src.tar.gz
Patch0:		%{name}-system-libpng.patch
URL:		http://www.doxygen.org/
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	ghostscript-fonts-std
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-static
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-plain-misc
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
Doxygen to system dokumentowania dla C, C++ i IDL. Mo�e generowa�
dokumentacj� klas on-line (w HTML) lub podr�cznik off-line (w LaTeX-u)
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
Summary(pl):	GUI do tworzenia i edycji plik�w konfiguracyjnych
Summary(pt_BR):	Wizard gr�fico para o Doxygen
Group:		X11/Applications
Requires:	%{name} = %{version}
Requires:	qt >= 2.2

%description doxywizard
Doxywizard is a GUI front-end for creating and editing configuration
files that are used by doxygen.

%description doxywizard -l pl
Doxywizard to frontend z graficznym interfejsem do tworzenia i edycji
plik�w konfiguracyjnych u�ywanych przez doxygen.

%description doxywizard -l pt_BR
Wizard gr�fico para o Doxygen

%prep
%setup -q -n %{name}-%{version}-%{relc}
%patch -p1

rm -rf libpng

%build
export QTDIR=%{_prefix}
## don't change it to %%configure!!!
./configure \
	--prefix %{_prefix} \
	--perl %{_bindir}/perl \
	--install %{_bindir}/install
#	--with-doxywizard

%{__make} \
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

#%files doxywizard
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/doxywizard
