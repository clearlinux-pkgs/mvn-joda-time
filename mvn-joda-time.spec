#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-joda-time
Version  : 2.2
Release  : 6
URL      : https://github.com/JodaOrg/joda-time/archive/v2.2.tar.gz
Source0  : https://github.com/JodaOrg/joda-time/archive/v2.2.tar.gz
Source1  : https://repo1.maven.org/maven2/joda-time/joda-time/1.6/joda-time-1.6.jar
Source2  : https://repo1.maven.org/maven2/joda-time/joda-time/1.6/joda-time-1.6.pom
Source3  : https://repo1.maven.org/maven2/joda-time/joda-time/2.0/joda-time-2.0.jar
Source4  : https://repo1.maven.org/maven2/joda-time/joda-time/2.0/joda-time-2.0.pom
Source5  : https://repo1.maven.org/maven2/joda-time/joda-time/2.10/joda-time-2.10.jar
Source6  : https://repo1.maven.org/maven2/joda-time/joda-time/2.10/joda-time-2.10.pom
Source7  : https://repo1.maven.org/maven2/joda-time/joda-time/2.2/joda-time-2.2.jar
Source8  : https://repo1.maven.org/maven2/joda-time/joda-time/2.2/joda-time-2.2.pom
Source9  : https://repo1.maven.org/maven2/joda-time/joda-time/2.5/joda-time-2.5.jar
Source10  : https://repo1.maven.org/maven2/joda-time/joda-time/2.5/joda-time-2.5.pom
Source11  : https://repo1.maven.org/maven2/joda-time/joda-time/2.7/joda-time-2.7.jar
Source12  : https://repo1.maven.org/maven2/joda-time/joda-time/2.7/joda-time-2.7.pom
Source13  : https://repo1.maven.org/maven2/joda-time/joda-time/2.8.2/joda-time-2.8.2.jar
Source14  : https://repo1.maven.org/maven2/joda-time/joda-time/2.8.2/joda-time-2.8.2.pom
Source15  : https://repo1.maven.org/maven2/joda-time/joda-time/2.9.3/joda-time-2.9.3.jar
Source16  : https://repo1.maven.org/maven2/joda-time/joda-time/2.9.3/joda-time-2.9.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-joda-time-data = %{version}-%{release}
Requires: mvn-joda-time-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
Joda-Time
=========
Joda-Time is a date and time library that vastly improves on the JDK.

%package data
Summary: data components for the mvn-joda-time package.
Group: Data

%description data
data components for the mvn-joda-time package.


%package license
Summary: license components for the mvn-joda-time package.
Group: Default

%description license
license components for the mvn-joda-time package.


%prep
%setup -q -n joda-time-2.2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-joda-time
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-joda-time/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/1.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/1.6/joda-time-1.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/1.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/1.6/joda-time-1.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.10
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.10/joda-time-2.10.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.10
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.10/joda-time-2.10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.2/joda-time-2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.2/joda-time-2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.5
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.5/joda-time-2.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.5
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.5/joda-time-2.5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.7
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.7/joda-time-2.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.7
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.7/joda-time-2.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.8.2
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.8.2/joda-time-2.8.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.8.2
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.8.2/joda-time-2.8.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.9.3
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.9.3/joda-time-2.9.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.9.3
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/joda-time/joda-time/2.9.3/joda-time-2.9.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/joda-time/joda-time/1.6/joda-time-1.6.jar
/usr/share/java/.m2/repository/joda-time/joda-time/1.6/joda-time-1.6.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.10/joda-time-2.10.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.10/joda-time-2.10.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.2/joda-time-2.2.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.2/joda-time-2.2.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.5/joda-time-2.5.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.5/joda-time-2.5.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.7/joda-time-2.7.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.7/joda-time-2.7.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.8.2/joda-time-2.8.2.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.8.2/joda-time-2.8.2.pom
/usr/share/java/.m2/repository/joda-time/joda-time/2.9.3/joda-time-2.9.3.jar
/usr/share/java/.m2/repository/joda-time/joda-time/2.9.3/joda-time-2.9.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-joda-time/LICENSE.txt
