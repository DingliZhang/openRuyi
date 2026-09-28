# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name aead
%global full_version 0.6.0-rc.3
%global pkgname aead-0.6.0-rc.3

Name:           rust-aead-0.6.0-rc.3
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "aead"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:03d2d54c4d9e7006f132f615a167865bff927a79ca63d8f637237575ce0a9795
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2.0-rc.5/default) >= 0.2.0-rc.5
Requires:       crate(inout-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "aead"

%package     -n %{name}+arrayvec
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "arrayvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec) = %{version}

%description -n %{name}+arrayvec
This metapackage enables feature "arrayvec" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blobby
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "blobby"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blobby-0.4.0-pre.1/default) >= 0.4.0-pre.1
Provides:       crate(%{pkgname}/blobby) = %{version}

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dev
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "dev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/blobby) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+dev
This metapackage enables feature "dev" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2.0-rc.5/getrandom) >= 0.2.0-rc.5
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API - feature "rand_core" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2.0-rc.5/rand-core) >= 0.2.0-rc.5
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust aead crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
