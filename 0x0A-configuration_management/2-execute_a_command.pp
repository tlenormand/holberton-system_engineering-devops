exec { 'pkill':
  path    => '/usr/bin:/usr/sbin:/bin',
  command => 'pkill killmenow',
}
