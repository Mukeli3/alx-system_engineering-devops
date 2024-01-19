#!usr/bin/pup
# Creating a file using Puppet
file { '/tmp/school':
  ensure => 'present',
content  => 'I love Puppet',
  group  => 'www-data',
  owner  => 'www-data',
  mode   => '0744',
}
