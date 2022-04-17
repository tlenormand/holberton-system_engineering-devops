# change ssh_config file
file_line { 'ssh_config PasswordAuthentication':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
}

file_line { 'ssh_config PasswordAuthentication':
    ensure  => 'present',
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/holberton',
}
