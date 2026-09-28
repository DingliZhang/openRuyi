# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name crypto-common
%global full_version 0.2.0-rc.15
%global pkgname crypto-common-0.2.0-rc.15

Name:           rust-crypto-common-0.2.0-rc.15
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "crypto-common"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:6f8441110cea75afde0b89a8d796e2bc67b23432f5a9566cb15d9d365d91a2b0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hybrid-array-0.4/default) >= 0.4.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "crypto-common"

%package     -n %{name}+getrandom
Summary:        Common cryptographic traits - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(getrandom-0.4/sys-rng) >= 0.4.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Common cryptographic traits - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Common cryptographic traits - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hybrid-array-0.4/zeroize) >= 0.4.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust crypto-common crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
