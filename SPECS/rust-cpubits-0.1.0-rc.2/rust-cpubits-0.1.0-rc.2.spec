# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cpubits
%global full_version 0.1.0-rc.2
%global pkgname cpubits-0.1.0-rc.2

Name:           rust-cpubits-0.1.0-rc.2
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "cpubits"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/utils
#!RemoteAsset:  sha256:4ee6439310d1504c84ab741743fc93ea845bb9f6ab8b44962237957810246118
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
`target_pointer_width`. Implemented as `macro_rules!`
Source code for takopackized Rust crate "cpubits"

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
