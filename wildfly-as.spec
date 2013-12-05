%global namedreltag .Beta1
%global namedversion %{version}%{?namedreltag}

# We don't need to repack jars for this package
%define __jar_repack %{nil}
# There are some arch dependent files, ignore them
%define _binaries_in_noarch_packages_terminate_build 0

Name:		      wildfly-as
Version:	    8.0.0
Release:	    0.1%{namedreltag}%{?dist}
Summary:	    WildFly Application Server

License:	    LGPLv2+ and ASL 2.0 and GPLv2 with exceptions
URL:		      http://wildfly.org/
Source0:	    http://download.jboss.org/wildfly/%{namedversion}/wildfly-%{namedversion}.tar.gz

Requires:	    java-devel >= 1:1.7

BuildArch:     noarch

%description
WildFly Application Server (formerly known as JBoss Application Server) is the
latest release in a series of WildFly offerings. WildFly Application Server, is
a fast, powerful, implementation of the Java Enterprise Edition 6
specification.  The state-of-the-art architecture built on the Modular Service
Container enables services on-demand when your application requires them.

Please note that this package is not following the Fedora guidelines. This
package is created to make the OpenShift cartridge for WildFly.

%prep
%setup -q -n wildfly-%{namedversion}

%install
install -d -m 755 %{buildroot}/opt/wildfly-%{namedversion}

cp -r * %{buildroot}/opt/wildfly-%{namedversion}

%files
/opt/wildfly-%{namedversion}
%doc README.txt README.txt

%changelog
* Thu Dec 05 2013 Marek Goldmann <mgoldman@redhat.com> - 8.0.0-0.1.Beta1
- Initial packaging


