#!/bin/sh

BASEDIR=$(dirname "$0")

ldapadd -h localhost -x -D 'cn=admin,cn=config' -w mysecretpassword -f $BASEDIR/ap.ldif
ldapadd -h localhost -x -D 'cn=admin,cn=config' -w mysecretpassword -f $BASEDIR/member_add.ldif
ldapadd -h localhost -x -D 'cn=admin,cn=config' -w mysecretpassword -f $BASEDIR/member_config.ldif
ldapadd -h localhost -x -D 'cn=admin,dc=ldap,dc=t3worldwide,dc=com' -w mysecretpassword -f $BASEDIR/ppolicy.ldif
ldapmodify -h localhost -x -D 'cn=admin,cn=config' -w mysecretpassword -f $BASEDIR/change_policy.ldif
ldapadd -h localhost -x -D 'cn=admin,dc=ldap,dc=t3worldwide,dc=com' -w mysecretpassword -f $BASEDIR/test_users.ldif
ldapadd -h localhost -x -D 'cn=admin,dc=ldap,dc=t3worldwide,dc=com' -w mysecretpassword -f $BASEDIR/test-ldap-ou-qa.ldif
ldapmodify -h localhost -x -D 'cn=admin,cn=config' -w mysecretpassword -f $BASEDIR/config_access.ldif
