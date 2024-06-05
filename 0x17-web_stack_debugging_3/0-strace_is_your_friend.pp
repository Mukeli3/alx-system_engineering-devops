# Puppet script fix and automate Apache returning a 500 error

$f_check = '/var/www/html/wp-settings.php'

exec { 'rep_lne':
    command => "sed -i 's/phpp/php/g' ${f_check}",
    path    => ['/bin','/usr/bin']
}
