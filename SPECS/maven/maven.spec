# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Use the upstream binary as the build tool until Maven can build itself.
%bcond bootstrap        1

# No native code: prevent RPM and OBS from generating debug file lists.
%global debug_package %{nil}
%undefine _build_create_debug

%global maven_home %{_datadir}/maven

Name:           maven
Version:        3.9.16
Release:        %autorelease
Summary:        Java project management and build tool
License:        Apache-2.0 AND BSD-3-Clause AND CDDL-1.1 AND EPL-2.0 AND LicenseRef-openRuyi-Public-Domain AND MIT
URL:            https://maven.apache.org/
VCS:            git:https://github.com/apache/maven.git
#!RemoteAsset:  sha256:f7031b091ad75a226a06a0c092cbf05860dcfc16d140e6da997e6c6b62dbd03c
Source0:        https://archive.apache.org/dist/maven/maven-3/%{version}/source/apache-maven-%{version}-src.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:80ffca22aed9e8b9713a232f3394fd81d7f20322df75efdb2b047dbd3e3a23bb
Source1:        https://archive.apache.org/dist/maven/maven-3/%{version}/binaries/apache-maven-%{version}-bin.tar.gz
%endif

#!RemoteAsset:  sha256:0addec670fedcd3f113c5c8091d783280d23f75e3acb841b61a9cdb079376a08
Source100:      https://repo.maven.apache.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.jar#/artifact-0000-aopalliance-1.0.jar
#!RemoteAsset:  sha256:26e82330157d6b844b67a8064945e206581e772977183e3e31fec6058aa9a59b
Source101:      https://repo.maven.apache.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom#/artifact-0001-aopalliance-1.0.pom
#!RemoteAsset:  sha256:c6c971b146ec8e596e660e64d5517aae02e34c3cce240de44bb92ccd98f046bf
Source102:      https://repo.maven.apache.org/maven2/avalon-framework/avalon-framework/4.1.3/avalon-framework-4.1.3.pom#/artifact-0002-avalon-framework-4.1.3.pom
#!RemoteAsset:  sha256:937afb220b91d8a394d78befdbf587c71aeed289d582e2a91e72a7d92172371d
Source103:      https://repo.maven.apache.org/maven2/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.jar#/artifact-0003-logback-classic-1.2.13.jar
#!RemoteAsset:  sha256:901aa9a2b52aa5fb14c853fabcdd66090c915306b623c41e91e43c11ec85f301
Source104:      https://repo.maven.apache.org/maven2/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.pom#/artifact-0004-logback-classic-1.2.13.pom
#!RemoteAsset:  sha256:07b1586faf220c05821d0f3ed8e2e417e214c83f40641f76e8a90b134c31ff6b
Source105:      https://repo.maven.apache.org/maven2/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.jar#/artifact-0005-logback-core-1.2.13.jar
#!RemoteAsset:  sha256:6a1402ecf487bb827315da679e1306e357b2aed2448578a8de058d5af39de9be
Source106:      https://repo.maven.apache.org/maven2/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.pom#/artifact-0006-logback-core-1.2.13.pom
#!RemoteAsset:  sha256:fa08315e836e63f337ad9d252194086aff541cdbd787a8b7903515ac3469364f
Source107:      https://repo.maven.apache.org/maven2/ch/qos/logback/logback-parent/1.2.13/logback-parent-1.2.13.pom#/artifact-0007-logback-parent-1.2.13.pom
#!RemoteAsset:  sha256:53ca085f4a150f703f49e1aabd935bd03b43e1ea3d55d135438292af22cef56b
Source108:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.21/jackson-annotations-2.21.jar#/artifact-0008-jackson-annotations-2.21.jar
#!RemoteAsset:  sha256:71cac5392151e2a528cc9a09179f0a334179f05c52f8e596cf58ddf12bb27f2b
Source109:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.21/jackson-annotations-2.21.pom#/artifact-0009-jackson-annotations-2.21.pom
#!RemoteAsset:  sha256:e22604bcd9b24e462d5df102007cb06e1ed811e86f1ce6081ca62f385f2db87b
Source110:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.21.0/jackson-core-2.21.0.jar#/artifact-0010-jackson-core-2.21.0.jar
#!RemoteAsset:  sha256:a0add9d219816d4da50a03d62ae21222329388822cb8aac8b5ab3d0af16aa7d6
Source111:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.21.0/jackson-core-2.21.0.pom#/artifact-0011-jackson-core-2.21.0.pom
#!RemoteAsset:  sha256:0057817ee40bc71544072dc2a3ba575ef91dce53a2d87489bde91c05f3a22621
Source112:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.21.0/jackson-databind-2.21.0.jar#/artifact-0012-jackson-databind-2.21.0.jar
#!RemoteAsset:  sha256:dc6b56c8a903d8b512791183a686769a351725bd4afb8d74ae7012ce6f0740b3
Source113:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.21.0/jackson-databind-2.21.0.pom#/artifact-0013-jackson-databind-2.21.0.pom
#!RemoteAsset:  sha256:dce86a926b76ba88d93d2b65d32dac2529ce864097cbd77808f5bb6046c8eb8b
Source114:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.21.0/jackson-base-2.21.0.pom#/artifact-0014-jackson-base-2.21.0.pom
#!RemoteAsset:  sha256:28b06c4e5f51330c4fced2b3bd6194188cfd237068ea17e592139164537721ff
Source115:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.21.0/jackson-bom-2.21.0.pom#/artifact-0015-jackson-bom-2.21.0.pom
#!RemoteAsset:  sha256:3851df627faeb46887b956104630b74a8bbb5f7de22e974cf15982e20e0373de
Source116:      https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.21/jackson-parent-2.21.pom#/artifact-0016-jackson-parent-2.21.pom
#!RemoteAsset:  sha256:fcbbf1c18c9047e6917d384f2064e21b42a58fc85fb0523a9e2e015eff7c619d
Source117:      https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/75/oss-parent-75.pom#/artifact-0017-oss-parent-75.pom
#!RemoteAsset:  sha256:bd8c30aecec123e7c00af8e8d1040d7bf824dcf175159623879aa28a3b6b2796
Source118:      https://repo.maven.apache.org/maven2/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.jar#/artifact-0018-javadoc-parser-0.3.1.jar
#!RemoteAsset:  sha256:a8d9af4593afe065251d2fbfdf12693036aae514f76fb0c50e9d40aac3385c38
Source119:      https://repo.maven.apache.org/maven2/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.pom#/artifact-0019-javadoc-parser-0.3.1.pom
#!RemoteAsset:  sha256:2dc0aa0eabd6f9f5a1f2fe62acfaa74caab834ced78518fed3750813e5dbd481
Source120:      https://repo.maven.apache.org/maven2/com/github/chhorz/javadoc-parser-parent/0.3.1/javadoc-parser-parent-0.3.1.pom#/artifact-0020-javadoc-parser-parent-0.3.1.pom
#!RemoteAsset:  sha256:fda65a9ad0e1ac0c88987106e89aa4d8b2a2495e7e042371efa83813f65b7295
Source121:      https://repo.maven.apache.org/maven2/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.jar#/artifact-0021-json-simple-3.0.2.jar
#!RemoteAsset:  sha256:b0dacb1479cd4dbe0810d1aa335bf0fb9bc3c4ff55369c87597ba68f5879fe4f
Source122:      https://repo.maven.apache.org/maven2/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.pom#/artifact-0022-json-simple-3.0.2.pom
#!RemoteAsset:  sha256:a0152b1897c4a6e7dd36e5f686f0e631c3839b5db208b38daa11a4f6dc9b25ff
Source123:      https://repo.maven.apache.org/maven2/com/github/luben/zstd-jni/1.5.5-11/zstd-jni-1.5.5-11.pom#/artifact-0023-zstd-jni-1.5.5-11.pom
#!RemoteAsset:  sha256:f72ede1b39258faf81277dc58de30c71cbae4253732558d2ce10b53d8b5763d5
Source124:      https://repo.maven.apache.org/maven2/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.jar#/artifact-0024-zstd-jni-1.5.6-3.jar
#!RemoteAsset:  sha256:dfd2fa7b1d23939216902f844fa5e86a79cdfb9209760e4c04242b5a58d49490
Source125:      https://repo.maven.apache.org/maven2/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.pom#/artifact-0025-zstd-jni-1.5.6-3.pom
#!RemoteAsset:  sha256:6d60134c7644852574cca4caa37573206b21ff21439fd3203c42785d071166b9
Source126:      https://repo.maven.apache.org/maven2/com/github/luben/zstd-jni/1.5.7-4/zstd-jni-1.5.7-4.pom#/artifact-0026-zstd-jni-1.5.7-4.pom
#!RemoteAsset:  sha256:8d6feb1da335f3ab13c584c613e23c7b3c61b392e37956872057baf8f0ca1d6f
Source127:      https://repo.maven.apache.org/maven2/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.jar#/artifact-0027-zstd-jni-1.5.7-6.jar
#!RemoteAsset:  sha256:794d9b995ed59165c54243dcc73fe9483d7fe1af7fb80fcd89a5ae5b693f3eb7
Source128:      https://repo.maven.apache.org/maven2/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.pom#/artifact-0028-zstd-jni-1.5.7-6.pom
#!RemoteAsset:  sha256:19889dbdf1b254b2601a5ee645b8147a974644882297684c798afe5d63d78dfe
Source129:      https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.pom#/artifact-0029-jsr305-3.0.2.pom
#!RemoteAsset:  sha256:dd0ce1b55a3ed2080cb70f9c655850cda86c206862310009dcb5e5c95265a5e0
Source130:      https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.13.2/gson-2.13.2.jar#/artifact-0030-gson-2.13.2.jar
#!RemoteAsset:  sha256:3aa06aa7c0f9af092961a42d09578e4324be146348a0ee6ed47857f7c2677b76
Source131:      https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.13.2/gson-2.13.2.pom#/artifact-0031-gson-2.13.2.pom
#!RemoteAsset:  sha256:83ab528a9d50fd76aeb8ad6f727b3ee9cb766586255774ed16ca8c4c76d9dacd
Source132:      https://repo.maven.apache.org/maven2/com/google/code/gson/gson-parent/2.13.2/gson-parent-2.13.2.pom#/artifact-0032-gson-parent-2.13.2.pom
#!RemoteAsset:  sha256:893d56afcea1b22f83220fd7e49a6668c5b8901e39bd59dc57b42f55673721ce
Source133:      https://repo.maven.apache.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.pom#/artifact-0033-google-collections-1.0.pom
#!RemoteAsset:  sha256:1326738a4b4f7ccacf607b866a11fb85193ef60f6a59461187ce7265f9be5bed
Source134:      https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.3.4/error_prone_annotations-2.3.4.pom#/artifact-0034-error_prone_annotations-2.3.4.pom
#!RemoteAsset:  sha256:a56e782b5b50811ac204073a355a21d915a2107fce13ec711331ad036f660fcc
Source135:      https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.jar#/artifact-0035-error_prone_annotations-2.41.0.jar
#!RemoteAsset:  sha256:a151df1e2e0b48618d8b06a180748a29b3abb39b1b2396f6a1c879a727488c6e
Source136:      https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.pom#/artifact-0036-error_prone_annotations-2.41.0.pom
#!RemoteAsset:  sha256:40495b437a60d2398f0fdfc054b89d9c394a82347a274a0721c2e950a4302186
Source137:      https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.3.4/error_prone_parent-2.3.4.pom#/artifact-0037-error_prone_parent-2.3.4.pom
#!RemoteAsset:  sha256:c538388d760a5c1c98dcf06f6ed3cfe5f11a651827db5cbd2ed8288c795cad42
Source138:      https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.41.0/error_prone_parent-2.41.0.pom#/artifact-0038-error_prone_parent-2.41.0.pom
#!RemoteAsset:  sha256:cd6db17a11a31ede794ccbd1df0e4d9750f640234731f21cff885a9997277e81
Source139:      https://repo.maven.apache.org/maven2/com/google/google/1/google-1.pom#/artifact-0039-google-1.pom
#!RemoteAsset:  sha256:e09d345e73ca3fbca7f3e05f30deb74e9d39dd6b79a93fee8c511f23417b6828
Source140:      https://repo.maven.apache.org/maven2/com/google/google/5/google-5.pom#/artifact-0040-google-5.pom
#!RemoteAsset:  sha256:e96042ce78fecba0da2be964522947c87b40a291b5fd3cd672a434924103c4b9
Source141:      https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.pom#/artifact-0041-failureaccess-1.0.1.pom
#!RemoteAsset:  sha256:cbfc3906b19b8f55dd7cfd6dfe0aa4532e834250d7f080bd8d211a3e246b59cb
Source142:      https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.jar#/artifact-0042-failureaccess-1.0.3.jar
#!RemoteAsset:  sha256:c54beff37f6d42d43e14722d54a522c9ad51ef97fc5b79277e62a3ebf882f3bb
Source143:      https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.pom#/artifact-0043-failureaccess-1.0.3.pom
#!RemoteAsset:  sha256:9646d4cd50094d4abe507e555d3f76d77e34a4c5566b22fb130ef55d4ebbe927
Source144:      https://repo.maven.apache.org/maven2/com/google/guava/guava/30.1-jre/guava-30.1-jre.pom#/artifact-0044-guava-30.1-jre.pom
#!RemoteAsset:  sha256:dc573e1fca4fd5454f4a5fd3d7da2df03002876a4175bafc14a95980dd7713b3
Source145:      https://repo.maven.apache.org/maven2/com/google/guava/guava/33.6.0-jre/guava-33.6.0-jre.jar#/artifact-0045-guava-33.6.0-jre.jar
#!RemoteAsset:  sha256:b45b78944280054311c53da9270809fb40dcabc408ce66ce55730099b4f57d32
Source146:      https://repo.maven.apache.org/maven2/com/google/guava/guava/33.6.0-jre/guava-33.6.0-jre.pom#/artifact-0046-guava-33.6.0-jre.pom
#!RemoteAsset:  sha256:f8698ab46ca996ce889c1afc8ca4f25eb8ac6b034dc898d4583742360016cc04
Source147:      https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom#/artifact-0047-guava-parent-26.0-android.pom
#!RemoteAsset:  sha256:e2afb747ebc4fe2328d6a90fa88c5d8a83bb1e32061bb9b10ff43e2c47ad6e73
Source148:      https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/30.1-jre/guava-parent-30.1-jre.pom#/artifact-0048-guava-parent-30.1-jre.pom
#!RemoteAsset:  sha256:7220ede61026596fbc720ee4b93246fa2d14f328058532b59ef053de397c7d83
Source149:      https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/33.4.0-android/guava-parent-33.4.0-android.pom#/artifact-0049-guava-parent-33.4.0-android.pom
#!RemoteAsset:  sha256:374bd31f61b1cf612bee9ab2e4d70bbdf77dd85a49b431f809d4fbdc901f2dd4
Source150:      https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/33.6.0-jre/guava-parent-33.6.0-jre.pom#/artifact-0050-guava-parent-33.6.0-jre.pom
#!RemoteAsset:  sha256:18d4b1db26153d4e55079ce1f76bb1fe05cdb862ef9954a88cbcc4ff38b8679b
Source151:      https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom#/artifact-0051-listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom
#!RemoteAsset:  sha256:142ad4475e19524d2fe3ac995b3f7cbc962fc726f2edb9dbdccc61feab9b2bf9
Source152:      https://repo.maven.apache.org/maven2/com/google/inject/guice/5.1.0/guice-5.1.0-classes.jar#/artifact-0052-guice-5.1.0-classes.jar
#!RemoteAsset:  sha256:b3b8dc65213d623fb70ed7958dbdd616324256ba836a31652560c388999fd9cd
Source153:      https://repo.maven.apache.org/maven2/com/google/inject/guice/5.1.0/guice-5.1.0.pom#/artifact-0053-guice-5.1.0.pom
#!RemoteAsset:  sha256:63d5c0c641797deba6c051c47d5f6923f3a103ef71e4ebc3a85d01c3e878596c
Source154:      https://repo.maven.apache.org/maven2/com/google/inject/guice-parent/5.1.0/guice-parent-5.1.0.pom#/artifact-0054-guice-parent-5.1.0.pom
#!RemoteAsset:  sha256:5faca824ba115bee458730337dfdb2fcea46ba2fd774d4304edbf30fa6a3f055
Source155:      https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/1.3/j2objc-annotations-1.3.pom#/artifact-0055-j2objc-annotations-1.3.pom
#!RemoteAsset:  sha256:1973d499cc2c1264aff2d6d052a1c716ae613d018ae1c2f610dd6a4d1c24578e
Source156:      https://repo.maven.apache.org/maven2/com/sun/activation/all/1.2.2/all-1.2.2.pom#/artifact-0056-all-1.2.2.pom
#!RemoteAsset:  sha256:ff70c10165714fe9546c418a65d74ecd5d57623ba408cecde9428f0a609b5d1c
Source157:      https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar#/artifact-0057-qdox-2.0.3.jar
#!RemoteAsset:  sha256:e7ebaead3c95e74934451fc5b5ae9d02066303db67430f59fe219714efcf3bf3
Source158:      https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom#/artifact-0058-qdox-2.0.3.pom
#!RemoteAsset:  sha256:c260c3230b2340af97d54bf01f7f67ebc57c901922736c881bb11cb981302be2
Source159:      https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.2.0/qdox-2.2.0.jar#/artifact-0059-qdox-2.2.0.jar
#!RemoteAsset:  sha256:c850fbad0b05eada85ca1bce22409a75f758aea0ca1e47a828c6a505ad361fab
Source160:      https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.2.0/qdox-2.2.0.pom#/artifact-0060-qdox-2.2.0.pom
#!RemoteAsset:  sha256:552ad56800bc6010f1e6ea8c7638f24c74230e9991a52568df20d5b5aa5c4b20
Source161:      https://repo.maven.apache.org/maven2/commons-beanutils/commons-beanutils/1.8.3/commons-beanutils-1.8.3.pom#/artifact-0061-commons-beanutils-1.8.3.pom
#!RemoteAsset:  sha256:7d938c81789028045c08c065e94be75fc280527620d5bd62b519d5838532368a
Source162:      https://repo.maven.apache.org/maven2/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.jar#/artifact-0062-commons-beanutils-1.9.4.jar
#!RemoteAsset:  sha256:c35cca7b61d4678d9578cbc0b901b8717b539abf9254441da78b8fe60de064d0
Source163:      https://repo.maven.apache.org/maven2/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.pom#/artifact-0063-commons-beanutils-1.9.4.pom
#!RemoteAsset:  sha256:e408f72da5ed4c5db6ae19e8c3b7ee36259c36c05f7a77f15509a014bfe7bcaa
Source164:      https://repo.maven.apache.org/maven2/commons-chain/commons-chain/1.1/commons-chain-1.1.jar#/artifact-0064-commons-chain-1.1.jar
#!RemoteAsset:  sha256:cf0c15c4e843507d95be11114039794494d6fc6259118581a90e03b2db5f5acb
Source165:      https://repo.maven.apache.org/maven2/commons-chain/commons-chain/1.1/commons-chain-1.1.pom#/artifact-0065-commons-chain-1.1.pom
#!RemoteAsset:  sha256:8f7f8605d68e15bf32db61ec94eac6fdafc51b1bdbe1e0e0802b57d23f387792
Source166:      https://repo.maven.apache.org/maven2/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.jar#/artifact-0066-commons-cli-1.11.0.jar
#!RemoteAsset:  sha256:96651f573e3c080e11052ff08bfc2e4cf04cf6eb1a3e3683010f4979496e0808
Source167:      https://repo.maven.apache.org/maven2/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.pom#/artifact-0067-commons-cli-1.11.0.pom
#!RemoteAsset:  sha256:69e1237059acd56f0f8654dcde09d8a1412eee82918bef5564d51f8fb275711b
Source168:      https://repo.maven.apache.org/maven2/commons-cli/commons-cli/1.6.0/commons-cli-1.6.0.jar#/artifact-0068-commons-cli-1.6.0.jar
#!RemoteAsset:  sha256:c770260b9534ef13940fa087a5b0196ac54a64d0dcd485deae66c4adaa6c1758
Source169:      https://repo.maven.apache.org/maven2/commons-cli/commons-cli/1.6.0/commons-cli-1.6.0.pom#/artifact-0069-commons-cli-1.6.0.pom
#!RemoteAsset:  sha256:e599d5318e97aa48f42136a2927e6dfa4e8881dff0e6c8e3109ddbbff51d7b7d
Source170:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.11/commons-codec-1.11.jar#/artifact-0070-commons-codec-1.11.jar
#!RemoteAsset:  sha256:c1e7140d1dea8fdf3528bc1e3c5444ac0b541297311f45f9806c213ec3ee9a10
Source171:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.11/commons-codec-1.11.pom#/artifact-0071-commons-codec-1.11.pom
#!RemoteAsset:  sha256:b826ddd92f9d7cc64371a02fa0830c154d67c98370ea54a2d196e72eb590ad28
Source172:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.16.1/commons-codec-1.16.1.pom#/artifact-0072-commons-codec-1.16.1.pom
#!RemoteAsset:  sha256:f700de80ac270d0344fdea7468201d8b9c805e5c648331c3619f2ee067ccfc59
Source173:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.jar#/artifact-0073-commons-codec-1.17.0.jar
#!RemoteAsset:  sha256:c01c4cda5e408f41ed1d83e4a0a170cf53801b6338aba49f0f904786bc1214fc
Source174:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.pom#/artifact-0074-commons-codec-1.17.0.pom
#!RemoteAsset:  sha256:5c3881e4f556855e9c532927ee0c9dfde94cc66760d5805c031a59887070af5f
Source175:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.jar#/artifact-0075-commons-codec-1.19.0.jar
#!RemoteAsset:  sha256:e0f3269fa23de0c83130c5659f5f9514cc5422c0bcdf45f2eae004a78b9fca34
Source176:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.pom#/artifact-0076-commons-codec-1.19.0.pom
#!RemoteAsset:  sha256:4da851cb6abfb98bfe9eb77c5e5fc47f5414fa28b94e21b7fd9a646705dc167f
Source177:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.21.0/commons-codec-1.21.0.jar#/artifact-0077-commons-codec-1.21.0.jar
#!RemoteAsset:  sha256:b230416ba6f5bf9df8fcb6e7f4a6c26b8fb0fe85ce371d13d5846ed3768309b7
Source178:      https://repo.maven.apache.org/maven2/commons-codec/commons-codec/1.21.0/commons-codec-1.21.0.pom#/artifact-0078-commons-codec-1.21.0.pom
#!RemoteAsset:  sha256:f8a93d50bfaf6fc0720eee8fde6e8fde20da33238ba296e9b1b7cba50ca6d772
Source179:      https://repo.maven.apache.org/maven2/commons-collections/commons-collections/2.1/commons-collections-2.1.pom#/artifact-0079-commons-collections-2.1.pom
#!RemoteAsset:  sha256:59c9e5fc75e5790e56976c166a89f2cbdad99f76c49b92f74a1749689af726a2
Source180:      https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.1/commons-collections-3.1.pom#/artifact-0080-commons-collections-3.1.pom
#!RemoteAsset:  sha256:6da6d5e61be60d77a7eea6c7d0b8ac3cc35ca73cef3cbff97d5982006553786d
Source181:      https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.2/commons-collections-3.2.pom#/artifact-0081-commons-collections-3.2.pom
#!RemoteAsset:  sha256:1f9626cbaa584ed5d86021866e4e367e26fe5efc248382652be68beeb43e7416
Source182:      https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.2.1/commons-collections-3.2.1.pom#/artifact-0082-commons-collections-3.2.1.pom
#!RemoteAsset:  sha256:eeeae917917144a68a741d4c0dff66aa5c5c5fd85593ff217bced3fc8ca783b8
Source183:      https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar#/artifact-0083-commons-collections-3.2.2.jar
#!RemoteAsset:  sha256:d5d81fcc288c0d8c711c302007cada4aa9a226ed1a112d4baa64cb1d6322170b
Source184:      https://repo.maven.apache.org/maven2/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.pom#/artifact-0084-commons-collections-3.2.2.pom
#!RemoteAsset:  sha256:9ef0db04ffe98d03eb9a921337364be7d123d58d66dcaff3eac763f0b0c63d48
Source185:      https://repo.maven.apache.org/maven2/commons-digester/commons-digester/1.6/commons-digester-1.6.pom#/artifact-0085-commons-digester-1.6.pom
#!RemoteAsset:  sha256:05662373044f3dff112567b7bb5dfa1174e91e074c0c727b4412788013f49d56
Source186:      https://repo.maven.apache.org/maven2/commons-digester/commons-digester/1.8/commons-digester-1.8.jar#/artifact-0086-commons-digester-1.8.jar
#!RemoteAsset:  sha256:c10144f223d7ab697ccea7da0e753b75603ea7fbc4e35570068e6c477068e9b5
Source187:      https://repo.maven.apache.org/maven2/commons-digester/commons-digester/1.8/commons-digester-1.8.pom#/artifact-0087-commons-digester-1.8.pom
#!RemoteAsset:  sha256:961b2f6d87dbacc5d54abf45ab7a6e2495f89b75598962d8c723cea9bc210908
Source188:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar#/artifact-0088-commons-io-2.11.0.jar
#!RemoteAsset:  sha256:2e016fd7e3244b5f2c20acad834d93aa4790486ee1e4564641361a3e831eef59
Source189:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom#/artifact-0089-commons-io-2.11.0.pom
#!RemoteAsset:  sha256:a58af12ee1b68cfd2ebb0c27caef164f084381a00ec81a48cc275fd7ea54e154
Source190:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.15.1/commons-io-2.15.1.jar#/artifact-0090-commons-io-2.15.1.jar
#!RemoteAsset:  sha256:171a1af82b6759eb5740b3b8809aca80113deaf1153036f2f4445901dfd3f91d
Source191:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.15.1/commons-io-2.15.1.pom#/artifact-0091-commons-io-2.15.1.pom
#!RemoteAsset:  sha256:f41f7baacd716896447ace9758621f62c1c6b0a91d89acee488da26fc477c84f
Source192:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.16.1/commons-io-2.16.1.jar#/artifact-0092-commons-io-2.16.1.jar
#!RemoteAsset:  sha256:5777d292251c7895c04a4c57015683ec3b353a12486c9b3e7178e9b0b3c38fff
Source193:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom#/artifact-0093-commons-io-2.16.1.pom
#!RemoteAsset:  sha256:484a939fff5310b8cb5c6b9029c2dcf155d3f93b8b8d6285f3f56bb2ba09fc49
Source194:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom#/artifact-0094-commons-io-2.17.0.pom
#!RemoteAsset:  sha256:824268919b4b62f9f40f08c54381de5993b078f58667e332d17348ae019d72b9
Source195:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar#/artifact-0095-commons-io-2.19.0.jar
#!RemoteAsset:  sha256:542b7a502ed61950d1b83112b51b1617d3407e3a4df5ab56a98d760e0f8c5950
Source196:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom#/artifact-0096-commons-io-2.19.0.pom
#!RemoteAsset:  sha256:df90bba0fe3cb586b7f164e78fe8f8f4da3f2dd5c27fa645f888100ccc25dd72
Source197:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.20.0/commons-io-2.20.0.jar#/artifact-0097-commons-io-2.20.0.jar
#!RemoteAsset:  sha256:bdbdf81072c190ee9a8b181a5c58f5bd917a750fb13a256debbf53f5dbd33a2a
Source198:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.20.0/commons-io-2.20.0.pom#/artifact-0098-commons-io-2.20.0.pom
#!RemoteAsset:  sha256:7d643a2afea8b058b762aa6fb90e5b256f6c729739f8b3784c3370ddc609e88d
Source199:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar#/artifact-0099-commons-io-2.21.0.jar
#!RemoteAsset:  sha256:ae47795e721803ec8ff1deed74be28a811a02713bd5a3ab0ac67c2b58cb635ab
Source200:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.21.0/commons-io-2.21.0.pom#/artifact-0100-commons-io-2.21.0.pom
#!RemoteAsset:  sha256:2b9a7b1f726fb86216dbd2c8321eabe0221dbd5b1be81c18e1cb53811b104758
Source201:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.22.0/commons-io-2.22.0.jar#/artifact-0101-commons-io-2.22.0.jar
#!RemoteAsset:  sha256:6425cec0ea760035efa77277de85f89fa6dbed147ab3dd95b8d2cbc55340accf
Source202:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.22.0/commons-io-2.22.0.pom#/artifact-0102-commons-io-2.22.0.pom
#!RemoteAsset:  sha256:28ebb2998bc7d7acb25078526971640892000f3413586ff42d611f1043bfec30
Source203:      https://repo.maven.apache.org/maven2/commons-io/commons-io/2.5/commons-io-2.5.pom#/artifact-0103-commons-io-2.5.pom
#!RemoteAsset:  sha256:226cb33a644995b084b3bdd42f2eb861509e6db71d7a343d411ee321387b0860
Source204:      https://repo.maven.apache.org/maven2/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.jar#/artifact-0104-commons-jxpath-1.4.0.jar
#!RemoteAsset:  sha256:d7b9524036a834ca39e6575a8d124eb2020a1884f069468aed2746630afdb8ac
Source205:      https://repo.maven.apache.org/maven2/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.pom#/artifact-0105-commons-jxpath-1.4.0.pom
#!RemoteAsset:  sha256:2c73b940c91250bc98346926270f13a6a10bb6e29d2c9316a70d134e382c873e
Source206:      https://repo.maven.apache.org/maven2/commons-lang/commons-lang/2.4/commons-lang-2.4.jar#/artifact-0106-commons-lang-2.4.jar
#!RemoteAsset:  sha256:90306278d39ed5a50dafa468adee4d272b635d54c4f7295e293e42bbdb8ad666
Source207:      https://repo.maven.apache.org/maven2/commons-lang/commons-lang/2.4/commons-lang-2.4.pom#/artifact-0107-commons-lang-2.4.pom
#!RemoteAsset:  sha256:52b3caa59ca5e8f6279421ecb517a0b24571d666ea86bb145462076760026a6f
Source208:      https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.0/commons-logging-1.0.pom#/artifact-0108-commons-logging-1.0.pom
#!RemoteAsset:  sha256:8c23c6e92f1df7f58b455cd2caa009dcc87a2fe64976e6ce461522e635aea41e
Source209:      https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.0.3/commons-logging-1.0.3.pom#/artifact-0109-commons-logging-1.0.3.pom
#!RemoteAsset:  sha256:1f68425fce1007c3343343a27c27057f1427970682cb6d33e493c111721f7cb6
Source210:      https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.1/commons-logging-1.1.pom#/artifact-0110-commons-logging-1.1.pom
#!RemoteAsset:  sha256:d0f2e16d054e8bb97add9ca26525eb2346f692809fcd2a28787da8ceb3c35ee8
Source211:      https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.pom#/artifact-0111-commons-logging-1.1.1.pom
#!RemoteAsset:  sha256:daddea1ea0be0f56978ab3006b8ac92834afeefbd9b7e4e6316fca57df0fa636
Source212:      https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.jar#/artifact-0112-commons-logging-1.2.jar
#!RemoteAsset:  sha256:c91ab5aa570d86f6fd07cc158ec6bc2c50080402972ee9179fe24100739fbb20
Source213:      https://repo.maven.apache.org/maven2/commons-logging/commons-logging/1.2/commons-logging-1.2.pom#/artifact-0113-commons-logging-1.2.pom
#!RemoteAsset:  sha256:50bd5c21b5fbd27b8bbb5f8050544b53f49a4480fd347ce9c46d55c706015156
Source214:      https://repo.maven.apache.org/maven2/dom4j/dom4j/1.1/dom4j-1.1.jar#/artifact-0114-dom4j-1.1.jar
#!RemoteAsset:  sha256:03c18c93b1df85cbce3a21a17d9b27e399e27478c1421071f5348c58bd0ab61f
Source215:      https://repo.maven.apache.org/maven2/dom4j/dom4j/1.1/dom4j-1.1.pom#/artifact-0115-dom4j-1.1.pom
#!RemoteAsset:  sha256:18ccd104cbd97eb44bd57b68c047ab7ff81fbc800987f82d815c68ac4c2304ce
Source216:      https://repo.maven.apache.org/maven2/io/airlift/airbase/112/airbase-112.pom#/artifact-0116-airbase-112.pom
#!RemoteAsset:  sha256:fdbef3137a28f63bb0cb93487803080ede746a4ec3d421e36c6f0c305c35e5e4
Source217:      https://repo.maven.apache.org/maven2/io/airlift/aircompressor/0.27/aircompressor-0.27.jar#/artifact-0117-aircompressor-0.27.jar
#!RemoteAsset:  sha256:5aacda89be38563bdf3bfac79333616c0802ca617070dea66ba649507c994441
Source218:      https://repo.maven.apache.org/maven2/io/airlift/aircompressor/0.27/aircompressor-0.27.pom#/artifact-0118-aircompressor-0.27.pom
#!RemoteAsset:  sha256:a187a939103aef5849a7af84bd7e27be2d120c410af291437375ffe061f4f09d
Source219:      https://repo.maven.apache.org/maven2/jakarta/activation/jakarta.activation-api/1.2.2/jakarta.activation-api-1.2.2.jar#/artifact-0119-jakarta.activation-api-1.2.2.jar
#!RemoteAsset:  sha256:5e50fe938068471f504a7efc4071823425b520eabc6f80c72d935ebd54683091
Source220:      https://repo.maven.apache.org/maven2/jakarta/activation/jakarta.activation-api/1.2.2/jakarta.activation-api-1.2.2.pom#/artifact-0120-jakarta.activation-api-1.2.2.pom
#!RemoteAsset:  sha256:c04539f472e9a6dd0c7685ea82d677282269ab8e7baca2e14500e381e0c6cec5
Source221:      https://repo.maven.apache.org/maven2/jakarta/xml/bind/jakarta.xml.bind-api/2.3.3/jakarta.xml.bind-api-2.3.3.jar#/artifact-0121-jakarta.xml.bind-api-2.3.3.jar
#!RemoteAsset:  sha256:7fe2ca5dce4b14a646bbf921d13ca42caf2a2c0654da155c7563865c989396fd
Source222:      https://repo.maven.apache.org/maven2/jakarta/xml/bind/jakarta.xml.bind-api/2.3.3/jakarta.xml.bind-api-2.3.3.pom#/artifact-0122-jakarta.xml.bind-api-2.3.3.pom
#!RemoteAsset:  sha256:280da531760166d4412368d0dd899ef4aebfd0a7d82bf233502e29856806ada9
Source223:      https://repo.maven.apache.org/maven2/jakarta/xml/bind/jakarta.xml.bind-api-parent/2.3.3/jakarta.xml.bind-api-parent-2.3.3.pom#/artifact-0123-jakarta.xml.bind-api-parent-2.3.3.pom
#!RemoteAsset:  sha256:e04ba5195bcd555dc95650f7cc614d151e4bcd52d29a10b8aa2197f3ab89ab9b
Source224:      https://repo.maven.apache.org/maven2/javax/annotation/javax.annotation-api/1.3.2/javax.annotation-api-1.3.2.jar#/artifact-0124-javax.annotation-api-1.3.2.jar
#!RemoteAsset:  sha256:46a4a251ca406e78e4853d7a2bae83282844a4992851439ee9a1f23716f06b97
Source225:      https://repo.maven.apache.org/maven2/javax/annotation/javax.annotation-api/1.3.2/javax.annotation-api-1.3.2.pom#/artifact-0125-javax.annotation-api-1.3.2.pom
#!RemoteAsset:  sha256:91c77044a50c481636c32d916fd89c9118a72195390452c81065080f957de7ff
Source226:      https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar#/artifact-0126-javax.inject-1.jar
#!RemoteAsset:  sha256:943e12b100627804638fa285805a0ab788a680266531e650921ebfe4621a8bfa
Source227:      https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.pom#/artifact-0127-javax.inject-1.pom
#!RemoteAsset:  sha256:cb54dedc5d8c4510148dfa792701cbac1a84c383a84f48f5a32e6d7e460bbb72
Source228:      https://repo.maven.apache.org/maven2/log4j/log4j/1.2.12/log4j-1.2.12.pom#/artifact-0128-log4j-1.2.12.pom
#!RemoteAsset:  sha256:3de328dfa1b563ba6dfc5829774cf2f8dab0dc9528ed2731c35251ab7fd6c4c6
Source229:      https://repo.maven.apache.org/maven2/logkit/logkit/1.0.1/logkit-1.0.1.pom#/artifact-0129-logkit-1.0.1.pom
#!RemoteAsset:  sha256:0e6b935bfcb3e451d525956acad53ec86ff916d714abdbd32b3d2039771896f8
Source230:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.jar#/artifact-0130-byte-buddy-1.10.14.jar
#!RemoteAsset:  sha256:3b39ca3d5ebb9ab757f9d42dcd6b677c88b4828edca7f6079f11bbf2ef3cee58
Source231:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.pom#/artifact-0131-byte-buddy-1.10.14.pom
#!RemoteAsset:  sha256:030704139e46f32c38d27060edee9e0676b0a0fff8a8be53461515154ba8a7be
Source232:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.jar#/artifact-0132-byte-buddy-1.12.19.jar
#!RemoteAsset:  sha256:435fb8664aa9b7e120c8dd6c707d4eafa642fa262dff6d5e3f71dc25c69e89eb
Source233:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.pom#/artifact-0133-byte-buddy-1.12.19.pom
#!RemoteAsset:  sha256:30272167eceb1cb68fa84730a12d1abfd1daed6ae0c19fdefee47a9a9a0cfd33
Source234:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.jar#/artifact-0134-byte-buddy-agent-1.10.14.jar
#!RemoteAsset:  sha256:8712c22885e16de69179f921d501516493a7cef64997995fc428e7e58b12ea8d
Source235:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.pom#/artifact-0135-byte-buddy-agent-1.10.14.pom
#!RemoteAsset:  sha256:3a70240de7cdcde04e7c504c2327d7035b9c25ae0206881e3bf4e6798a273ed8
Source236:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.jar#/artifact-0136-byte-buddy-agent-1.12.19.jar
#!RemoteAsset:  sha256:b5a2cff643681de1687fc40acd251feefdfca23e673e049fb3c3692b53526d4b
Source237:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.pom#/artifact-0137-byte-buddy-agent-1.12.19.pom
#!RemoteAsset:  sha256:1fceef152e3962c8fbb3a860110324c7b14f417b925b07edf6ba997cdcf52eb9
Source238:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.10.14/byte-buddy-parent-1.10.14.pom#/artifact-0138-byte-buddy-parent-1.10.14.pom
#!RemoteAsset:  sha256:72ab6fef409e812921f4728b3c4b6ef4fa53bc25fabb0488fc2cae367368b54d
Source239:      https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.12.19/byte-buddy-parent-1.12.19.pom#/artifact-0139-byte-buddy-parent-1.12.19.pom
#!RemoteAsset:  sha256:30f5789efa39ddbf96095aada3fc1260c4561faf2f714686717cb2dc5049475a
Source240:      https://repo.maven.apache.org/maven2/net/java/jvnet-parent/3/jvnet-parent-3.pom#/artifact-0140-jvnet-parent-3.pom
#!RemoteAsset:  sha256:6080016e148acf31bd0763ce0d73e4b49f68a7d7c0e35b71ac7ebe3561e6d59e
Source241:      https://repo.maven.apache.org/maven2/nl/basjes/codeowners/codeowners-parent/1.3.1/codeowners-parent-1.3.1.pom#/artifact-0141-codeowners-parent-1.3.1.pom
#!RemoteAsset:  sha256:0806c490191002861b9df874568670b997f78872cd2a65bd890e19543adea5ef
Source242:      https://repo.maven.apache.org/maven2/nl/basjes/gitignore/gitignore-reader/1.3.1/gitignore-reader-1.3.1.jar#/artifact-0142-gitignore-reader-1.3.1.jar
#!RemoteAsset:  sha256:c38fbe50d078d44885162d2b95e75691588ba75a22760a37a25eb8197aa97d32
Source243:      https://repo.maven.apache.org/maven2/nl/basjes/gitignore/gitignore-reader/1.3.1/gitignore-reader-1.3.1.pom#/artifact-0143-gitignore-reader-1.3.1.pom
#!RemoteAsset:  sha256:ff513db0361fd41237bef4784968bc15aae478d4ec0a9496f811072ccaf3841d
Source244:      https://repo.maven.apache.org/maven2/org/apache/apache/13/apache-13.pom#/artifact-0144-apache-13.pom
#!RemoteAsset:  sha256:9f85ff2fd7d6cb3097aa47fb419ee7f0ebe869109f98aba9f4eca3f49e74a40e
Source245:      https://repo.maven.apache.org/maven2/org/apache/apache/16/apache-16.pom#/artifact-0145-apache-16.pom
#!RemoteAsset:  sha256:7831307285fd475bbc36b20ae38e7882f11c3153b1d5930f852d44eda8f33c17
Source246:      https://repo.maven.apache.org/maven2/org/apache/apache/18/apache-18.pom#/artifact-0146-apache-18.pom
#!RemoteAsset:  sha256:91f7a33096ea69bac2cbaf6d01feb934cac002c48d8c8cfa9c240b40f1ec21df
Source247:      https://repo.maven.apache.org/maven2/org/apache/apache/19/apache-19.pom#/artifact-0147-apache-19.pom
#!RemoteAsset:  sha256:af10c108da014f17cafac7b52b2b4b5a3a1c18265fa2af97a325d9143537b380
Source248:      https://repo.maven.apache.org/maven2/org/apache/apache/21/apache-21.pom#/artifact-0148-apache-21.pom
#!RemoteAsset:  sha256:bc10624e0623f36577fac5639ca2936d3240ed152fb6d8d533ab4d270543491c
Source249:      https://repo.maven.apache.org/maven2/org/apache/apache/23/apache-23.pom#/artifact-0149-apache-23.pom
#!RemoteAsset:  sha256:3e49037174820bbd0df63420a977255886398954c2a06291fa61f727ac35b377
Source250:      https://repo.maven.apache.org/maven2/org/apache/apache/29/apache-29.pom#/artifact-0150-apache-29.pom
#!RemoteAsset:  sha256:63dd4a393a9c0dfcb314efe83871a41d243bc8d200cbc7f2d197f30da78239d8
Source251:      https://repo.maven.apache.org/maven2/org/apache/apache/30/apache-30.pom#/artifact-0151-apache-30.pom
#!RemoteAsset:  sha256:555d0c9eaa69c042aff924927b9381e8f8174136d355eead445224452e6291cc
Source252:      https://repo.maven.apache.org/maven2/org/apache/apache/31/apache-31.pom#/artifact-0152-apache-31.pom
#!RemoteAsset:  sha256:cfd872c0ec27f53ae68f43dbc0fecded8add773079a53afbd390e407b42ce72f
Source253:      https://repo.maven.apache.org/maven2/org/apache/apache/32/apache-32.pom#/artifact-0153-apache-32.pom
#!RemoteAsset:  sha256:d78bd8524c5f8380a190a6525686629a95dfe512df21111383a6d8c0923a4415
Source254:      https://repo.maven.apache.org/maven2/org/apache/apache/33/apache-33.pom#/artifact-0154-apache-33.pom
#!RemoteAsset:  sha256:3671ae9d4d062ae3bb985731c76088bb2f6f7d7254e2d304ee9f690b97651328
Source255:      https://repo.maven.apache.org/maven2/org/apache/apache/34/apache-34.pom#/artifact-0155-apache-34.pom
#!RemoteAsset:  sha256:ea297dcd114136e8b8e8b630230d52a76c2fc69f6c5db25d672b1857000728b8
Source256:      https://repo.maven.apache.org/maven2/org/apache/apache/35/apache-35.pom#/artifact-0156-apache-35.pom
#!RemoteAsset:  sha256:524ec4787aff73af6b3a9fafa154c7f1881b648299b663fdbfcadda1286f2353
Source257:      https://repo.maven.apache.org/maven2/org/apache/apache/37/apache-37.pom#/artifact-0157-apache-37.pom
#!RemoteAsset:  sha256:9b0a5f28ddfb4b7500a37022bee8245efdd044fb9a3d79fb827550923eccc4b5
Source258:      https://repo.maven.apache.org/maven2/org/apache/apache/38/apache-38.pom#/artifact-0158-apache-38.pom
#!RemoteAsset:  sha256:9e9323a26ba8eb2394efef0c96d31b70df570808630dc147cab1e73541cc5194
Source259:      https://repo.maven.apache.org/maven2/org/apache/apache/4/apache-4.pom#/artifact-0159-apache-4.pom
#!RemoteAsset:  sha256:1933a6037439b389bda2feaccfc0113880fd8d88f7d240d2052b91108dd5ae89
Source260:      https://repo.maven.apache.org/maven2/org/apache/apache/5/apache-5.pom#/artifact-0160-apache-5.pom
#!RemoteAsset:  sha256:12edb5096e13f40c362d0bd40902589fa9586505123fa26799ce50b116fa5bb3
Source261:      https://repo.maven.apache.org/maven2/org/apache/apache/6/apache-6.pom#/artifact-0161-apache-6.pom
#!RemoteAsset:  sha256:1397ce1db433adc9f223dbf07496d133681448751f4ae29e58f68e78fb4b6c25
Source262:      https://repo.maven.apache.org/maven2/org/apache/apache/7/apache-7.pom#/artifact-0162-apache-7.pom
#!RemoteAsset:  sha256:4946e60a547c8eda69f3bc23c5b6f0dadcf8469ea49b1d1da7de34aecfcf18dd
Source263:      https://repo.maven.apache.org/maven2/org/apache/apache/9/apache-9.pom#/artifact-0163-apache-9.pom
#!RemoteAsset:  sha256:eb9dba4d79e9984360fe7768671a4c1cfb84d594d92f952803decdcc82a613fe
Source264:      https://repo.maven.apache.org/maven2/org/apache/apache/resources/apache-jar-resource-bundle/1.8/apache-jar-resource-bundle-1.8.jar#/artifact-0164-apache-jar-resource-bundle-1.8.jar
#!RemoteAsset:  sha256:1df8b9430b5c8ed143d7815e403e33ef5371b2400aadbe9bda0883762e0846d1
Source265:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.jar#/artifact-0165-commons-collections4-4.4.jar
#!RemoteAsset:  sha256:271bd673839af46e73aff957e2918d4bf96f5ac4f6c6cf4d5be93fd1f1271c4d
Source266:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.pom#/artifact-0166-commons-collections4-4.4.pom
#!RemoteAsset:  sha256:d0ec8014ebbb0749f471803122b21796afddf2e98e194e4374622e5fbaf69f49
Source267:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.25.0/commons-compress-1.25.0.jar#/artifact-0167-commons-compress-1.25.0.jar
#!RemoteAsset:  sha256:ba5cda496643a906fcb77b1f13c5c7de817133c977a417e8a835fe28a6518ece
Source268:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.25.0/commons-compress-1.25.0.pom#/artifact-0168-commons-compress-1.25.0.pom
#!RemoteAsset:  sha256:5f448a021d88c96f3840dfe619128d62e5cfb62712cd6e66dca8a7704945b06e
Source269:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.26.1/commons-compress-1.26.1.pom#/artifact-0169-commons-compress-1.26.1.pom
#!RemoteAsset:  sha256:9168a03141d8fc7eda21a2360d83cc0412bcbb1d6204d992bd48c2573cb3c6b8
Source270:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.jar#/artifact-0170-commons-compress-1.26.2.jar
#!RemoteAsset:  sha256:1428719895cd0a913aee33e2424b9a804b10f1197e5d35a9ce99cf2a1174cb0e
Source271:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.pom#/artifact-0171-commons-compress-1.26.2.pom
#!RemoteAsset:  sha256:e1522945218456f3649a39bc4afd70ce4bd466221519dba7d378f2141a4642ca
Source272:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.jar#/artifact-0172-commons-compress-1.28.0.jar
#!RemoteAsset:  sha256:033f4c78d632da88d0eb8ead974fc14a264392cebf12ab6c68d6cea7adf0c64a
Source273:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.pom#/artifact-0173-commons-compress-1.28.0.pom
#!RemoteAsset:  sha256:1c150e3d2df4b4237b47e28fea2079fb0da324578d5cca6a5fed2e37a62082ec
Source274:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.jar#/artifact-0174-commons-digester3-3.2.jar
#!RemoteAsset:  sha256:5bb8a198adb597c30204b4f1c336fdb3d2816536403e9ad3349ab200032e5445
Source275:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.pom#/artifact-0175-commons-digester3-3.2.pom
#!RemoteAsset:  sha256:005b5a3a88736bd2584f69cc59467e67c106e6a4b7a2dbd1ba2251267e96011d
Source276:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.10/commons-lang3-3.10.pom#/artifact-0176-commons-lang3-3.10.pom
#!RemoteAsset:  sha256:980d665d83fed04665134f0578e507442a0e750691073784391b0a7988724a75
Source277:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.11/commons-lang3-3.11.pom#/artifact-0177-commons-lang3-3.11.pom
#!RemoteAsset:  sha256:110438863bad37c28f906bf87016e38c7a8c758ba321e09d11dc5a2363a8e79e
Source278:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom#/artifact-0178-commons-lang3-3.14.0.pom
#!RemoteAsset:  sha256:6ee731df5c8e5a2976a1ca023b6bb320ea8d3539fbe64c8a1d5cb765127c33b4
Source279:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar#/artifact-0179-commons-lang3-3.17.0.jar
#!RemoteAsset:  sha256:351c6e4940e939b1f330df47f60f13ba383db81ee008181af541f3a2a6d2a56c
Source280:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom#/artifact-0180-commons-lang3-3.17.0.pom
#!RemoteAsset:  sha256:4eeeae8d20c078abb64b015ec158add383ac581571cddc45c68f0c9ae0230720
Source281:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.jar#/artifact-0181-commons-lang3-3.18.0.jar
#!RemoteAsset:  sha256:aa254b373b6f6d46bc9dca86331b072a8ab86eb25ea9921fd439618392e98a16
Source282:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.pom#/artifact-0182-commons-lang3-3.18.0.pom
#!RemoteAsset:  sha256:32733ab4bc90b45b63eb72677d886961003fd4ed113e07b1028f9877cb2ac735
Source283:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.19.0/commons-lang3-3.19.0.jar#/artifact-0183-commons-lang3-3.19.0.jar
#!RemoteAsset:  sha256:d7463906ab3081ff42cf3531eb793b240fb0ca3f1c26fd58fc84fb23032a72b7
Source284:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.19.0/commons-lang3-3.19.0.pom#/artifact-0184-commons-lang3-3.19.0.pom
#!RemoteAsset:  sha256:69e5c9fa35da7a51a5fd2099dfe56a2d8d32cf233e2f6d770e796146440263f4
Source285:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar#/artifact-0185-commons-lang3-3.20.0.jar
#!RemoteAsset:  sha256:7ca83b2709c1e7a9e03b576cd41422190379489a80866e542f8c8b955411a2aa
Source286:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.pom#/artifact-0186-commons-lang3-3.20.0.pom
#!RemoteAsset:  sha256:24f2e52bde65e2dc9cfcebb2fc22d8de0edb3726925ccf80b13db4eeb515a302
Source287:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/14/commons-parent-14.pom#/artifact-0187-commons-parent-14.pom
#!RemoteAsset:  sha256:fb8c5e55e30a7addb4ff210858a0e8d2494ed6757bbe19012da99d51586c3cbb
Source288:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/22/commons-parent-22.pom#/artifact-0188-commons-parent-22.pom
#!RemoteAsset:  sha256:3a2e69d06d641d1f3b293126dc9e2e4ea6563bf8c36c87e0ab6fa4292d04b79c
Source289:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/34/commons-parent-34.pom#/artifact-0189-commons-parent-34.pom
#!RemoteAsset:  sha256:87cd27e1a02a5c3eb6d85059ce98696bb1b44c2b8b650f0567c86df60fa61da7
Source290:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/39/commons-parent-39.pom#/artifact-0190-commons-parent-39.pom
#!RemoteAsset:  sha256:cd313494c670b483ec256972af1698b330e598f807002354eb765479f604b09c
Source291:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom#/artifact-0191-commons-parent-42.pom
#!RemoteAsset:  sha256:9c88623ecfa91f012c673ee4622c0eeb4367e5e0d222d960f76cd208b1a4fda6
Source292:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/45/commons-parent-45.pom#/artifact-0192-commons-parent-45.pom
#!RemoteAsset:  sha256:8a8ecb570553bf9f1ffae211a8d4ca9ee630c17afe59293368fba7bd9b42fcb7
Source293:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/47/commons-parent-47.pom#/artifact-0193-commons-parent-47.pom
#!RemoteAsset:  sha256:1e1f7de9370a7b7901f128f1dacd1422be74e3f47f9558b0f79e04c0637ca0b4
Source294:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/48/commons-parent-48.pom#/artifact-0194-commons-parent-48.pom
#!RemoteAsset:  sha256:8bd632c00bdf80a7de36c22b60f12452c147d8eca2f00d79d66699ebe7daa02a
Source295:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/5/commons-parent-5.pom#/artifact-0195-commons-parent-5.pom
#!RemoteAsset:  sha256:7b7a2db3f747074b5867f553d5efc8072be26ede32879d052c347e7c81117f06
Source296:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/50/commons-parent-50.pom#/artifact-0196-commons-parent-50.pom
#!RemoteAsset:  sha256:9b779d18b22d8de559605558e7bb0a0a31b3f00c2abb9c878117c398aacabeca
Source297:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/51/commons-parent-51.pom#/artifact-0197-commons-parent-51.pom
#!RemoteAsset:  sha256:75dbe8f34e98e4c3ff42daae4a2f9eb4cbcd3b5f1047d54460ace906dbb4502e
Source298:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/52/commons-parent-52.pom#/artifact-0198-commons-parent-52.pom
#!RemoteAsset:  sha256:6f19638994e8357b4ed734696f992057efaafa1235673998133299798e2ccddb
Source299:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/64/commons-parent-64.pom#/artifact-0199-commons-parent-64.pom
#!RemoteAsset:  sha256:6cf3495fc2e6ac913a2b7f2e03fb5908fb3f229fb06d3358dc45678d5af3e36e
Source300:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/65/commons-parent-65.pom#/artifact-0200-commons-parent-65.pom
#!RemoteAsset:  sha256:48fd6dc846e56b1f408660d163e75300f9e384bb63be482a8082a21d72a8db9c
Source301:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/66/commons-parent-66.pom#/artifact-0201-commons-parent-66.pom
#!RemoteAsset:  sha256:d50da9c39bdca823d618d1b4a03b73f196497fcb8616fd0da727c8623592a9bb
Source302:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/69/commons-parent-69.pom#/artifact-0202-commons-parent-69.pom
#!RemoteAsset:  sha256:4ed44560b07f8448479dfd1e83a422ba4e83e60b36e51b2871ac502a6d5c1bea
Source303:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/73/commons-parent-73.pom#/artifact-0203-commons-parent-73.pom
#!RemoteAsset:  sha256:80eb61b0c87fdd826a069313b28b672da3f1885832da447b51e6e8a6197e7ecb
Source304:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/74/commons-parent-74.pom#/artifact-0204-commons-parent-74.pom
#!RemoteAsset:  sha256:348d4e7c131be6114c854a719ce7a44307a7c39bd366084977b24fd29ad0edb4
Source305:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/81/commons-parent-81.pom#/artifact-0205-commons-parent-81.pom
#!RemoteAsset:  sha256:d189ff2c0027e96bb65d31e6f227ed2af966169b36af1e973dd5ba08926dc7b5
Source306:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/85/commons-parent-85.pom#/artifact-0206-commons-parent-85.pom
#!RemoteAsset:  sha256:8bf726150d1d6a43ba0aa92060e552933caf2873aa193952d9d496470fa9fbd8
Source307:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/88/commons-parent-88.pom#/artifact-0207-commons-parent-88.pom
#!RemoteAsset:  sha256:5331b7d3e0aed59728c80f1118e4dbf78565d4109e81d16602c9cadbdb23a128
Source308:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/9/commons-parent-9.pom#/artifact-0208-commons-parent-9.pom
#!RemoteAsset:  sha256:d2f8b6fd4800b6aaf120f5a38226d5f9d5fc6db837af99e2f9b33067868b9872
Source309:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/91/commons-parent-91.pom#/artifact-0209-commons-parent-91.pom
#!RemoteAsset:  sha256:94f6c027b15f6402995dd1b2c7ea35bfe1ebc88b6832b3134368b41998721953
Source310:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/92/commons-parent-92.pom#/artifact-0210-commons-parent-92.pom
#!RemoteAsset:  sha256:2cd3289b44efa53052d9cdaf3f05544833a520a682f9c7ffd403a00bbb157f9a
Source311:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/96/commons-parent-96.pom#/artifact-0211-commons-parent-96.pom
#!RemoteAsset:  sha256:d40318527f56033e0ff0789971cc38c856aa99a685eea11270814e7f1eda9fba
Source312:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/98/commons-parent-98.pom#/artifact-0212-commons-parent-98.pom
#!RemoteAsset:  sha256:de023257ff166044a56bd1aa9124e843cd05dac5806cc705a9311f3556d5a15f
Source313:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.jar#/artifact-0213-commons-text-1.12.0.jar
#!RemoteAsset:  sha256:b2d4341c921981cb35d5570f4fc9732a08a34b1528dee84c0507c7f2719a334f
Source314:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom#/artifact-0214-commons-text-1.12.0.pom
#!RemoteAsset:  sha256:8185b3a5311092d83ed1f184c2d093b3105d726bbd76867c32b3511542bb99a8
Source315:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.3/commons-text-1.3.jar#/artifact-0215-commons-text-1.3.jar
#!RemoteAsset:  sha256:deeb2ba9701e495dc31d32633eb86b94b24b0a96e0dc67fb87e7062f153027aa
Source316:      https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.3/commons-text-1.3.pom#/artifact-0216-commons-text-1.3.pom
#!RemoteAsset:  sha256:b9ed2f9dd434631158d77308ee5648622c229ccece1722c5e377a4296923dae6
Source317:      https://repo.maven.apache.org/maven2/org/apache/geronimo/genesis/genesis/2.0/genesis-2.0.pom#/artifact-0217-genesis-2.0.pom
#!RemoteAsset:  sha256:08e6e146f4e245266dff9dd800b12875dd2367d3f67a34ab660a126c811215f8
Source318:      https://repo.maven.apache.org/maven2/org/apache/geronimo/genesis/genesis-default-flava/2.0/genesis-default-flava-2.0.pom#/artifact-0218-genesis-default-flava-2.0.pom
#!RemoteAsset:  sha256:e7c5358bbbbc27daa5b327f63bc12650a75ddc9f9ac6d4bfa12789be1f2c29db
Source319:      https://repo.maven.apache.org/maven2/org/apache/geronimo/genesis/genesis-java5-flava/2.0/genesis-java5-flava-2.0.pom#/artifact-0219-genesis-java5-flava-2.0.pom
#!RemoteAsset:  sha256:6fe9026a566c6a5001608cf3fc32196641f6c1e5e1986d1037ccdbd5f31ef743
Source320:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar#/artifact-0220-httpclient-4.5.13.jar
#!RemoteAsset:  sha256:78eb9ada74929fcd63d07adc4f49236841a45cc29d5f817bf45801f513fd7e6c
Source321:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.pom#/artifact-0221-httpclient-4.5.13.pom
#!RemoteAsset:  sha256:c8bc7e1c51a6d4ce72f40d2ebbabf1c4b68bfe76e732104b04381b493478e9d6
Source322:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.jar#/artifact-0222-httpclient-4.5.14.jar
#!RemoteAsset:  sha256:f18355af4cf80a8a4ef04ebd742a47e90a7eaf080c725b2095dbc4fc5dbdefb7
Source323:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.pom#/artifact-0223-httpclient-4.5.14.pom
#!RemoteAsset:  sha256:9cba594c08db7271d0c20e9845d622bb39e69583910b45e7d5df82f6058d4dd9
Source324:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.5.13/httpcomponents-client-4.5.13.pom#/artifact-0224-httpcomponents-client-4.5.13.pom
#!RemoteAsset:  sha256:5bad1de4f101447659f89d089868ccbad64a68cc503d2d65410b51f6904aa061
Source325:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.5.14/httpcomponents-client-4.5.14.pom#/artifact-0225-httpcomponents-client-4.5.14.pom
#!RemoteAsset:  sha256:c554e7008e4517c7ef54e005cc8b74f4c87a54a0ea2c6f57be5d0569df51936b
Source326:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.4.13/httpcomponents-core-4.4.13.pom#/artifact-0226-httpcomponents-core-4.4.13.pom
#!RemoteAsset:  sha256:209ed931cb57998252dfe027caa9c03ada620613642329679131165f8b1cbad1
Source327:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.4.14/httpcomponents-core-4.4.14.pom#/artifact-0227-httpcomponents-core-4.4.14.pom
#!RemoteAsset:  sha256:f2d75a2c2d423ad18539bf21656d56f88a4091944a662fcaf159d5ae283db7f7
Source328:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.4.16/httpcomponents-core-4.4.16.pom#/artifact-0228-httpcomponents-core-4.4.16.pom
#!RemoteAsset:  sha256:a901f87b115c55070c7ee43efff63e20e7b02d30af2443ae292bf1f4e532d3aa
Source329:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcomponents-parent/11/httpcomponents-parent-11.pom#/artifact-0229-httpcomponents-parent-11.pom
#!RemoteAsset:  sha256:8f812d9fa7b72a3d4aa7f825278932a5df344b42a6d8398905879431a1bf9a97
Source330:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcore/4.4.13/httpcore-4.4.13.pom#/artifact-0230-httpcore-4.4.13.pom
#!RemoteAsset:  sha256:f956209e450cb1d0c51776dfbd23e53e9dd8db9a1298ed62b70bf0944ba63b28
Source331:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcore/4.4.14/httpcore-4.4.14.jar#/artifact-0231-httpcore-4.4.14.jar
#!RemoteAsset:  sha256:55716398a978f10203f9e25c8aefc0580daf7f0907c6ed0aead81ec5fb6b7fd8
Source332:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcore/4.4.14/httpcore-4.4.14.pom#/artifact-0232-httpcore-4.4.14.pom
#!RemoteAsset:  sha256:6c9b3dd142a09dc468e23ad39aad6f75a0f2b85125104469f026e52a474e464f
Source333:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.jar#/artifact-0233-httpcore-4.4.16.jar
#!RemoteAsset:  sha256:3cbad849b35dacfe6cec31adada2c623c026c3261141b0d26eec7e399c6cd7fa
Source334:      https://repo.maven.apache.org/maven2/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.pom#/artifact-0234-httpcore-4.4.16.pom
#!RemoteAsset:  sha256:38246291439393fd08f54c6d7fedde2db0fd5c94d0910f17b99e8d59a2858e98
Source335:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/1.0/doxia-1.0.pom#/artifact-0235-doxia-1.0.pom
#!RemoteAsset:  sha256:784c41e3398c840f01d755a8abb1049c708caff55820ef68eb65719be8feabba
Source336:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/1.11.1/doxia-1.11.1.pom#/artifact-0236-doxia-1.11.1.pom
#!RemoteAsset:  sha256:2d02a0bd64f331b767cee7455b3193c6fb82110143a119858abc968798a5fc29
Source337:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/1.12.0/doxia-1.12.0.pom#/artifact-0237-doxia-1.12.0.pom
#!RemoteAsset:  sha256:59f40c92b9f525bb6ca6f8845ec63b13dab18c3c1da93d17620cb8d2ea4c61b8
Source338:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia/2.0.0/doxia-2.0.0.pom#/artifact-0238-doxia-2.0.0.pom
#!RemoteAsset:  sha256:d22567378e3481adfa8d06ee2a6e882533c2c270c5b8653f1c159fd2de05b168
Source339:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.11.1/doxia-core-1.11.1.pom#/artifact-0239-doxia-core-1.11.1.pom
#!RemoteAsset:  sha256:5e49cd827bebbcea5829d3b3883d17ad1ce15ebd6394aeb50ad50d7dfd939fcd
Source340:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.12.0/doxia-core-1.12.0.jar#/artifact-0240-doxia-core-1.12.0.jar
#!RemoteAsset:  sha256:b0388f748a0885e13e7c2c453921f8bb9dd4fb5b1905be745685476cf3456ea3
Source341:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/1.12.0/doxia-core-1.12.0.pom#/artifact-0241-doxia-core-1.12.0.pom
#!RemoteAsset:  sha256:939183cf5ced6741745b2475a4adf78ca85885ee0dad6dae28dd3f25bd447ff3
Source342:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.jar#/artifact-0242-doxia-core-2.0.0.jar
#!RemoteAsset:  sha256:f3e804d91571075e6367cff9020641d79d66bc46a6c13a62fcba1d369cd8936d
Source343:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.pom#/artifact-0243-doxia-core-2.0.0.pom
#!RemoteAsset:  sha256:411fc167774f2e3573f280c57a278fbe7bae677ee596a8ad24bd6c6bb2c5bbce
Source344:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-decoration-model/1.11.1/doxia-decoration-model-1.11.1.jar#/artifact-0244-doxia-decoration-model-1.11.1.jar
#!RemoteAsset:  sha256:fd2040e074d6b00c595562c7fc8117f4d378038aa0c5c2bc8fb84c2b8e6246fb
Source345:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-decoration-model/1.11.1/doxia-decoration-model-1.11.1.pom#/artifact-0245-doxia-decoration-model-1.11.1.pom
#!RemoteAsset:  sha256:eee789dcb86f37f290c6c22198ea56bf529edf21590294e549a77a490ed21dbe
Source346:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-integration-tools/1.11.1/doxia-integration-tools-1.11.1.jar#/artifact-0246-doxia-integration-tools-1.11.1.jar
#!RemoteAsset:  sha256:1ad03814f59e835fbe6ba81d214b7f27cc6a8a688ac80791c2baa036ca53ec12
Source347:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-integration-tools/1.11.1/doxia-integration-tools-1.11.1.pom#/artifact-0247-doxia-integration-tools-1.11.1.pom
#!RemoteAsset:  sha256:4aee72f9b30b507964c2f52b63f70e7b41fb9d957359cb5dc13c428abb4b6189
Source348:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.jar#/artifact-0248-doxia-integration-tools-2.0.0.jar
#!RemoteAsset:  sha256:b3707bdb06778745b0304985c340a9847eeda20f4ca7f2902faf6c266cc29653
Source349:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.pom#/artifact-0249-doxia-integration-tools-2.0.0.pom
#!RemoteAsset:  sha256:89001fcd98d29ab1c3102b14e7ddf5a3eb8cc3fce38558b485772bfc694c8600
Source350:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-logging-api/1.11.1/doxia-logging-api-1.11.1.pom#/artifact-0250-doxia-logging-api-1.11.1.pom
#!RemoteAsset:  sha256:985306162c0a9f4c309d46109447f30f02bf6fc9bc16a3e039d59e1dabd0192f
Source351:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-logging-api/1.12.0/doxia-logging-api-1.12.0.jar#/artifact-0251-doxia-logging-api-1.12.0.jar
#!RemoteAsset:  sha256:9dd99b4350223846585310694c446318b1692ba746ed717376d59619a27123b4
Source352:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-logging-api/1.12.0/doxia-logging-api-1.12.0.pom#/artifact-0252-doxia-logging-api-1.12.0.pom
#!RemoteAsset:  sha256:f4a846c448ca85358279184a310f6ee3f46fa39688f74a72961c1bfe222f28a6
Source353:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.jar#/artifact-0253-doxia-module-apt-2.0.0.jar
#!RemoteAsset:  sha256:15d5d2bcd6fe003c4d181f1b9e88b3e09611e85385246105fc5977301f2c7e96
Source354:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.pom#/artifact-0254-doxia-module-apt-2.0.0.pom
#!RemoteAsset:  sha256:7956aca14f8adbc48bac86b218701dd44cc990063a69edbfca363b105994a474
Source355:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.jar#/artifact-0255-doxia-module-xdoc-2.0.0.jar
#!RemoteAsset:  sha256:c2e591fac5e62327c13a267c41ec21d1330e5fcbb943c56fbd6803132e7b1115
Source356:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.pom#/artifact-0256-doxia-module-xdoc-2.0.0.pom
#!RemoteAsset:  sha256:9613c4b89005fa005c0f57e37a5b4129a345f55250ef951cdca1b4deb3d9336b
Source357:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.11.1/doxia-module-xhtml-1.11.1.pom#/artifact-0257-doxia-module-xhtml-1.11.1.pom
#!RemoteAsset:  sha256:49448d279a05b3c5d14a06c6cfd073b2ad03479ee3fa41a9e9600f1662d0e9f7
Source358:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.12.0/doxia-module-xhtml-1.12.0.jar#/artifact-0258-doxia-module-xhtml-1.12.0.jar
#!RemoteAsset:  sha256:08c8b1053a50567941bf7ec9dfbd8faa7d02c1a07a8f67aeb94858e03d6c216f
Source359:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml/1.12.0/doxia-module-xhtml-1.12.0.pom#/artifact-0259-doxia-module-xhtml-1.12.0.pom
#!RemoteAsset:  sha256:3583ae17f9ae97db41da038dc67552a386e7a9f850f45fa6fdb0d2b9ef36a31c
Source360:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml5/1.11.1/doxia-module-xhtml5-1.11.1.jar#/artifact-0260-doxia-module-xhtml5-1.11.1.jar
#!RemoteAsset:  sha256:a322ee9d8b5b300f337994c710be006dd8b05f2d83e07a9bef64c2530ac9282b
Source361:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml5/1.11.1/doxia-module-xhtml5-1.11.1.pom#/artifact-0261-doxia-module-xhtml5-1.11.1.pom
#!RemoteAsset:  sha256:c91557679a0eb9fde3175055628ceb7b8fd5ab6d308340770d236fb06265dc26
Source362:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.jar#/artifact-0262-doxia-module-xhtml5-2.0.0.jar
#!RemoteAsset:  sha256:3c6bff4151d35b94c3afb4a0c9377c262ced4eb2dd1009970396d4c79eb73e6e
Source363:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.pom#/artifact-0263-doxia-module-xhtml5-2.0.0.pom
#!RemoteAsset:  sha256:d6c12f3529a45ec1a757455267d3ec450af1a7e72b53ccc19e1452611b806866
Source364:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-modules/1.11.1/doxia-modules-1.11.1.pom#/artifact-0264-doxia-modules-1.11.1.pom
#!RemoteAsset:  sha256:ab8ff6bb4793cfba59b14fb383ff351a349b1091d071c66b1fcbca728d505bdc
Source365:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-modules/1.12.0/doxia-modules-1.12.0.pom#/artifact-0265-doxia-modules-1.12.0.pom
#!RemoteAsset:  sha256:9c56654ceff62d08b19b802d7d4d77dca54b17548b9802a0ba493f72f2adaf34
Source366:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-modules/2.0.0/doxia-modules-2.0.0.pom#/artifact-0266-doxia-modules-2.0.0.pom
#!RemoteAsset:  sha256:50d699f86369802baf2cd16c31d936ad8f0c1a8976120cd1dc3dc70c8abed99a
Source367:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.pom#/artifact-0267-doxia-sink-api-1.0.pom
#!RemoteAsset:  sha256:780f9b25ba1a38ef6494f32236a59f1ba5b5298724ab4ff3419e9aa3195b9858
Source368:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.11.1/doxia-sink-api-1.11.1.pom#/artifact-0268-doxia-sink-api-1.11.1.pom
#!RemoteAsset:  sha256:5dca6aaaa9e70d8a0766e143ddcf9db09de5fde0fbcc78cb635d74e764dfcca5
Source369:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.12.0/doxia-sink-api-1.12.0.jar#/artifact-0269-doxia-sink-api-1.12.0.jar
#!RemoteAsset:  sha256:26b51fddb69b5ca6e044cda28b8d1c1a37b6fafd0cfb9bfb15a919de57c671d5
Source370:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/1.12.0/doxia-sink-api-1.12.0.pom#/artifact-0270-doxia-sink-api-1.12.0.pom
#!RemoteAsset:  sha256:fba33eaee3b01547bcd14b05ebc37f7dacef1819ad9ee7a5b27899afd3472cf4
Source371:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.jar#/artifact-0271-doxia-sink-api-2.0.0.jar
#!RemoteAsset:  sha256:4b05895d1cd65013d4b8e7eeb09cde6b567b4c31729fe5c77c0f0898b5e04b88
Source372:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.pom#/artifact-0272-doxia-sink-api-2.0.0.pom
#!RemoteAsset:  sha256:f6ec9ef75a41d1b826e5ecf02d92c5de90a6bc70ea93d5340988703223bf2205
Source373:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.jar#/artifact-0273-doxia-site-model-2.0.0.jar
#!RemoteAsset:  sha256:25a17abcbd162cf65dfae5bd7400611d19e424d679e132e9a9228346c6d78d42
Source374:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.pom#/artifact-0274-doxia-site-model-2.0.0.pom
#!RemoteAsset:  sha256:f279a087910d3e0728daad9114da8f3211cfb49b5e8457d05ee9ee5f04284527
Source375:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/1.11.1/doxia-site-renderer-1.11.1.jar#/artifact-0275-doxia-site-renderer-1.11.1.jar
#!RemoteAsset:  sha256:bd9ac2f023c8fbf7fc2ab00cee25dffbc18249870ce0da2ec46ba6689066184f
Source376:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/1.11.1/doxia-site-renderer-1.11.1.pom#/artifact-0276-doxia-site-renderer-1.11.1.pom
#!RemoteAsset:  sha256:6cdee370194f4b9f742d12ef46528042f480d9bdf3de832de2792e1ae9ffc68d
Source377:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.jar#/artifact-0277-doxia-site-renderer-2.0.0.jar
#!RemoteAsset:  sha256:3add9e92edb232902aaf8f663b48d9f8dbec1792436f4f9c36f3665b86266d8d
Source378:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.pom#/artifact-0278-doxia-site-renderer-2.0.0.pom
#!RemoteAsset:  sha256:1ee7c5b411e6c91b70a19683ef96ac6fd273f9323d3f4a396e201949f48aa748
Source379:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sitetools/1.11.1/doxia-sitetools-1.11.1.pom#/artifact-0279-doxia-sitetools-1.11.1.pom
#!RemoteAsset:  sha256:ad3dcd30a40d45148350f066f2312ed9f946b7fd94f9c197ede0f3b9558b80a3
Source380:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-sitetools/2.0.0/doxia-sitetools-2.0.0.pom#/artifact-0280-doxia-sitetools-2.0.0.pom
#!RemoteAsset:  sha256:5337efbe45413d24b71422d145062f84bde96271dab9f3a5caa3fab461974bf4
Source381:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-skin-model/1.11.1/doxia-skin-model-1.11.1.jar#/artifact-0281-doxia-skin-model-1.11.1.jar
#!RemoteAsset:  sha256:358009924c031e858910e19dcfee1eddb9c352add9e3172e09a06f2afdcbf201
Source382:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-skin-model/1.11.1/doxia-skin-model-1.11.1.pom#/artifact-0282-doxia-skin-model-1.11.1.pom
#!RemoteAsset:  sha256:3ced0d90353f49e8eb1458f54664b93ec117d79b9789a576da41e2f6f99723e0
Source383:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.jar#/artifact-0283-doxia-skin-model-2.0.0.jar
#!RemoteAsset:  sha256:10bbc5674fab0fa2bbcf8f7696796d3e1b92ab31525330921fbdb8da74fe1472
Source384:      https://repo.maven.apache.org/maven2/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.pom#/artifact-0284-doxia-skin-model-2.0.0.pom
#!RemoteAsset:  sha256:9c99512c5ebd887a256ea6457dadce455eee27cb6544176c830bc5ad8540035c
Source385:      https://repo.maven.apache.org/maven2/org/apache/maven/enforcer/enforcer/3.6.2/enforcer-3.6.2.pom#/artifact-0285-enforcer-3.6.2.pom
#!RemoteAsset:  sha256:96205145b1eb4957903590ddd0d87f084ec95c1a56a5326cb7c6dec4678ea27a
Source386:      https://repo.maven.apache.org/maven2/org/apache/maven/enforcer/enforcer-api/3.6.2/enforcer-api-3.6.2.jar#/artifact-0286-enforcer-api-3.6.2.jar
#!RemoteAsset:  sha256:7dfe2d5575f8934776ed08c32c2d750e41ecb49f36d81dc8934005c26de146c8
Source387:      https://repo.maven.apache.org/maven2/org/apache/maven/enforcer/enforcer-api/3.6.2/enforcer-api-3.6.2.pom#/artifact-0287-enforcer-api-3.6.2.pom
#!RemoteAsset:  sha256:32df6061b38212d347d1306fa254f0bd216025259763dd4affb22965521bc750
Source388:      https://repo.maven.apache.org/maven2/org/apache/maven/enforcer/enforcer-rules/3.6.2/enforcer-rules-3.6.2.jar#/artifact-0288-enforcer-rules-3.6.2.jar
#!RemoteAsset:  sha256:dc8b3b277701081e8e025aa1539e29863c9e85f2e5630ea01784b35ed5639527
Source389:      https://repo.maven.apache.org/maven2/org/apache/maven/enforcer/enforcer-rules/3.6.2/enforcer-rules-3.6.2.pom#/artifact-0289-enforcer-rules-3.6.2.pom
#!RemoteAsset:  sha256:d135cff96dcbbc8a5fab30180e557cae620373cf26941d4c738a88896a2d98ed
Source390:      https://repo.maven.apache.org/maven2/org/apache/maven/maven/2.2.1/maven-2.2.1.pom#/artifact-0290-maven-2.2.1.pom
#!RemoteAsset:  sha256:28fc63720c4a5ff92bf0e358ed55a6f24626f35bccc13cc3e194231e158848f6
Source391:      https://repo.maven.apache.org/maven2/org/apache/maven/maven/3.0/maven-3.0.pom#/artifact-0291-maven-3.0.pom
#!RemoteAsset:  sha256:1f895a587df4844d9b7565e8e9a6352afe1d55532458a0dbeb746bc1d02e9216
Source392:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.jar#/artifact-0292-maven-archiver-3.6.2.jar
#!RemoteAsset:  sha256:8b117b0dc205a71abda33463f8c7ff891513cfb92241d8a011f9e8ac5ea21e77
Source393:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.pom#/artifact-0293-maven-archiver-3.6.2.pom
#!RemoteAsset:  sha256:83566129898c7a384bffaa118a76a40667d546948460b43eeb8563fa17635848
Source394:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.jar#/artifact-0294-maven-archiver-3.6.3.jar
#!RemoteAsset:  sha256:bc130259c5e1087a270ea8cf3f8182fecc90bf93113a2074d640a1a67f102ec4
Source395:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.pom#/artifact-0295-maven-archiver-3.6.3.pom
#!RemoteAsset:  sha256:cea5dd2b7c6be818fa8d6b73cff4edacaecefec5842d361a791b7f47974fe156
Source396:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.jar#/artifact-0296-maven-archiver-3.6.5.jar
#!RemoteAsset:  sha256:87b2c403256b17c3903a3ba35320ac32a79b3838b62ab9eda010a0976ca49ba3
Source397:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.pom#/artifact-0297-maven-archiver-3.6.5.pom
#!RemoteAsset:  sha256:d53062ffe8677a4f5e1ad3a1d1fa37ed600fab39166d39be7ed204635c5f839b
Source398:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar#/artifact-0298-maven-artifact-2.2.1.jar
#!RemoteAsset:  sha256:f658a628efd6e0efe416b977638ba144af660fe6413f3637a4d03feb6a1ce806
Source399:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.pom#/artifact-0299-maven-artifact-2.2.1.pom
#!RemoteAsset:  sha256:c56a0dbd90cea691f83e58fa9a6388fb3ac6bc3c14b8c04d2e112544651fa528
Source400:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.pom#/artifact-0300-maven-artifact-3.0.pom
#!RemoteAsset:  sha256:153b32f474fd676ec36ad807c508885005139140fc92168bb76bf6be31f8efb8
Source401:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.jar#/artifact-0301-maven-model-2.2.1.jar
#!RemoteAsset:  sha256:62dd8e35a2c4432bb22f8250bbfe08639635599b4064d5d747bd24cf3c02fac5
Source402:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.pom#/artifact-0302-maven-model-2.2.1.pom
#!RemoteAsset:  sha256:3d6fdeb72b2967f1fa2784134fb832d08d8d6e879b7ace7712f2c7281994fc1e
Source403:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-model/3.0/maven-model-3.0.pom#/artifact-0303-maven-model-3.0.pom
#!RemoteAsset:  sha256:81fe14cb9779d36e0c610e1049e5b32a6b9974957f257921acf628b31c5486c8
Source404:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/10/maven-parent-10.pom#/artifact-0304-maven-parent-10.pom
#!RemoteAsset:  sha256:7450c3330cf06c254db9f0dc5ef49eac15502311cf19e0208ba473076ee043d6
Source405:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/11/maven-parent-11.pom#/artifact-0305-maven-parent-11.pom
#!RemoteAsset:  sha256:e25770d5d46dcdfdbb9e38ca04f272c5bdf476d88392ab4044ba90678e616d54
Source406:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/15/maven-parent-15.pom#/artifact-0306-maven-parent-15.pom
#!RemoteAsset:  sha256:70cef83d246309a2aa355c38f2004edda3621ae0bc5c55a7a139eaeef4d1231a
Source407:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/16/maven-parent-16.pom#/artifact-0307-maven-parent-16.pom
#!RemoteAsset:  sha256:5425501edd9e0bd7b01eca53cc92e06836d24851151304f9c6759e1713541685
Source408:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/23/maven-parent-23.pom#/artifact-0308-maven-parent-23.pom
#!RemoteAsset:  sha256:70709ad646f5aa57bb44e2a8b4f3de4993b108202ba095bd164e41cdc3181e70
Source409:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/30/maven-parent-30.pom#/artifact-0309-maven-parent-30.pom
#!RemoteAsset:  sha256:3856e3fcd169502d5f12fe2452604ebf6c7c025f15656bfa558ea99ed29d73ea
Source410:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/33/maven-parent-33.pom#/artifact-0310-maven-parent-33.pom
#!RemoteAsset:  sha256:1a8faf7a6a2b848acb26a959954ee115c0d79dbe75a6206fb3b8c7c2f45a237f
Source411:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/34/maven-parent-34.pom#/artifact-0311-maven-parent-34.pom
#!RemoteAsset:  sha256:cfe4820aa1d96ae51d1dc5b0e2a9dc582c42478c24c95ca8238f547e60bef721
Source412:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/39/maven-parent-39.pom#/artifact-0312-maven-parent-39.pom
#!RemoteAsset:  sha256:762fcdd4ce8621c5fa0a2cf6495ad26972a8093eb432aa3e402bc2d4e2500c53
Source413:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/41/maven-parent-41.pom#/artifact-0313-maven-parent-41.pom
#!RemoteAsset:  sha256:04534dea350a2187970a5b74444338bcf78ba8e537d44f262acfba16ebb33056
Source414:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/42/maven-parent-42.pom#/artifact-0314-maven-parent-42.pom
#!RemoteAsset:  sha256:468a1262e9aaa5febf9d604e2836267f815351f2b4520f28fb17f53c71e33554
Source415:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/43/maven-parent-43.pom#/artifact-0315-maven-parent-43.pom
#!RemoteAsset:  sha256:1c0a088d7352d52ea8f3581d05778c0c4a679613fff2c58737fba55f1007fe24
Source416:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/44/maven-parent-44.pom#/artifact-0316-maven-parent-44.pom
#!RemoteAsset:  sha256:94fe869eb9b4ce9fce3995d05ea86b168c85d927f9d17beb814a1960c76d7e6f
Source417:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/45/maven-parent-45.pom#/artifact-0317-maven-parent-45.pom
#!RemoteAsset:  sha256:82d0112ba1907ff5fd13a2485829c97df66c6a81e075359a561a422f7d1582d3
Source418:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/47/maven-parent-47.pom#/artifact-0318-maven-parent-47.pom
#!RemoteAsset:  sha256:cc9eed84b90a96cbc33aefecc93facb9a49f960ad678909162c579356cfe12c9
Source419:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/48/maven-parent-48.pom#/artifact-0319-maven-parent-48.pom
#!RemoteAsset:  sha256:72a47a963563009c5e8b851491ced3f63e2d276b862bde1f9d10d53abac5b22f
Source420:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/2.2.1/maven-plugin-api-2.2.1.jar#/artifact-0320-maven-plugin-api-2.2.1.jar
#!RemoteAsset:  sha256:c10d0460c2d5c5076304598965991d6257d1bf31bdef921a17ce3d059bce654e
Source421:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/2.2.1/maven-plugin-api-2.2.1.pom#/artifact-0321-maven-plugin-api-2.2.1.pom
#!RemoteAsset:  sha256:8a722af2564205ae996f9035cc04670d3e9e4ae592f5a643c58fb7b0f43e1501
Source422:      https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/3.0/maven-plugin-api-3.0.pom#/artifact-0322-maven-plugin-api-3.0.pom
#!RemoteAsset:  sha256:b7c76ae8bd983b8be40cc7912538c1ac8af075d47c6bfb6d18dc513bdd37359a
Source423:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.jar#/artifact-0323-maven-assembly-plugin-3.8.0.jar
#!RemoteAsset:  sha256:02b4ab89683aa46a7df3df762eeb47fc5dfe8c5e163fade3033e20add9343bfb
Source424:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.pom#/artifact-0324-maven-assembly-plugin-3.8.0.pom
#!RemoteAsset:  sha256:6ea0ca0558ccf248c514aa94908d1f895a92e9b4e4604c1bb29f7a4ab1b833f0
Source425:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.15.0/maven-compiler-plugin-3.15.0.jar#/artifact-0325-maven-compiler-plugin-3.15.0.jar
#!RemoteAsset:  sha256:2d2f7a7073c1def3b1473fbedad7dbfc559ed6fb0dc5a94edc347fd4905e7651
Source426:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.15.0/maven-compiler-plugin-3.15.0.pom#/artifact-0326-maven-compiler-plugin-3.15.0.pom
#!RemoteAsset:  sha256:f5c804d7cdecb3591e04e1dd423600c2f0d13605ee6d4a5d1393a5bc5a3b9070
Source427:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-dependency-plugin/3.10.0/maven-dependency-plugin-3.10.0.jar#/artifact-0327-maven-dependency-plugin-3.10.0.jar
#!RemoteAsset:  sha256:d53783d7849e34bd389ec69763200be42c5c7e0ad25ed108e744c34e9d3e60cc
Source428:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-dependency-plugin/3.10.0/maven-dependency-plugin-3.10.0.pom#/artifact-0328-maven-dependency-plugin-3.10.0.pom
#!RemoteAsset:  sha256:88189ac3d0d2049ce9efabaf9895aee074f4eddb0f224defeb48c34ffe9d6fd8
Source429:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/3.6.2/maven-enforcer-plugin-3.6.2.jar#/artifact-0329-maven-enforcer-plugin-3.6.2.jar
#!RemoteAsset:  sha256:d8fd2a11c0339478e164a3036abba40a2ce5bf35f198f0e26041441398e1a7fe
Source430:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-enforcer-plugin/3.6.2/maven-enforcer-plugin-3.6.2.pom#/artifact-0330-maven-enforcer-plugin-3.6.2.pom
#!RemoteAsset:  sha256:1ca520d5450077453a530bd976c61e9c65aafa70b88e29ac15e5435b4c9e6fb1
Source431:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-failsafe-plugin/3.5.5/maven-failsafe-plugin-3.5.5.jar#/artifact-0331-maven-failsafe-plugin-3.5.5.jar
#!RemoteAsset:  sha256:2446624171b30d083ae7a2853f23e27cbb938f40f209bf321ab5bb4c7cc4b55d
Source432:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-failsafe-plugin/3.5.5/maven-failsafe-plugin-3.5.5.pom#/artifact-0332-maven-failsafe-plugin-3.5.5.pom
#!RemoteAsset:  sha256:7562657fc3492649dee836ffdda07990aaf46f4133cad048c4dcd7330bfd3917
Source433:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.5.0/maven-jar-plugin-3.5.0.jar#/artifact-0333-maven-jar-plugin-3.5.0.jar
#!RemoteAsset:  sha256:571d9446537993c3a7226cecb3169ee3df75710bcae8daeefb0d80768ec35917
Source434:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-jar-plugin/3.5.0/maven-jar-plugin-3.5.0.pom#/artifact-0334-maven-jar-plugin-3.5.0.pom
#!RemoteAsset:  sha256:a177f84e01c3829a357b8f135686ae7dd8c35d1c2089a390ef089340aa47cd21
Source435:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/43/maven-plugins-43.pom#/artifact-0335-maven-plugins-43.pom
#!RemoteAsset:  sha256:c0f58b12039f152641e3e53a07acc12887012ef149fac83065a9785aac51de0e
Source436:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/45/maven-plugins-45.pom#/artifact-0336-maven-plugins-45.pom
#!RemoteAsset:  sha256:58ddbb8e429cb5e9054c2f5f7b7cdfeb7adbcdfda21d92b67f67fa2b94edf982
Source437:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/47/maven-plugins-47.pom#/artifact-0337-maven-plugins-47.pom
#!RemoteAsset:  sha256:16fd64538837bbe6c6823008fc6153cf16ba833afb1e90a95b7cf1992b434b34
Source438:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.jar#/artifact-0338-maven-remote-resources-plugin-3.3.0.jar
#!RemoteAsset:  sha256:38f9c044c3eedcdeb173acb4a3f93c07237e682adb3084cd9c534e43e55b313a
Source439:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.pom#/artifact-0339-maven-remote-resources-plugin-3.3.0.pom
#!RemoteAsset:  sha256:2c923c63a197565a3e78f2b16d762d0f49bb83250dd2b1e6286704ea0f447060
Source440:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.jar#/artifact-0340-maven-resources-plugin-3.5.0.jar
#!RemoteAsset:  sha256:9f2275ca2ba3a3ab38caf6c2bc21be787c7305ea5333d1c33f52a530afc0bc7f
Source441:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.pom#/artifact-0341-maven-resources-plugin-3.5.0.pom
#!RemoteAsset:  sha256:1ae06fc7dbb22140610327e6e94e6285176c993cf8d1a850adb6f87f535f8cb4
Source442:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.5.5/maven-surefire-plugin-3.5.5.jar#/artifact-0342-maven-surefire-plugin-3.5.5.jar
#!RemoteAsset:  sha256:04dd9d39989cb719f5e583058f2a4a296190ee6a18f7b2f83842aad7bbf70b1b
Source443:      https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.5.5/maven-surefire-plugin-3.5.5.pom#/artifact-0343-maven-surefire-plugin-3.5.5.pom
#!RemoteAsset:  sha256:efaa4fc4832aad9703df46b89cb02845dbf4db6f6ac88534b7824c4956a3a5fb
Source444:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.pom#/artifact-0344-maven-reporting-api-3.0.pom
#!RemoteAsset:  sha256:25be6603c97d28fa3dcd122073054271c8fcaf667d220dce7a26a61a6f3cffd1
Source445:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-api/3.1.1/maven-reporting-api-3.1.1.jar#/artifact-0345-maven-reporting-api-3.1.1.jar
#!RemoteAsset:  sha256:74903e91bafbc97bfd43a73daf64e2ee86045563cef43ee8713b588946b1a16c
Source446:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-api/3.1.1/maven-reporting-api-3.1.1.pom#/artifact-0346-maven-reporting-api-3.1.1.pom
#!RemoteAsset:  sha256:cb2cbde3c9c7288f7398a250dcf3c90cf92714cff301f22b298e1091b5def33c
Source447:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.jar#/artifact-0347-maven-reporting-api-4.0.0.jar
#!RemoteAsset:  sha256:2032531f05994121c2fdb5df7235ed548f53d294d0b7ac45e797148d85a30ee2
Source448:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.pom#/artifact-0348-maven-reporting-api-4.0.0.pom
#!RemoteAsset:  sha256:e9e70fdb26ff8b1f15435e3a68866a25c85b1694007e0fbdfe84e48e946fe463
Source449:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.jar#/artifact-0349-maven-reporting-impl-4.0.0.jar
#!RemoteAsset:  sha256:e049cf5b77d09c24e83db9fd8f5019bdf86dc37a3357f5634c56fb157ecda248
Source450:      https://repo.maven.apache.org/maven2/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.pom#/artifact-0350-maven-reporting-impl-4.0.0.pom
#!RemoteAsset:  sha256:831c3849751101226495acfe9119582feb734a4539b070e0fbd9e85b03b501ce
Source451:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver/1.4.1/maven-resolver-1.4.1.pom#/artifact-0351-maven-resolver-1.4.1.pom
#!RemoteAsset:  sha256:65da85f16b9a31cb3db26d1b3f0aa8f6fde0b9b2170ed725a9bf2f8267690508
Source452:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver/1.9.23/maven-resolver-1.9.23.pom#/artifact-0352-maven-resolver-1.9.23.pom
#!RemoteAsset:  sha256:c0870a6e68e160851cc7c1108ffc77198edf90715520d1a87c50484e7281c06e
Source453:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver/1.9.25/maven-resolver-1.9.25.pom#/artifact-0353-maven-resolver-1.9.25.pom
#!RemoteAsset:  sha256:8924b41711cce058f83c46d79ad83d6e04edcf13ed5631ec11135656e0b87f56
Source454:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver/1.9.27/maven-resolver-1.9.27.pom#/artifact-0354-maven-resolver-1.9.27.pom
#!RemoteAsset:  sha256:33dc67306cc95da14e5444e8b494d967924abf1d01bae1894676164cbd3f6112
Source455:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.jar#/artifact-0355-maven-resolver-api-1.4.1.jar
#!RemoteAsset:  sha256:335513ce1dd2cf4c7d1dbfa1b8aa14656d9be5f9f3f0d0875ac528893c9f0f06
Source456:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.pom#/artifact-0356-maven-resolver-api-1.4.1.pom
#!RemoteAsset:  sha256:c3174c617715faf583d55bdbcf7928e4ee71a8a78eedbfca775e23de28304086
Source457:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.9.23/maven-resolver-api-1.9.23.pom#/artifact-0357-maven-resolver-api-1.9.23.pom
#!RemoteAsset:  sha256:d2a68bc43e04adaf767970122de0c44430458fee25dd967d0039401dc260171a
Source458:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.9.25/maven-resolver-api-1.9.25.pom#/artifact-0358-maven-resolver-api-1.9.25.pom
#!RemoteAsset:  sha256:a895d222283666a7320ddc76615e2e93a41fabd93ce9a6bf9ddee39272bb87b4
Source459:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.9.27/maven-resolver-api-1.9.27.jar#/artifact-0359-maven-resolver-api-1.9.27.jar
#!RemoteAsset:  sha256:98dc031f75f2c9b7efeef344e1c74bb3d009c584e36e82a0ec3d263d2bfef373
Source460:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-api/1.9.27/maven-resolver-api-1.9.27.pom#/artifact-0360-maven-resolver-api-1.9.27.pom
#!RemoteAsset:  sha256:3bd98e3a426f9adcae39e3786db229e2be77e08a743ecd9be15c5ed77be3a625
Source461:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-connector-basic/1.9.27/maven-resolver-connector-basic-1.9.27.jar#/artifact-0361-maven-resolver-connector-basic-1.9.27.jar
#!RemoteAsset:  sha256:494fd7b5b48b9dd65ff624ef38c900e7caab4d815567dca1ba6fb9d80278a19f
Source462:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-connector-basic/1.9.27/maven-resolver-connector-basic-1.9.27.pom#/artifact-0362-maven-resolver-connector-basic-1.9.27.pom
#!RemoteAsset:  sha256:295d48ea2a8bb3aef51888967f105fb6251997d111f13c32d28919fd9b1c951e
Source463:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-impl/1.9.27/maven-resolver-impl-1.9.27.jar#/artifact-0363-maven-resolver-impl-1.9.27.jar
#!RemoteAsset:  sha256:ce9b47e8aeb58e46dfd05eb8fd0fe3ebfe152a06ff0f23bb42127d1576cd6914
Source464:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-impl/1.9.27/maven-resolver-impl-1.9.27.pom#/artifact-0364-maven-resolver-impl-1.9.27.pom
#!RemoteAsset:  sha256:b39ecd4da98fdac5068e6f5d16910a71f4e4d48e95e17d107f6603e18f2b3fdf
Source465:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-named-locks/1.9.27/maven-resolver-named-locks-1.9.27.jar#/artifact-0365-maven-resolver-named-locks-1.9.27.jar
#!RemoteAsset:  sha256:41ef2c7170eb0672cb7bc97caa765bad5386d49d93bbe8ae430887238c8e669a
Source466:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-named-locks/1.9.27/maven-resolver-named-locks-1.9.27.pom#/artifact-0366-maven-resolver-named-locks-1.9.27.pom
#!RemoteAsset:  sha256:1cab02f45bc58d5f4d8e084eaf032f13ea1a5fc9021d8bd74f8360ebb6593e5a
Source467:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-spi/1.9.27/maven-resolver-spi-1.9.27.jar#/artifact-0367-maven-resolver-spi-1.9.27.jar
#!RemoteAsset:  sha256:c6310e360bb5b543aa0c7a6892b18e964add6feaf3917ac88c85264ed377c676
Source468:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-spi/1.9.27/maven-resolver-spi-1.9.27.pom#/artifact-0368-maven-resolver-spi-1.9.27.pom
#!RemoteAsset:  sha256:3988261bd31e2e79eda802b3971992fce44756b0029557a05c7b871d3c3ddef7
Source469:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-transport-file/1.9.27/maven-resolver-transport-file-1.9.27.jar#/artifact-0369-maven-resolver-transport-file-1.9.27.jar
#!RemoteAsset:  sha256:4832099eb3a535b19903a898bb03f4cc654886deb07661bd38f8cb3f002ebe54
Source470:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-transport-file/1.9.27/maven-resolver-transport-file-1.9.27.pom#/artifact-0370-maven-resolver-transport-file-1.9.27.pom
#!RemoteAsset:  sha256:723f3d9d717a693d0aac589e266b995f76e9c63edd48ecc8a0cf9e86a77e459c
Source471:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-transport-http/1.9.27/maven-resolver-transport-http-1.9.27.jar#/artifact-0371-maven-resolver-transport-http-1.9.27.jar
#!RemoteAsset:  sha256:a7eae6d54a490eedf286193d7f280f7e97d89588da7d5adf117f0133098dbe2e
Source472:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-transport-http/1.9.27/maven-resolver-transport-http-1.9.27.pom#/artifact-0372-maven-resolver-transport-http-1.9.27.pom
#!RemoteAsset:  sha256:ddf1c8744f7ef50d8ab78526611b690ab1da0e9ad8d99f72d9dbe1b259aa9a8b
Source473:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-transport-wagon/1.9.27/maven-resolver-transport-wagon-1.9.27.jar#/artifact-0373-maven-resolver-transport-wagon-1.9.27.jar
#!RemoteAsset:  sha256:8dc4eb6a727abe07d6fa8c94056920050dbac039cf714e51e633e430aa2d6002
Source474:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-transport-wagon/1.9.27/maven-resolver-transport-wagon-1.9.27.pom#/artifact-0374-maven-resolver-transport-wagon-1.9.27.pom
#!RemoteAsset:  sha256:6b2184872fa7cc2ef5a90481b56af9711c15b371e69ab52f0f31bf24e910dd82
Source475:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.jar#/artifact-0375-maven-resolver-util-1.4.1.jar
#!RemoteAsset:  sha256:a58c932e967e85e7bcb8d4adaedd14a5221a1750a1d089c5086c4d73df505155
Source476:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.pom#/artifact-0376-maven-resolver-util-1.4.1.pom
#!RemoteAsset:  sha256:a6b81ce281313cc2adf19e697d59d53a83793d83e33707fc44836c4934f4030f
Source477:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.9.23/maven-resolver-util-1.9.23.jar#/artifact-0377-maven-resolver-util-1.9.23.jar
#!RemoteAsset:  sha256:ecc014d22b31def225b5ae4e1e715d2350cfe959b05f98d4df0c39a741918c2f
Source478:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.9.23/maven-resolver-util-1.9.23.pom#/artifact-0378-maven-resolver-util-1.9.23.pom
#!RemoteAsset:  sha256:e31330fdb29045f3087b4985cb488a5b5ebbcbd7d879fda14e6ed4dd61b1fdf7
Source479:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.jar#/artifact-0379-maven-resolver-util-1.9.25.jar
#!RemoteAsset:  sha256:2283fb0bb5cec9f7524cba93498c6e89739aac5edd25d3a418f0fc4f6ce30007
Source480:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.pom#/artifact-0380-maven-resolver-util-1.9.25.pom
#!RemoteAsset:  sha256:74a12548f0d6aad13c728666288c1e81201c24bd05bb4e4ec8c1558517b379a7
Source481:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.jar#/artifact-0381-maven-resolver-util-1.9.27.jar
#!RemoteAsset:  sha256:b2b3c7774cdc61887da814b42338c9421babbab9b1e87c3e6493885ffda53231
Source482:      https://repo.maven.apache.org/maven2/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.pom#/artifact-0382-maven-resolver-util-1.9.27.pom
#!RemoteAsset:  sha256:32ac469785dd1547ac71437e4c3916c4a56a3d69303cb08d789ecdd0bfd1d6de
Source483:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.jar#/artifact-0383-file-management-3.2.0.jar
#!RemoteAsset:  sha256:04e3bdd6d1920d1cdba206bc35dd3c6e0646c5730969f8b5d5397e5f1c7b5edd
Source484:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.pom#/artifact-0384-file-management-3.2.0.pom
#!RemoteAsset:  sha256:1ac88accde99ed71e65253bd130868c0e654f940f01ade073b895eb2f817cf06
Source485:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.jar#/artifact-0385-maven-artifact-transfer-0.13.1.jar
#!RemoteAsset:  sha256:e4b15a1e7cfbfe480408cfbaa148d66ea3324bf19e9ac6d6c17053bdb18ac4cd
Source486:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.pom#/artifact-0386-maven-artifact-transfer-0.13.1.pom
#!RemoteAsset:  sha256:034e12a9d1d5f5618a9e0dda23aadda4ed659ec55240876b6e954cc2172be456
Source487:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.1.0/maven-common-artifact-filters-3.1.0.pom#/artifact-0387-maven-common-artifact-filters-3.1.0.pom
#!RemoteAsset:  sha256:931a77aa9dad6c91f10fcfafa70adc7608c004576b4924c74ecbffb27568a880
Source488:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.jar#/artifact-0388-maven-common-artifact-filters-3.4.0.jar
#!RemoteAsset:  sha256:c93581d69b337c1fcc0957c727c430180b6387276ef1d3c2976c175e93765eb1
Source489:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.pom#/artifact-0389-maven-common-artifact-filters-3.4.0.pom
#!RemoteAsset:  sha256:2710707f61af4556ccd9fb21ceb8f59119afcb8637b100ddabb3225bd948b9be
Source490:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.17.0/maven-dependency-analyzer-1.17.0.jar#/artifact-0390-maven-dependency-analyzer-1.17.0.jar
#!RemoteAsset:  sha256:691d70cd2fbf7ce0f33a1c258d9c188bdde0816dbe94ded670eda8c2eab472f3
Source491:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-analyzer/1.17.0/maven-dependency-analyzer-1.17.0.pom#/artifact-0391-maven-dependency-analyzer-1.17.0.pom
#!RemoteAsset:  sha256:a3353f6a82feb950d5e7e64b0cd4ceadea7eb62112e447172e34974a510316f4
Source492:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.jar#/artifact-0392-maven-dependency-tree-3.3.0.jar
#!RemoteAsset:  sha256:06d3cdd58a0bcec206558ade256147aade63a166b042ef53215df6c51206d920
Source493:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.pom#/artifact-0393-maven-dependency-tree-3.3.0.pom
#!RemoteAsset:  sha256:ff04a5297c69d95f6face0af8934d6ee7bf1389dec50648bdd5e8569fb9d8e26
Source494:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.jar#/artifact-0394-maven-filtering-3.4.0.jar
#!RemoteAsset:  sha256:bb698e6a90534e82a8842a199b7dff470781a822d4e5868fb76ba953ed08ed6a
Source495:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.pom#/artifact-0395-maven-filtering-3.4.0.pom
#!RemoteAsset:  sha256:7adb0e46b5fff4fc03aab4baafbdee0b29e444cffe4478858c63082d497220bf
Source496:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.jar#/artifact-0396-maven-filtering-3.5.0.jar
#!RemoteAsset:  sha256:06b492b0244a82434470161f851b247271ec8fdaeea1c29de98abde066f80c64
Source497:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.pom#/artifact-0397-maven-filtering-3.5.0.pom
#!RemoteAsset:  sha256:6a58eb24291600f75ce0fe369b73fe6700f575ace4b664724d3cd0a6b85b63ee
Source498:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/15/maven-shared-components-15.pom#/artifact-0398-maven-shared-components-15.pom
#!RemoteAsset:  sha256:d82408269aada2eb1521ee8ff17f7c67333684f8ed2a09a9e35badd2e7575957
Source499:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom#/artifact-0399-maven-shared-components-19.pom
#!RemoteAsset:  sha256:ad9df3b73df8bbc0309ad42818fa9779cd10528df0708788f4aceddc514bd031
Source500:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/30/maven-shared-components-30.pom#/artifact-0400-maven-shared-components-30.pom
#!RemoteAsset:  sha256:f43ff6fee0b32533765b3406648d6a5532f85d5e488079480788cb36e79d0980
Source501:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/33/maven-shared-components-33.pom#/artifact-0401-maven-shared-components-33.pom
#!RemoteAsset:  sha256:64d0edb5f21cfff600b1c3ab7d45f9754cd18ba5fbf83b3d1bb7c4849437d8e3
Source502:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom#/artifact-0402-maven-shared-components-34.pom
#!RemoteAsset:  sha256:17e81388d88ba61c4055450ec90a32ee30acd07f46dc6e31e096b8e53735f4b2
Source503:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom#/artifact-0403-maven-shared-components-39.pom
#!RemoteAsset:  sha256:c6bd81e2588e0f0f87392d4db590e1d81c126a25ee9253252ef89c506cde1e34
Source504:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/41/maven-shared-components-41.pom#/artifact-0404-maven-shared-components-41.pom
#!RemoteAsset:  sha256:aa66faa11c11b900d099bfef0ee9fe8485d7e7fc74e87193e1f74572ed9587c5
Source505:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/42/maven-shared-components-42.pom#/artifact-0405-maven-shared-components-42.pom
#!RemoteAsset:  sha256:6072dd103bdba3199584c5b73ed45b00567cd3ea918e2160b10bc7437c9e8181
Source506:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/43/maven-shared-components-43.pom#/artifact-0406-maven-shared-components-43.pom
#!RemoteAsset:  sha256:41fbab97912beb3a061b1e3845d2e06d2bb214cc71f92fa7f396480dc765a14e
Source507:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/44/maven-shared-components-44.pom#/artifact-0407-maven-shared-components-44.pom
#!RemoteAsset:  sha256:5879e023d9bcafda006d28b42b2495c6f3db587d3e71eefa0a3cedeeea36d987
Source508:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/45/maven-shared-components-45.pom#/artifact-0408-maven-shared-components-45.pom
#!RemoteAsset:  sha256:3bd3d07c910477091bb9602f931f696c4aa115c86a322bff6a604ec7543afc07
Source509:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/47/maven-shared-components-47.pom#/artifact-0409-maven-shared-components-47.pom
#!RemoteAsset:  sha256:61988e54486a5dc38f06c70fdae5b108556c63bd433697b9f4305fcdb30fa40e
Source510:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar#/artifact-0410-maven-shared-incremental-1.1.jar
#!RemoteAsset:  sha256:f21d19eb49b4a66cd85354a9ee7335439ea92a368173760a202766008cc19924
Source511:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom#/artifact-0411-maven-shared-incremental-1.1.pom
#!RemoteAsset:  sha256:68f9fdef85d2c89f53c63cbc559920e0115bd30eb6f7076c9854931d3829027b
Source512:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.pom#/artifact-0412-maven-shared-utils-3.1.0.pom
#!RemoteAsset:  sha256:b613357e1bad4dfc1dead801691c9460f9585fe7c6b466bc25186212d7d18487
Source513:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.jar#/artifact-0413-maven-shared-utils-3.4.2.jar
#!RemoteAsset:  sha256:a941745d7faeb8dc9a75edc2c330c994b7440b9a44d21142716b6053967a41c1
Source514:      https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.pom#/artifact-0414-maven-shared-utils-3.4.2.pom
#!RemoteAsset:  sha256:698c03595550549fd51bd2d9bd801d70e70b73e4c562f315fd63550cc2bbbf14
Source515:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.5.5/common-java5-3.5.5.jar#/artifact-0415-common-java5-3.5.5.jar
#!RemoteAsset:  sha256:21f8ca88e5727ebce18db5045a2b5d0470cf37e9b90a4c6f2f9c5a4a61cf75a1
Source516:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.5.5/common-java5-3.5.5.pom#/artifact-0416-common-java5-3.5.5.pom
#!RemoteAsset:  sha256:ee2fd8f0f86150940b54866ea77b0361a1efe7ae0f0b62f2e3834c2ea11ec9cc
Source517:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.5.5/maven-surefire-common-3.5.5.jar#/artifact-0417-maven-surefire-common-3.5.5.jar
#!RemoteAsset:  sha256:47577ce85e4726ba689470359d009ab3dd54a2a66a54604c376c5ea3d36657fc
Source518:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.5.5/maven-surefire-common-3.5.5.pom#/artifact-0418-maven-surefire-common-3.5.5.pom
#!RemoteAsset:  sha256:05658c71ed1ac0100adb3b5eea1d0facd0010867144ed046882d157ef674b3be
Source519:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire/3.5.5/surefire-3.5.5.pom#/artifact-0419-surefire-3.5.5.pom
#!RemoteAsset:  sha256:b5694cc7b6016acb45af77500fa465755030b14c15985b2c90213b46287ec2d4
Source520:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.5.5/surefire-api-3.5.5.jar#/artifact-0420-surefire-api-3.5.5.jar
#!RemoteAsset:  sha256:ad893f1333c98f47353734bdc2c3024df175748848e5da96e0739829597678c3
Source521:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.5.5/surefire-api-3.5.5.pom#/artifact-0421-surefire-api-3.5.5.pom
#!RemoteAsset:  sha256:c4f2be4d00eb7b79f797c7d9719c0b3e9cec43ba1cae4880ebabc60961e42e30
Source522:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.5.5/surefire-booter-3.5.5.jar#/artifact-0422-surefire-booter-3.5.5.jar
#!RemoteAsset:  sha256:3329accc720aa884d87631978010e14ce0598452ad39433a8ca993619dcea3f3
Source523:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.5.5/surefire-booter-3.5.5.pom#/artifact-0423-surefire-booter-3.5.5.pom
#!RemoteAsset:  sha256:eb992fe8b019a336c03aa558779f5792f58bb72050cd4c4d33fc1da5a24cb1b6
Source524:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.5.5/surefire-extensions-api-3.5.5.jar#/artifact-0424-surefire-extensions-api-3.5.5.jar
#!RemoteAsset:  sha256:93d972aea168469673ddb86330f64dc9967f50e003e42b285c8cef7d58be1be1
Source525:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.5.5/surefire-extensions-api-3.5.5.pom#/artifact-0425-surefire-extensions-api-3.5.5.pom
#!RemoteAsset:  sha256:e3bff2e5e9641db26d2e4a9579d8dc4d6ab3d6b9065c6e132f5596be86b875f0
Source526:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.5.5/surefire-extensions-spi-3.5.5.jar#/artifact-0426-surefire-extensions-spi-3.5.5.jar
#!RemoteAsset:  sha256:e1e0db5d9e9a61e1fd816d09c41bb2717d8846bbfb33281e5d30aade69c181ec
Source527:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.5.5/surefire-extensions-spi-3.5.5.pom#/artifact-0427-surefire-extensions-spi-3.5.5.pom
#!RemoteAsset:  sha256:a7b8b507bf76765229d0bf020a12eb969ba75cd6299cbca5ae9cd06d4c9949ec
Source528:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/3.5.5/surefire-junit-platform-3.5.5.jar#/artifact-0428-surefire-junit-platform-3.5.5.jar
#!RemoteAsset:  sha256:554d4312197987b90d5a2f6c4c3b8dab4725260a51933738200ed5b5ab24eaa8
Source529:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-junit-platform/3.5.5/surefire-junit-platform-3.5.5.pom#/artifact-0429-surefire-junit-platform-3.5.5.pom
#!RemoteAsset:  sha256:5ff01941b8cef7c530e62099ba2a793467b68098a2bceb2f031d6530916e3cd9
Source530:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.5.5/surefire-logger-api-3.5.5.jar#/artifact-0430-surefire-logger-api-3.5.5.jar
#!RemoteAsset:  sha256:05499020753ee74b93b9cb91cbc05885af900a368ec7cc8510277e68a6a5b9da
Source531:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.5.5/surefire-logger-api-3.5.5.pom#/artifact-0431-surefire-logger-api-3.5.5.pom
#!RemoteAsset:  sha256:2b4a0251be22ad6e88bb0698f9797b38f033f00f16a2a46879da53637f501ac3
Source532:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/3.5.5/surefire-providers-3.5.5.pom#/artifact-0432-surefire-providers-3.5.5.pom
#!RemoteAsset:  sha256:50b880ae1a95c6e5301c055ef46bfd1281c2a6c3e26e25e6465d1c22a7eabc2d
Source533:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.5.5/surefire-shared-utils-3.5.5.jar#/artifact-0433-surefire-shared-utils-3.5.5.jar
#!RemoteAsset:  sha256:61df0ff0b033305b956d3e4d614b368d53775e72fb89cc4fbb5f6764f5e893fd
Source534:      https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.5.5/surefire-shared-utils-3.5.5.pom#/artifact-0434-surefire-shared-utils-3.5.5.pom
#!RemoteAsset:  sha256:7c10b8bac59268fe7957f2ab2b50965d90069ebf850c756bb55ea807ce440f0b
Source535:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon/3.5.3/wagon-3.5.3.pom#/artifact-0435-wagon-3.5.3.pom
#!RemoteAsset:  sha256:afc9216fa97b78dad227b4a8d4d67b9897bf113a57f80598d62993841113e103
Source536:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.jar#/artifact-0436-wagon-file-3.5.3.jar
#!RemoteAsset:  sha256:b89e540a7e432329bb5d93f2dfc578f898960afed66ae6a2dfeaa3d48d32c09c
Source537:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.pom#/artifact-0437-wagon-file-3.5.3.pom
#!RemoteAsset:  sha256:d2b6e48c9fcbe579e1858c622d14464011ff265fa6e28e794004a6882154a509
Source538:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.jar#/artifact-0438-wagon-http-3.5.3.jar
#!RemoteAsset:  sha256:934f2f9c87e497c4f795be4bb05b360b8c231467d460103c19012b79b8c03c6b
Source539:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.pom#/artifact-0439-wagon-http-3.5.3.pom
#!RemoteAsset:  sha256:8e7da766f55164fde8779aaaa125832506c2848cab4876b5305138873e28037f
Source540:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.jar#/artifact-0440-wagon-http-shared-3.5.3.jar
#!RemoteAsset:  sha256:6014b1e64abf455c6834a0918248e15638050f835da12051d33cda7e946d88f8
Source541:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.pom#/artifact-0441-wagon-http-shared-3.5.3.pom
#!RemoteAsset:  sha256:5e72000338945ed3e96f8e4f578d1d0672e1af7e19c0e9014197ae5b31af3ef4
Source542:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.jar#/artifact-0442-wagon-provider-api-3.5.3.jar
#!RemoteAsset:  sha256:64d6a085e8a6bede9607cbd029ea58cd1c87304410862492174a6d59b9d17142
Source543:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.pom#/artifact-0443-wagon-provider-api-3.5.3.pom
#!RemoteAsset:  sha256:807c51ffccdef6c01130b74aeed27815ec162bc2686c01e9d29f16efc526a44a
Source544:      https://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-providers/3.5.3/wagon-providers-3.5.3.pom#/artifact-0444-wagon-providers-3.5.3.pom
#!RemoteAsset:  sha256:710620b3d2a14505e0a29885e4a8251ec0e525c617a12788f47c18cdd70fff4d
Source545:      https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-core/0.16.1/apache-rat-core-0.16.1.jar#/artifact-0445-apache-rat-core-0.16.1.jar
#!RemoteAsset:  sha256:d0964fe6855c78b7bf6b35543dd4fff7c03934efc6ced47365a5ed09bdbc8174
Source546:      https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-core/0.16.1/apache-rat-core-0.16.1.pom#/artifact-0446-apache-rat-core-0.16.1.pom
#!RemoteAsset:  sha256:331971651bd1da6922eea4c9cc86169b9da28a07f281957bd575a50b6d9a4444
Source547:      https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-plugin/0.16.1/apache-rat-plugin-0.16.1.jar#/artifact-0447-apache-rat-plugin-0.16.1.jar
#!RemoteAsset:  sha256:ae75978aef81bbef3ada4ee120069ea8fb6973f4708766577c8a05959ab60e41
Source548:      https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-plugin/0.16.1/apache-rat-plugin-0.16.1.pom#/artifact-0448-apache-rat-plugin-0.16.1.pom
#!RemoteAsset:  sha256:eb211cec7b87631acdaf8a5be3dfd94103ca66a912c226e92832ab748e5a37f0
Source549:      https://repo.maven.apache.org/maven2/org/apache/rat/apache-rat-project/0.16.1/apache-rat-project-0.16.1.pom#/artifact-0449-apache-rat-project-0.16.1.pom
#!RemoteAsset:  sha256:8258cfdcaa16127f35ffe610a3fa4f76b7ebe51b88922c73c4ee39ce8f378ce5
Source550:      https://repo.maven.apache.org/maven2/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.jar#/artifact-0450-velocity-tools-generic-3.1.jar
#!RemoteAsset:  sha256:a6f50cb3f413875c039652269d2a89f8878d0d9fc8cc662fc13591ca20d84758
Source551:      https://repo.maven.apache.org/maven2/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.pom#/artifact-0451-velocity-tools-generic-3.1.pom
#!RemoteAsset:  sha256:5a597b88dba795090e77015bcdf53461b41d45da2d7d1764e4ece8b30a226fcd
Source552:      https://repo.maven.apache.org/maven2/org/apache/velocity/tools/velocity-tools-parent/3.1/velocity-tools-parent-3.1.pom#/artifact-0452-velocity-tools-parent-3.1.pom
#!RemoteAsset:  sha256:f663422e0b92069dcb30d58a2652660b727252ae94e40e8616e710723c64cdec
Source553:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.6.2/velocity-1.6.2.pom#/artifact-0453-velocity-1.6.2.pom
#!RemoteAsset:  sha256:ec92dae810034f4b46dbb16ef4364a4013b0efb24a8c5dd67435cae46a290d8e
Source554:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.7/velocity-1.7.jar#/artifact-0454-velocity-1.7.jar
#!RemoteAsset:  sha256:a3f97ceab5f073ed93ef8fe6304e35252d83ecf2442c83fe0492b8b73da3b40b
Source555:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity/1.7/velocity-1.7.pom#/artifact-0455-velocity-1.7.pom
#!RemoteAsset:  sha256:d4242a6174243f1e680434571ba4e6a1dbae199c0bc350a987d5fb9c3ce1e0d3
Source556:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom#/artifact-0456-velocity-engine-core-2.3.pom
#!RemoteAsset:  sha256:a9eee9d59ac787f9c379ec4f37af7e04f8d62161a1e602a4274014d0dc41b0cb
Source557:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.4/velocity-engine-core-2.4.pom#/artifact-0457-velocity-engine-core-2.4.pom
#!RemoteAsset:  sha256:1c19157d1171d560088e485be97c93a7a2f7e9f56e517f0a30273c5c39df6231
Source558:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.jar#/artifact-0458-velocity-engine-core-2.4.1.jar
#!RemoteAsset:  sha256:ac7cd94f0d9fb39bcba3b28287c4c40005dc0f53a986fb587e4f67a4ccb3e5b6
Source559:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.pom#/artifact-0459-velocity-engine-core-2.4.1.pom
#!RemoteAsset:  sha256:4c0e4a92f6870f399b946d5bb789d177e4a47941147c3fddc2e6f063e9cb96db
Source560:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom#/artifact-0460-velocity-engine-parent-2.3.pom
#!RemoteAsset:  sha256:d4b9e31a7e9ea490c562a2bdeced94eef3f08c8d0a5378add3d6bcf8828334bf
Source561:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.4/velocity-engine-parent-2.4.pom#/artifact-0461-velocity-engine-parent-2.4.pom
#!RemoteAsset:  sha256:8efb661b7e1b44b7a056f23650ab2b43b8fcdb09bbe2ec3d3d02185d5658fd4a
Source562:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.4.1/velocity-engine-parent-2.4.1.pom#/artifact-0462-velocity-engine-parent-2.4.1.pom
#!RemoteAsset:  sha256:7a2ac73c90dd104b5a07e6e2cd03e95ec28d29f3b8304f3dd7fffcecb049712e
Source563:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-master/4/velocity-master-4.pom#/artifact-0463-velocity-master-4.pom
#!RemoteAsset:  sha256:943a046c1fe36b28b3cea11fb0d34e8b836b245433087f8fa916c0a752393181
Source564:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-master/7/velocity-master-7.pom#/artifact-0464-velocity-master-7.pom
#!RemoteAsset:  sha256:b174eb36bc48c25dce10571c7d3d5dca4e4c1b3e2e31a92b9ed68fe9dea688d9
Source565:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.jar#/artifact-0465-velocity-tools-2.0.jar
#!RemoteAsset:  sha256:b12f13ab462281d48c573acabf124e067a9d49e65ec72b27597db9e91f721b95
Source566:      https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.pom#/artifact-0466-velocity-tools-2.0.pom
#!RemoteAsset:  sha256:ea717132de8404b62fc9097a1f3215c705d525d457be9a5f12653adc68c33ab7
Source567:      https://repo.maven.apache.org/maven2/org/apache/xbean/xbean/3.7/xbean-3.7.pom#/artifact-0467-xbean-3.7.pom
#!RemoteAsset:  sha256:9795c15322c5d19af336eebd9e164fa7d5897c4b004a7d66e21635a173e748a9
Source568:      https://repo.maven.apache.org/maven2/org/apache/xbean/xbean-reflect/3.7/xbean-reflect-3.7.pom#/artifact-0468-xbean-reflect-3.7.pom
#!RemoteAsset:  sha256:a17955976070c0573235ee662f2794a78082758b61accffce8d3f8aedcd91047
Source569:      https://repo.maven.apache.org/maven2/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.jar#/artifact-0469-bsh-2.0b6.jar
#!RemoteAsset:  sha256:679be8f12aa2864f7c286f7f5bcbac8365851c01821de5b99a12d6f772f521e6
Source570:      https://repo.maven.apache.org/maven2/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.pom#/artifact-0470-bsh-2.0b6.pom
#!RemoteAsset:  sha256:b509448ac506d607319f182537f0b35d71007582ec741832a1f111e5b5b70b38
Source571:      https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar#/artifact-0471-apiguardian-api-1.1.2.jar
#!RemoteAsset:  sha256:32355081d109095c3d5d374d5a43b4f4c1b75d549e983ef50723e2772e5302a0
Source572:      https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom#/artifact-0472-apiguardian-api-1.1.2.pom
#!RemoteAsset:  sha256:1c09f6c04c905e1e5cdb22d5dfa5f11a496e19e881de0850b523ed53a0519f5b
Source573:      https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.7/assertj-bom-3.27.7.pom#/artifact-0473-assertj-bom-3.27.7.pom
#!RemoteAsset:  sha256:2836b3b8a78edb31a1803592e60fc767b21f2d190764631ba6efa0837bb35721
Source574:      https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.5.0/checker-qual-3.5.0.pom#/artifact-0474-checker-qual-3.5.0.pom
#!RemoteAsset:  sha256:919bc8dadbfa220657bdda3015317c87b55f56eec36415280884ca63b8a558c7
Source575:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello/2.6.0/modello-2.6.0.pom#/artifact-0475-modello-2.6.0.pom
#!RemoteAsset:  sha256:8cf06d52a8b3e0b28247c35d55e97f7fa14082738dad2c57d08bb812da7c617a
Source576:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-core/2.6.0/modello-core-2.6.0.jar#/artifact-0476-modello-core-2.6.0.jar
#!RemoteAsset:  sha256:6f014177557812e08ee9ddc9d7544cc5c34707079ed54defe4902c471489f04a
Source577:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-core/2.6.0/modello-core-2.6.0.pom#/artifact-0477-modello-core-2.6.0.pom
#!RemoteAsset:  sha256:7984c96a9857a52780fbd7ac601b738e4b9d991ddc86725d4d6c5e8945be39b5
Source578:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-maven-plugin/2.6.0/modello-maven-plugin-2.6.0.jar#/artifact-0478-modello-maven-plugin-2.6.0.jar
#!RemoteAsset:  sha256:634dce5ca6a36bd587963c79b7a8aeeda211c4dee295e3d89fe4a359a04b931e
Source579:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-maven-plugin/2.6.0/modello-maven-plugin-2.6.0.pom#/artifact-0479-modello-maven-plugin-2.6.0.pom
#!RemoteAsset:  sha256:2662574ca7df3fbed24de5826712986d4a6936eae3399af7d559555339be3406
Source580:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-converters/2.6.0/modello-plugin-converters-2.6.0.jar#/artifact-0480-modello-plugin-converters-2.6.0.jar
#!RemoteAsset:  sha256:5bd89d9e4ad3df2c6a136c841217b164a5c498891eeee868b2099bdb03b3b660
Source581:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-converters/2.6.0/modello-plugin-converters-2.6.0.pom#/artifact-0481-modello-plugin-converters-2.6.0.pom
#!RemoteAsset:  sha256:69953286d40d1ae67e2470147a94f47d4df53c2c2f729f350b8d417ca5f7365f
Source582:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-dom4j/2.6.0/modello-plugin-dom4j-2.6.0.jar#/artifact-0482-modello-plugin-dom4j-2.6.0.jar
#!RemoteAsset:  sha256:759605c6a99f109d9f2f6ae5eb8d0f6a99a05d96fa1ffb7909ba9bedd2952900
Source583:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-dom4j/2.6.0/modello-plugin-dom4j-2.6.0.pom#/artifact-0483-modello-plugin-dom4j-2.6.0.pom
#!RemoteAsset:  sha256:5c84fdba40ec3b86cad67220d6414736b29898c07d482f68e528c8825851132a
Source584:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-jackson/2.6.0/modello-plugin-jackson-2.6.0.jar#/artifact-0484-modello-plugin-jackson-2.6.0.jar
#!RemoteAsset:  sha256:2431d8d1b642dbab60b740fd1065c5d5535c361ec7bd99174d2a62079f64ec5a
Source585:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-jackson/2.6.0/modello-plugin-jackson-2.6.0.pom#/artifact-0485-modello-plugin-jackson-2.6.0.pom
#!RemoteAsset:  sha256:927ff3c54b58daeabd6e5426e1e5e584c857c5fc998e620641761793e5a0013b
Source586:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-java/2.6.0/modello-plugin-java-2.6.0.jar#/artifact-0486-modello-plugin-java-2.6.0.jar
#!RemoteAsset:  sha256:77246778bc23b7af5d65ff0bb522d11463280ac97a94f04343358f19afe6973f
Source587:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-java/2.6.0/modello-plugin-java-2.6.0.pom#/artifact-0487-modello-plugin-java-2.6.0.pom
#!RemoteAsset:  sha256:2c05658dc28ab4635c037d77cc8dce50654ef724b992460fcf11d2160fdbde3e
Source588:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-jdom/2.6.0/modello-plugin-jdom-2.6.0.jar#/artifact-0488-modello-plugin-jdom-2.6.0.jar
#!RemoteAsset:  sha256:b3f74c0b71b86816f330ddc2979dc778f7d66133415bc4626257bd58550d3864
Source589:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-jdom/2.6.0/modello-plugin-jdom-2.6.0.pom#/artifact-0489-modello-plugin-jdom-2.6.0.pom
#!RemoteAsset:  sha256:80d2d46f48c156715f791a7529b356b31ccc18f2f5294fe55dfb0cc05de34972
Source590:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-jsonschema/2.6.0/modello-plugin-jsonschema-2.6.0.jar#/artifact-0490-modello-plugin-jsonschema-2.6.0.jar
#!RemoteAsset:  sha256:5435d9151cfe36eeb22f3230033083251d63b24975c503bcfbb9624781bff759
Source591:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-jsonschema/2.6.0/modello-plugin-jsonschema-2.6.0.pom#/artifact-0491-modello-plugin-jsonschema-2.6.0.pom
#!RemoteAsset:  sha256:cc1631f4ed441e7f8a39a69ea61d3a32eead9f4de06669ed9cd4a5e3798de3b1
Source592:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-sax/2.6.0/modello-plugin-sax-2.6.0.jar#/artifact-0492-modello-plugin-sax-2.6.0.jar
#!RemoteAsset:  sha256:b2fa886162ab22d956724b46a5b9b0ca449184312952477ea1da73fe58876899
Source593:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-sax/2.6.0/modello-plugin-sax-2.6.0.pom#/artifact-0493-modello-plugin-sax-2.6.0.pom
#!RemoteAsset:  sha256:1907ee952e372dd8ac835505967f72489600fb3fc6d0e3849da6ab0c6799f987
Source594:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-snakeyaml/2.6.0/modello-plugin-snakeyaml-2.6.0.jar#/artifact-0494-modello-plugin-snakeyaml-2.6.0.jar
#!RemoteAsset:  sha256:a3752065a9f51326ba43a204bb213d4463addd89323679123ba47ee7038f60df
Source595:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-snakeyaml/2.6.0/modello-plugin-snakeyaml-2.6.0.pom#/artifact-0495-modello-plugin-snakeyaml-2.6.0.pom
#!RemoteAsset:  sha256:5c25c77c53b7bcb600fa60bf52276ec0a29ec0fb8085eda7cedbc6058a459366
Source596:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-stax/2.6.0/modello-plugin-stax-2.6.0.jar#/artifact-0496-modello-plugin-stax-2.6.0.jar
#!RemoteAsset:  sha256:3b7de7db00cdcb765033dae0f913fec4569dddf15fa852c5c476bdfde5214326
Source597:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-stax/2.6.0/modello-plugin-stax-2.6.0.pom#/artifact-0497-modello-plugin-stax-2.6.0.pom
#!RemoteAsset:  sha256:4a3e3336f2248feed6fcdfa4c2b4db078c37942db43acbaccd8c2b96fd351712
Source598:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-velocity/2.6.0/modello-plugin-velocity-2.6.0.jar#/artifact-0498-modello-plugin-velocity-2.6.0.jar
#!RemoteAsset:  sha256:6d62b3fe51689c052bcee1f86cec606b5bf94f6a345fc2fe0bb502c8f8190eb6
Source599:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-velocity/2.6.0/modello-plugin-velocity-2.6.0.pom#/artifact-0499-modello-plugin-velocity-2.6.0.pom
#!RemoteAsset:  sha256:96627fe783e5a53446a0a365dd096a377f9fdc00554ec426929c6aa5a776e9e2
Source600:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xdoc/2.6.0/modello-plugin-xdoc-2.6.0.jar#/artifact-0500-modello-plugin-xdoc-2.6.0.jar
#!RemoteAsset:  sha256:47299addf15cff15e8b80bdd62a844a730d826d4b4bf2c69f2785e7ff8914d00
Source601:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xdoc/2.6.0/modello-plugin-xdoc-2.6.0.pom#/artifact-0501-modello-plugin-xdoc-2.6.0.pom
#!RemoteAsset:  sha256:582edcc6beb2ae58f414b49b7b956e80ac29fbcc4e3f5a3705b90340e117f0b3
Source602:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xml/2.6.0/modello-plugin-xml-2.6.0.jar#/artifact-0502-modello-plugin-xml-2.6.0.jar
#!RemoteAsset:  sha256:2d8231bea604e9680d631100b7d57779bc5e271cc2e8695a0bf742bfd9ef7fc4
Source603:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xml/2.6.0/modello-plugin-xml-2.6.0.pom#/artifact-0503-modello-plugin-xml-2.6.0.pom
#!RemoteAsset:  sha256:1ace21e108696240fca109b4017eb7376612c6cfdd84f467c05131bce6ca51ab
Source604:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xpp3/2.6.0/modello-plugin-xpp3-2.6.0.jar#/artifact-0504-modello-plugin-xpp3-2.6.0.jar
#!RemoteAsset:  sha256:c24092cbdc1d86f2d9f06ca3306abde6b4b34f581847f59b25f4e9bc6563299e
Source605:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xpp3/2.6.0/modello-plugin-xpp3-2.6.0.pom#/artifact-0505-modello-plugin-xpp3-2.6.0.pom
#!RemoteAsset:  sha256:67282352b67923867d1db9653e2aeb582e0f7f735c45c2fb0e77c0215bd0ea75
Source606:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xsd/2.6.0/modello-plugin-xsd-2.6.0.jar#/artifact-0506-modello-plugin-xsd-2.6.0.jar
#!RemoteAsset:  sha256:10e58ad062c1622b431d512ee7ab5ffc9e38ca1dbaba0b9e3074c5b0a910a934
Source607:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugin-xsd/2.6.0/modello-plugin-xsd-2.6.0.pom#/artifact-0507-modello-plugin-xsd-2.6.0.pom
#!RemoteAsset:  sha256:19ffd4270dc134101d1f8b7613f5628004ef9565d77ba3da678ab12139886bd3
Source608:      https://repo.maven.apache.org/maven2/org/codehaus/modello/modello-plugins/2.6.0/modello-plugins-2.6.0.pom#/artifact-0508-modello-plugins-2.6.0.pom
#!RemoteAsset:  sha256:01823780affe8916f42872e52780490cb256c49b0fdcbfb9749a4c520a89067b
Source609:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer/1.27/animal-sniffer-1.27.jar#/artifact-0509-animal-sniffer-1.27.jar
#!RemoteAsset:  sha256:147bdaf486183f68c055f0cc1149c394c346d71506b006020d499b9b52ce0d94
Source610:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer/1.27/animal-sniffer-1.27.pom#/artifact-0510-animal-sniffer-1.27.pom
#!RemoteAsset:  sha256:cfd7e51a828fe6b98bc0dbb99e34900c9e9012322cb9ddd57fd8dd0b02da5e27
Source611:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer-annotations/1.27/animal-sniffer-annotations-1.27.jar#/artifact-0511-animal-sniffer-annotations-1.27.jar
#!RemoteAsset:  sha256:e596be247f2d3ef943be65edb0c05334d1996fed5fe0fe5518ff00a50b28c769
Source612:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer-annotations/1.27/animal-sniffer-annotations-1.27.pom#/artifact-0512-animal-sniffer-annotations-1.27.pom
#!RemoteAsset:  sha256:f05ebd3895f3d24c03cc3d126e139a563e2c9185b77c178bdd1e6e29ffdf84df
Source613:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer-maven-plugin/1.27/animal-sniffer-maven-plugin-1.27.jar#/artifact-0513-animal-sniffer-maven-plugin-1.27.jar
#!RemoteAsset:  sha256:bc12551d48d96a53c2536d334d79ae30dfdca860e63bdc26e613a3a38cb43849
Source614:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer-maven-plugin/1.27/animal-sniffer-maven-plugin-1.27.pom#/artifact-0514-animal-sniffer-maven-plugin-1.27.pom
#!RemoteAsset:  sha256:680260a8b94111ec2fcd439287391fdc40340292ba2e3167f8bef0d797003cec
Source615:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/animal-sniffer-parent/1.27/animal-sniffer-parent-1.27.pom#/artifact-0515-animal-sniffer-parent-1.27.pom
#!RemoteAsset:  sha256:772765fc101dfd292a85541037096bd12daf9d5f657d6808bb85cf16ff9f4427
Source616:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/build-helper-maven-plugin/3.6.1/build-helper-maven-plugin-3.6.1.jar#/artifact-0516-build-helper-maven-plugin-3.6.1.jar
#!RemoteAsset:  sha256:dbdfd37ddb8f976a4f8f35327f12b033863feca8c55381ca94f6dce965b6a657
Source617:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/build-helper-maven-plugin/3.6.1/build-helper-maven-plugin-3.6.1.pom#/artifact-0517-build-helper-maven-plugin-3.6.1.pom
#!RemoteAsset:  sha256:346f1f7b77ff648be853d0cf4bf18ba4115f27396156bb413c464b7a6137803a
Source618:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/extra-enforcer-rules/1.12.0/extra-enforcer-rules-1.12.0.jar#/artifact-0518-extra-enforcer-rules-1.12.0.jar
#!RemoteAsset:  sha256:2f3b5560ebd9528e66dd49599e924100dd28d25d73edef09f301b870591b7ba4
Source619:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/extra-enforcer-rules/1.12.0/extra-enforcer-rules-1.12.0.pom#/artifact-0519-extra-enforcer-rules-1.12.0.pom
#!RemoteAsset:  sha256:fdae779afab25278cd54301bd9910bfedb45576b6b81f157801eb4d62edec338
Source620:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/java-boot-classpath-detector/1.27/java-boot-classpath-detector-1.27.jar#/artifact-0520-java-boot-classpath-detector-1.27.jar
#!RemoteAsset:  sha256:47582d4b34302fd8bd2ea04b30632c49872346f9978ce501cd859283d60c417b
Source621:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/java-boot-classpath-detector/1.27/java-boot-classpath-detector-1.27.pom#/artifact-0521-java-boot-classpath-detector-1.27.pom
#!RemoteAsset:  sha256:6c75af0e0cfae6a7e3fb4db3478771d6c5d65a9a238c35dc6410f153d81877b1
Source622:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/mojo-parent/91/mojo-parent-91.pom#/artifact-0522-mojo-parent-91.pom
#!RemoteAsset:  sha256:4fdf1aa46d1fb722e15508b4edeb7b651344c6e29774cd2b76cbec3a84c23a11
Source623:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/mojo-parent/95/mojo-parent-95.pom#/artifact-0523-mojo-parent-95.pom
#!RemoteAsset:  sha256:0baed9a022fc38db6d41b15c988ca41bf8d25fc84716073986bd3dc1c36a8839
Source624:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/mojo-parent/96/mojo-parent-96.pom#/artifact-0524-mojo-parent-96.pom
#!RemoteAsset:  sha256:8cce892cfda0272e00dbdbf2acc607ffd5391734629fbdce349c5691ccf8d7fb
Source625:      https://repo.maven.apache.org/maven2/org/codehaus/mojo/signature/java18/1.0/java18-1.0.signature#/artifact-0525-java18-1.0.signature
#!RemoteAsset:  sha256:09b999a969e73525a6cc3ad2868ea744766e1d93b25c6c656d61a5ff9c881da9
Source626:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/1.0.10/plexus-1.0.10.pom#/artifact-0526-plexus-1.0.10.pom
#!RemoteAsset:  sha256:5197630dcd2336f5b4ab8e6d26e5b8675f5ebd83bd8c91d6aba431b09627d626
Source627:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/1.0.11/plexus-1.0.11.pom#/artifact-0527-plexus-1.0.11.pom
#!RemoteAsset:  sha256:bba9c521064b9ca132ce97cc1cc7eb4afc2dbe32bc88cb872c88e99f6162301f
Source628:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/10/plexus-10.pom#/artifact-0528-plexus-10.pom
#!RemoteAsset:  sha256:575945dc08966c66eb03d5bae9135bd22ca3920a1865bb99d3ecd93bef55abd3
Source629:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/13/plexus-13.pom#/artifact-0529-plexus-13.pom
#!RemoteAsset:  sha256:68d4eed65a3dbbc342ed80dd138fbe9c67cb7fb4c2abc4f5201cdb5b9f645868
Source630:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/16/plexus-16.pom#/artifact-0530-plexus-16.pom
#!RemoteAsset:  sha256:91526ee66327c7f50fbb25bd41bfcb916e284414b868e31d50a23004bd7deea7
Source631:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/17/plexus-17.pom#/artifact-0531-plexus-17.pom
#!RemoteAsset:  sha256:b43ee89c8890b9e5bc48d079fcb4c44f082b5139253356dc455806a33c3dd8fd
Source632:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/18/plexus-18.pom#/artifact-0532-plexus-18.pom
#!RemoteAsset:  sha256:8d3e51c3902fd7596e548eab121ebf6b0d4aa73857077f26a24fc86f9b8455b4
Source633:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/19/plexus-19.pom#/artifact-0533-plexus-19.pom
#!RemoteAsset:  sha256:e246e2a062b5d989fdefc521c9c56431ba5554ff8d2344edee9218a34a546a33
Source634:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.2/plexus-2.0.2.pom#/artifact-0534-plexus-2.0.2.pom
#!RemoteAsset:  sha256:72b31dc11351a5bf4f5841221be5b1afc2b802ff96f23f2b77838f6d46cd3ad5
Source635:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.5/plexus-2.0.5.pom#/artifact-0535-plexus-2.0.5.pom
#!RemoteAsset:  sha256:bea12e747708d25e73410ca1c731ebdfa102e8bdb6ec7d81bd4522583b234bcc
Source636:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.6/plexus-2.0.6.pom#/artifact-0536-plexus-2.0.6.pom
#!RemoteAsset:  sha256:a7b594b002fc791733c8e94470d09045f4fd69a93ad5c375752f2057f84633b4
Source637:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/20/plexus-20.pom#/artifact-0537-plexus-20.pom
#!RemoteAsset:  sha256:7728c57471730a6ec9e04654b60f37f57c01a2708e53aa6a0d7005aad29cbb10
Source638:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/23/plexus-23.pom#/artifact-0538-plexus-23.pom
#!RemoteAsset:  sha256:89a1bc79e46c35ab108b7e215bb2c5c215ff8f3af1ae3cfef82d9a2b33b06c51
Source639:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/24/plexus-24.pom#/artifact-0539-plexus-24.pom
#!RemoteAsset:  sha256:faa7947c2020967ad0c92b259ee9fa361d05e90cd036d17c37098bb1edaea3a3
Source640:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/25/plexus-25.pom#/artifact-0540-plexus-25.pom
#!RemoteAsset:  sha256:0a1b692d7fcc90d6a45dae2e50f4660d48f7a44504f174aa60ef34fbe1327f6a
Source641:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/4.0/plexus-4.0.pom#/artifact-0541-plexus-4.0.pom
#!RemoteAsset:  sha256:a343e44ff5796aed0ea60be11454c935ce20ab1c5f164acc8da574482dcbc7e9
Source642:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom#/artifact-0542-plexus-5.1.pom
#!RemoteAsset:  sha256:ffa349db04e7abf65885bdc5a2062f4197c0ff9d3f1f4e2aa5720b77233f742c
Source643:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/8/plexus-8.pom#/artifact-0543-plexus-8.pom
#!RemoteAsset:  sha256:4c07814ff4a39199999ae82bba1e38aa4f25637467fcac6a66ed63a76535799a
Source644:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.jar#/artifact-0544-plexus-archiver-4.10.0.jar
#!RemoteAsset:  sha256:93ca001fd33da53d38b74f6daf19e71bc9736ed6143091ff9003cd4c05ace6c9
Source645:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.pom#/artifact-0545-plexus-archiver-4.10.0.pom
#!RemoteAsset:  sha256:0ce7e5f325bb2153febdc5e599e5aabda28bbfb902245ac87951a13b44fce8ac
Source646:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.10.2/plexus-archiver-4.10.2.pom#/artifact-0546-plexus-archiver-4.10.2.pom
#!RemoteAsset:  sha256:1f39d4f2906a04f501567cd1211cef3fd95fea4cb979e1eba1d8dd84e4b67098
Source647:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.jar#/artifact-0547-plexus-archiver-4.10.4.jar
#!RemoteAsset:  sha256:53a2103d9257c801a8fc9c211d9fedea7e3ee1bf516bbbc28021ef45c1a219c5
Source648:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.pom#/artifact-0548-plexus-archiver-4.10.4.pom
#!RemoteAsset:  sha256:d24c3ca2185009d81b1ce3ee90cff1cfeab53b70fadbb3ae0c02a867d7c96034
Source649:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.jar#/artifact-0549-plexus-archiver-4.11.0.jar
#!RemoteAsset:  sha256:22a5a7c25e445560604cb0e1e5cc3d3af2669a0549c3d7db8265dcf8d8ebb4e3
Source650:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.pom#/artifact-0550-plexus-archiver-4.11.0.pom
#!RemoteAsset:  sha256:7b4a569c92f60c859ae69594f8935d11bcbb940d86c518742c30f0925a48ba9f
Source651:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-archiver/4.9.2/plexus-archiver-4.9.2.pom#/artifact-0551-plexus-archiver-4.9.2.pom
#!RemoteAsset:  sha256:570ae55a95e1887c3004882d30dc4e9035d2a46ba8d58b991de04175f141d88f
Source652:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.jar#/artifact-0552-plexus-build-api-1.2.0.jar
#!RemoteAsset:  sha256:47c7b0e65718ca89df6fdf5cb3f24a49e076cacd9499236c7e18ad78e993cddb
Source653:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.pom#/artifact-0553-plexus-build-api-1.2.0.pom
#!RemoteAsset:  sha256:9a7f1b5c5a9effd61eadfd8731452a2f76a8e79111fac391ef75ea801bea203a
Source654:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.jar#/artifact-0554-plexus-cipher-2.0.jar
#!RemoteAsset:  sha256:04842f331b0225b85a5e20439710d228ea7a6302abe6d53c9c9846fbc5bf99ff
Source655:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.pom#/artifact-0555-plexus-cipher-2.0.pom
#!RemoteAsset:  sha256:8971f135490070bc5fde7413fcc8db7c997fda4bebfb5c31185900d66edcbbb2
Source656:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.11.0/plexus-classworlds-2.11.0.jar#/artifact-0556-plexus-classworlds-2.11.0.jar
#!RemoteAsset:  sha256:281d317bf8a5fe818708cdd00e377dd234ec949f498d30f4b363f6b9771e1fa2
Source657:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.11.0/plexus-classworlds-2.11.0.pom#/artifact-0557-plexus-classworlds-2.11.0.pom
#!RemoteAsset:  sha256:a2d14b6752e30a100a6cb03c040d0160b71b61928daf8ea97cabfb4a3335b213
Source658:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.pom#/artifact-0558-plexus-classworlds-2.2.3.pom
#!RemoteAsset:  sha256:52f77c5ec49f787c9c417ebed5d6efd9922f44a202f217376e4f94c0d74f3549
Source659:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar#/artifact-0559-plexus-classworlds-2.6.0.jar
#!RemoteAsset:  sha256:469a6c59f92effa62c0797ce7d52d2c03cf8ee1034b923c360dd78a9f505a7ba
Source660:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom#/artifact-0560-plexus-classworlds-2.6.0.pom
#!RemoteAsset:  sha256:53124330e5e1b45d1ef6eff5e41c4d4defe04403e5c894795b44269515b6611e
Source661:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler/2.16.2/plexus-compiler-2.16.2.pom#/artifact-0561-plexus-compiler-2.16.2.pom
#!RemoteAsset:  sha256:db34d13c8d688063a946922f4de448c909ba43fec355ea15514495f33072b031
Source662:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.16.2/plexus-compiler-api-2.16.2.jar#/artifact-0562-plexus-compiler-api-2.16.2.jar
#!RemoteAsset:  sha256:ae7ca19e5a3bafdf92a403edf8af5876c746024424059c719b1544de48384ff8
Source663:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.16.2/plexus-compiler-api-2.16.2.pom#/artifact-0563-plexus-compiler-api-2.16.2.pom
#!RemoteAsset:  sha256:e48141c146d6cb96619aafb07b2e10e1ac08f339e96ae4067ddd9c2d0f626672
Source664:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.16.2/plexus-compiler-javac-2.16.2.jar#/artifact-0564-plexus-compiler-javac-2.16.2.jar
#!RemoteAsset:  sha256:b648754e6d99b381f7fc40328849c6f24d454263c03cf89c737d7c29831eb208
Source665:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.16.2/plexus-compiler-javac-2.16.2.pom#/artifact-0565-plexus-compiler-javac-2.16.2.pom
#!RemoteAsset:  sha256:99630ac196571a2754baa143a12723795b13020631902a6dff18dfb997e59b0e
Source666:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.16.2/plexus-compiler-manager-2.16.2.jar#/artifact-0566-plexus-compiler-manager-2.16.2.jar
#!RemoteAsset:  sha256:ba8d233dd73fc97c10f84bf23ef8f632cd19ced0f85dc335be2bdcb8e28e7bd0
Source667:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.16.2/plexus-compiler-manager-2.16.2.pom#/artifact-0567-plexus-compiler-manager-2.16.2.pom
#!RemoteAsset:  sha256:835e6a3f53ed9f39d14a0fd2b367a47fde78698115464eddba4b5c5d9fd1250f
Source668:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compilers/2.16.2/plexus-compilers-2.16.2.pom#/artifact-0568-plexus-compilers-2.16.2.pom
#!RemoteAsset:  sha256:0124227bc47efc9a00b9aa4fc3ef7f70823d322213c26489e5369a914339c84a
Source669:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.4/plexus-component-annotations-1.5.4.pom#/artifact-0569-plexus-component-annotations-1.5.4.pom
#!RemoteAsset:  sha256:405eef6fc9188241ec88579c3e473f5c8997455c69bcd62e142492aca15106bc
Source670:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.jar#/artifact-0570-plexus-component-annotations-2.0.0.jar
#!RemoteAsset:  sha256:dcf193612b315713771e267b42de2d44de090be5945b2577345ed5ab8de2d271
Source671:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.pom#/artifact-0571-plexus-component-annotations-2.0.0.pom
#!RemoteAsset:  sha256:bde3617ce9b5bcf9584126046080043af6a4b3baea40a3b153f02e7bbc32acac
Source672:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.jar#/artifact-0572-plexus-component-annotations-2.1.0.jar
#!RemoteAsset:  sha256:0670b605255f7dc9a454daaec7912918ccf1b5475cbfca374363b51fcfd4ea00
Source673:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.pom#/artifact-0573-plexus-component-annotations-2.1.0.pom
#!RemoteAsset:  sha256:50edb93c73786e62822b4fe1336e22880fdf147191373cf5c911370e16748fcf
Source674:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.jar#/artifact-0574-plexus-component-annotations-2.2.0.jar
#!RemoteAsset:  sha256:c5483fc9c8e1a7ef6b0f899e37aaa6ce2f8afae54955bfa559fd63a33dbb065b
Source675:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.pom#/artifact-0575-plexus-component-annotations-2.2.0.pom
#!RemoteAsset:  sha256:e70deff19306932ca60416bd3246d699a71a2827aeac437704cc9c7ebc61ea9f
Source676:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.jar#/artifact-0576-plexus-component-metadata-2.2.0.jar
#!RemoteAsset:  sha256:c9646f8e148af1da83cefc7281cf12d190a0bacb5075dc26747202964c81bf90
Source677:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.pom#/artifact-0577-plexus-component-metadata-2.2.0.pom
#!RemoteAsset:  sha256:a854365061c28821ddf1a520b8a197991613fd1d56f50f42c468b789b4714f20
Source678:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.1.12/plexus-components-1.1.12.pom#/artifact-0578-plexus-components-1.1.12.pom
#!RemoteAsset:  sha256:1a5c0f95f65ed3e98edcf4f3b27c21cbcb14567384d9e4cf07f83a49675347ed
Source679:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/4.0/plexus-components-4.0.pom#/artifact-0579-plexus-components-4.0.pom
#!RemoteAsset:  sha256:8b8c20e630bdcc795cc985024c4c1045c147be116052c2c975e30c608f7f3b45
Source680:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-container-default/2.1.0/plexus-container-default-2.1.0.pom#/artifact-0580-plexus-container-default-2.1.0.pom
#!RemoteAsset:  sha256:18b4a1b0a65c0d6b7cf9cd48ee9f3467b6deb8ace4c1309522c184f94c4cfa2e
Source681:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.5.4/plexus-containers-1.5.4.pom#/artifact-0581-plexus-containers-1.5.4.pom
#!RemoteAsset:  sha256:be5e3f8e59edce852a0fdaef8caedb32f364bf13db654d15f98e17930e456487
Source682:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.0.0/plexus-containers-2.0.0.pom#/artifact-0582-plexus-containers-2.0.0.pom
#!RemoteAsset:  sha256:94d5aedb3c46023265396527cf8ce7fc944b7bd79e4ebab907386418eb5a08d7
Source683:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.1.0/plexus-containers-2.1.0.pom#/artifact-0583-plexus-containers-2.1.0.pom
#!RemoteAsset:  sha256:743f42d967d02826ee79f0601108e2deeb11dd3e6add24fc5f2758b1b68634ec
Source684:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.2.0/plexus-containers-2.2.0.pom#/artifact-0584-plexus-containers-2.2.0.pom
#!RemoteAsset:  sha256:b87f25b512ffafcafbf4a05ab943812e9c6915291370c6b46016eb3836886c41
Source685:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar#/artifact-0585-plexus-i18n-1.0-beta-10.jar
#!RemoteAsset:  sha256:4073a94aadf4d511d85bce597c09f8e9355a458ccbb07f2ed82f4c39303fe374
Source686:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.pom#/artifact-0586-plexus-i18n-1.0-beta-10.pom
#!RemoteAsset:  sha256:995c0792669a031c94d91960a5beb60e1516abcec17a104f9f47470b36e56e27
Source687:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.jar#/artifact-0587-plexus-i18n-1.1.0.jar
#!RemoteAsset:  sha256:4915a0a3683e9afad03db155ee85050396bbcdc240a83bf04aba58701b36d8ba
Source688:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.pom#/artifact-0588-plexus-i18n-1.1.0.pom
#!RemoteAsset:  sha256:b3b5412ce17889103ea564bcdfcf9fb3dfa540344ffeac6b538a73c9d7182662
Source689:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.jar#/artifact-0589-plexus-interpolation-1.26.jar
#!RemoteAsset:  sha256:e1c10b3a6335641eb74a668daa9ee86ae4ab06610174e59ba07c8c68042327f7
Source690:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.pom#/artifact-0590-plexus-interpolation-1.26.pom
#!RemoteAsset:  sha256:3fb4fb6143fdf964024c3cb738551524b9ea84e5c211cd660c559ad0703e5230
Source691:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.jar#/artifact-0591-plexus-interpolation-1.27.jar
#!RemoteAsset:  sha256:d54fbcbc4399e352322874a4128b9d28fe9fe1583f89ec361de242ea38d33f9b
Source692:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.pom#/artifact-0592-plexus-interpolation-1.27.pom
#!RemoteAsset:  sha256:ab2a8715570438a2e4164d85ad3e8d489eabc38ea5093c2eb8ab7f58403535b5
Source693:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.28/plexus-interpolation-1.28.jar#/artifact-0593-plexus-interpolation-1.28.jar
#!RemoteAsset:  sha256:0f4665c943df2692d75e28b6b24923ab18ff00369b8c7f5eba4bedef07e4ecd4
Source694:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.28/plexus-interpolation-1.28.pom#/artifact-0594-plexus-interpolation-1.28.pom
#!RemoteAsset:  sha256:088d444dbcedfb384630d8686697ece3c401d6f33c8f8b3aa7259ea1c6996878
Source695:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.jar#/artifact-0595-plexus-interpolation-1.29.jar
#!RemoteAsset:  sha256:ce0d5634297bb1e065dddfdc8a2a5675717c08e8f4783edcf581543711516938
Source696:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.pom#/artifact-0596-plexus-interpolation-1.29.pom
#!RemoteAsset:  sha256:aafc90ce29fe79bc6a0aeafb2bf6bdeaf979a1b8211493428a2290228170355d
Source697:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/3.4.2/plexus-io-3.4.2.pom#/artifact-0597-plexus-io-3.4.2.pom
#!RemoteAsset:  sha256:965ed28912cf1ae4c628112c4009e0c19819bc44ed5db8af54ee5eda21036a3e
Source698:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.jar#/artifact-0598-plexus-io-3.5.0.jar
#!RemoteAsset:  sha256:f5b86cd223a0bf4ba649de19e7e8e4e1f14344ff636f8b0024c89c46d28cc9d8
Source699:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.pom#/artifact-0599-plexus-io-3.5.0.pom
#!RemoteAsset:  sha256:f7a76d3a3bbeb53f5f36e19ee57ddc2099f3be1d599039090254d1f0fdf0b854
Source700:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/3.5.1/plexus-io-3.5.1.pom#/artifact-0600-plexus-io-3.5.1.pom
#!RemoteAsset:  sha256:fc0f3effea7514e4f214df1afb672f54c982e78e5ca3b32b34196c7d056a1aa4
Source701:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.jar#/artifact-0601-plexus-io-3.6.0.jar
#!RemoteAsset:  sha256:653432ed213573b6b209deb7346dc2ed89f20e647dbdb6fc868051b334b31d27
Source702:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.pom#/artifact-0602-plexus-io-3.6.0.pom
#!RemoteAsset:  sha256:1e6a4298e145c1e23af430b04ac53d76dc11077e0f3d36ef9c027ce790d96505
Source703:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.5.2/plexus-java-1.5.2.jar#/artifact-0603-plexus-java-1.5.2.jar
#!RemoteAsset:  sha256:9617b619010dbb95c237e35bff7ee1d336cbcfd9ff5c229a935a9e3587ff0c37
Source704:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.5.2/plexus-java-1.5.2.pom#/artifact-0604-plexus-java-1.5.2.pom
#!RemoteAsset:  sha256:9e7d29fc65089d69e75b559efaa5db8117dab3c579d0ef19759776d5643a492b
Source705:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-languages/1.5.2/plexus-languages-1.5.2.pom#/artifact-0605-plexus-languages-1.5.2.pom
#!RemoteAsset:  sha256:827baaa0215caedcdca59d091f04480566f7a43996183b9f9871fecff7abebea
Source706:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.jar#/artifact-0606-plexus-resources-1.3.0.jar
#!RemoteAsset:  sha256:e99efc42e01c1a01f2a207e36b8997473406d2cf11b4caab740c553e8a7fcf74
Source707:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.pom#/artifact-0607-plexus-resources-1.3.0.pom
#!RemoteAsset:  sha256:873139960c4c780176dda580b003a2c4bf82188bdce5bb99234e224ef7acfceb
Source708:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.jar#/artifact-0608-plexus-sec-dispatcher-2.0.jar
#!RemoteAsset:  sha256:9b28bb307017938a94d06c85b2b099bc46912b859d084fb293e569f432eadb7c
Source709:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.pom#/artifact-0609-plexus-sec-dispatcher-2.0.pom
#!RemoteAsset:  sha256:205acf1ab0a8294f90df6dd99b746ace54ba8c5ce673ca0a093aeadfe8461de2
Source710:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.jar#/artifact-0610-plexus-testing-2.1.0.jar
#!RemoteAsset:  sha256:7827298f18f1c4804c0100b255568fa8b0070b2a63b62e4c70941ff29d5ddb7d
Source711:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.pom#/artifact-0611-plexus-testing-2.1.0.pom
#!RemoteAsset:  sha256:687d05a9521ecb8e319e6beb46abcf53e0e61be647f1c7642a86e22f46814336
Source712:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.4.5/plexus-utils-1.4.5.pom#/artifact-0612-plexus-utils-1.4.5.pom
#!RemoteAsset:  sha256:12a3c9a32b82fdc95223cab1f9d344e14ef3e396da14c4d0013451646f3280e7
Source713:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/1.5.15/plexus-utils-1.5.15.pom#/artifact-0613-plexus-utils-1.5.15.pom
#!RemoteAsset:  sha256:2896dbf57e8c82121481400e8be4df6110edd37e346a6c144b3156f24bf98f72
Source714:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/2.0.4/plexus-utils-2.0.4.pom#/artifact-0614-plexus-utils-2.0.4.pom
#!RemoteAsset:  sha256:6e9ef6a42b78c418176d07882762f53664bc39bac88135be8cb56337c050e6dd
Source715:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.1.1/plexus-utils-3.1.1.pom#/artifact-0615-plexus-utils-3.1.1.pom
#!RemoteAsset:  sha256:79c9792073fdee3cdbebd61a76ba8c2dd11624a9f85d128bae56bda19e20475c
Source716:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.3.0/plexus-utils-3.3.0.pom#/artifact-0616-plexus-utils-3.3.0.pom
#!RemoteAsset:  sha256:86e0255d4c879c61b4833ed7f13124e8bb679df47debb127326e7db7dd49a07b
Source717:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar#/artifact-0617-plexus-utils-3.5.1.jar
#!RemoteAsset:  sha256:94ff68edeb48204d12c99189c767164d3a9f778a1372d1dce11a41462e6236f2
Source718:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom#/artifact-0618-plexus-utils-3.5.1.pom
#!RemoteAsset:  sha256:27ef130e32c236090e408fb5498d94cb9ea26d14070fb1c8985d607b62d098d1
Source719:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.jar#/artifact-0619-plexus-utils-3.6.0.jar
#!RemoteAsset:  sha256:6138300481471c7fe6aeb115f912961f886e1a46ee9c2bd2841b65184824da28
Source720:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.pom#/artifact-0620-plexus-utils-3.6.0.pom
#!RemoteAsset:  sha256:05a63effd67e2d6b9d610cc82e2bd7473289d34802e57a529b28110f28af5679
Source721:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.6.1/plexus-utils-3.6.1.jar#/artifact-0621-plexus-utils-3.6.1.jar
#!RemoteAsset:  sha256:c8397373781af640a76c5da88f1674293b4fc9a2391d0768ee3fc791883b040d
Source722:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.6.1/plexus-utils-3.6.1.pom#/artifact-0622-plexus-utils-3.6.1.pom
#!RemoteAsset:  sha256:96b9cc44439191d2d0635974e2d44e768736b4fb2abcb65f94cd95e41912fa8b
Source723:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.jar#/artifact-0623-plexus-utils-4.0.1.jar
#!RemoteAsset:  sha256:bc4235a95cd1ebae42644c81ebba9c1d4c52565f81e96ab204b6e56e3e378cc1
Source724:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.pom#/artifact-0624-plexus-utils-4.0.1.pom
#!RemoteAsset:  sha256:8957274e75fe2c278b1428dd16a0daeee1dd38152cb6eff816177ac28fccb697
Source725:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.jar#/artifact-0625-plexus-utils-4.0.2.jar
#!RemoteAsset:  sha256:5151c13bdd7cc3a5569583a7f4267392f013ffd3115eab8db5f86de420a366af
Source726:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.pom#/artifact-0626-plexus-utils-4.0.2.pom
#!RemoteAsset:  sha256:b4c4a0dbeacad54306a1ae230eff5ab45d58e3ab88c86ab7245d3a0772be57ab
Source727:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.jar#/artifact-0627-plexus-velocity-1.2.jar
#!RemoteAsset:  sha256:508a1682a95da8220e9bd582e2a9e1629d016cfe67c4769ee0b1755279ff5fd6
Source728:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.pom#/artifact-0628-plexus-velocity-1.2.pom
#!RemoteAsset:  sha256:3e7e902f492c973cf210ddb8267843a3b65e83f5067467e2f4d9af0051f6b8b9
Source729:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.jar#/artifact-0629-plexus-velocity-2.2.0.jar
#!RemoteAsset:  sha256:6f6a9b05f40e8e84af4aa9576f6b1e435ded6d5b56931b2a269b697bf72ce49d
Source730:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.pom#/artifact-0630-plexus-velocity-2.2.0.pom
#!RemoteAsset:  sha256:c1a510a87a62bd2d74ac1472dd31c3f9e9b0b8b8568f37d77c0f135415bebd05
Source731:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.jar#/artifact-0631-plexus-xml-3.0.1.jar
#!RemoteAsset:  sha256:3242ddc20873f71b381c333b22afb9cf3596d6a63b6683036a16bd51bc8721a4
Source732:      https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.pom#/artifact-0632-plexus-xml-3.0.1.pom
#!RemoteAsset:  sha256:4e7d8329d8da7dcf30779d824241be145f27108932f5a5a24eb907677bc8d72d
Source733:      https://repo.maven.apache.org/maven2/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom#/artifact-0633-project-1.0.6.pom
#!RemoteAsset:  sha256:1cbd7a965a5e2a9ea823bab311962a4e5aa5c240705bdbad5a52b40ffdfa1004
Source734:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M4/org.eclipse.sisu.inject-0.9.0.M4.jar#/artifact-0634-org.eclipse.sisu.inject-0.9.0.M4.jar
#!RemoteAsset:  sha256:33966b3abd12908001b707688dfb7c09908b1e86556dc3fac1e85122a686f059
Source735:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M4/org.eclipse.sisu.inject-0.9.0.M4.pom#/artifact-0635-org.eclipse.sisu.inject-0.9.0.M4.pom
#!RemoteAsset:  sha256:3ab8d7bfe68f3b6ec95c1a0a47e628edbc9d76e90634cb0a0ba121fbb11b8e42
Source736:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.jar#/artifact-0636-org.eclipse.sisu.inject-1.0.0.jar
#!RemoteAsset:  sha256:ea0fb93dafec8adde218ce2a11f0f84ebec2b822c1d9be8b2ed9cd61ed654cf3
Source737:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.pom#/artifact-0637-org.eclipse.sisu.inject-1.0.0.pom
#!RemoteAsset:  sha256:b90579bc652eac7331436e0a25533fce14130b9c6e015f2dd3a3d4bb07e942b7
Source738:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.jar#/artifact-0638-org.eclipse.sisu.plexus-0.9.0.M4.jar
#!RemoteAsset:  sha256:90b4be7a71c979d0c4dea20c20a28eb9e76a29df68ab9018cf011019a3e4f562
Source739:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.pom#/artifact-0639-org.eclipse.sisu.plexus-0.9.0.M4.pom
#!RemoteAsset:  sha256:865b5300034fc08c790215d7d97f141914c932191bef9338a7dcef589f7536e9
Source740:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.jar#/artifact-0640-org.eclipse.sisu.plexus-1.0.0.jar
#!RemoteAsset:  sha256:f9bd338be70d4bc4d8f3f10cdfab7baec089fd3b3ef1013d4ca64c4e7f2163d5
Source741:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.pom#/artifact-0641-org.eclipse.sisu.plexus-1.0.0.pom
#!RemoteAsset:  sha256:0c829c9641ccac870d7d7ff012cbbad8447e912eb9a26d0d7283f09cba44c0d9
Source742:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-inject/0.9.0.M4/sisu-inject-0.9.0.M4.pom#/artifact-0642-sisu-inject-0.9.0.M4.pom
#!RemoteAsset:  sha256:98656aa9a4841078ac7efde2ae7fdaa87724c1f504afea7a4151acd3ed066fc2
Source743:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-inject/1.0.0/sisu-inject-1.0.0.pom#/artifact-0643-sisu-inject-1.0.0.pom
#!RemoteAsset:  sha256:1c8601d32cdb0e9874618d8aa5e0b5d354e4b611978fa81538414e9708f5d543
Source744:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-maven-plugin/1.0.0/sisu-maven-plugin-1.0.0.jar#/artifact-0644-sisu-maven-plugin-1.0.0.jar
#!RemoteAsset:  sha256:f8fbe42faeb53523a152b46976932d28f4a0cc68324190f7062cca85765447c2
Source745:      https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-maven-plugin/1.0.0/sisu-maven-plugin-1.0.0.pom#/artifact-0645-sisu-maven-plugin-1.0.0.pom
#!RemoteAsset:  sha256:c40d960daadcef7b01c1b1c6657afbac4fffb5e53168f8fcb0b28b84e6fdcca1
Source746:      https://repo.maven.apache.org/maven2/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom#/artifact-0646-fusesource-pom-1.12.pom
#!RemoteAsset:  sha256:ec168cf31c4c3849348dfff7a04e90170615f7784f1255ee6747b98a854c04c5
Source747:      https://repo.maven.apache.org/maven2/org/fusesource/jansi/jansi/2.4.3/jansi-2.4.3.jar#/artifact-0647-jansi-2.4.3.jar
#!RemoteAsset:  sha256:97229ddcd9aa86eee77bc4e62f47cec630be9edebf6cedfb29716aedf1317710
Source748:      https://repo.maven.apache.org/maven2/org/fusesource/jansi/jansi/2.4.3/jansi-2.4.3.pom#/artifact-0648-jansi-2.4.3.pom
#!RemoteAsset:  sha256:5d66b6a4a680755cb6ed7cb104fa7835ef644667586ff0737adeb977c39ecdbc
Source749:      https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest/3.0/hamcrest-3.0.jar#/artifact-0649-hamcrest-3.0.jar
#!RemoteAsset:  sha256:4a04a68133bf32461f47b8a53c8ee9df4ce2f49a0dad9794bce8717bee5bac31
Source750:      https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest/3.0/hamcrest-3.0.pom#/artifact-0650-hamcrest-3.0.pom
#!RemoteAsset:  sha256:a709ce17111e4149d9b79a5295644e0cd5a8355aec4b2ef4c0436aba7b25d08a
Source751:      https://repo.maven.apache.org/maven2/org/iq80/snappy/snappy/0.4/snappy-0.4.pom#/artifact-0651-snappy-0.4.pom
#!RemoteAsset:  sha256:0b20f45e3a0fd8f0d12cdc5316b06776e902b1365db00118876f9175c60f302c
Source752:      https://repo.maven.apache.org/maven2/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.jar#/artifact-0652-jdom2-2.0.6.1.jar
#!RemoteAsset:  sha256:55795e1018b8ae647b937967cf810a99b08582c2374e7873c128734c8c914bf3
Source753:      https://repo.maven.apache.org/maven2/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.pom#/artifact-0653-jdom2-2.0.6.1.pom
#!RemoteAsset:  sha256:cfd3298d8720cddfb0545109ccc6ea0ef39eff7e9c40a10ad95c93a65f01c916
Source754:      https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.22.1/jsoup-1.22.1.jar#/artifact-0654-jsoup-1.22.1.jar
#!RemoteAsset:  sha256:89c4213d6152a2699408caa440af5050a899073c82ba2df37a2f5f5eeda8e160
Source755:      https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.22.1/jsoup-1.22.1.pom#/artifact-0655-jsoup-1.22.1.pom
#!RemoteAsset:  sha256:1fad6e6be7557781e4d33729d49ae1cdc8fdda6fe477bb0cc68ce351eafdfbab
Source756:      https://repo.maven.apache.org/maven2/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.jar#/artifact-0656-jspecify-1.0.0.jar
#!RemoteAsset:  sha256:cdab929a3b95211f43d2090c5e2d0dfe8465960e378bc32b35841dab324433a6
Source757:      https://repo.maven.apache.org/maven2/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.pom#/artifact-0657-jspecify-1.0.0.pom
#!RemoteAsset:  sha256:e006dd8894f9fc7b75fc32bb12fe5ed8be65667d5b454f99e2e0b8c5bb8d30b3
Source758:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom#/artifact-0658-junit-bom-5.10.0.pom
#!RemoteAsset:  sha256:21c4b0286f4b20069577ff4b20978a85c100ac8a46b6f1c8672fbaab337bc3f2
Source759:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom#/artifact-0659-junit-bom-5.10.1.pom
#!RemoteAsset:  sha256:169dd904a4b0f6520cffe658cc62292bfe9f3c14a989fa92120724cde43a9968
Source760:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom#/artifact-0660-junit-bom-5.10.2.pom
#!RemoteAsset:  sha256:10937d44c425984cb8739225d34712e1a3145641ca93ac3f7ef186fa25f6babc
Source761:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.3/junit-bom-5.10.3.pom#/artifact-0661-junit-bom-5.10.3.pom
#!RemoteAsset:  sha256:e67459d4882424ac6374f40db1c8f4a2e88946b340ba072c80be932a2be4644d
Source762:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom#/artifact-0662-junit-bom-5.11.0.pom
#!RemoteAsset:  sha256:c72124a9c9a79910c1858766b72c350e1a39244cbfb4b076348fbfe078281965
Source763:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.1/junit-bom-5.11.1.pom#/artifact-0663-junit-bom-5.11.1.pom
#!RemoteAsset:  sha256:f48e88538aac145eb3ae0345a9ebd055b28f329a35dce8d1e9281325ca9b0ea2
Source764:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.2/junit-bom-5.11.2.pom#/artifact-0664-junit-bom-5.11.2.pom
#!RemoteAsset:  sha256:19d4b747b204805325b6334553296f986562277a4ac1cb5e593a5e4c4f5e4115
Source765:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom#/artifact-0665-junit-bom-5.11.4.pom
#!RemoteAsset:  sha256:7c826bc72beddc817dad9263027f9012a0f55a377d38df89c42932a2501c2bf0
Source766:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.12.1/junit-bom-5.12.1.pom#/artifact-0666-junit-bom-5.12.1.pom
#!RemoteAsset:  sha256:cef80fec86454f6806bfb0df24669b5c6f32e2cb728539ea859f47dfdc9bbc17
Source767:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.12.2/junit-bom-5.12.2.pom#/artifact-0667-junit-bom-5.12.2.pom
#!RemoteAsset:  sha256:d48f54bc0598dab0e91a0d975c7d7c954666eac4fee63941876e3f92ea1e59c6
Source768:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.0/junit-bom-5.13.0.pom#/artifact-0668-junit-bom-5.13.0.pom
#!RemoteAsset:  sha256:fa68451ea830572ed43ffe51d75b6a05f7a5e665a602a51f49d6be02063a65f3
Source769:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom#/artifact-0669-junit-bom-5.13.1.pom
#!RemoteAsset:  sha256:d7a08a99b2502f0bb68cd4e1f984f0bf69324aaa208bd0f73366c03fc3548a42
Source770:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom#/artifact-0670-junit-bom-5.13.4.pom
#!RemoteAsset:  sha256:01b01dfa366550b40ac5760548a7d728b6109d17c451e83864d1e5e0ce862c94
Source771:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.14.1/junit-bom-5.14.1.pom#/artifact-0671-junit-bom-5.14.1.pom
#!RemoteAsset:  sha256:ed2dcc7855bd460bccc93a1bf0c962e63b566ff7d8f1ded0f1f2593ba8183aaf
Source772:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.14.2/junit-bom-5.14.2.pom#/artifact-0672-junit-bom-5.14.2.pom
#!RemoteAsset:  sha256:08a02856e487c9357f9b29e38745f8ae805848111e72d15aad0352338f1632e1
Source773:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.14.3/junit-bom-5.14.3.pom#/artifact-0673-junit-bom-5.14.3.pom
#!RemoteAsset:  sha256:5706e8f29a0a07f56efbbea4a0670793414194bb8d24d8143ba1e787a2f32856
Source774:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.14.4/junit-bom-5.14.4.pom#/artifact-0674-junit-bom-5.14.4.pom
#!RemoteAsset:  sha256:cd14aaa869991f82021c585d570d31ff342bcba58bb44233b70193771b96487b
Source775:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom#/artifact-0675-junit-bom-5.7.2.pom
#!RemoteAsset:  sha256:77144432ffc68bd98a790ab1069619d91032cfc0e4e13c08163aa03da36fd6e2
Source776:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.8.0-M1/junit-bom-5.8.0-M1.pom#/artifact-0676-junit-bom-5.8.0-M1.pom
#!RemoteAsset:  sha256:4d0329cd9e72f2420e5ca15724cbfe6ffa6e5fd2888361516271190fdc342ed7
Source777:      https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom#/artifact-0677-junit-bom-5.9.3.pom
#!RemoteAsset:  sha256:aa1ae085fd92dfdbf85d867e60e59adc599bac183b46fc7e0698198bf426ad3f
Source778:      https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.jar#/artifact-0678-junit-jupiter-api-5.14.4.jar
#!RemoteAsset:  sha256:4c175189fd774dcd90cb23cfcab2ce9dbf2f5d0a16d7ef3702e7cfcd6411a762
Source779:      https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.pom#/artifact-0679-junit-jupiter-api-5.14.4.pom
#!RemoteAsset:  sha256:e1e35cf651ae1635638d431ea4412d5c65938be54150444f07ba659586042b11
Source780:      https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.jar#/artifact-0680-junit-jupiter-engine-5.14.4.jar
#!RemoteAsset:  sha256:12329741c655ff5010a3d4758bb34b98e57ac8f971a6fa0fb872c6d60ab87e84
Source781:      https://repo.maven.apache.org/maven2/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.pom#/artifact-0681-junit-jupiter-engine-5.14.4.pom
#!RemoteAsset:  sha256:e683a01e85dfabea520c056ac6015a6162756e602ec653c0da85e233f0afbc18
Source782:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.12.2/junit-platform-commons-1.12.2.jar#/artifact-0682-junit-platform-commons-1.12.2.jar
#!RemoteAsset:  sha256:4f2b8a9065c909c6892d8622d553b6ab0a70321624499e3b69c1289f59ecc077
Source783:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.12.2/junit-platform-commons-1.12.2.pom#/artifact-0683-junit-platform-commons-1.12.2.pom
#!RemoteAsset:  sha256:55c8a0c069ac1bc4e1f8bbb26b5eae95cbd10e4ff1b23248441ab61a607381e1
Source784:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.jar#/artifact-0684-junit-platform-commons-1.14.4.jar
#!RemoteAsset:  sha256:d77be81708cf9836db7a09908e6d9e4d94c527e090bd594cc4af06711b9d853d
Source785:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.pom#/artifact-0685-junit-platform-commons-1.14.4.pom
#!RemoteAsset:  sha256:cef0efcb5bd2e05e2b808d38bab5c655089c0c3001527376e74cb606a7911ec8
Source786:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.12.2/junit-platform-engine-1.12.2.jar#/artifact-0686-junit-platform-engine-1.12.2.jar
#!RemoteAsset:  sha256:9480b18a7965769d0083c2cb71105423f5302a8f046bb2047e6dbff09f383490
Source787:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.12.2/junit-platform-engine-1.12.2.pom#/artifact-0687-junit-platform-engine-1.12.2.pom
#!RemoteAsset:  sha256:3c7f3f84a6747aef0db6bd5fdd2a6c8fe37132e653c939bd67387377af66d91c
Source788:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.jar#/artifact-0688-junit-platform-engine-1.14.4.jar
#!RemoteAsset:  sha256:180af15472ac69c91902fbbd210566e78a82fd6d34e63d3fbada687f51614e64
Source789:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.pom#/artifact-0689-junit-platform-engine-1.14.4.pom
#!RemoteAsset:  sha256:dccf2c1fa0a977c53ad094ad859bfdddd524d97594b76307ad787de71985757f
Source790:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.12.2/junit-platform-launcher-1.12.2.jar#/artifact-0690-junit-platform-launcher-1.12.2.jar
#!RemoteAsset:  sha256:619145cd215d32225372be625bba28683d74142fee1a5dfdb1c64b52fe9c0b51
Source791:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.12.2/junit-platform-launcher-1.12.2.pom#/artifact-0691-junit-platform-launcher-1.12.2.pom
#!RemoteAsset:  sha256:768d62f1b2a523713b702db53609c230af62bbd645fc2c07a7d794df4da32228
Source792:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.jar#/artifact-0692-junit-platform-launcher-1.14.4.jar
#!RemoteAsset:  sha256:1197a74ac2b4d71172f56cb9c4b09e54c001e6ae89f46a7873b38c6e6b608bd5
Source793:      https://repo.maven.apache.org/maven2/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.pom#/artifact-0693-junit-platform-launcher-1.14.4.pom
#!RemoteAsset:  sha256:4b909690cab288c761eb94c0bf0e814496cf3921d8affac84cd87774530351e5
Source794:      https://repo.maven.apache.org/maven2/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar#/artifact-0694-mockito-core-4.11.0.jar
#!RemoteAsset:  sha256:2bc2e3c8c8b313fdac231f23822225b07831dc899d067072f49d5f8ae37e739a
Source795:      https://repo.maven.apache.org/maven2/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.pom#/artifact-0695-mockito-core-4.11.0.pom
#!RemoteAsset:  sha256:7a8ff780b9ff48415d7c705f60030b0acaa616e7f823c98eede3b63508d4e984
Source796:      https://repo.maven.apache.org/maven2/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar#/artifact-0696-objenesis-3.0.1.jar
#!RemoteAsset:  sha256:3dc1377e570974e6f182a6a1680d3284335b5d5cf3a8fea7bec1a5438bbdaff8
Source797:      https://repo.maven.apache.org/maven2/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom#/artifact-0697-objenesis-3.0.1.pom
#!RemoteAsset:  sha256:02dfd0b0439a5591e35b708ed2f5474eb0948f53abf74637e959b8e4ef69bfeb
Source798:      https://repo.maven.apache.org/maven2/org/objenesis/objenesis/3.3/objenesis-3.3.jar#/artifact-0698-objenesis-3.3.jar
#!RemoteAsset:  sha256:ba0c40da2669a048b6e24ef7066a471f0fbcbfcc509e6a3e856ca4ddfa614ad3
Source799:      https://repo.maven.apache.org/maven2/org/objenesis/objenesis/3.3/objenesis-3.3.pom#/artifact-0699-objenesis-3.3.pom
#!RemoteAsset:  sha256:53372dbe8ec3814370937a87c03b42b70facb5ba570f99f89c126937d1d8bbcf
Source800:      https://repo.maven.apache.org/maven2/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom#/artifact-0700-objenesis-parent-3.0.1.pom
#!RemoteAsset:  sha256:305c384aa2f1e1c7fe53a96da41c3ec35243b97d428d24a8f779818cc10be4ff
Source801:      https://repo.maven.apache.org/maven2/org/objenesis/objenesis-parent/3.3/objenesis-parent-3.3.pom#/artifact-0701-objenesis-parent-3.3.pom
#!RemoteAsset:  sha256:48e2df636cab6563ced64dcdff8abb2355627cb236ef0bf37598682ddf742f1b
Source802:      https://repo.maven.apache.org/maven2/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.jar#/artifact-0702-opentest4j-1.3.0.jar
#!RemoteAsset:  sha256:9bf7cffc410f3e8372c2522578df9ca56d9d43bd937e30948706c232a943b355
Source803:      https://repo.maven.apache.org/maven2/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.pom#/artifact-0703-opentest4j-1.3.0.pom
#!RemoteAsset:  sha256:3c6fac2424db3d4a853b669f4e3d1d9c3c552235e19a319673f887083c2303a1
Source804:      https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.6/asm-9.6.jar#/artifact-0704-asm-9.6.jar
#!RemoteAsset:  sha256:92eee24bc3c843e4881d46c1dd6505471ee3142facfb466b428cfea5a56c6b60
Source805:      https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.6/asm-9.6.pom#/artifact-0705-asm-9.6.pom
#!RemoteAsset:  sha256:c1367c3bb383d7619e7f797e38df7513885f2eef04ae7b5908f68222657b5baa
Source806:      https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.8/asm-9.8.pom#/artifact-0706-asm-9.8.pom
#!RemoteAsset:  sha256:6f3828a215c920059a5efa2fb55c233d6c54ec5cadca99ce1b1bdd10077c7ddd
Source807:      https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar#/artifact-0707-asm-9.9.1.jar
#!RemoteAsset:  sha256:aca68dee9ba2f6cd90ffde728efdc7e3ebfcf59f3f41fbfe248d2d01d5b866af
Source808:      https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom#/artifact-0708-asm-9.9.1.pom
#!RemoteAsset:  sha256:321ddbb7ee6fe4f53dea6b4cd6db74154d6bfa42391c1f763b361b9f485acf05
Source809:      https://repo.maven.apache.org/maven2/org/ow2/ow2/1.5.1/ow2-1.5.1.pom#/artifact-0709-ow2-1.5.1.pom
#!RemoteAsset:  sha256:a1374bd368b52b54b252d5281b9391363b58cb667a6375242fd6a3f482bc8c23
Source810:      https://repo.maven.apache.org/maven2/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.jar#/artifact-0710-powermock-reflect-2.0.9.jar
#!RemoteAsset:  sha256:316ff63f5b09e3e240a4d4e1cafeb7fcfb27208ccabaaf17fee8a455e8654a24
Source811:      https://repo.maven.apache.org/maven2/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.pom#/artifact-0711-powermock-reflect-2.0.9.pom
#!RemoteAsset:  sha256:ab57ca8fd223772c17365d121f59e94ecbf0ae59d08c03a3cb5b81071c019195
Source812:      https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/1.7.36/jcl-over-slf4j-1.7.36.jar#/artifact-0712-jcl-over-slf4j-1.7.36.jar
#!RemoteAsset:  sha256:bd96243d7d4218cd7cc7d45c0e30fa13480a1a4f91d356edd7dfe93f1ffb68e6
Source813:      https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/1.7.36/jcl-over-slf4j-1.7.36.pom#/artifact-0713-jcl-over-slf4j-1.7.36.pom
#!RemoteAsset:  sha256:7e0747751e9b67e19dcb5206f04ea22cc03d250c422426402eadd03513f2c314
Source814:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom#/artifact-0714-slf4j-api-1.7.30.pom
#!RemoteAsset:  sha256:d3ef575e3e4979678dc01bf1dcce51021493b4d11fb7f1be8ad982877c16a1c0
Source815:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar#/artifact-0715-slf4j-api-1.7.36.jar
#!RemoteAsset:  sha256:fb046a9c229437928bb11c2d27c8b5d773eb8a25e60cbd253d985210dedc2684
Source816:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom#/artifact-0716-slf4j-api-1.7.36.pom
#!RemoteAsset:  sha256:afaf8e74019b230d3f56fdd7c93fb1070c0dca34f3d2d5ab5dea9fc616bd5ca4
Source817:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.pom#/artifact-0717-slf4j-api-1.7.5.pom
#!RemoteAsset:  sha256:c214958b07816cb4412b30c7bdbd4308ffdc6ba2a83767b8f3a9229cbd9274d6
Source818:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.jar#/artifact-0718-slf4j-nop-1.7.36.jar
#!RemoteAsset:  sha256:20a0f7c060020d75fef4470ae6948661d418ebd5ea4549c68abedf20ee86cb65
Source819:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.pom#/artifact-0719-slf4j-nop-1.7.36.pom
#!RemoteAsset:  sha256:11647956e48a0c5bfb3ac33f6da7e83f341002b6857efd335a505b687be34b75
Source820:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom#/artifact-0720-slf4j-parent-1.7.30.pom
#!RemoteAsset:  sha256:bb388d37fbcdd3cde64c3cede21838693218dc451f04040c5df360a78ed7e812
Source821:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom#/artifact-0721-slf4j-parent-1.7.36.pom
#!RemoteAsset:  sha256:c43bc5a022dbfd9de82be232dffe46208cbc7de12c14385b5da824e331e535bb
Source822:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.5/slf4j-parent-1.7.5.pom#/artifact-0722-slf4j-parent-1.7.5.pom
#!RemoteAsset:  sha256:c11b4197b7100eb4c4986c93493d4230f1efccfc53f39fbdbb84573493722379
Source823:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36-sources.jar#/artifact-0723-slf4j-simple-1.7.36-sources.jar
#!RemoteAsset:  sha256:2f39bed943d624dfa8f4102d0571283a10870b6aa36f197a8a506f147010c10f
Source824:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36.jar#/artifact-0724-slf4j-simple-1.7.36.jar
#!RemoteAsset:  sha256:c56b80a0a6bea2a0463e70d0892ae338a9e507e486767a520453409812058d1b
Source825:      https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36.pom#/artifact-0725-slf4j-simple-1.7.36.pom
#!RemoteAsset:  sha256:c14fb9c32b59cc03251f609416db7c0cff01f811edcccb4f6a865d6e7046bd0b
Source826:      https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/10/forge-parent-10.pom#/artifact-0726-forge-parent-10.pom
#!RemoteAsset:  sha256:e56188aa8ce51278006aa90bc7e0f304a81e2f1219f462e7d21f262535cd2795
Source827:      https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/5/forge-parent-5.pom#/artifact-0727-forge-parent-5.pom
#!RemoteAsset:  sha256:9c5f7cd5226ac8c3798cb1f800c031f7dedc1606dc50dc29567877c8224459a7
Source828:      https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/6/forge-parent-6.pom#/artifact-0728-forge-parent-6.pom
#!RemoteAsset:  sha256:b51f8867c92b6a722499557fc3a1fdea77bdf9ef574722fe90ce436a29559454
Source829:      https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/7/oss-parent-7.pom#/artifact-0729-oss-parent-7.pom
#!RemoteAsset:  sha256:fb40265f982548212ff82e362e59732b2187ec6f0d80182885c14ef1f982827a
Source830:      https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/9/oss-parent-9.pom#/artifact-0730-oss-parent-9.pom
#!RemoteAsset:  sha256:934171640fbd3d2495c50b79b0d9adb11e2c83e65bad157df8fe34bcac0ff798
Source831:      https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar#/artifact-0731-plexus-build-api-0.0.7.jar
#!RemoteAsset:  sha256:e067317a47ed9e84b2ba85a76d3cf72980e2b0dc873a90b9cbfe74fe80c37c17
Source832:      https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom#/artifact-0732-plexus-build-api-0.0.7.pom
#!RemoteAsset:  sha256:d2ee7efbcdc82206c69559548aef86a99add95378f03cc58b4d9696b3969c8bb
Source833:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/inject/guice-bean/1.4.2/guice-bean-1.4.2.pom#/artifact-0733-guice-bean-1.4.2.pom
#!RemoteAsset:  sha256:13a66ca6e6ad1a186076513eea822db2c3c0e460a983a0a31f4d937de336ad98
Source834:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/inject/guice-plexus/1.4.2/guice-plexus-1.4.2.pom#/artifact-0734-guice-plexus-1.4.2.pom
#!RemoteAsset:  sha256:2b3f02f2d0ec3e95884f9ab415596ce627492469c2d8fd75e3fb00fb69532c44
Source835:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.pom#/artifact-0735-sisu-guice-2.1.7.pom
#!RemoteAsset:  sha256:a5991ead85259ba9f8c985d194aace3b069e14bcd8cde68fce928223714d3968
Source836:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-inject/1.4.2/sisu-inject-1.4.2.pom#/artifact-0736-sisu-inject-1.4.2.pom
#!RemoteAsset:  sha256:06d75dd6f2a0dc9ea6bf73a67491ba4790f92251c654bf4925511e5e4f48f1df
Source837:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-inject-bean/1.4.2/sisu-inject-bean-1.4.2.pom#/artifact-0737-sisu-inject-bean-1.4.2.pom
#!RemoteAsset:  sha256:e302200cf462cf1af9f3e870738253cdf90d7abc8279b9d3b507a5d0d3b9f289
Source838:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-inject-plexus/1.4.2/sisu-inject-plexus-1.4.2.pom#/artifact-0738-sisu-inject-plexus-1.4.2.pom
#!RemoteAsset:  sha256:abb04084d0885319fd0b372d77655f8feb8aa8bb091699fcd99b45798a9587d5
Source839:      https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-parent/1.4.2/sisu-parent-1.4.2.pom#/artifact-0739-sisu-parent-1.4.2.pom
#!RemoteAsset:  sha256:13d15ddfe9946b8427bb7b4b081ab63962285eed0bf6fa5142aea25a46e15814
Source840:      https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/15/spice-parent-15.pom#/artifact-0740-spice-parent-15.pom
#!RemoteAsset:  sha256:95c63c1a55b22dd6453890a419cc1a640f790bbf7d8ae82db1e30aefefb08888
Source841:      https://repo.maven.apache.org/maven2/org/tukaani/xz/1.10/xz-1.10.jar#/artifact-0741-xz-1.10.jar
#!RemoteAsset:  sha256:ef608b83c3bb6c8e3e6b3beaa38842ba15963b46495e4af91b0746c8b750f3b9
Source842:      https://repo.maven.apache.org/maven2/org/tukaani/xz/1.10/xz-1.10.pom#/artifact-0742-xz-1.10.pom
#!RemoteAsset:  sha256:0a4077f6aeae2865532a564807af8d30c26acc6f63b7928d93bd7ab1f2190449
Source843:      https://repo.maven.apache.org/maven2/org/tukaani/xz/1.11/xz-1.11.jar#/artifact-0743-xz-1.11.jar
#!RemoteAsset:  sha256:7bd2fe2f145c8479824757ab76130c0815a7b55850714ef0c28b39bd5d692ca4
Source844:      https://repo.maven.apache.org/maven2/org/tukaani/xz/1.11/xz-1.11.pom#/artifact-0744-xz-1.11.pom
#!RemoteAsset:  sha256:211b306cfc44f8f96df3a0a3ddaf75ba8c5289eed77d60d72f889bb855f535e5
Source845:      https://repo.maven.apache.org/maven2/org/tukaani/xz/1.9/xz-1.9.jar#/artifact-0745-xz-1.9.jar
#!RemoteAsset:  sha256:093be1b03331bce2932d6825c37e98272d7621e6a9e9fb93289a002518b8dd5a
Source846:      https://repo.maven.apache.org/maven2/org/tukaani/xz/1.9/xz-1.9.pom#/artifact-0746-xz-1.9.pom
#!RemoteAsset:  sha256:50970e6069c21182689eb44ae9f8193970e080b6f37fc13f22aa4201cca2dfe4
Source847:      https://repo.maven.apache.org/maven2/org/xmlunit/xmlunit-core/2.11.0/xmlunit-core-2.11.0.jar#/artifact-0747-xmlunit-core-2.11.0.jar
#!RemoteAsset:  sha256:b6ba473c8f8e98baee71963949ec47538f696fdd206289e4962f5eb4ecfe7640
Source848:      https://repo.maven.apache.org/maven2/org/xmlunit/xmlunit-core/2.11.0/xmlunit-core-2.11.0.pom#/artifact-0748-xmlunit-core-2.11.0.pom
#!RemoteAsset:  sha256:4ab26d94afa656cec39a23d1435de6a1fd40c65488c3761e12c31ae6694bef0d
Source849:      https://repo.maven.apache.org/maven2/org/xmlunit/xmlunit-matchers/2.11.0/xmlunit-matchers-2.11.0.jar#/artifact-0749-xmlunit-matchers-2.11.0.jar
#!RemoteAsset:  sha256:97388712382fbd2692285132b1c9f33a0dea8c6b8e7541bdf20558300750478c
Source850:      https://repo.maven.apache.org/maven2/org/xmlunit/xmlunit-matchers/2.11.0/xmlunit-matchers-2.11.0.pom#/artifact-0750-xmlunit-matchers-2.11.0.pom
#!RemoteAsset:  sha256:2effb33e41b5b0899bf4b7c8889ae20810f80c8aebee1844935758842527a4c2
Source851:      https://repo.maven.apache.org/maven2/org/xmlunit/xmlunit-parent/2.11.0/xmlunit-parent-2.11.0.pom#/artifact-0751-xmlunit-parent-2.11.0.pom
#!RemoteAsset:  sha256:e6682acf1ace77508ef13649cbf4f8d09d2cf5457bdb61d25ffb6ac0233d78dd
Source852:      https://repo.maven.apache.org/maven2/org/yaml/snakeyaml/2.5/snakeyaml-2.5.jar#/artifact-0752-snakeyaml-2.5.jar
#!RemoteAsset:  sha256:ba01ae7a744cb52fe8ecf3b023cbc32e0ccc8c6beef9f26de77a47808239447d
Source853:      https://repo.maven.apache.org/maven2/org/yaml/snakeyaml/2.5/snakeyaml-2.5.pom#/artifact-0753-snakeyaml-2.5.pom
#!RemoteAsset:  sha256:e00ccdad5df7eb43fdee44232ef64602bf63807c2d133a7be83ba09fd49af26e
Source854:      https://repo.maven.apache.org/maven2/oro/oro/2.0.8/oro-2.0.8.jar#/artifact-0754-oro-2.0.8.jar
#!RemoteAsset:  sha256:9aa9dfeb2e85e1d5e7932c87140697cecc2b0fadd933d679fd420a2e43831a82
Source855:      https://repo.maven.apache.org/maven2/oro/oro/2.0.8/oro-2.0.8.pom#/artifact-0755-oro-2.0.8.pom
#!RemoteAsset:  sha256:7bc38e7a0f8ca20b0caed607e00cbb144dc8d006ebec4aa193f55dcf391bad50
Source856:      https://repo.maven.apache.org/maven2/xml-apis/xml-apis/1.0.b2/xml-apis-1.0.b2.pom#/artifact-0756-xml-apis-1.0.b2.pom
BuildArch:      noarch

# Disable developer source formatting and SCM discovery in release tarballs.
Patch2000:      2000-disable-formatting-and-scm-for-offline-build.patch

BuildRequires:  fdupes
BuildRequires:  java-21-openjdk
BuildRequires:  unzip
BuildRequires:  zip
%if %{without bootstrap}
BuildRequires:  maven >= 3.9.16
%endif

# Private libraries shipped in the upstream distribution.
Provides:       bundled(aopalliance) = 1.0
Provides:       bundled(asm) = 9.9.1
Provides:       bundled(commons-cli) = 1.11.0
Provides:       bundled(commons-codec) = 1.21.0
Provides:       bundled(error_prone_annotations) = 2.41.0
Provides:       bundled(failureaccess) = 1.0.3
Provides:       bundled(gson) = 2.13.2
Provides:       bundled(guava) = 33.6.0
Provides:       bundled(guice) = 5.1.0
Provides:       bundled(httpclient) = 4.5.14
Provides:       bundled(httpcore) = 4.4.16
Provides:       bundled(jansi) = 2.4.3
Provides:       bundled(javax.annotation-api) = 1.3.2
Provides:       bundled(javax.inject) = 1
Provides:       bundled(jcl-over-slf4j) = 1.7.36
Provides:       bundled(jspecify) = 1.0.0
Provides:       bundled(maven-resolver) = 1.9.27
Provides:       bundled(maven-shared-utils) = 3.4.2
Provides:       bundled(maven-wagon) = 3.5.3
Provides:       bundled(org.eclipse.sisu.inject) = 1.0.0
Provides:       bundled(org.eclipse.sisu.plexus) = 1.0.0
Provides:       bundled(plexus-cipher) = 2.0
Provides:       bundled(plexus-classworlds) = 2.11.0
Provides:       bundled(plexus-component-annotations) = 2.2.0
Provides:       bundled(plexus-interpolation) = 1.29
Provides:       bundled(plexus-sec-dispatcher) = 2.0
Provides:       bundled(plexus-utils) = 3.6.1
Provides:       bundled(slf4j-api) = 1.7.36
Requires:       coreutils
Requires:       java-21-openjdk

%description
Apache Maven is a project management and build tool for Java projects. It
provides dependency management, compilation, testing, and packaging through
a declarative project object model.

Maven is compiled from upstream source using a pinned offline repository of
bootstrap dependencies. Its private third-party runtime libraries remain
bundled. The bootstrap build uses the upstream binary as its build tool;
later builds use the maven package by disabling the bootstrap condition.

%prep
%autosetup -n apache-maven-%{version} -p1
# Keep build inputs under target, outside the upstream source license scan.
# OBS fetches the inputs; Maven requires their coordinate directory layout.
install -Dm644 %{SOURCE100} target/repository/aopalliance/aopalliance/1.0/aopalliance-1.0.jar
install -Dm644 %{SOURCE101} target/repository/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
install -Dm644 %{SOURCE102} target/repository/avalon-framework/avalon-framework/4.1.3/avalon-framework-4.1.3.pom
install -Dm644 %{SOURCE103} target/repository/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.jar
install -Dm644 %{SOURCE104} target/repository/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.pom
install -Dm644 %{SOURCE105} target/repository/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.jar
install -Dm644 %{SOURCE106} target/repository/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.pom
install -Dm644 %{SOURCE107} target/repository/ch/qos/logback/logback-parent/1.2.13/logback-parent-1.2.13.pom
install -Dm644 %{SOURCE108} target/repository/com/fasterxml/jackson/core/jackson-annotations/2.21/jackson-annotations-2.21.jar
install -Dm644 %{SOURCE109} target/repository/com/fasterxml/jackson/core/jackson-annotations/2.21/jackson-annotations-2.21.pom
install -Dm644 %{SOURCE110} target/repository/com/fasterxml/jackson/core/jackson-core/2.21.0/jackson-core-2.21.0.jar
install -Dm644 %{SOURCE111} target/repository/com/fasterxml/jackson/core/jackson-core/2.21.0/jackson-core-2.21.0.pom
install -Dm644 %{SOURCE112} target/repository/com/fasterxml/jackson/core/jackson-databind/2.21.0/jackson-databind-2.21.0.jar
install -Dm644 %{SOURCE113} target/repository/com/fasterxml/jackson/core/jackson-databind/2.21.0/jackson-databind-2.21.0.pom
install -Dm644 %{SOURCE114} target/repository/com/fasterxml/jackson/jackson-base/2.21.0/jackson-base-2.21.0.pom
install -Dm644 %{SOURCE115} target/repository/com/fasterxml/jackson/jackson-bom/2.21.0/jackson-bom-2.21.0.pom
install -Dm644 %{SOURCE116} target/repository/com/fasterxml/jackson/jackson-parent/2.21/jackson-parent-2.21.pom
install -Dm644 %{SOURCE117} target/repository/com/fasterxml/oss-parent/75/oss-parent-75.pom
install -Dm644 %{SOURCE118} target/repository/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.jar
install -Dm644 %{SOURCE119} target/repository/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.pom
install -Dm644 %{SOURCE120} target/repository/com/github/chhorz/javadoc-parser-parent/0.3.1/javadoc-parser-parent-0.3.1.pom
install -Dm644 %{SOURCE121} target/repository/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.jar
install -Dm644 %{SOURCE122} target/repository/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.pom
install -Dm644 %{SOURCE123} target/repository/com/github/luben/zstd-jni/1.5.5-11/zstd-jni-1.5.5-11.pom
install -Dm644 %{SOURCE124} target/repository/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.jar
install -Dm644 %{SOURCE125} target/repository/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.pom
install -Dm644 %{SOURCE126} target/repository/com/github/luben/zstd-jni/1.5.7-4/zstd-jni-1.5.7-4.pom
install -Dm644 %{SOURCE127} target/repository/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.jar
install -Dm644 %{SOURCE128} target/repository/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.pom
install -Dm644 %{SOURCE129} target/repository/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.pom
install -Dm644 %{SOURCE130} target/repository/com/google/code/gson/gson/2.13.2/gson-2.13.2.jar
install -Dm644 %{SOURCE131} target/repository/com/google/code/gson/gson/2.13.2/gson-2.13.2.pom
install -Dm644 %{SOURCE132} target/repository/com/google/code/gson/gson-parent/2.13.2/gson-parent-2.13.2.pom
install -Dm644 %{SOURCE133} target/repository/com/google/collections/google-collections/1.0/google-collections-1.0.pom
install -Dm644 %{SOURCE134} target/repository/com/google/errorprone/error_prone_annotations/2.3.4/error_prone_annotations-2.3.4.pom
install -Dm644 %{SOURCE135} target/repository/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.jar
install -Dm644 %{SOURCE136} target/repository/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.pom
install -Dm644 %{SOURCE137} target/repository/com/google/errorprone/error_prone_parent/2.3.4/error_prone_parent-2.3.4.pom
install -Dm644 %{SOURCE138} target/repository/com/google/errorprone/error_prone_parent/2.41.0/error_prone_parent-2.41.0.pom
install -Dm644 %{SOURCE139} target/repository/com/google/google/1/google-1.pom
install -Dm644 %{SOURCE140} target/repository/com/google/google/5/google-5.pom
install -Dm644 %{SOURCE141} target/repository/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.pom
install -Dm644 %{SOURCE142} target/repository/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.jar
install -Dm644 %{SOURCE143} target/repository/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.pom
install -Dm644 %{SOURCE144} target/repository/com/google/guava/guava/30.1-jre/guava-30.1-jre.pom
install -Dm644 %{SOURCE145} target/repository/com/google/guava/guava/33.6.0-jre/guava-33.6.0-jre.jar
install -Dm644 %{SOURCE146} target/repository/com/google/guava/guava/33.6.0-jre/guava-33.6.0-jre.pom
install -Dm644 %{SOURCE147} target/repository/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom
install -Dm644 %{SOURCE148} target/repository/com/google/guava/guava-parent/30.1-jre/guava-parent-30.1-jre.pom
install -Dm644 %{SOURCE149} target/repository/com/google/guava/guava-parent/33.4.0-android/guava-parent-33.4.0-android.pom
install -Dm644 %{SOURCE150} target/repository/com/google/guava/guava-parent/33.6.0-jre/guava-parent-33.6.0-jre.pom
install -Dm644 %{SOURCE151} target/repository/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom
install -Dm644 %{SOURCE152} target/repository/com/google/inject/guice/5.1.0/guice-5.1.0-classes.jar
install -Dm644 %{SOURCE153} target/repository/com/google/inject/guice/5.1.0/guice-5.1.0.pom
install -Dm644 %{SOURCE154} target/repository/com/google/inject/guice-parent/5.1.0/guice-parent-5.1.0.pom
install -Dm644 %{SOURCE155} target/repository/com/google/j2objc/j2objc-annotations/1.3/j2objc-annotations-1.3.pom
install -Dm644 %{SOURCE156} target/repository/com/sun/activation/all/1.2.2/all-1.2.2.pom
install -Dm644 %{SOURCE157} target/repository/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar
install -Dm644 %{SOURCE158} target/repository/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom
install -Dm644 %{SOURCE159} target/repository/com/thoughtworks/qdox/qdox/2.2.0/qdox-2.2.0.jar
install -Dm644 %{SOURCE160} target/repository/com/thoughtworks/qdox/qdox/2.2.0/qdox-2.2.0.pom
install -Dm644 %{SOURCE161} target/repository/commons-beanutils/commons-beanutils/1.8.3/commons-beanutils-1.8.3.pom
install -Dm644 %{SOURCE162} target/repository/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.jar
install -Dm644 %{SOURCE163} target/repository/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.pom
install -Dm644 %{SOURCE164} target/repository/commons-chain/commons-chain/1.1/commons-chain-1.1.jar
install -Dm644 %{SOURCE165} target/repository/commons-chain/commons-chain/1.1/commons-chain-1.1.pom
install -Dm644 %{SOURCE166} target/repository/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.jar
install -Dm644 %{SOURCE167} target/repository/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.pom
install -Dm644 %{SOURCE168} target/repository/commons-cli/commons-cli/1.6.0/commons-cli-1.6.0.jar
install -Dm644 %{SOURCE169} target/repository/commons-cli/commons-cli/1.6.0/commons-cli-1.6.0.pom
install -Dm644 %{SOURCE170} target/repository/commons-codec/commons-codec/1.11/commons-codec-1.11.jar
install -Dm644 %{SOURCE171} target/repository/commons-codec/commons-codec/1.11/commons-codec-1.11.pom
install -Dm644 %{SOURCE172} target/repository/commons-codec/commons-codec/1.16.1/commons-codec-1.16.1.pom
install -Dm644 %{SOURCE173} target/repository/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.jar
install -Dm644 %{SOURCE174} target/repository/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.pom
install -Dm644 %{SOURCE175} target/repository/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.jar
install -Dm644 %{SOURCE176} target/repository/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.pom
install -Dm644 %{SOURCE177} target/repository/commons-codec/commons-codec/1.21.0/commons-codec-1.21.0.jar
install -Dm644 %{SOURCE178} target/repository/commons-codec/commons-codec/1.21.0/commons-codec-1.21.0.pom
install -Dm644 %{SOURCE179} target/repository/commons-collections/commons-collections/2.1/commons-collections-2.1.pom
install -Dm644 %{SOURCE180} target/repository/commons-collections/commons-collections/3.1/commons-collections-3.1.pom
install -Dm644 %{SOURCE181} target/repository/commons-collections/commons-collections/3.2/commons-collections-3.2.pom
install -Dm644 %{SOURCE182} target/repository/commons-collections/commons-collections/3.2.1/commons-collections-3.2.1.pom
install -Dm644 %{SOURCE183} target/repository/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar
install -Dm644 %{SOURCE184} target/repository/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.pom
install -Dm644 %{SOURCE185} target/repository/commons-digester/commons-digester/1.6/commons-digester-1.6.pom
install -Dm644 %{SOURCE186} target/repository/commons-digester/commons-digester/1.8/commons-digester-1.8.jar
install -Dm644 %{SOURCE187} target/repository/commons-digester/commons-digester/1.8/commons-digester-1.8.pom
install -Dm644 %{SOURCE188} target/repository/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar
install -Dm644 %{SOURCE189} target/repository/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom
install -Dm644 %{SOURCE190} target/repository/commons-io/commons-io/2.15.1/commons-io-2.15.1.jar
install -Dm644 %{SOURCE191} target/repository/commons-io/commons-io/2.15.1/commons-io-2.15.1.pom
install -Dm644 %{SOURCE192} target/repository/commons-io/commons-io/2.16.1/commons-io-2.16.1.jar
install -Dm644 %{SOURCE193} target/repository/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom
install -Dm644 %{SOURCE194} target/repository/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
install -Dm644 %{SOURCE195} target/repository/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar
install -Dm644 %{SOURCE196} target/repository/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
install -Dm644 %{SOURCE197} target/repository/commons-io/commons-io/2.20.0/commons-io-2.20.0.jar
install -Dm644 %{SOURCE198} target/repository/commons-io/commons-io/2.20.0/commons-io-2.20.0.pom
install -Dm644 %{SOURCE199} target/repository/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar
install -Dm644 %{SOURCE200} target/repository/commons-io/commons-io/2.21.0/commons-io-2.21.0.pom
install -Dm644 %{SOURCE201} target/repository/commons-io/commons-io/2.22.0/commons-io-2.22.0.jar
install -Dm644 %{SOURCE202} target/repository/commons-io/commons-io/2.22.0/commons-io-2.22.0.pom
install -Dm644 %{SOURCE203} target/repository/commons-io/commons-io/2.5/commons-io-2.5.pom
install -Dm644 %{SOURCE204} target/repository/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.jar
install -Dm644 %{SOURCE205} target/repository/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.pom
install -Dm644 %{SOURCE206} target/repository/commons-lang/commons-lang/2.4/commons-lang-2.4.jar
install -Dm644 %{SOURCE207} target/repository/commons-lang/commons-lang/2.4/commons-lang-2.4.pom
install -Dm644 %{SOURCE208} target/repository/commons-logging/commons-logging/1.0/commons-logging-1.0.pom
install -Dm644 %{SOURCE209} target/repository/commons-logging/commons-logging/1.0.3/commons-logging-1.0.3.pom
install -Dm644 %{SOURCE210} target/repository/commons-logging/commons-logging/1.1/commons-logging-1.1.pom
install -Dm644 %{SOURCE211} target/repository/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.pom
install -Dm644 %{SOURCE212} target/repository/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
install -Dm644 %{SOURCE213} target/repository/commons-logging/commons-logging/1.2/commons-logging-1.2.pom
install -Dm644 %{SOURCE214} target/repository/dom4j/dom4j/1.1/dom4j-1.1.jar
install -Dm644 %{SOURCE215} target/repository/dom4j/dom4j/1.1/dom4j-1.1.pom
install -Dm644 %{SOURCE216} target/repository/io/airlift/airbase/112/airbase-112.pom
install -Dm644 %{SOURCE217} target/repository/io/airlift/aircompressor/0.27/aircompressor-0.27.jar
install -Dm644 %{SOURCE218} target/repository/io/airlift/aircompressor/0.27/aircompressor-0.27.pom
install -Dm644 %{SOURCE219} target/repository/jakarta/activation/jakarta.activation-api/1.2.2/jakarta.activation-api-1.2.2.jar
install -Dm644 %{SOURCE220} target/repository/jakarta/activation/jakarta.activation-api/1.2.2/jakarta.activation-api-1.2.2.pom
install -Dm644 %{SOURCE221} target/repository/jakarta/xml/bind/jakarta.xml.bind-api/2.3.3/jakarta.xml.bind-api-2.3.3.jar
install -Dm644 %{SOURCE222} target/repository/jakarta/xml/bind/jakarta.xml.bind-api/2.3.3/jakarta.xml.bind-api-2.3.3.pom
install -Dm644 %{SOURCE223} target/repository/jakarta/xml/bind/jakarta.xml.bind-api-parent/2.3.3/jakarta.xml.bind-api-parent-2.3.3.pom
install -Dm644 %{SOURCE224} target/repository/javax/annotation/javax.annotation-api/1.3.2/javax.annotation-api-1.3.2.jar
install -Dm644 %{SOURCE225} target/repository/javax/annotation/javax.annotation-api/1.3.2/javax.annotation-api-1.3.2.pom
install -Dm644 %{SOURCE226} target/repository/javax/inject/javax.inject/1/javax.inject-1.jar
install -Dm644 %{SOURCE227} target/repository/javax/inject/javax.inject/1/javax.inject-1.pom
install -Dm644 %{SOURCE228} target/repository/log4j/log4j/1.2.12/log4j-1.2.12.pom
install -Dm644 %{SOURCE229} target/repository/logkit/logkit/1.0.1/logkit-1.0.1.pom
install -Dm644 %{SOURCE230} target/repository/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.jar
install -Dm644 %{SOURCE231} target/repository/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.pom
install -Dm644 %{SOURCE232} target/repository/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.jar
install -Dm644 %{SOURCE233} target/repository/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.pom
install -Dm644 %{SOURCE234} target/repository/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.jar
install -Dm644 %{SOURCE235} target/repository/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.pom
install -Dm644 %{SOURCE236} target/repository/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.jar
install -Dm644 %{SOURCE237} target/repository/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.pom
install -Dm644 %{SOURCE238} target/repository/net/bytebuddy/byte-buddy-parent/1.10.14/byte-buddy-parent-1.10.14.pom
install -Dm644 %{SOURCE239} target/repository/net/bytebuddy/byte-buddy-parent/1.12.19/byte-buddy-parent-1.12.19.pom
install -Dm644 %{SOURCE240} target/repository/net/java/jvnet-parent/3/jvnet-parent-3.pom
install -Dm644 %{SOURCE241} target/repository/nl/basjes/codeowners/codeowners-parent/1.3.1/codeowners-parent-1.3.1.pom
install -Dm644 %{SOURCE242} target/repository/nl/basjes/gitignore/gitignore-reader/1.3.1/gitignore-reader-1.3.1.jar
install -Dm644 %{SOURCE243} target/repository/nl/basjes/gitignore/gitignore-reader/1.3.1/gitignore-reader-1.3.1.pom
install -Dm644 %{SOURCE244} target/repository/org/apache/apache/13/apache-13.pom
install -Dm644 %{SOURCE245} target/repository/org/apache/apache/16/apache-16.pom
install -Dm644 %{SOURCE246} target/repository/org/apache/apache/18/apache-18.pom
install -Dm644 %{SOURCE247} target/repository/org/apache/apache/19/apache-19.pom
install -Dm644 %{SOURCE248} target/repository/org/apache/apache/21/apache-21.pom
install -Dm644 %{SOURCE249} target/repository/org/apache/apache/23/apache-23.pom
install -Dm644 %{SOURCE250} target/repository/org/apache/apache/29/apache-29.pom
install -Dm644 %{SOURCE251} target/repository/org/apache/apache/30/apache-30.pom
install -Dm644 %{SOURCE252} target/repository/org/apache/apache/31/apache-31.pom
install -Dm644 %{SOURCE253} target/repository/org/apache/apache/32/apache-32.pom
install -Dm644 %{SOURCE254} target/repository/org/apache/apache/33/apache-33.pom
install -Dm644 %{SOURCE255} target/repository/org/apache/apache/34/apache-34.pom
install -Dm644 %{SOURCE256} target/repository/org/apache/apache/35/apache-35.pom
install -Dm644 %{SOURCE257} target/repository/org/apache/apache/37/apache-37.pom
install -Dm644 %{SOURCE258} target/repository/org/apache/apache/38/apache-38.pom
install -Dm644 %{SOURCE259} target/repository/org/apache/apache/4/apache-4.pom
install -Dm644 %{SOURCE260} target/repository/org/apache/apache/5/apache-5.pom
install -Dm644 %{SOURCE261} target/repository/org/apache/apache/6/apache-6.pom
install -Dm644 %{SOURCE262} target/repository/org/apache/apache/7/apache-7.pom
install -Dm644 %{SOURCE263} target/repository/org/apache/apache/9/apache-9.pom
install -Dm644 %{SOURCE264} target/repository/org/apache/apache/resources/apache-jar-resource-bundle/1.8/apache-jar-resource-bundle-1.8.jar
install -Dm644 %{SOURCE265} target/repository/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.jar
install -Dm644 %{SOURCE266} target/repository/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.pom
install -Dm644 %{SOURCE267} target/repository/org/apache/commons/commons-compress/1.25.0/commons-compress-1.25.0.jar
install -Dm644 %{SOURCE268} target/repository/org/apache/commons/commons-compress/1.25.0/commons-compress-1.25.0.pom
install -Dm644 %{SOURCE269} target/repository/org/apache/commons/commons-compress/1.26.1/commons-compress-1.26.1.pom
install -Dm644 %{SOURCE270} target/repository/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.jar
install -Dm644 %{SOURCE271} target/repository/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.pom
install -Dm644 %{SOURCE272} target/repository/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.jar
install -Dm644 %{SOURCE273} target/repository/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.pom
install -Dm644 %{SOURCE274} target/repository/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.jar
install -Dm644 %{SOURCE275} target/repository/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.pom
install -Dm644 %{SOURCE276} target/repository/org/apache/commons/commons-lang3/3.10/commons-lang3-3.10.pom
install -Dm644 %{SOURCE277} target/repository/org/apache/commons/commons-lang3/3.11/commons-lang3-3.11.pom
install -Dm644 %{SOURCE278} target/repository/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom
install -Dm644 %{SOURCE279} target/repository/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar
install -Dm644 %{SOURCE280} target/repository/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
install -Dm644 %{SOURCE281} target/repository/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.jar
install -Dm644 %{SOURCE282} target/repository/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.pom
install -Dm644 %{SOURCE283} target/repository/org/apache/commons/commons-lang3/3.19.0/commons-lang3-3.19.0.jar
install -Dm644 %{SOURCE284} target/repository/org/apache/commons/commons-lang3/3.19.0/commons-lang3-3.19.0.pom
install -Dm644 %{SOURCE285} target/repository/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar
install -Dm644 %{SOURCE286} target/repository/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.pom
install -Dm644 %{SOURCE287} target/repository/org/apache/commons/commons-parent/14/commons-parent-14.pom
install -Dm644 %{SOURCE288} target/repository/org/apache/commons/commons-parent/22/commons-parent-22.pom
install -Dm644 %{SOURCE289} target/repository/org/apache/commons/commons-parent/34/commons-parent-34.pom
install -Dm644 %{SOURCE290} target/repository/org/apache/commons/commons-parent/39/commons-parent-39.pom
install -Dm644 %{SOURCE291} target/repository/org/apache/commons/commons-parent/42/commons-parent-42.pom
install -Dm644 %{SOURCE292} target/repository/org/apache/commons/commons-parent/45/commons-parent-45.pom
install -Dm644 %{SOURCE293} target/repository/org/apache/commons/commons-parent/47/commons-parent-47.pom
install -Dm644 %{SOURCE294} target/repository/org/apache/commons/commons-parent/48/commons-parent-48.pom
install -Dm644 %{SOURCE295} target/repository/org/apache/commons/commons-parent/5/commons-parent-5.pom
install -Dm644 %{SOURCE296} target/repository/org/apache/commons/commons-parent/50/commons-parent-50.pom
install -Dm644 %{SOURCE297} target/repository/org/apache/commons/commons-parent/51/commons-parent-51.pom
install -Dm644 %{SOURCE298} target/repository/org/apache/commons/commons-parent/52/commons-parent-52.pom
install -Dm644 %{SOURCE299} target/repository/org/apache/commons/commons-parent/64/commons-parent-64.pom
install -Dm644 %{SOURCE300} target/repository/org/apache/commons/commons-parent/65/commons-parent-65.pom
install -Dm644 %{SOURCE301} target/repository/org/apache/commons/commons-parent/66/commons-parent-66.pom
install -Dm644 %{SOURCE302} target/repository/org/apache/commons/commons-parent/69/commons-parent-69.pom
install -Dm644 %{SOURCE303} target/repository/org/apache/commons/commons-parent/73/commons-parent-73.pom
install -Dm644 %{SOURCE304} target/repository/org/apache/commons/commons-parent/74/commons-parent-74.pom
install -Dm644 %{SOURCE305} target/repository/org/apache/commons/commons-parent/81/commons-parent-81.pom
install -Dm644 %{SOURCE306} target/repository/org/apache/commons/commons-parent/85/commons-parent-85.pom
install -Dm644 %{SOURCE307} target/repository/org/apache/commons/commons-parent/88/commons-parent-88.pom
install -Dm644 %{SOURCE308} target/repository/org/apache/commons/commons-parent/9/commons-parent-9.pom
install -Dm644 %{SOURCE309} target/repository/org/apache/commons/commons-parent/91/commons-parent-91.pom
install -Dm644 %{SOURCE310} target/repository/org/apache/commons/commons-parent/92/commons-parent-92.pom
install -Dm644 %{SOURCE311} target/repository/org/apache/commons/commons-parent/96/commons-parent-96.pom
install -Dm644 %{SOURCE312} target/repository/org/apache/commons/commons-parent/98/commons-parent-98.pom
install -Dm644 %{SOURCE313} target/repository/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.jar
install -Dm644 %{SOURCE314} target/repository/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom
install -Dm644 %{SOURCE315} target/repository/org/apache/commons/commons-text/1.3/commons-text-1.3.jar
install -Dm644 %{SOURCE316} target/repository/org/apache/commons/commons-text/1.3/commons-text-1.3.pom
install -Dm644 %{SOURCE317} target/repository/org/apache/geronimo/genesis/genesis/2.0/genesis-2.0.pom
install -Dm644 %{SOURCE318} target/repository/org/apache/geronimo/genesis/genesis-default-flava/2.0/genesis-default-flava-2.0.pom
install -Dm644 %{SOURCE319} target/repository/org/apache/geronimo/genesis/genesis-java5-flava/2.0/genesis-java5-flava-2.0.pom
install -Dm644 %{SOURCE320} target/repository/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar
install -Dm644 %{SOURCE321} target/repository/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.pom
install -Dm644 %{SOURCE322} target/repository/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.jar
install -Dm644 %{SOURCE323} target/repository/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.pom
install -Dm644 %{SOURCE324} target/repository/org/apache/httpcomponents/httpcomponents-client/4.5.13/httpcomponents-client-4.5.13.pom
install -Dm644 %{SOURCE325} target/repository/org/apache/httpcomponents/httpcomponents-client/4.5.14/httpcomponents-client-4.5.14.pom
install -Dm644 %{SOURCE326} target/repository/org/apache/httpcomponents/httpcomponents-core/4.4.13/httpcomponents-core-4.4.13.pom
install -Dm644 %{SOURCE327} target/repository/org/apache/httpcomponents/httpcomponents-core/4.4.14/httpcomponents-core-4.4.14.pom
install -Dm644 %{SOURCE328} target/repository/org/apache/httpcomponents/httpcomponents-core/4.4.16/httpcomponents-core-4.4.16.pom
install -Dm644 %{SOURCE329} target/repository/org/apache/httpcomponents/httpcomponents-parent/11/httpcomponents-parent-11.pom
install -Dm644 %{SOURCE330} target/repository/org/apache/httpcomponents/httpcore/4.4.13/httpcore-4.4.13.pom
install -Dm644 %{SOURCE331} target/repository/org/apache/httpcomponents/httpcore/4.4.14/httpcore-4.4.14.jar
install -Dm644 %{SOURCE332} target/repository/org/apache/httpcomponents/httpcore/4.4.14/httpcore-4.4.14.pom
install -Dm644 %{SOURCE333} target/repository/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.jar
install -Dm644 %{SOURCE334} target/repository/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.pom
install -Dm644 %{SOURCE335} target/repository/org/apache/maven/doxia/doxia/1.0/doxia-1.0.pom
install -Dm644 %{SOURCE336} target/repository/org/apache/maven/doxia/doxia/1.11.1/doxia-1.11.1.pom
install -Dm644 %{SOURCE337} target/repository/org/apache/maven/doxia/doxia/1.12.0/doxia-1.12.0.pom
install -Dm644 %{SOURCE338} target/repository/org/apache/maven/doxia/doxia/2.0.0/doxia-2.0.0.pom
install -Dm644 %{SOURCE339} target/repository/org/apache/maven/doxia/doxia-core/1.11.1/doxia-core-1.11.1.pom
install -Dm644 %{SOURCE340} target/repository/org/apache/maven/doxia/doxia-core/1.12.0/doxia-core-1.12.0.jar
install -Dm644 %{SOURCE341} target/repository/org/apache/maven/doxia/doxia-core/1.12.0/doxia-core-1.12.0.pom
install -Dm644 %{SOURCE342} target/repository/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.jar
install -Dm644 %{SOURCE343} target/repository/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.pom
install -Dm644 %{SOURCE344} target/repository/org/apache/maven/doxia/doxia-decoration-model/1.11.1/doxia-decoration-model-1.11.1.jar
install -Dm644 %{SOURCE345} target/repository/org/apache/maven/doxia/doxia-decoration-model/1.11.1/doxia-decoration-model-1.11.1.pom
install -Dm644 %{SOURCE346} target/repository/org/apache/maven/doxia/doxia-integration-tools/1.11.1/doxia-integration-tools-1.11.1.jar
install -Dm644 %{SOURCE347} target/repository/org/apache/maven/doxia/doxia-integration-tools/1.11.1/doxia-integration-tools-1.11.1.pom
install -Dm644 %{SOURCE348} target/repository/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.jar
install -Dm644 %{SOURCE349} target/repository/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.pom
install -Dm644 %{SOURCE350} target/repository/org/apache/maven/doxia/doxia-logging-api/1.11.1/doxia-logging-api-1.11.1.pom
install -Dm644 %{SOURCE351} target/repository/org/apache/maven/doxia/doxia-logging-api/1.12.0/doxia-logging-api-1.12.0.jar
install -Dm644 %{SOURCE352} target/repository/org/apache/maven/doxia/doxia-logging-api/1.12.0/doxia-logging-api-1.12.0.pom
install -Dm644 %{SOURCE353} target/repository/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.jar
install -Dm644 %{SOURCE354} target/repository/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.pom
install -Dm644 %{SOURCE355} target/repository/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.jar
install -Dm644 %{SOURCE356} target/repository/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.pom
install -Dm644 %{SOURCE357} target/repository/org/apache/maven/doxia/doxia-module-xhtml/1.11.1/doxia-module-xhtml-1.11.1.pom
install -Dm644 %{SOURCE358} target/repository/org/apache/maven/doxia/doxia-module-xhtml/1.12.0/doxia-module-xhtml-1.12.0.jar
install -Dm644 %{SOURCE359} target/repository/org/apache/maven/doxia/doxia-module-xhtml/1.12.0/doxia-module-xhtml-1.12.0.pom
install -Dm644 %{SOURCE360} target/repository/org/apache/maven/doxia/doxia-module-xhtml5/1.11.1/doxia-module-xhtml5-1.11.1.jar
install -Dm644 %{SOURCE361} target/repository/org/apache/maven/doxia/doxia-module-xhtml5/1.11.1/doxia-module-xhtml5-1.11.1.pom
install -Dm644 %{SOURCE362} target/repository/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.jar
install -Dm644 %{SOURCE363} target/repository/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.pom
install -Dm644 %{SOURCE364} target/repository/org/apache/maven/doxia/doxia-modules/1.11.1/doxia-modules-1.11.1.pom
install -Dm644 %{SOURCE365} target/repository/org/apache/maven/doxia/doxia-modules/1.12.0/doxia-modules-1.12.0.pom
install -Dm644 %{SOURCE366} target/repository/org/apache/maven/doxia/doxia-modules/2.0.0/doxia-modules-2.0.0.pom
install -Dm644 %{SOURCE367} target/repository/org/apache/maven/doxia/doxia-sink-api/1.0/doxia-sink-api-1.0.pom
install -Dm644 %{SOURCE368} target/repository/org/apache/maven/doxia/doxia-sink-api/1.11.1/doxia-sink-api-1.11.1.pom
install -Dm644 %{SOURCE369} target/repository/org/apache/maven/doxia/doxia-sink-api/1.12.0/doxia-sink-api-1.12.0.jar
install -Dm644 %{SOURCE370} target/repository/org/apache/maven/doxia/doxia-sink-api/1.12.0/doxia-sink-api-1.12.0.pom
install -Dm644 %{SOURCE371} target/repository/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.jar
install -Dm644 %{SOURCE372} target/repository/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.pom
install -Dm644 %{SOURCE373} target/repository/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.jar
install -Dm644 %{SOURCE374} target/repository/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.pom
install -Dm644 %{SOURCE375} target/repository/org/apache/maven/doxia/doxia-site-renderer/1.11.1/doxia-site-renderer-1.11.1.jar
install -Dm644 %{SOURCE376} target/repository/org/apache/maven/doxia/doxia-site-renderer/1.11.1/doxia-site-renderer-1.11.1.pom
install -Dm644 %{SOURCE377} target/repository/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.jar
install -Dm644 %{SOURCE378} target/repository/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.pom
install -Dm644 %{SOURCE379} target/repository/org/apache/maven/doxia/doxia-sitetools/1.11.1/doxia-sitetools-1.11.1.pom
install -Dm644 %{SOURCE380} target/repository/org/apache/maven/doxia/doxia-sitetools/2.0.0/doxia-sitetools-2.0.0.pom
install -Dm644 %{SOURCE381} target/repository/org/apache/maven/doxia/doxia-skin-model/1.11.1/doxia-skin-model-1.11.1.jar
install -Dm644 %{SOURCE382} target/repository/org/apache/maven/doxia/doxia-skin-model/1.11.1/doxia-skin-model-1.11.1.pom
install -Dm644 %{SOURCE383} target/repository/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.jar
install -Dm644 %{SOURCE384} target/repository/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.pom
install -Dm644 %{SOURCE385} target/repository/org/apache/maven/enforcer/enforcer/3.6.2/enforcer-3.6.2.pom
install -Dm644 %{SOURCE386} target/repository/org/apache/maven/enforcer/enforcer-api/3.6.2/enforcer-api-3.6.2.jar
install -Dm644 %{SOURCE387} target/repository/org/apache/maven/enforcer/enforcer-api/3.6.2/enforcer-api-3.6.2.pom
install -Dm644 %{SOURCE388} target/repository/org/apache/maven/enforcer/enforcer-rules/3.6.2/enforcer-rules-3.6.2.jar
install -Dm644 %{SOURCE389} target/repository/org/apache/maven/enforcer/enforcer-rules/3.6.2/enforcer-rules-3.6.2.pom
install -Dm644 %{SOURCE390} target/repository/org/apache/maven/maven/2.2.1/maven-2.2.1.pom
install -Dm644 %{SOURCE391} target/repository/org/apache/maven/maven/3.0/maven-3.0.pom
install -Dm644 %{SOURCE392} target/repository/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.jar
install -Dm644 %{SOURCE393} target/repository/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.pom
install -Dm644 %{SOURCE394} target/repository/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.jar
install -Dm644 %{SOURCE395} target/repository/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.pom
install -Dm644 %{SOURCE396} target/repository/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.jar
install -Dm644 %{SOURCE397} target/repository/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.pom
install -Dm644 %{SOURCE398} target/repository/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.jar
install -Dm644 %{SOURCE399} target/repository/org/apache/maven/maven-artifact/2.2.1/maven-artifact-2.2.1.pom
install -Dm644 %{SOURCE400} target/repository/org/apache/maven/maven-artifact/3.0/maven-artifact-3.0.pom
install -Dm644 %{SOURCE401} target/repository/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.jar
install -Dm644 %{SOURCE402} target/repository/org/apache/maven/maven-model/2.2.1/maven-model-2.2.1.pom
install -Dm644 %{SOURCE403} target/repository/org/apache/maven/maven-model/3.0/maven-model-3.0.pom
install -Dm644 %{SOURCE404} target/repository/org/apache/maven/maven-parent/10/maven-parent-10.pom
install -Dm644 %{SOURCE405} target/repository/org/apache/maven/maven-parent/11/maven-parent-11.pom
install -Dm644 %{SOURCE406} target/repository/org/apache/maven/maven-parent/15/maven-parent-15.pom
install -Dm644 %{SOURCE407} target/repository/org/apache/maven/maven-parent/16/maven-parent-16.pom
install -Dm644 %{SOURCE408} target/repository/org/apache/maven/maven-parent/23/maven-parent-23.pom
install -Dm644 %{SOURCE409} target/repository/org/apache/maven/maven-parent/30/maven-parent-30.pom
install -Dm644 %{SOURCE410} target/repository/org/apache/maven/maven-parent/33/maven-parent-33.pom
install -Dm644 %{SOURCE411} target/repository/org/apache/maven/maven-parent/34/maven-parent-34.pom
install -Dm644 %{SOURCE412} target/repository/org/apache/maven/maven-parent/39/maven-parent-39.pom
install -Dm644 %{SOURCE413} target/repository/org/apache/maven/maven-parent/41/maven-parent-41.pom
install -Dm644 %{SOURCE414} target/repository/org/apache/maven/maven-parent/42/maven-parent-42.pom
install -Dm644 %{SOURCE415} target/repository/org/apache/maven/maven-parent/43/maven-parent-43.pom
install -Dm644 %{SOURCE416} target/repository/org/apache/maven/maven-parent/44/maven-parent-44.pom
install -Dm644 %{SOURCE417} target/repository/org/apache/maven/maven-parent/45/maven-parent-45.pom
install -Dm644 %{SOURCE418} target/repository/org/apache/maven/maven-parent/47/maven-parent-47.pom
install -Dm644 %{SOURCE419} target/repository/org/apache/maven/maven-parent/48/maven-parent-48.pom
install -Dm644 %{SOURCE420} target/repository/org/apache/maven/maven-plugin-api/2.2.1/maven-plugin-api-2.2.1.jar
install -Dm644 %{SOURCE421} target/repository/org/apache/maven/maven-plugin-api/2.2.1/maven-plugin-api-2.2.1.pom
install -Dm644 %{SOURCE422} target/repository/org/apache/maven/maven-plugin-api/3.0/maven-plugin-api-3.0.pom
install -Dm644 %{SOURCE423} target/repository/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.jar
install -Dm644 %{SOURCE424} target/repository/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.pom
install -Dm644 %{SOURCE425} target/repository/org/apache/maven/plugins/maven-compiler-plugin/3.15.0/maven-compiler-plugin-3.15.0.jar
install -Dm644 %{SOURCE426} target/repository/org/apache/maven/plugins/maven-compiler-plugin/3.15.0/maven-compiler-plugin-3.15.0.pom
install -Dm644 %{SOURCE427} target/repository/org/apache/maven/plugins/maven-dependency-plugin/3.10.0/maven-dependency-plugin-3.10.0.jar
install -Dm644 %{SOURCE428} target/repository/org/apache/maven/plugins/maven-dependency-plugin/3.10.0/maven-dependency-plugin-3.10.0.pom
install -Dm644 %{SOURCE429} target/repository/org/apache/maven/plugins/maven-enforcer-plugin/3.6.2/maven-enforcer-plugin-3.6.2.jar
install -Dm644 %{SOURCE430} target/repository/org/apache/maven/plugins/maven-enforcer-plugin/3.6.2/maven-enforcer-plugin-3.6.2.pom
install -Dm644 %{SOURCE431} target/repository/org/apache/maven/plugins/maven-failsafe-plugin/3.5.5/maven-failsafe-plugin-3.5.5.jar
install -Dm644 %{SOURCE432} target/repository/org/apache/maven/plugins/maven-failsafe-plugin/3.5.5/maven-failsafe-plugin-3.5.5.pom
install -Dm644 %{SOURCE433} target/repository/org/apache/maven/plugins/maven-jar-plugin/3.5.0/maven-jar-plugin-3.5.0.jar
install -Dm644 %{SOURCE434} target/repository/org/apache/maven/plugins/maven-jar-plugin/3.5.0/maven-jar-plugin-3.5.0.pom
install -Dm644 %{SOURCE435} target/repository/org/apache/maven/plugins/maven-plugins/43/maven-plugins-43.pom
install -Dm644 %{SOURCE436} target/repository/org/apache/maven/plugins/maven-plugins/45/maven-plugins-45.pom
install -Dm644 %{SOURCE437} target/repository/org/apache/maven/plugins/maven-plugins/47/maven-plugins-47.pom
install -Dm644 %{SOURCE438} target/repository/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.jar
install -Dm644 %{SOURCE439} target/repository/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.pom
install -Dm644 %{SOURCE440} target/repository/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.jar
install -Dm644 %{SOURCE441} target/repository/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.pom
install -Dm644 %{SOURCE442} target/repository/org/apache/maven/plugins/maven-surefire-plugin/3.5.5/maven-surefire-plugin-3.5.5.jar
install -Dm644 %{SOURCE443} target/repository/org/apache/maven/plugins/maven-surefire-plugin/3.5.5/maven-surefire-plugin-3.5.5.pom
install -Dm644 %{SOURCE444} target/repository/org/apache/maven/reporting/maven-reporting-api/3.0/maven-reporting-api-3.0.pom
install -Dm644 %{SOURCE445} target/repository/org/apache/maven/reporting/maven-reporting-api/3.1.1/maven-reporting-api-3.1.1.jar
install -Dm644 %{SOURCE446} target/repository/org/apache/maven/reporting/maven-reporting-api/3.1.1/maven-reporting-api-3.1.1.pom
install -Dm644 %{SOURCE447} target/repository/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.jar
install -Dm644 %{SOURCE448} target/repository/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.pom
install -Dm644 %{SOURCE449} target/repository/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.jar
install -Dm644 %{SOURCE450} target/repository/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.pom
install -Dm644 %{SOURCE451} target/repository/org/apache/maven/resolver/maven-resolver/1.4.1/maven-resolver-1.4.1.pom
install -Dm644 %{SOURCE452} target/repository/org/apache/maven/resolver/maven-resolver/1.9.23/maven-resolver-1.9.23.pom
install -Dm644 %{SOURCE453} target/repository/org/apache/maven/resolver/maven-resolver/1.9.25/maven-resolver-1.9.25.pom
install -Dm644 %{SOURCE454} target/repository/org/apache/maven/resolver/maven-resolver/1.9.27/maven-resolver-1.9.27.pom
install -Dm644 %{SOURCE455} target/repository/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.jar
install -Dm644 %{SOURCE456} target/repository/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.pom
install -Dm644 %{SOURCE457} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.23/maven-resolver-api-1.9.23.pom
install -Dm644 %{SOURCE458} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.25/maven-resolver-api-1.9.25.pom
install -Dm644 %{SOURCE459} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.27/maven-resolver-api-1.9.27.jar
install -Dm644 %{SOURCE460} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.27/maven-resolver-api-1.9.27.pom
install -Dm644 %{SOURCE461} target/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.9.27/maven-resolver-connector-basic-1.9.27.jar
install -Dm644 %{SOURCE462} target/repository/org/apache/maven/resolver/maven-resolver-connector-basic/1.9.27/maven-resolver-connector-basic-1.9.27.pom
install -Dm644 %{SOURCE463} target/repository/org/apache/maven/resolver/maven-resolver-impl/1.9.27/maven-resolver-impl-1.9.27.jar
install -Dm644 %{SOURCE464} target/repository/org/apache/maven/resolver/maven-resolver-impl/1.9.27/maven-resolver-impl-1.9.27.pom
install -Dm644 %{SOURCE465} target/repository/org/apache/maven/resolver/maven-resolver-named-locks/1.9.27/maven-resolver-named-locks-1.9.27.jar
install -Dm644 %{SOURCE466} target/repository/org/apache/maven/resolver/maven-resolver-named-locks/1.9.27/maven-resolver-named-locks-1.9.27.pom
install -Dm644 %{SOURCE467} target/repository/org/apache/maven/resolver/maven-resolver-spi/1.9.27/maven-resolver-spi-1.9.27.jar
install -Dm644 %{SOURCE468} target/repository/org/apache/maven/resolver/maven-resolver-spi/1.9.27/maven-resolver-spi-1.9.27.pom
install -Dm644 %{SOURCE469} target/repository/org/apache/maven/resolver/maven-resolver-transport-file/1.9.27/maven-resolver-transport-file-1.9.27.jar
install -Dm644 %{SOURCE470} target/repository/org/apache/maven/resolver/maven-resolver-transport-file/1.9.27/maven-resolver-transport-file-1.9.27.pom
install -Dm644 %{SOURCE471} target/repository/org/apache/maven/resolver/maven-resolver-transport-http/1.9.27/maven-resolver-transport-http-1.9.27.jar
install -Dm644 %{SOURCE472} target/repository/org/apache/maven/resolver/maven-resolver-transport-http/1.9.27/maven-resolver-transport-http-1.9.27.pom
install -Dm644 %{SOURCE473} target/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.9.27/maven-resolver-transport-wagon-1.9.27.jar
install -Dm644 %{SOURCE474} target/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/1.9.27/maven-resolver-transport-wagon-1.9.27.pom
install -Dm644 %{SOURCE475} target/repository/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.jar
install -Dm644 %{SOURCE476} target/repository/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.pom
install -Dm644 %{SOURCE477} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.23/maven-resolver-util-1.9.23.jar
install -Dm644 %{SOURCE478} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.23/maven-resolver-util-1.9.23.pom
install -Dm644 %{SOURCE479} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.jar
install -Dm644 %{SOURCE480} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.pom
install -Dm644 %{SOURCE481} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.jar
install -Dm644 %{SOURCE482} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.pom
install -Dm644 %{SOURCE483} target/repository/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.jar
install -Dm644 %{SOURCE484} target/repository/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.pom
install -Dm644 %{SOURCE485} target/repository/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.jar
install -Dm644 %{SOURCE486} target/repository/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.pom
install -Dm644 %{SOURCE487} target/repository/org/apache/maven/shared/maven-common-artifact-filters/3.1.0/maven-common-artifact-filters-3.1.0.pom
install -Dm644 %{SOURCE488} target/repository/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.jar
install -Dm644 %{SOURCE489} target/repository/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.pom
install -Dm644 %{SOURCE490} target/repository/org/apache/maven/shared/maven-dependency-analyzer/1.17.0/maven-dependency-analyzer-1.17.0.jar
install -Dm644 %{SOURCE491} target/repository/org/apache/maven/shared/maven-dependency-analyzer/1.17.0/maven-dependency-analyzer-1.17.0.pom
install -Dm644 %{SOURCE492} target/repository/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.jar
install -Dm644 %{SOURCE493} target/repository/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.pom
install -Dm644 %{SOURCE494} target/repository/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.jar
install -Dm644 %{SOURCE495} target/repository/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.pom
install -Dm644 %{SOURCE496} target/repository/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.jar
install -Dm644 %{SOURCE497} target/repository/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.pom
install -Dm644 %{SOURCE498} target/repository/org/apache/maven/shared/maven-shared-components/15/maven-shared-components-15.pom
install -Dm644 %{SOURCE499} target/repository/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
install -Dm644 %{SOURCE500} target/repository/org/apache/maven/shared/maven-shared-components/30/maven-shared-components-30.pom
install -Dm644 %{SOURCE501} target/repository/org/apache/maven/shared/maven-shared-components/33/maven-shared-components-33.pom
install -Dm644 %{SOURCE502} target/repository/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom
install -Dm644 %{SOURCE503} target/repository/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom
install -Dm644 %{SOURCE504} target/repository/org/apache/maven/shared/maven-shared-components/41/maven-shared-components-41.pom
install -Dm644 %{SOURCE505} target/repository/org/apache/maven/shared/maven-shared-components/42/maven-shared-components-42.pom
install -Dm644 %{SOURCE506} target/repository/org/apache/maven/shared/maven-shared-components/43/maven-shared-components-43.pom
install -Dm644 %{SOURCE507} target/repository/org/apache/maven/shared/maven-shared-components/44/maven-shared-components-44.pom
install -Dm644 %{SOURCE508} target/repository/org/apache/maven/shared/maven-shared-components/45/maven-shared-components-45.pom
install -Dm644 %{SOURCE509} target/repository/org/apache/maven/shared/maven-shared-components/47/maven-shared-components-47.pom
install -Dm644 %{SOURCE510} target/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
install -Dm644 %{SOURCE511} target/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
install -Dm644 %{SOURCE512} target/repository/org/apache/maven/shared/maven-shared-utils/3.1.0/maven-shared-utils-3.1.0.pom
install -Dm644 %{SOURCE513} target/repository/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.jar
install -Dm644 %{SOURCE514} target/repository/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.pom
install -Dm644 %{SOURCE515} target/repository/org/apache/maven/surefire/common-java5/3.5.5/common-java5-3.5.5.jar
install -Dm644 %{SOURCE516} target/repository/org/apache/maven/surefire/common-java5/3.5.5/common-java5-3.5.5.pom
install -Dm644 %{SOURCE517} target/repository/org/apache/maven/surefire/maven-surefire-common/3.5.5/maven-surefire-common-3.5.5.jar
install -Dm644 %{SOURCE518} target/repository/org/apache/maven/surefire/maven-surefire-common/3.5.5/maven-surefire-common-3.5.5.pom
install -Dm644 %{SOURCE519} target/repository/org/apache/maven/surefire/surefire/3.5.5/surefire-3.5.5.pom
install -Dm644 %{SOURCE520} target/repository/org/apache/maven/surefire/surefire-api/3.5.5/surefire-api-3.5.5.jar
install -Dm644 %{SOURCE521} target/repository/org/apache/maven/surefire/surefire-api/3.5.5/surefire-api-3.5.5.pom
install -Dm644 %{SOURCE522} target/repository/org/apache/maven/surefire/surefire-booter/3.5.5/surefire-booter-3.5.5.jar
install -Dm644 %{SOURCE523} target/repository/org/apache/maven/surefire/surefire-booter/3.5.5/surefire-booter-3.5.5.pom
install -Dm644 %{SOURCE524} target/repository/org/apache/maven/surefire/surefire-extensions-api/3.5.5/surefire-extensions-api-3.5.5.jar
install -Dm644 %{SOURCE525} target/repository/org/apache/maven/surefire/surefire-extensions-api/3.5.5/surefire-extensions-api-3.5.5.pom
install -Dm644 %{SOURCE526} target/repository/org/apache/maven/surefire/surefire-extensions-spi/3.5.5/surefire-extensions-spi-3.5.5.jar
install -Dm644 %{SOURCE527} target/repository/org/apache/maven/surefire/surefire-extensions-spi/3.5.5/surefire-extensions-spi-3.5.5.pom
install -Dm644 %{SOURCE528} target/repository/org/apache/maven/surefire/surefire-junit-platform/3.5.5/surefire-junit-platform-3.5.5.jar
install -Dm644 %{SOURCE529} target/repository/org/apache/maven/surefire/surefire-junit-platform/3.5.5/surefire-junit-platform-3.5.5.pom
install -Dm644 %{SOURCE530} target/repository/org/apache/maven/surefire/surefire-logger-api/3.5.5/surefire-logger-api-3.5.5.jar
install -Dm644 %{SOURCE531} target/repository/org/apache/maven/surefire/surefire-logger-api/3.5.5/surefire-logger-api-3.5.5.pom
install -Dm644 %{SOURCE532} target/repository/org/apache/maven/surefire/surefire-providers/3.5.5/surefire-providers-3.5.5.pom
install -Dm644 %{SOURCE533} target/repository/org/apache/maven/surefire/surefire-shared-utils/3.5.5/surefire-shared-utils-3.5.5.jar
install -Dm644 %{SOURCE534} target/repository/org/apache/maven/surefire/surefire-shared-utils/3.5.5/surefire-shared-utils-3.5.5.pom
install -Dm644 %{SOURCE535} target/repository/org/apache/maven/wagon/wagon/3.5.3/wagon-3.5.3.pom
install -Dm644 %{SOURCE536} target/repository/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.jar
install -Dm644 %{SOURCE537} target/repository/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.pom
install -Dm644 %{SOURCE538} target/repository/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.jar
install -Dm644 %{SOURCE539} target/repository/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.pom
install -Dm644 %{SOURCE540} target/repository/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.jar
install -Dm644 %{SOURCE541} target/repository/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.pom
install -Dm644 %{SOURCE542} target/repository/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.jar
install -Dm644 %{SOURCE543} target/repository/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.pom
install -Dm644 %{SOURCE544} target/repository/org/apache/maven/wagon/wagon-providers/3.5.3/wagon-providers-3.5.3.pom
install -Dm644 %{SOURCE545} target/repository/org/apache/rat/apache-rat-core/0.16.1/apache-rat-core-0.16.1.jar
install -Dm644 %{SOURCE546} target/repository/org/apache/rat/apache-rat-core/0.16.1/apache-rat-core-0.16.1.pom
install -Dm644 %{SOURCE547} target/repository/org/apache/rat/apache-rat-plugin/0.16.1/apache-rat-plugin-0.16.1.jar
install -Dm644 %{SOURCE548} target/repository/org/apache/rat/apache-rat-plugin/0.16.1/apache-rat-plugin-0.16.1.pom
install -Dm644 %{SOURCE549} target/repository/org/apache/rat/apache-rat-project/0.16.1/apache-rat-project-0.16.1.pom
install -Dm644 %{SOURCE550} target/repository/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.jar
install -Dm644 %{SOURCE551} target/repository/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.pom
install -Dm644 %{SOURCE552} target/repository/org/apache/velocity/tools/velocity-tools-parent/3.1/velocity-tools-parent-3.1.pom
install -Dm644 %{SOURCE553} target/repository/org/apache/velocity/velocity/1.6.2/velocity-1.6.2.pom
install -Dm644 %{SOURCE554} target/repository/org/apache/velocity/velocity/1.7/velocity-1.7.jar
install -Dm644 %{SOURCE555} target/repository/org/apache/velocity/velocity/1.7/velocity-1.7.pom
install -Dm644 %{SOURCE556} target/repository/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom
install -Dm644 %{SOURCE557} target/repository/org/apache/velocity/velocity-engine-core/2.4/velocity-engine-core-2.4.pom
install -Dm644 %{SOURCE558} target/repository/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.jar
install -Dm644 %{SOURCE559} target/repository/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.pom
install -Dm644 %{SOURCE560} target/repository/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom
install -Dm644 %{SOURCE561} target/repository/org/apache/velocity/velocity-engine-parent/2.4/velocity-engine-parent-2.4.pom
install -Dm644 %{SOURCE562} target/repository/org/apache/velocity/velocity-engine-parent/2.4.1/velocity-engine-parent-2.4.1.pom
install -Dm644 %{SOURCE563} target/repository/org/apache/velocity/velocity-master/4/velocity-master-4.pom
install -Dm644 %{SOURCE564} target/repository/org/apache/velocity/velocity-master/7/velocity-master-7.pom
install -Dm644 %{SOURCE565} target/repository/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.jar
install -Dm644 %{SOURCE566} target/repository/org/apache/velocity/velocity-tools/2.0/velocity-tools-2.0.pom
install -Dm644 %{SOURCE567} target/repository/org/apache/xbean/xbean/3.7/xbean-3.7.pom
install -Dm644 %{SOURCE568} target/repository/org/apache/xbean/xbean-reflect/3.7/xbean-reflect-3.7.pom
install -Dm644 %{SOURCE569} target/repository/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.jar
install -Dm644 %{SOURCE570} target/repository/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.pom
install -Dm644 %{SOURCE571} target/repository/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar
install -Dm644 %{SOURCE572} target/repository/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom
install -Dm644 %{SOURCE573} target/repository/org/assertj/assertj-bom/3.27.7/assertj-bom-3.27.7.pom
install -Dm644 %{SOURCE574} target/repository/org/checkerframework/checker-qual/3.5.0/checker-qual-3.5.0.pom
install -Dm644 %{SOURCE575} target/repository/org/codehaus/modello/modello/2.6.0/modello-2.6.0.pom
install -Dm644 %{SOURCE576} target/repository/org/codehaus/modello/modello-core/2.6.0/modello-core-2.6.0.jar
install -Dm644 %{SOURCE577} target/repository/org/codehaus/modello/modello-core/2.6.0/modello-core-2.6.0.pom
install -Dm644 %{SOURCE578} target/repository/org/codehaus/modello/modello-maven-plugin/2.6.0/modello-maven-plugin-2.6.0.jar
install -Dm644 %{SOURCE579} target/repository/org/codehaus/modello/modello-maven-plugin/2.6.0/modello-maven-plugin-2.6.0.pom
install -Dm644 %{SOURCE580} target/repository/org/codehaus/modello/modello-plugin-converters/2.6.0/modello-plugin-converters-2.6.0.jar
install -Dm644 %{SOURCE581} target/repository/org/codehaus/modello/modello-plugin-converters/2.6.0/modello-plugin-converters-2.6.0.pom
install -Dm644 %{SOURCE582} target/repository/org/codehaus/modello/modello-plugin-dom4j/2.6.0/modello-plugin-dom4j-2.6.0.jar
install -Dm644 %{SOURCE583} target/repository/org/codehaus/modello/modello-plugin-dom4j/2.6.0/modello-plugin-dom4j-2.6.0.pom
install -Dm644 %{SOURCE584} target/repository/org/codehaus/modello/modello-plugin-jackson/2.6.0/modello-plugin-jackson-2.6.0.jar
install -Dm644 %{SOURCE585} target/repository/org/codehaus/modello/modello-plugin-jackson/2.6.0/modello-plugin-jackson-2.6.0.pom
install -Dm644 %{SOURCE586} target/repository/org/codehaus/modello/modello-plugin-java/2.6.0/modello-plugin-java-2.6.0.jar
install -Dm644 %{SOURCE587} target/repository/org/codehaus/modello/modello-plugin-java/2.6.0/modello-plugin-java-2.6.0.pom
install -Dm644 %{SOURCE588} target/repository/org/codehaus/modello/modello-plugin-jdom/2.6.0/modello-plugin-jdom-2.6.0.jar
install -Dm644 %{SOURCE589} target/repository/org/codehaus/modello/modello-plugin-jdom/2.6.0/modello-plugin-jdom-2.6.0.pom
install -Dm644 %{SOURCE590} target/repository/org/codehaus/modello/modello-plugin-jsonschema/2.6.0/modello-plugin-jsonschema-2.6.0.jar
install -Dm644 %{SOURCE591} target/repository/org/codehaus/modello/modello-plugin-jsonschema/2.6.0/modello-plugin-jsonschema-2.6.0.pom
install -Dm644 %{SOURCE592} target/repository/org/codehaus/modello/modello-plugin-sax/2.6.0/modello-plugin-sax-2.6.0.jar
install -Dm644 %{SOURCE593} target/repository/org/codehaus/modello/modello-plugin-sax/2.6.0/modello-plugin-sax-2.6.0.pom
install -Dm644 %{SOURCE594} target/repository/org/codehaus/modello/modello-plugin-snakeyaml/2.6.0/modello-plugin-snakeyaml-2.6.0.jar
install -Dm644 %{SOURCE595} target/repository/org/codehaus/modello/modello-plugin-snakeyaml/2.6.0/modello-plugin-snakeyaml-2.6.0.pom
install -Dm644 %{SOURCE596} target/repository/org/codehaus/modello/modello-plugin-stax/2.6.0/modello-plugin-stax-2.6.0.jar
install -Dm644 %{SOURCE597} target/repository/org/codehaus/modello/modello-plugin-stax/2.6.0/modello-plugin-stax-2.6.0.pom
install -Dm644 %{SOURCE598} target/repository/org/codehaus/modello/modello-plugin-velocity/2.6.0/modello-plugin-velocity-2.6.0.jar
install -Dm644 %{SOURCE599} target/repository/org/codehaus/modello/modello-plugin-velocity/2.6.0/modello-plugin-velocity-2.6.0.pom
install -Dm644 %{SOURCE600} target/repository/org/codehaus/modello/modello-plugin-xdoc/2.6.0/modello-plugin-xdoc-2.6.0.jar
install -Dm644 %{SOURCE601} target/repository/org/codehaus/modello/modello-plugin-xdoc/2.6.0/modello-plugin-xdoc-2.6.0.pom
install -Dm644 %{SOURCE602} target/repository/org/codehaus/modello/modello-plugin-xml/2.6.0/modello-plugin-xml-2.6.0.jar
install -Dm644 %{SOURCE603} target/repository/org/codehaus/modello/modello-plugin-xml/2.6.0/modello-plugin-xml-2.6.0.pom
install -Dm644 %{SOURCE604} target/repository/org/codehaus/modello/modello-plugin-xpp3/2.6.0/modello-plugin-xpp3-2.6.0.jar
install -Dm644 %{SOURCE605} target/repository/org/codehaus/modello/modello-plugin-xpp3/2.6.0/modello-plugin-xpp3-2.6.0.pom
install -Dm644 %{SOURCE606} target/repository/org/codehaus/modello/modello-plugin-xsd/2.6.0/modello-plugin-xsd-2.6.0.jar
install -Dm644 %{SOURCE607} target/repository/org/codehaus/modello/modello-plugin-xsd/2.6.0/modello-plugin-xsd-2.6.0.pom
install -Dm644 %{SOURCE608} target/repository/org/codehaus/modello/modello-plugins/2.6.0/modello-plugins-2.6.0.pom
install -Dm644 %{SOURCE609} target/repository/org/codehaus/mojo/animal-sniffer/1.27/animal-sniffer-1.27.jar
install -Dm644 %{SOURCE610} target/repository/org/codehaus/mojo/animal-sniffer/1.27/animal-sniffer-1.27.pom
install -Dm644 %{SOURCE611} target/repository/org/codehaus/mojo/animal-sniffer-annotations/1.27/animal-sniffer-annotations-1.27.jar
install -Dm644 %{SOURCE612} target/repository/org/codehaus/mojo/animal-sniffer-annotations/1.27/animal-sniffer-annotations-1.27.pom
install -Dm644 %{SOURCE613} target/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.27/animal-sniffer-maven-plugin-1.27.jar
install -Dm644 %{SOURCE614} target/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.27/animal-sniffer-maven-plugin-1.27.pom
install -Dm644 %{SOURCE615} target/repository/org/codehaus/mojo/animal-sniffer-parent/1.27/animal-sniffer-parent-1.27.pom
install -Dm644 %{SOURCE616} target/repository/org/codehaus/mojo/build-helper-maven-plugin/3.6.1/build-helper-maven-plugin-3.6.1.jar
install -Dm644 %{SOURCE617} target/repository/org/codehaus/mojo/build-helper-maven-plugin/3.6.1/build-helper-maven-plugin-3.6.1.pom
install -Dm644 %{SOURCE618} target/repository/org/codehaus/mojo/extra-enforcer-rules/1.12.0/extra-enforcer-rules-1.12.0.jar
install -Dm644 %{SOURCE619} target/repository/org/codehaus/mojo/extra-enforcer-rules/1.12.0/extra-enforcer-rules-1.12.0.pom
install -Dm644 %{SOURCE620} target/repository/org/codehaus/mojo/java-boot-classpath-detector/1.27/java-boot-classpath-detector-1.27.jar
install -Dm644 %{SOURCE621} target/repository/org/codehaus/mojo/java-boot-classpath-detector/1.27/java-boot-classpath-detector-1.27.pom
install -Dm644 %{SOURCE622} target/repository/org/codehaus/mojo/mojo-parent/91/mojo-parent-91.pom
install -Dm644 %{SOURCE623} target/repository/org/codehaus/mojo/mojo-parent/95/mojo-parent-95.pom
install -Dm644 %{SOURCE624} target/repository/org/codehaus/mojo/mojo-parent/96/mojo-parent-96.pom
install -Dm644 %{SOURCE625} target/repository/org/codehaus/mojo/signature/java18/1.0/java18-1.0.signature
install -Dm644 %{SOURCE626} target/repository/org/codehaus/plexus/plexus/1.0.10/plexus-1.0.10.pom
install -Dm644 %{SOURCE627} target/repository/org/codehaus/plexus/plexus/1.0.11/plexus-1.0.11.pom
install -Dm644 %{SOURCE628} target/repository/org/codehaus/plexus/plexus/10/plexus-10.pom
install -Dm644 %{SOURCE629} target/repository/org/codehaus/plexus/plexus/13/plexus-13.pom
install -Dm644 %{SOURCE630} target/repository/org/codehaus/plexus/plexus/16/plexus-16.pom
install -Dm644 %{SOURCE631} target/repository/org/codehaus/plexus/plexus/17/plexus-17.pom
install -Dm644 %{SOURCE632} target/repository/org/codehaus/plexus/plexus/18/plexus-18.pom
install -Dm644 %{SOURCE633} target/repository/org/codehaus/plexus/plexus/19/plexus-19.pom
install -Dm644 %{SOURCE634} target/repository/org/codehaus/plexus/plexus/2.0.2/plexus-2.0.2.pom
install -Dm644 %{SOURCE635} target/repository/org/codehaus/plexus/plexus/2.0.5/plexus-2.0.5.pom
install -Dm644 %{SOURCE636} target/repository/org/codehaus/plexus/plexus/2.0.6/plexus-2.0.6.pom
install -Dm644 %{SOURCE637} target/repository/org/codehaus/plexus/plexus/20/plexus-20.pom
install -Dm644 %{SOURCE638} target/repository/org/codehaus/plexus/plexus/23/plexus-23.pom
install -Dm644 %{SOURCE639} target/repository/org/codehaus/plexus/plexus/24/plexus-24.pom
install -Dm644 %{SOURCE640} target/repository/org/codehaus/plexus/plexus/25/plexus-25.pom
install -Dm644 %{SOURCE641} target/repository/org/codehaus/plexus/plexus/4.0/plexus-4.0.pom
install -Dm644 %{SOURCE642} target/repository/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom
install -Dm644 %{SOURCE643} target/repository/org/codehaus/plexus/plexus/8/plexus-8.pom
install -Dm644 %{SOURCE644} target/repository/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.jar
install -Dm644 %{SOURCE645} target/repository/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.pom
install -Dm644 %{SOURCE646} target/repository/org/codehaus/plexus/plexus-archiver/4.10.2/plexus-archiver-4.10.2.pom
install -Dm644 %{SOURCE647} target/repository/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.jar
install -Dm644 %{SOURCE648} target/repository/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.pom
install -Dm644 %{SOURCE649} target/repository/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.jar
install -Dm644 %{SOURCE650} target/repository/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.pom
install -Dm644 %{SOURCE651} target/repository/org/codehaus/plexus/plexus-archiver/4.9.2/plexus-archiver-4.9.2.pom
install -Dm644 %{SOURCE652} target/repository/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.jar
install -Dm644 %{SOURCE653} target/repository/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.pom
install -Dm644 %{SOURCE654} target/repository/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.jar
install -Dm644 %{SOURCE655} target/repository/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.pom
install -Dm644 %{SOURCE656} target/repository/org/codehaus/plexus/plexus-classworlds/2.11.0/plexus-classworlds-2.11.0.jar
install -Dm644 %{SOURCE657} target/repository/org/codehaus/plexus/plexus-classworlds/2.11.0/plexus-classworlds-2.11.0.pom
install -Dm644 %{SOURCE658} target/repository/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.pom
install -Dm644 %{SOURCE659} target/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar
install -Dm644 %{SOURCE660} target/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom
install -Dm644 %{SOURCE661} target/repository/org/codehaus/plexus/plexus-compiler/2.16.2/plexus-compiler-2.16.2.pom
install -Dm644 %{SOURCE662} target/repository/org/codehaus/plexus/plexus-compiler-api/2.16.2/plexus-compiler-api-2.16.2.jar
install -Dm644 %{SOURCE663} target/repository/org/codehaus/plexus/plexus-compiler-api/2.16.2/plexus-compiler-api-2.16.2.pom
install -Dm644 %{SOURCE664} target/repository/org/codehaus/plexus/plexus-compiler-javac/2.16.2/plexus-compiler-javac-2.16.2.jar
install -Dm644 %{SOURCE665} target/repository/org/codehaus/plexus/plexus-compiler-javac/2.16.2/plexus-compiler-javac-2.16.2.pom
install -Dm644 %{SOURCE666} target/repository/org/codehaus/plexus/plexus-compiler-manager/2.16.2/plexus-compiler-manager-2.16.2.jar
install -Dm644 %{SOURCE667} target/repository/org/codehaus/plexus/plexus-compiler-manager/2.16.2/plexus-compiler-manager-2.16.2.pom
install -Dm644 %{SOURCE668} target/repository/org/codehaus/plexus/plexus-compilers/2.16.2/plexus-compilers-2.16.2.pom
install -Dm644 %{SOURCE669} target/repository/org/codehaus/plexus/plexus-component-annotations/1.5.4/plexus-component-annotations-1.5.4.pom
install -Dm644 %{SOURCE670} target/repository/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.jar
install -Dm644 %{SOURCE671} target/repository/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.pom
install -Dm644 %{SOURCE672} target/repository/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.jar
install -Dm644 %{SOURCE673} target/repository/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.pom
install -Dm644 %{SOURCE674} target/repository/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.jar
install -Dm644 %{SOURCE675} target/repository/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.pom
install -Dm644 %{SOURCE676} target/repository/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.jar
install -Dm644 %{SOURCE677} target/repository/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.pom
install -Dm644 %{SOURCE678} target/repository/org/codehaus/plexus/plexus-components/1.1.12/plexus-components-1.1.12.pom
install -Dm644 %{SOURCE679} target/repository/org/codehaus/plexus/plexus-components/4.0/plexus-components-4.0.pom
install -Dm644 %{SOURCE680} target/repository/org/codehaus/plexus/plexus-container-default/2.1.0/plexus-container-default-2.1.0.pom
install -Dm644 %{SOURCE681} target/repository/org/codehaus/plexus/plexus-containers/1.5.4/plexus-containers-1.5.4.pom
install -Dm644 %{SOURCE682} target/repository/org/codehaus/plexus/plexus-containers/2.0.0/plexus-containers-2.0.0.pom
install -Dm644 %{SOURCE683} target/repository/org/codehaus/plexus/plexus-containers/2.1.0/plexus-containers-2.1.0.pom
install -Dm644 %{SOURCE684} target/repository/org/codehaus/plexus/plexus-containers/2.2.0/plexus-containers-2.2.0.pom
install -Dm644 %{SOURCE685} target/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar
install -Dm644 %{SOURCE686} target/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.pom
install -Dm644 %{SOURCE687} target/repository/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.jar
install -Dm644 %{SOURCE688} target/repository/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.pom
install -Dm644 %{SOURCE689} target/repository/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.jar
install -Dm644 %{SOURCE690} target/repository/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.pom
install -Dm644 %{SOURCE691} target/repository/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.jar
install -Dm644 %{SOURCE692} target/repository/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.pom
install -Dm644 %{SOURCE693} target/repository/org/codehaus/plexus/plexus-interpolation/1.28/plexus-interpolation-1.28.jar
install -Dm644 %{SOURCE694} target/repository/org/codehaus/plexus/plexus-interpolation/1.28/plexus-interpolation-1.28.pom
install -Dm644 %{SOURCE695} target/repository/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.jar
install -Dm644 %{SOURCE696} target/repository/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.pom
install -Dm644 %{SOURCE697} target/repository/org/codehaus/plexus/plexus-io/3.4.2/plexus-io-3.4.2.pom
install -Dm644 %{SOURCE698} target/repository/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.jar
install -Dm644 %{SOURCE699} target/repository/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.pom
install -Dm644 %{SOURCE700} target/repository/org/codehaus/plexus/plexus-io/3.5.1/plexus-io-3.5.1.pom
install -Dm644 %{SOURCE701} target/repository/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.jar
install -Dm644 %{SOURCE702} target/repository/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.pom
install -Dm644 %{SOURCE703} target/repository/org/codehaus/plexus/plexus-java/1.5.2/plexus-java-1.5.2.jar
install -Dm644 %{SOURCE704} target/repository/org/codehaus/plexus/plexus-java/1.5.2/plexus-java-1.5.2.pom
install -Dm644 %{SOURCE705} target/repository/org/codehaus/plexus/plexus-languages/1.5.2/plexus-languages-1.5.2.pom
install -Dm644 %{SOURCE706} target/repository/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.jar
install -Dm644 %{SOURCE707} target/repository/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.pom
install -Dm644 %{SOURCE708} target/repository/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.jar
install -Dm644 %{SOURCE709} target/repository/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.pom
install -Dm644 %{SOURCE710} target/repository/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.jar
install -Dm644 %{SOURCE711} target/repository/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.pom
install -Dm644 %{SOURCE712} target/repository/org/codehaus/plexus/plexus-utils/1.4.5/plexus-utils-1.4.5.pom
install -Dm644 %{SOURCE713} target/repository/org/codehaus/plexus/plexus-utils/1.5.15/plexus-utils-1.5.15.pom
install -Dm644 %{SOURCE714} target/repository/org/codehaus/plexus/plexus-utils/2.0.4/plexus-utils-2.0.4.pom
install -Dm644 %{SOURCE715} target/repository/org/codehaus/plexus/plexus-utils/3.1.1/plexus-utils-3.1.1.pom
install -Dm644 %{SOURCE716} target/repository/org/codehaus/plexus/plexus-utils/3.3.0/plexus-utils-3.3.0.pom
install -Dm644 %{SOURCE717} target/repository/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar
install -Dm644 %{SOURCE718} target/repository/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom
install -Dm644 %{SOURCE719} target/repository/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.jar
install -Dm644 %{SOURCE720} target/repository/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.pom
install -Dm644 %{SOURCE721} target/repository/org/codehaus/plexus/plexus-utils/3.6.1/plexus-utils-3.6.1.jar
install -Dm644 %{SOURCE722} target/repository/org/codehaus/plexus/plexus-utils/3.6.1/plexus-utils-3.6.1.pom
install -Dm644 %{SOURCE723} target/repository/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.jar
install -Dm644 %{SOURCE724} target/repository/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.pom
install -Dm644 %{SOURCE725} target/repository/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.jar
install -Dm644 %{SOURCE726} target/repository/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.pom
install -Dm644 %{SOURCE727} target/repository/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.jar
install -Dm644 %{SOURCE728} target/repository/org/codehaus/plexus/plexus-velocity/1.2/plexus-velocity-1.2.pom
install -Dm644 %{SOURCE729} target/repository/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.jar
install -Dm644 %{SOURCE730} target/repository/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.pom
install -Dm644 %{SOURCE731} target/repository/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.jar
install -Dm644 %{SOURCE732} target/repository/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.pom
install -Dm644 %{SOURCE733} target/repository/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom
install -Dm644 %{SOURCE734} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M4/org.eclipse.sisu.inject-0.9.0.M4.jar
install -Dm644 %{SOURCE735} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M4/org.eclipse.sisu.inject-0.9.0.M4.pom
install -Dm644 %{SOURCE736} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.jar
install -Dm644 %{SOURCE737} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.pom
install -Dm644 %{SOURCE738} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.jar
install -Dm644 %{SOURCE739} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.pom
install -Dm644 %{SOURCE740} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.jar
install -Dm644 %{SOURCE741} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.pom
install -Dm644 %{SOURCE742} target/repository/org/eclipse/sisu/sisu-inject/0.9.0.M4/sisu-inject-0.9.0.M4.pom
install -Dm644 %{SOURCE743} target/repository/org/eclipse/sisu/sisu-inject/1.0.0/sisu-inject-1.0.0.pom
install -Dm644 %{SOURCE744} target/repository/org/eclipse/sisu/sisu-maven-plugin/1.0.0/sisu-maven-plugin-1.0.0.jar
install -Dm644 %{SOURCE745} target/repository/org/eclipse/sisu/sisu-maven-plugin/1.0.0/sisu-maven-plugin-1.0.0.pom
install -Dm644 %{SOURCE746} target/repository/org/fusesource/fusesource-pom/1.12/fusesource-pom-1.12.pom
install -Dm644 %{SOURCE747} target/repository/org/fusesource/jansi/jansi/2.4.3/jansi-2.4.3.jar
install -Dm644 %{SOURCE748} target/repository/org/fusesource/jansi/jansi/2.4.3/jansi-2.4.3.pom
install -Dm644 %{SOURCE749} target/repository/org/hamcrest/hamcrest/3.0/hamcrest-3.0.jar
install -Dm644 %{SOURCE750} target/repository/org/hamcrest/hamcrest/3.0/hamcrest-3.0.pom
install -Dm644 %{SOURCE751} target/repository/org/iq80/snappy/snappy/0.4/snappy-0.4.pom
install -Dm644 %{SOURCE752} target/repository/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.jar
install -Dm644 %{SOURCE753} target/repository/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.pom
install -Dm644 %{SOURCE754} target/repository/org/jsoup/jsoup/1.22.1/jsoup-1.22.1.jar
install -Dm644 %{SOURCE755} target/repository/org/jsoup/jsoup/1.22.1/jsoup-1.22.1.pom
install -Dm644 %{SOURCE756} target/repository/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.jar
install -Dm644 %{SOURCE757} target/repository/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.pom
install -Dm644 %{SOURCE758} target/repository/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom
install -Dm644 %{SOURCE759} target/repository/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom
install -Dm644 %{SOURCE760} target/repository/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
install -Dm644 %{SOURCE761} target/repository/org/junit/junit-bom/5.10.3/junit-bom-5.10.3.pom
install -Dm644 %{SOURCE762} target/repository/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
install -Dm644 %{SOURCE763} target/repository/org/junit/junit-bom/5.11.1/junit-bom-5.11.1.pom
install -Dm644 %{SOURCE764} target/repository/org/junit/junit-bom/5.11.2/junit-bom-5.11.2.pom
install -Dm644 %{SOURCE765} target/repository/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
install -Dm644 %{SOURCE766} target/repository/org/junit/junit-bom/5.12.1/junit-bom-5.12.1.pom
install -Dm644 %{SOURCE767} target/repository/org/junit/junit-bom/5.12.2/junit-bom-5.12.2.pom
install -Dm644 %{SOURCE768} target/repository/org/junit/junit-bom/5.13.0/junit-bom-5.13.0.pom
install -Dm644 %{SOURCE769} target/repository/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom
install -Dm644 %{SOURCE770} target/repository/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom
install -Dm644 %{SOURCE771} target/repository/org/junit/junit-bom/5.14.1/junit-bom-5.14.1.pom
install -Dm644 %{SOURCE772} target/repository/org/junit/junit-bom/5.14.2/junit-bom-5.14.2.pom
install -Dm644 %{SOURCE773} target/repository/org/junit/junit-bom/5.14.3/junit-bom-5.14.3.pom
install -Dm644 %{SOURCE774} target/repository/org/junit/junit-bom/5.14.4/junit-bom-5.14.4.pom
install -Dm644 %{SOURCE775} target/repository/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom
install -Dm644 %{SOURCE776} target/repository/org/junit/junit-bom/5.8.0-M1/junit-bom-5.8.0-M1.pom
install -Dm644 %{SOURCE777} target/repository/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom
install -Dm644 %{SOURCE778} target/repository/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.jar
install -Dm644 %{SOURCE779} target/repository/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.pom
install -Dm644 %{SOURCE780} target/repository/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.jar
install -Dm644 %{SOURCE781} target/repository/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.pom
install -Dm644 %{SOURCE782} target/repository/org/junit/platform/junit-platform-commons/1.12.2/junit-platform-commons-1.12.2.jar
install -Dm644 %{SOURCE783} target/repository/org/junit/platform/junit-platform-commons/1.12.2/junit-platform-commons-1.12.2.pom
install -Dm644 %{SOURCE784} target/repository/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.jar
install -Dm644 %{SOURCE785} target/repository/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.pom
install -Dm644 %{SOURCE786} target/repository/org/junit/platform/junit-platform-engine/1.12.2/junit-platform-engine-1.12.2.jar
install -Dm644 %{SOURCE787} target/repository/org/junit/platform/junit-platform-engine/1.12.2/junit-platform-engine-1.12.2.pom
install -Dm644 %{SOURCE788} target/repository/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.jar
install -Dm644 %{SOURCE789} target/repository/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.pom
install -Dm644 %{SOURCE790} target/repository/org/junit/platform/junit-platform-launcher/1.12.2/junit-platform-launcher-1.12.2.jar
install -Dm644 %{SOURCE791} target/repository/org/junit/platform/junit-platform-launcher/1.12.2/junit-platform-launcher-1.12.2.pom
install -Dm644 %{SOURCE792} target/repository/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.jar
install -Dm644 %{SOURCE793} target/repository/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.pom
install -Dm644 %{SOURCE794} target/repository/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar
install -Dm644 %{SOURCE795} target/repository/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.pom
install -Dm644 %{SOURCE796} target/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar
install -Dm644 %{SOURCE797} target/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom
install -Dm644 %{SOURCE798} target/repository/org/objenesis/objenesis/3.3/objenesis-3.3.jar
install -Dm644 %{SOURCE799} target/repository/org/objenesis/objenesis/3.3/objenesis-3.3.pom
install -Dm644 %{SOURCE800} target/repository/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom
install -Dm644 %{SOURCE801} target/repository/org/objenesis/objenesis-parent/3.3/objenesis-parent-3.3.pom
install -Dm644 %{SOURCE802} target/repository/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.jar
install -Dm644 %{SOURCE803} target/repository/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.pom
install -Dm644 %{SOURCE804} target/repository/org/ow2/asm/asm/9.6/asm-9.6.jar
install -Dm644 %{SOURCE805} target/repository/org/ow2/asm/asm/9.6/asm-9.6.pom
install -Dm644 %{SOURCE806} target/repository/org/ow2/asm/asm/9.8/asm-9.8.pom
install -Dm644 %{SOURCE807} target/repository/org/ow2/asm/asm/9.9.1/asm-9.9.1.jar
install -Dm644 %{SOURCE808} target/repository/org/ow2/asm/asm/9.9.1/asm-9.9.1.pom
install -Dm644 %{SOURCE809} target/repository/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
install -Dm644 %{SOURCE810} target/repository/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.jar
install -Dm644 %{SOURCE811} target/repository/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.pom
install -Dm644 %{SOURCE812} target/repository/org/slf4j/jcl-over-slf4j/1.7.36/jcl-over-slf4j-1.7.36.jar
install -Dm644 %{SOURCE813} target/repository/org/slf4j/jcl-over-slf4j/1.7.36/jcl-over-slf4j-1.7.36.pom
install -Dm644 %{SOURCE814} target/repository/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom
install -Dm644 %{SOURCE815} target/repository/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
install -Dm644 %{SOURCE816} target/repository/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom
install -Dm644 %{SOURCE817} target/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.pom
install -Dm644 %{SOURCE818} target/repository/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.jar
install -Dm644 %{SOURCE819} target/repository/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.pom
install -Dm644 %{SOURCE820} target/repository/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom
install -Dm644 %{SOURCE821} target/repository/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom
install -Dm644 %{SOURCE822} target/repository/org/slf4j/slf4j-parent/1.7.5/slf4j-parent-1.7.5.pom
install -Dm644 %{SOURCE823} target/repository/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36-sources.jar
install -Dm644 %{SOURCE824} target/repository/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36.jar
install -Dm644 %{SOURCE825} target/repository/org/slf4j/slf4j-simple/1.7.36/slf4j-simple-1.7.36.pom
install -Dm644 %{SOURCE826} target/repository/org/sonatype/forge/forge-parent/10/forge-parent-10.pom
install -Dm644 %{SOURCE827} target/repository/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
install -Dm644 %{SOURCE828} target/repository/org/sonatype/forge/forge-parent/6/forge-parent-6.pom
install -Dm644 %{SOURCE829} target/repository/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
install -Dm644 %{SOURCE830} target/repository/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
install -Dm644 %{SOURCE831} target/repository/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar
install -Dm644 %{SOURCE832} target/repository/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom
install -Dm644 %{SOURCE833} target/repository/org/sonatype/sisu/inject/guice-bean/1.4.2/guice-bean-1.4.2.pom
install -Dm644 %{SOURCE834} target/repository/org/sonatype/sisu/inject/guice-plexus/1.4.2/guice-plexus-1.4.2.pom
install -Dm644 %{SOURCE835} target/repository/org/sonatype/sisu/sisu-guice/2.1.7/sisu-guice-2.1.7.pom
install -Dm644 %{SOURCE836} target/repository/org/sonatype/sisu/sisu-inject/1.4.2/sisu-inject-1.4.2.pom
install -Dm644 %{SOURCE837} target/repository/org/sonatype/sisu/sisu-inject-bean/1.4.2/sisu-inject-bean-1.4.2.pom
install -Dm644 %{SOURCE838} target/repository/org/sonatype/sisu/sisu-inject-plexus/1.4.2/sisu-inject-plexus-1.4.2.pom
install -Dm644 %{SOURCE839} target/repository/org/sonatype/sisu/sisu-parent/1.4.2/sisu-parent-1.4.2.pom
install -Dm644 %{SOURCE840} target/repository/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
install -Dm644 %{SOURCE841} target/repository/org/tukaani/xz/1.10/xz-1.10.jar
install -Dm644 %{SOURCE842} target/repository/org/tukaani/xz/1.10/xz-1.10.pom
install -Dm644 %{SOURCE843} target/repository/org/tukaani/xz/1.11/xz-1.11.jar
install -Dm644 %{SOURCE844} target/repository/org/tukaani/xz/1.11/xz-1.11.pom
install -Dm644 %{SOURCE845} target/repository/org/tukaani/xz/1.9/xz-1.9.jar
install -Dm644 %{SOURCE846} target/repository/org/tukaani/xz/1.9/xz-1.9.pom
install -Dm644 %{SOURCE847} target/repository/org/xmlunit/xmlunit-core/2.11.0/xmlunit-core-2.11.0.jar
install -Dm644 %{SOURCE848} target/repository/org/xmlunit/xmlunit-core/2.11.0/xmlunit-core-2.11.0.pom
install -Dm644 %{SOURCE849} target/repository/org/xmlunit/xmlunit-matchers/2.11.0/xmlunit-matchers-2.11.0.jar
install -Dm644 %{SOURCE850} target/repository/org/xmlunit/xmlunit-matchers/2.11.0/xmlunit-matchers-2.11.0.pom
install -Dm644 %{SOURCE851} target/repository/org/xmlunit/xmlunit-parent/2.11.0/xmlunit-parent-2.11.0.pom
install -Dm644 %{SOURCE852} target/repository/org/yaml/snakeyaml/2.5/snakeyaml-2.5.jar
install -Dm644 %{SOURCE853} target/repository/org/yaml/snakeyaml/2.5/snakeyaml-2.5.pom
install -Dm644 %{SOURCE854} target/repository/oro/oro/2.0.8/oro-2.0.8.jar
install -Dm644 %{SOURCE855} target/repository/oro/oro/2.0.8/oro-2.0.8.pom
install -Dm644 %{SOURCE856} target/repository/xml-apis/xml-apis/1.0.b2/xml-apis-1.0.b2.pom
%if %{with bootstrap}
mkdir -p target/bootstrap
tar -xf %{SOURCE1} -C target/bootstrap --strip-components=1
%endif

%build
# Resolve the selected JDK independently of this noarch package's libdir.
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")"
export MAVEN_SKIP_RC=1
unset MAVEN_ARGS MAVEN_OPTS MAVEN_DEBUG_OPTS MAVEN_BASEDIR MAVEN_CONFIG
%if %{with bootstrap}
MAVEN="$PWD/target/bootstrap/bin/mvn"
%else
MAVEN=mvn
%endif
# Use upstream defaults instead of the builder's user or system configuration.
"$MAVEN" --batch-mode --offline --no-transfer-progress \
    --settings apache-maven/src/conf/settings.xml \
    --global-settings apache-maven/src/conf/settings.xml \
    --toolchains apache-maven/src/conf/toolchains.xml \
    --global-toolchains apache-maven/src/conf/toolchains.xml \
    -Dmaven.repo.local="$PWD/target/repository" \
    -DbuildNumber=openRuyi -DskipTests package
mkdir -p target/maven-dist
tar -xf apache-maven/target/apache-maven-%{version}-bin.tar.gz \
    -C target/maven-dist --strip-components=1
# Use Jansi's Java fallback on every architecture, including RISC-V.
zip -d target/maven-dist/lib/jansi-*.jar 'org/fusesource/jansi/internal/native/*'
rm -rf target/maven-dist/lib/jansi-native
rm -f target/maven-dist/bin/*.cmd

%install
install -d %{buildroot}%{maven_home} %{buildroot}%{_bindir}
cp -a target/maven-dist/bin target/maven-dist/boot target/maven-dist/lib %{buildroot}%{maven_home}/
install -d %{buildroot}%{_sysconfdir}/maven
cp -a target/maven-dist/conf/. %{buildroot}%{_sysconfdir}/maven/
mv %{buildroot}%{maven_home}/bin/m2.conf %{buildroot}%{_sysconfdir}/maven/
ln -s ../../..%{_sysconfdir}/maven %{buildroot}%{maven_home}/conf
ln -s ../../../..%{_sysconfdir}/maven/m2.conf %{buildroot}%{maven_home}/bin/m2.conf
# Absolute targets also work when the launcher is found through /bin.
for command in mvn mvnDebug mvnyjp; do
    ln -s %{maven_home}/bin/$command %{buildroot}%{_bindir}/$command
done
%fdupes %{buildroot}%{maven_home}

%check
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")"
export MAVEN_SKIP_RC=1
unset MAVEN_ARGS MAVEN_OPTS MAVEN_DEBUG_OPTS MAVEN_BASEDIR MAVEN_CONFIG
# Run the upstream unit tests with Maven built above, still fully offline.
./target/maven-dist/bin/mvn --batch-mode --offline --no-transfer-progress \
    --settings apache-maven/src/conf/settings.xml \
    --global-settings apache-maven/src/conf/settings.xml \
    --toolchains apache-maven/src/conf/toolchains.xml \
    --global-toolchains apache-maven/src/conf/toolchains.xml \
    -Dmaven.repo.local="$PWD/target/repository" \
    -DbuildNumber=openRuyi test
%{buildroot}%{maven_home}/bin/mvn --version > maven-version.txt
grep -F 'Apache Maven %{version}' maven-version.txt

# Keep the noarch claim valid when updating the upstream distribution.
for jar in %{buildroot}%{maven_home}/boot/*.jar %{buildroot}%{maven_home}/lib/*.jar; do
    unzip -t "$jar" > /dev/null
    unzip -Z1 "$jar" > jar-contents.txt
    if grep -E '\.(so([.][0-9]+)*|dll|dylib|jnilib|exe)$' jar-contents.txt; then
        echo "Unexpected native binary in $jar" >&2
        exit 1
    fi
done

%files
%license target/maven-dist/LICENSE target/maven-dist/NOTICE
%doc target/maven-dist/README.txt
%{_bindir}/mvn
%{_bindir}/mvnDebug
%{_bindir}/mvnyjp
%dir %{_sysconfdir}/maven
%dir %{_sysconfdir}/maven/logging
%config(noreplace) %{_sysconfdir}/maven/m2.conf
%config(noreplace) %{_sysconfdir}/maven/settings.xml
%config(noreplace) %{_sysconfdir}/maven/toolchains.xml
%config(noreplace) %{_sysconfdir}/maven/logging/simplelogger.properties
%dir %{maven_home}
%{maven_home}/bin
%dir %{maven_home}/boot
%{maven_home}/boot/*.jar
%license %{maven_home}/boot/*.license
%{maven_home}/conf
%dir %{maven_home}/lib
%{maven_home}/lib/*.jar
%license %{maven_home}/lib/*.license
%{maven_home}/lib/ext

%changelog
%autochangelog
