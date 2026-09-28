# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rand_core
%global full_version 0.10.0-rc-6
%global pkgname rand-core-0.10.0-rc.6

Name:           rust-rand-core-0.10.0-rc.6
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "rand_core"
License:        MIT OR Apache-2.0
URL:            https://rust-random.github.io/book
#!RemoteAsset:  sha256:70765ff7112b0fb2d272d24d9a2f907fc206211304328fe58b2db15a5649ef28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rand_core"

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-0.10.0-rc.6
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-0.10.0-rc.6/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-0.10.0-rc.6/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-0.10.0-rc.6/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-0.10.0-rc.6/

%changelog
%autochangelog
