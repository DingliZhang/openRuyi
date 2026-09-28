# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name primefield
%global full_version 0.14.0-rc.7
%global pkgname primefield-0.14.0-rc.7

Name:           rust-primefield-0.14.0-rc.7
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "primefield"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/primefield
#!RemoteAsset:  sha256:93401c13cc7ff24684571cfca9d3cf9ebabfaf3d4b7b9963ade41ec54da196b5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-bigint-0.7.0-rc.25/hybrid-array) >= 0.7.0-rc.25
Requires:       crate(crypto-bigint-0.7.0-rc.25/rand-core) >= 0.7.0-rc.25
Requires:       crate(crypto-bigint-0.7.0-rc.25/subtle) >= 0.7.0-rc.25
Requires:       crate(crypto-common-0.2.0-rc.15/default) >= 0.2.0-rc.15
Requires:       crate(crypto-common-0.2.0-rc.15/rand-core) >= 0.2.0-rc.15
Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(rustcrypto-ff-0.14.0-rc.0) >= 0.14.0-rc.0
Requires:       crate(subtle-2/const-generics) >= 2.6.0
Requires:       crate(zeroize-1) >= 1.7.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "primefield"

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
