# change ssh_config file
file_line { 'ssh_config PasswordAuthentication':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}

file_line { 'ssh_config IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}
