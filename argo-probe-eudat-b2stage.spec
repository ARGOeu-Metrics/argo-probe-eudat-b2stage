Name:		nagios-plugins-eudat-b2stage
Version:	0.9.1
Release:	1%{?dist}
Summary:	Nagios probe for B2STAGE
License:	GPLv3+
Packager:	Themis Zamani <themiszamani@gmail.com>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
AutoReqProv: no

%description
Nagios probe to check functionality of B2STAGE service

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2stage
install -d %{buildroot}/%{_sysconfdir}/nagios/plugins/eudat-b2stage
install -m 755 check_b2stage_http-api.py %{buildroot}/%{_libexecdir}/argo-monitoring/probes/eudat-b2stage/check_b2stage_http-api.py

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/eudat-b2stage

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes//eudat-b2stage/check_b2stage_http-api.py

%changelog
* Mon May 04 2020 Themis Zamani  <themiszamani@gmail.com> - 0.9.1-1
- Check service healthchek
* Fri Apr 03 2020 Themis Zamani  <themiszamani@gmail.com> - 0.9-1
- Small updates to messages
* Fri Apr 03 2020 Themis Zamani  <themiszamani@gmail.com> - 0.8-1
- Small updates to messages
* Mon Dec 17 2018 Themis Zamani  <themiszamani@gmail.com> - 0.7-1
- Updated package version. 
* Mon Dec 17 2018 Themis Zamani  <themiszamani@gmail.com> - 0.6-1
- Updated package version. 
* Fri Oct 19 2018 Themis Zamani  <themiszamani@gmail.com> - 0.1-1
- Initial version of the package. 
* Thu Oct 18 2018 Mattia D'Antonio  <m.dantonio@cineca.it> - 0.1-1
- Initial version of the package. 
