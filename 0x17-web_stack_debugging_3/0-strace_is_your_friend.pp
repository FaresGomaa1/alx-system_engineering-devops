# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache configuration issue causing 500 Internal Server Error

file { '/var/www/html/index.html':
  ensure  => file,
  content => '<html><body><h1>It works!</h1></body></html>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

service { 'apache2':
  ensure => running,
  enable => true,
}

file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  source  => 'puppet:///modules/your_module/000-default.conf',
  notify  => Service['apache2'],
}
