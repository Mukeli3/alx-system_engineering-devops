#!usr/bin/pup
# Creating a file using Puppet
file { '/tmp/school':
  ensure => 'present'
  group  => 'www-data'
  owner  => 'www-data'
  mode   => '0744'
}
