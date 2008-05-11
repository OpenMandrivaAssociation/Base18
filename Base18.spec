Name:               Base18
Summary:            Zope product to implement multilingual portals
Version:            0.2.0
Release:            %mkrel 18
Group:              Development/Python
Requires:           zope
License:            GPL
URL:                http://www.erp5.org
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir

Source: %{name}-%{version}.tar.bz2

#----------------------------------------------------------------------
%description
Base18 is a Zope product to implement multilingual portals
It extends the Zope CMF by allowing documents to be split into
a list of paragraphs which can be translated through a message catalog.

http://www.erp5.org

#----------------------------------------------------------------------
%prep

rm -rf $RPM_BUILD_ROOT
%setup -a 0

#----------------------------------------------------------------------
%build

#----------------------------------------------------------------------
%install
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/
install %{name}-%{version}/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/
install %{name}-%{version}/*.txt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/
install %{name}-%{version}/*.png $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/default_wiki_content
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/dtml
install %{name}-%{version}/dtml/*.dtml $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/dtml
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/Extensions
install %{name}-%{version}/Extensions/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/Extensions
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help
install %{name}-%{version}/help/*.stx $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/interfaces
install %{name}-%{version}/interfaces/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/interfaces
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/content18
install %{name}-%{version}/skins/content18/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/content18
install %{name}-%{version}/skins/content18/*.dtml $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/content18
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/nexedi
install %{name}-%{version}/skins/nexedi/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/nexedi
install %{name}-%{version}/skins/nexedi/*.dtml $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/nexedi
install %{name}-%{version}/skins/nexedi/*.png $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/nexedi
install %{name}-%{version}/skins/nexedi/*.pt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/nexedi
install %{name}-%{version}/skins/nexedi/*.props $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/nexedi
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/zpt_content18
install %{name}-%{version}/skins/zpt_content18/*.pt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/zpt_content18
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/zpt_nexedi
install %{name}-%{version}/skins/zpt_nexedi/*.pt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/zpt_nexedi
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/spec
%clean
rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------------------
%files
%defattr(-,root,root,0755)
%doc README.txt INSTALL.txt CREDITS.txt GPL.txt ZPL.txt
%{_libdir}/zope/lib/python/Products/%{name}/
#----------------------------------------------------------------------
