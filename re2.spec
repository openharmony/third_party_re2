Name:           re2
Version:        20240201
Release:        1
Summary:        Provide backtracking RE engine
License:        BSD
URL:            http://github.com/google/re2/
Source0:        https://github.com/google/re2/archive/2024-02-01.tar.gz
Patch1:         add-some-testcases-for-abnormal-branches.patch
BuildRequires:  gcc-c++ abseil-cpp-devel

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python. It is a C++ library.

%package        devel
Summary:        Provide re2 symbolic links with C ++ header files and libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains C ++ header files and symbolic links to re2's shared libraries.
If you want to develop programs using re2, you need to install re2-devel.

%prep
%autosetup -n %{name}-2024-02-01 -p1

%build
sed -i 's/RE2_LDFLAGS?=-pthread/RE2_LDFLAGS?=-pthread -Wl,--as-needed/g' Makefile
%make_build CXXFLAGS="${CXXFLAGS:-%optflags} -pthread -std=c++17" \
            LDFLAGS="${LDFLAGS:-%__global_ldflags} -pthread" \
            includedir=%{_includedir} libdir=%{_libdir}

%install
%make_install includedir=%{_includedir} libdir=%{_libdir}

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}:LD_LIBRARY_PATH
%ctest || true

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc README LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/{lib%{name}.so,pkgconfig/%{name}.pc}
%exclude %{_libdir}/libre2.a

%changelog
* Wed Feb 07 2024 gaihuiying <eaglegai@163.com> - 20240201-1
- update to 20240201

* Tue Jan 23 2024 gaihuiying <eaglegai@163.com> - 20230901-2
- add '-Wl, --as-needed' for re2 to link dynamic library

* Wed Oct 18 2023 wulei <wu_lei@hoperun.com> - 20230901-1
- Update to 20230901

* Wed Dec 14 2022 zhouyihang <zhouyihang3@h-partners.com> - 20211101-3
- add some testcases for abnormal branches

* Mon Oct 24 2022 gaihuiying <eaglegai@163.com> - 20211101-2
- fix 64 to 32 bit clang conversion warning

* Sat Mar 19 2022 xihaochen <xihaochen@h-partners.com> - 20211101-1
- upgrade to 20211101

* Thu Dec 3 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 20200801-1
- upgrade to 20200801

* Fri Nov 29 2019 fengbing <fengbing7@huawei.com> - 20160401-8
- Package init
