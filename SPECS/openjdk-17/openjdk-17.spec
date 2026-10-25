# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorver        17
%global minorver        0
%global securityver     21
%global buildver        9
%global newjavaver      %{majorver}.%{minorver}.%{securityver}
%global _jvmdir         %{_libdir}/jvm
%global jvm_home        %{_jvmdir}/%{name}
%global system_cacerts  %{_sysconfdir}/pki/ca-trust/extracted/java/cacerts
%global rpm_state_dir   %{_localstatedir}/lib/rpm-state/java-openjdk
%global alternatives_priority %{majorver}

# Force the facilities to be recreated after RPM removes a ghost link that
# an older, still-installed monolithic package did not declare as its own.
%define refresh_alternatives() %{expand:
case "$(LC_ALL=C alternatives --display java 2>/dev/null)" in
    *'status is auto.'*)
        alternatives --auto java || : ;;
    *'status is manual.'*)
        selected_java=$(readlink -f %{_sysconfdir}/alternatives/java)
        if [ -x "$selected_java" ]; then
            alternatives --set java "$selected_java" || :
        fi ;;
esac
:
}

# Refresh the single Java group when optional tools are installed or removed.
# Repeating this after the transaction also repairs the old monolithic postun.
%define register_alternatives() %{expand:
if [ -x %{jvm_home}/bin/java ]; then
    java_was_auto=false
    case "$(LC_ALL=C alternatives --display java 2>/dev/null)" in
        *'status is auto.'*) java_was_auto=true ;;
    esac
    set -- --install %{_bindir}/java java %{jvm_home}/bin/java %{alternatives_priority} --slave %{_jvmdir}/default-java java_home %{jvm_home}
    for tool in %{jvm_home}/bin/*; do
        [ -x "$tool" ] || continue
        tool_name=${tool##*/}
        if [ "$tool_name" != java ]; then
            set -- "$@" --slave %{_bindir}/"$tool_name" "$tool_name" "$tool"
        fi
        for manpage in %{jvm_home}/man/man1/"$tool_name".1*; do
            [ -f "$manpage" ] || continue
            set -- "$@" --slave %{_mandir}/man1/"${manpage##*/}" "$tool_name.1" "$manpage"
        done
    done
    alternatives "$@" || :
    # chkconfig 1.33 can lose auto mode when an existing priority changes.
    if [ "$java_was_auto" = true ]; then
        alternatives --auto java || :
    else
        %refresh_alternatives
    fi
fi
:
}

%bcond bootstrap        1

Name:           java-17-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK 17 Runtime Environment
License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk17u
#!RemoteAsset:  sha256:d91412620f9a5b645e78c4a041189c88d6f0dc9a4bdf1490e764bc0ae75e8496
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{newjavaver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:42cc01235222a27576de8331a532da200ce36c9d155c93e9e0b4d565dcaf684a
Source1:        https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.16%2B8/OpenJDK17U-jdk_riscv64_linux_hotspot_17.0.16_8.tar.gz
#!RemoteAsset:  sha256:166774efcf0f722f2ee18eba0039de2d685b350ee14d7b69e6f83437dafd2af1
Source2:        https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.16%2B8/OpenJDK17U-jdk_x64_linux_hotspot_17.0.16_8.tar.gz
%endif

# CVE-2026-91403: backport JDK-8395142 from jdk-17.0.21.0.2-ga.
# Upstream: https://github.com/openjdk/jdk17u/commit/10d196353d5abdcc64f6d4bcf4f5ddcbfd97839e
Patch0:         1000-CA-Enhancements.patch

BuildRequires:  ca-certificates
BuildRequires:  findutils
BuildRequires:  gzip
BuildRequires:  fonts-dejavu
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  zip
BuildRequires:  pkgconfig
%if %{without bootstrap}
BuildRequires:  java-17-openjdk-devel
%endif
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives

%description
The OpenJDK desktop runtime libraries and graphical monitoring tool.

%package headless
Summary:        OpenJDK %{majorver} headless runtime environment
Requires:       ca-certificates
Requires:       p11-kit(ca-trust-source)
Requires:       fontconfig
Requires:       fonts-dejavu
Requires(post): coreutils
Requires(postun): coreutils
Requires(posttrans): coreutils
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives

%description headless
The OpenJDK runtime environment without desktop and audio libraries.
The default-java link in the JVM directory follows the selected Java runtime.

%package devel
Summary:        OpenJDK %{majorver} development tools
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives

%description devel
The OpenJDK compiler, command-line development tools, and JNI headers.
Install the jmods subpackage to create custom runtimes with jlink.

%package jmods
Summary:        OpenJDK %{majorver} packaged modules
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}

%description jmods
Packaged OpenJDK modules for creating custom runtimes with jlink.

%package src
Summary:        OpenJDK %{majorver} Java source archive
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}

%description src
The Java source archive for the OpenJDK class libraries.

%package demo
Summary:        OpenJDK %{majorver} demonstration programs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description demo
Demonstration programs and examples for the OpenJDK development kit.

%prep
%autosetup -p1 -n jdk17u-jdk-%{newjavaver}-%{buildver}

%build
%if %{with bootstrap}
%ifarch riscv64
tar -xf %{SOURCE1} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-17.0.16+8
%endif
%ifarch x86_64
tar -xf %{SOURCE2} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-17.0.16+8
%endif
%else
BOOTJDKPATH=%{_jvmdir}/java-17-openjdk
%endif

ARCH=$(uname -m)
echo $BOOTJDKPATH

mkdir -p build-release
pushd build-release
bash ../configure \
    --with-version-build=%{buildver} \
    --with-version-pre= \
    --with-version-opt= \
    --with-boot-jdk=$BOOTJDKPATH \
    --with-cacerts-file=%{system_cacerts} \
    --with-debug-level=release \
    --with-native-debug-symbols=internal \
    --with-vendor-version-string=openRuyi \
    --with-vendor-name="%{_vendor_name}" \
    --with-vendor-url="%{_vendor_url}" \
    --with-vendor-bug-url="%{_vendor_bug_url}" \
    --enable-unlimited-crypto \
    --disable-warnings-as-errors
make images
popd

%install -p
mkdir -p %{buildroot}%{_jvmdir}
cp -a build-release/images/jdk %{buildroot}%{jvm_home}
# Some image configurations keep packaged modules outside the JDK image.
if [ ! -d %{buildroot}%{jvm_home}/jmods ]; then
    cp -a build-release/images/jmods %{buildroot}%{jvm_home}/jmods
fi

# Compress versioned manuals before creating the alternatives ghost entries.
if [ -d %{buildroot}%{jvm_home}/man ]; then
    find %{buildroot}%{jvm_home}/man -type f -name '*.1' -exec gzip -9n {} +
fi

# Keep the JDK's blocked.certs; only the positive trust store is system-wide.
rm %{buildroot}%{jvm_home}/lib/security/cacerts
ln -s %{system_cacerts} %{buildroot}%{jvm_home}/lib/security/cacerts
mkdir -p %{buildroot}%{rpm_state_dir} %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
touch %{buildroot}%{_jvmdir}/default-java

# List each payload once, including directories and editable configuration.
for package in headless desktop devel jmods src demo; do
    : > "$package.files"
done
find %{buildroot}%{jvm_home} -print | LC_ALL=C sort | while IFS= read -r file; do
    path=${file#%{buildroot}}
    relative=${path#%{jvm_home}}
    case "$relative" in
        /jmods|/jmods/*) package=jmods ;;
        /demo|/demo/*) package=demo ;;
        /include|/include/*|/lib/ct.sym|/lib/libsaproc.so) package=devel ;;
        /lib/src.zip) package=src ;;
        /lib/libawt_xawt.so|/lib/libjawt.so|/lib/libsplashscreen.so|/lib/libjsound.so)
            package=desktop ;;
        /bin/*|/man/man1/*)
            tool=${relative##*/}
            tool=${tool%%.1*}
            case "$tool" in
                java|keytool|jfr|rmiregistry) package=headless ;;
                jconsole) package=desktop ;;
                *) package=devel ;;
            esac ;;
        *) package=headless ;;
    esac
    if [ -d "$file" ] && [ ! -L "$file" ]; then
        entry="%%dir $path"
    elif [ "${relative#/conf/}" != "$relative" ]; then
        entry="%%config(noreplace) $path"
    else
        entry=$path
    fi
    printf '%s\n' "$entry" >> "$package.files"
    case "$relative" in
        /bin/*)
            link=%{_bindir}/${relative##*/}
            touch "%{buildroot}$link"
            printf '%s\n' "%%ghost $link" >> "$package.files" ;;
        /man/man1/*)
            link=%{_mandir}/man1/${relative##*/}
            touch "%{buildroot}$link"
            # brp-compress also reads ghost placeholders, so use valid gzip.
            gzip -9nc < /dev/null > "%{buildroot}$link"
            printf '%s\n' "%%ghost $link" >> "$package.files" ;;
    esac
done
printf '%s\n' "%%ghost %{_jvmdir}/default-java" >> headless.files

%check
build-release/images/jdk/bin/java -version
build-release/images/jdk/bin/javac -version
build-release/images/jdk/bin/keytool -list -keystore %{system_cacerts} \
    -storepass changeit > build-release/system-cacerts.txt
test -s build-release/images/jdk/lib/security/blocked.certs
test "$(readlink %{buildroot}%{jvm_home}/lib/security/cacerts)" = "%{system_cacerts}"

cat > build-release/PackagingSmoke.java <<'EOF'
import java.awt.image.BufferedImage;
import javax.net.ssl.SSLContext;

public class PackagingSmoke {
    public static void main(String[] args) throws Exception {
        var image = new BufferedImage(8, 8, BufferedImage.TYPE_INT_RGB);
        var graphics = image.createGraphics();
        graphics.drawLine(0, 0, 7, 7);
        graphics.drawString("Java", 0, 7);
        if (graphics.getFontMetrics().stringWidth("Java") <= 0) {
            throw new AssertionError("No usable headless font");
        }
        graphics.dispose();
        SSLContext.getDefault();
    }
}
EOF
build-release/images/jdk/bin/javac -d build-release build-release/PackagingSmoke.java
build-release/images/jdk/bin/java -Djava.awt.headless=true -cp build-release PackagingSmoke

# Exercise the separately packaged modules, including configurations without
# jmods in images/jdk.
rm -rf build-release/packaging-test-runtime
build-release/images/jdk/bin/jlink --module-path build-release/images/jmods \
    --add-modules java.base --output build-release/packaging-test-runtime
build-release/packaging-test-runtime/bin/java -version

%pretrans headless
# Snapshot the group before any old monolithic postun can change its mode.
# All JDK variants share this state and pretrans runs before payload changes.
# On a fresh system alternatives may not be installed until this transaction.
if command -v alternatives >/dev/null 2>&1 && command -v readlink >/dev/null 2>&1; then
    mkdir -p %{rpm_state_dir}
    rm -f %{rpm_state_dir}/java-auto %{rpm_state_dir}/java-manual
    case "$(LC_ALL=C alternatives --display java 2>/dev/null)" in
        *'status is auto.'*)
            touch %{rpm_state_dir}/java-auto ;;
        *'status is manual.'*)
            readlink -f %{_bindir}/java > %{rpm_state_dir}/java-manual || \
                rm -f %{rpm_state_dir}/java-manual ;;
    esac
fi
:

%post headless
%register_alternatives

%posttrans headless
%register_alternatives
if [ -f %{rpm_state_dir}/java-auto ]; then
    alternatives --auto java && rm -f %{rpm_state_dir}/java-auto
elif [ -s %{rpm_state_dir}/java-manual ]; then
    selected_java=$(cat %{rpm_state_dir}/java-manual)
    if [ -x "$selected_java" ]; then
        # Another JDK's posttrans may still need to restore its candidate.
        alternatives --set java "$selected_java" && rm -f %{rpm_state_dir}/java-manual
    else
        rm -f %{rpm_state_dir}/java-manual
    fi
fi
:

%postun headless
if [ "$1" -eq 0 ]; then
    alternatives --remove java %{jvm_home}/bin/java || :
    %refresh_alternatives
fi

%post
%register_alternatives

%posttrans
%register_alternatives

%postun
if [ "$1" -eq 0 ]; then
    %register_alternatives
fi

%post devel
%register_alternatives

%posttrans devel
%register_alternatives

%postun devel
if [ "$1" -eq 0 ]; then
    %register_alternatives
fi

%files -f desktop.files

%files headless -f headless.files
%license LICENSE
%doc README.md
%dir %{_jvmdir}
%dir %{rpm_state_dir}

%files devel -f devel.files

%files jmods -f jmods.files

%files src -f src.files

%files demo -f demo.files

%changelog
%autochangelog
