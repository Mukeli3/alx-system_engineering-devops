#!/usr/bin/pup
# Puppet
file_line { 'Remove passwd auth':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}

file_line { 'identityFille':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/school',
}
