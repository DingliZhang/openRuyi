# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha3
%global full_version 0.11.0-rc.9
%global pkgname sha3-0.11.0-rc.9

Name:           rust-sha3-0.11.0-rc.9
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "sha3"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:0b233a7d59d7bfc027208506a33ffc9532b2acb24ddc61fe7e758dc2250db431
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(digest-0.11/default) >= 0.11.0
Requires:       crate(keccak-0.2.0-rc.2/default) >= 0.2.0-rc.2

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sha3"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/alloc) >= 0.11.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/oid) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/oid) >= 0.11.0
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash functions including the SHAKE family of eXtendable-Output Functions (XOFs), as well as the accelerated variant TurboSHAKE - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11/zeroize) >= 0.11.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sha3 crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
