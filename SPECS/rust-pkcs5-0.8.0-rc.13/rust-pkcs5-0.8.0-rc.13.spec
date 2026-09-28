# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pkcs5
%global full_version 0.8.0-rc.13
%global pkgname pkcs5-0.8.0-rc.13

Name:           rust-pkcs5-0.8.0-rc.13
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "pkcs5"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/formats/tree/master/pkcs5
#!RemoteAsset:  sha256:c5a777c6e26664bc9504b3ce3f6133f8f20d9071f130a4f9fcbd3186959d8dd6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(der-0.8.0-rc.10/default) >= 0.8.0-rc.10
Requires:       crate(der-0.8.0-rc.10/oid) >= 0.8.0-rc.10
Requires:       crate(spki-0.8.0-rc.4/default) >= 0.8.0-rc.4

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "pkcs5"

%package     -n %{name}+3des
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5: Password-Based Cryptography Specification Version 2.1 (RFC 8018) - feature "3des" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pbes2) = %{version}
Requires:       crate(des-0.9.0-rc.2) >= 0.9.0-rc.2
Provides:       crate(%{pkgname}/3des) = %{version}
Provides:       crate(%{pkgname}/des-insecure) = %{version}

%description -n %{name}+3des
This metapackage enables feature "3des" for the Rust pkcs5 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "des-insecure" feature.

%package     -n %{name}+pbes2
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5: Password-Based Cryptography Specification Version 2.1 (RFC 8018) - feature "pbes2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(aes-0.9.0-rc.2) >= 0.9.0-rc.2
Requires:       crate(aes-gcm-0.11.0-rc.2/aes) >= 0.11.0-rc.2
Requires:       crate(cbc-0.2.0-rc.2/default) >= 0.2.0-rc.2
Requires:       crate(pbkdf2-0.13.0-rc.8/hmac) >= 0.13.0-rc.8
Requires:       crate(scrypt-0.12.0-rc.9) >= 0.12.0-rc.9
Requires:       crate(sha2-0.11.0-rc.4) >= 0.11.0-rc.4
Provides:       crate(%{pkgname}/pbes2) = %{version}

%description -n %{name}+pbes2
This metapackage enables feature "pbes2" for the Rust pkcs5 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5: Password-Based Cryptography Specification Version 2.1 (RFC 8018) - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10.0-rc.6) >= 0.10.0-rc.6
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust pkcs5 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1-insecure
Summary:        Pure Rust implementation of Public-Key Cryptography Standards (PKCS) #5: Password-Based Cryptography Specification Version 2.1 (RFC 8018) - feature "sha1-insecure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pbes2) = %{version}
Requires:       crate(sha1-0.11.0-rc.4) >= 0.11.0-rc.4
Provides:       crate(%{pkgname}/sha1-insecure) = %{version}

%description -n %{name}+sha1-insecure
This metapackage enables feature "sha1-insecure" for the Rust pkcs5 crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
