wildfly-as-rpm
==============

This is POC RPM with WildFly for OpenShift. This is not following the packaging guidelines.

Use `spectool -g wildfly-as.spec` to get the wildfly distribution. The spectool command is in the rpmdevtools package; use `yum install rpmdevtools` to get the spectool command.


## Full step from clean install ##
1. yum install rpmdevtools
2. rpmdev-setuptree
2. spectool -g wildfly-as.spec
3. mv wildfly-8.0.0.Beta1.tar.gz ~/rpmbuild/SOURCES/
4. rpmbuild -ba wildfly-as.spec
