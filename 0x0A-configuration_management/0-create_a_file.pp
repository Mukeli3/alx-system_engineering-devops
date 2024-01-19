#!usr/bin/pup
# Creating a file using Puppet
file { '\etc':
  ensure => symlink,
  target => '/tmp/school'
  group  => 'www-data'
  owner  => 'www-data'
  mode   => '0744'
}
