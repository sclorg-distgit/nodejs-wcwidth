%{?scl:%scl_package nodejs-wcwidth}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-wcwidth
Version:        1.0.0
Release:        4%{?dist}
Summary:        Port of C's wcwidth() and wcswidth()
License:        MIT
Group:          Development/Languages/Other
Url:            https://github.com/mycoboco/wcwidth.js
Source:         http://registry.npmjs.org/wcwidth/-/wcwidth-%{version}.tgz
BuildRequires:  nodejs010
BuildRequires:  nodejs010-runtime
Requires:	nodejs010
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%description
Determine columns needed for a fixed-size wide-character string.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/wcwidth
cp -pr package.json index.js combining.js \
        %{buildroot}%{nodejs_sitelib}/wcwidth/

%nodejs_symlink_deps

%files
%defattr(-,root,root,-)
%doc docs/index.md LICENSE Readme.md
%{nodejs_sitelib}/wcwidth

%changelog
* Tue Jul 21 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-4
- Add missing build require 

* Mon Jul 20 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Fix url, Resolves: RHBZ#1210384

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial build

