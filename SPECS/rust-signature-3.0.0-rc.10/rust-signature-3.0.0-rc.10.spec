# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name signature
%global full_version 3.0.0-rc.10
%global pkgname signature-3.0.0-rc.10

Name:           rust-signature-3.0.0-rc.10
Version:        3.0.0
Release:        %autorelease
Summary:        Rust crate "signature"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:7f1880df446116126965eeec169136b2e0251dba37c6223bcc819569550edea3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
ECDSA, Ed25519)
Source code for takopackized Rust crate "signature"

%package     -n %{name}+digest
Summary:        Traits for cryptographic signature algorithms (e.g - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.8) >= 0.11.0-rc.8
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
ECDSA, Ed25519)
This metapackage enables feature "digest" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic signature algorithms (e.g - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
ECDSA, Ed25519)
This metapackage enables feature "rand_core" for the Rust signature crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
