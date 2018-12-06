# https://github.com/cznic/internal
%global goipath github.com/cznic/internal
%global commit  4747030f7cf2f4c0a01512b00cd68734b167ac3b

%gometa

Name:           golang-github-cznic-internal
Version:        1.0.0
Release:        9%{?dist}
Summary:        Shared dependencies for other cznic Go libraries
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/cznic/fileutil)
BuildRequires:  golang(github.com/cznic/mathutil)
BuildRequires:  golang(github.com/edsrzf/mmap-go)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS README.md AUTHORS


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-9
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.0-8
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-7.20170905git4747030
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6.20170905.git4747030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.20170905.git4747030
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 06 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-4.20170905.git4747030
- Bump to commit 4747030.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20170516.git6c349f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20170516.git6c349f9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1.20170516.git6c349f9
- Bump to commit 6c349f9.

* Sat Mar 11 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1.20170124.gite5e1c3e
- First package for Fedora

