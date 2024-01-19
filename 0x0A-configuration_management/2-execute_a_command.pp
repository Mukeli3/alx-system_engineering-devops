#!/usr/bin/pup
# Kill a process
exec { 'pkill':
command  => 'pkill killmenow',
provider => 'shell',
}
