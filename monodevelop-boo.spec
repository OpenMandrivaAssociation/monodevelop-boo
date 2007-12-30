# Find version of boo
%define boo_version %(rpm -q boo --queryformat '%{VERSION}')
Name:     	monodevelop-boo
Version:	0.18.1
Release:	%mkrel 1
License:	LGPL
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://go-mono.com/sources/monodevelop-boo/%{name}-%{version}.tar.gz
BuildRequires:	boo monodevelop >= 0.18
Summary:	Monodevelop Boo Addin
Group:		Development/Other
# Boo's assemblies are always version at 1.0.0.0.  Force built against or newer.
Requires:       boo >= %boo_version

%description
Monodevelop Boo Addin


%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%_prefix/share/pkgconfig
mv $RPM_BUILD_ROOT%_prefix/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%_prefix/share/pkgconfig
for langdir in %buildroot%_prefix/lib/monodevelop/AddIns/BooBinding/locale/*; do
echo "%lang($(basename $langdir)) $(echo $langdir |sed s!%buildroot!!)" >> %name.lang
done


%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %name.lang
%defattr(-, root, root)
%_datadir/pkgconfig/monodevelop-boo.pc
%_prefix/lib/monodevelop/AddIns/BooBinding/BooShell.dll*
%_prefix/lib/monodevelop/AddIns/BooBinding/BooBinding.dll*
%dir %_prefix/lib/monodevelop/AddIns/BooBinding/locale/

