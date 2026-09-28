# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name p256
%global full_version 0.14.0-rc.7
%global pkgname p256-0.14.0-rc.7

Name:           rust-p256-0.14.0-rc.7
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "p256"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/elliptic-curves/tree/master/p256
#!RemoteAsset:  sha256:018bfbb86e05fd70a83e985921241035ee09fcd369c4a2c3680b389a01d2ad28
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28

Provides:       crate(%{pkgname}) = %{version}

%description
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
Source code for takopackized Rust crate "p256"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/alloc) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/alloc) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(primeorder-0.14.0-rc.7/alloc) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "alloc" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+arithmetic
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "arithmetic" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.14.0-rc.28/arithmetic) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(primefield-0.14.0-rc.7/default) >= 0.14.0-rc.7
Requires:       crate(primeorder-0.14.0-rc.7/default) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/arithmetic) = %{version}
Provides:       crate(%{pkgname}/expose-field) = %{version}

%description -n %{name}+arithmetic
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "arithmetic" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "expose-field" feature.

%package     -n %{name}+bits
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "bits"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.14.0-rc.28/bits) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/bits) = %{version}

%description -n %{name}+bits
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "bits" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "default" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+digest
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "digest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/digest) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/hazmat) >= 0.17.0-rc.16
Provides:       crate(%{pkgname}/digest) = %{version}

%description -n %{name}+digest
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "digest" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdh
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "ecdh"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(elliptic-curve-0.14.0-rc.28/ecdh) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/ecdh) = %{version}

%description -n %{name}+ecdh
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "ecdh" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "ecdsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(%{pkgname}/sha256) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/algorithm) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Provides:       crate(%{pkgname}/ecdsa) = %{version}

%description -n %{name}+ecdsa
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "ecdsa" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa-core
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "ecdsa-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Provides:       crate(%{pkgname}/ecdsa-core) = %{version}

%description -n %{name}+ecdsa-core
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "ecdsa-core" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(elliptic-curve-0.14.0-rc.28/getrandom) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "getrandom" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+group-digest
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "group-digest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hash2curve) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/group-digest) = %{version}
Provides:       crate(%{pkgname}/oprf) = %{version}

%description -n %{name}+group-digest
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "group-digest" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oprf" feature.

%package     -n %{name}+hash2curve
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "hash2curve"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/arithmetic) = %{version}
Requires:       crate(hash2curve-0.14.0-rc.10/default) >= 0.14.0-rc.10
Requires:       crate(primeorder-0.14.0-rc.7/hash2curve) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/hash2curve) = %{version}

%description -n %{name}+hash2curve
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "hash2curve" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pkcs8) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/pem) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/pem) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "pem" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pkcs8
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "pkcs8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/pkcs8) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/pkcs8) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/pkcs8) = %{version}

%description -n %{name}+pkcs8
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "pkcs8" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serdect) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/serde) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/serde) >= 0.14.0-rc.28
Requires:       crate(primeorder-0.14.0-rc.7/serde) >= 0.14.0-rc.7
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "serde" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serdect
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "serdect"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serdect-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/serdect) = %{version}

%description -n %{name}+serdect
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "serdect" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11.0-rc.5) >= 0.11.0-rc.5
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "sha2" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha256
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "sha256"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/digest) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/sha256) = %{version}

%description -n %{name}+sha256
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "sha256" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/getrandom) = %{version}
Requires:       crate(ecdsa-0.17.0-rc.16/der) >= 0.17.0-rc.16
Requires:       crate(ecdsa-0.17.0-rc.16/std) >= 0.17.0-rc.16
Requires:       crate(elliptic-curve-0.14.0-rc.28/sec1) >= 0.14.0-rc.28
Requires:       crate(elliptic-curve-0.14.0-rc.28/std) >= 0.14.0-rc.28
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "std" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-vectors
Summary:        Pure Rust implementation of the NIST P-256 (a.k.a - feature "test-vectors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hex-literal-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/test-vectors) = %{version}

%description -n %{name}+test-vectors
secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic
This metapackage enables feature "test-vectors" for the Rust p256 crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
