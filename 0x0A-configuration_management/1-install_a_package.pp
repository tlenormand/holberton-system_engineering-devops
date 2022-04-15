# install puppet-lint 2.5.0
exec {'sudo gem install puppet-lint -v 2.5.0':
  path    => ['/usr/bin'],
}
