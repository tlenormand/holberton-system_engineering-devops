# Add a custom HTTP header with Puppet
exec {'apt update -y':
  path => ['/usr/bin'],
}

exec {'apt install -y nginx':
  path => ['/usr/bin'],
}

nginx::nginx_vhosts:
  add_header:
    X-Served-By: $(hostname)

exec {'service nginx restart':
  path => ['/usr/bin'],
}
