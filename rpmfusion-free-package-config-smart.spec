%define debug_package %{nil}

Summary:    RPM Fusion (free) configuration files for the Smart package manager
Name:       rpmfusion-free-package-config-smart
Version:    9
Release:    4
License:    GPLv2+
Group:      System Environment/Base
URL:        http://rpmfusion.org/
Source0:    COPYING
Source1:    rpmfusion-free.channel
Source2:    rpmfusion-free-rawhide.channel
Source3:    rpmfusion-free-updates.channel
Source4:    rpmfusion-free-updates-testing.channel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   smart
Provides:   smart-config-rpmfusion-free = %{version}-%{release}

%description
This package provides the configuration files required by the Smart package
manager to use RPM Fusion's "free" software repository.


%prep
%setup -cT
cp %{SOURCE0} .

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels
for channel in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4};do
  name=$(basename $channel)
  install -p -m0644 $channel $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels/$name
  sed -i 's/\$basearch/%{_target_cpu}/' $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels/$name
  sed -i 's/\$releasever/%{fedora}/' $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels/$name
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) %{_sysconfdir}/smart/channels/*.channel

%changelog
* Mon Dec 22 2008 Stewart Adam <s.adam at diffingo.com> 9-4
- Another workaround since buildsys doesn't seem to like ||:

* Sun Dec 21 2008 Stewart Adam <s.adam at diffingo.com> 9-3
- Append ||: to cp so build doesn't fail on "make local"
- Modifications for F-9 from universal SRPM

* Thu Dec 11 2008 Stewart Adam <s.adam at diffingo.com> 9-2
- Make summary and description fields clearer

* Sat Dec 6 2008 Stewart Adam <s.adam at diffingo.com> 9-1
- Split rpmfusion-package-config-smart into free and nonfree
- Don't use %%{__commandname} in some places but not others

