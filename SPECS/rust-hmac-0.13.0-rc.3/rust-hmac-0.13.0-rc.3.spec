# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hmac
%global full_version 0.13.0-rc.3
%global pkgname hmac-0.13.0-rc.3

Name:           rust-hmac-0.13.0-rc.3
Version:        0.13.0
Release:        %autorelease
Summary:        Rust crate "hmac"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/MACs
#!RemoteAsset:  sha256:f1c597ac7d6cc8143e30e83ef70915e7f883b18d8bec2e2b2bce47f5bbb06d57
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11.0-rc.4/default) >= 0.11.0-rc.4
Requires:       crate(digest-0.11.0-rc.4/mac) >= 0.11.0-rc.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "hmac"

%package     -n %{name}+zeroize
Summary:        Generic implementation of Hash-based Message Authentication Code (HMAC) - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.4/mac) >= 0.11.0-rc.4
Requires:       crate(digest-0.11.0-rc.4/zeroize) >= 0.11.0-rc.4
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust hmac crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
