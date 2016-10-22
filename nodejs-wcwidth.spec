%{?scl:%scl_package nodejs-wcwidth}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-wcwidth
Version:        1.0.0
Release:        7%{?dist}
Summary:        Port of C's wcwidth() and wcswidth()
License:        MIT
Url:            https://github.com/mycoboco/wcwidth.js
Source:         http://registry.npmjs.org/wcwidth/-/wcwidth-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs-devel
Requires:		%{?scl_prefix}nodejs-devel
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
%doc docs/index.md LICENSE Readme.md
%{nodejs_sitelib}/wcwidth

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-7
- Use macro in -runtime dependency

* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-6
- Fix hardcoded dependency on metapackage

* Tue Jul 21 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-4
- Add missing build require 

* Mon Jul 20 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Fix url, Resolves: RHBZ#1210384

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Initial build

