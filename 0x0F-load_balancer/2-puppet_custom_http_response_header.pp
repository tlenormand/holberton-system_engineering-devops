# Add a custom HTTP header with Puppet
exec {'apt update -y':
  path => ['/usr/bin'],
}

exec {'apt install -y nginx':
  path => ['/usr/bin'],
}

file_line { '/etc/nginx/sites-available/default':
  path => '/etc/nginx/sites-available/default',
  line => '    add_header X-Served-By $(hostname);',
}

exec {'service nginx restart':
  path => ['/usr/bin'],
}
