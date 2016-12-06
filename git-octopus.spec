Name:       git-octopus
Version:    1.4
Release:    2%{?dist}
Summary:    Git commands for continuous delivery

License:    LGPLv3
URL:        https://github.com/lesfurets/git-octopus
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   git >= 1.8
Requires:   %{_bindir}/shasum
BuildRequires: asciidoc


%description
The continuous merge workflow is meant for continuous integration/delivery and
is based on feature branching. git-octopus provides git commands to implement
it.


%prep
%setup -q


%build
%make_build
make build-docs


%install
%make_install prefix="%{buildroot}%{_prefix}" \
              docdir="%{buildroot}%{_docdir}/%{name}%{?rhel:-%{version}}"


%files
%doc README.md doc/*.html
%license LICENSE
%{_bindir}/git-*
%{_mandir}/man1/git-*.1*


%changelog
* Tue Dec 06 2016 Andrea Baita <andrea@baita.pro> - 1.4-2
- added documentation build, updated build requires

* Wed Nov 30 2016 Andrea Baita <andrea@baita.pro> - 1.4-1
- Packaging of version 1.4.

* Thu Nov 17 2016 Xavier Bachelot <xavier@bachelot.org> - 1.3-1
- Initial package.
