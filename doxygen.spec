Name:		doxygen
Summary:	Doxygen is THE documentation system for C/C++
Version:	1.2.3
Release:	1
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
License:	GPL
URL:		http://www.stack.nl/~dimitri/doxygen/
Source0:	http://www.stack.nl/~dimitri/doxygen/dl/%{name}-%{version}.src.tar.gz
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExcludeArch:	alpha

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

%prep
%setup -q

%build
export QTDIR=%{_prefix}
%configure 

%{__make}
%{__make} docs
%{__make} ps
mkdir ps
mv -f latex/doxygen_manual.ps ps

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -s bin/doxy* ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc html examples ps
%doc README LICENSE
%{_bindir}/doxygen
%{_bindir}/doxytag
%{_bindir}/doxysearch
