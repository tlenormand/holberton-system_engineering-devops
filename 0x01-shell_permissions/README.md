# 0x01. Shell, permissions

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/5uUsOHrMbVBOpZFteNyBLg" title="Permissions" target="_blank">Permissions</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>chmod</code></li>
<li><code>sudo</code></li>
<li><code>su</code></li>
<li><code>chown</code></li>
<li><code>chgrp</code></li>
<li><code>id</code></li>
<li><code>groups</code></li>
<li><code>whoami</code></li>
<li><code>adduser</code></li>
<li><code>useradd</code></li>
<li><code>addgroup</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/Y35d0Jims8dedreTJJiaAw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>Permissions</h3>

<ul>
<li>What do the commands <code>chmod</code>, <code>sudo</code>, <code>su</code>, <code>chown</code>, <code>chgrp</code> do</li>
<li>Linux file permissions</li>
<li>How to represent each of the three sets of permissions (owner, group, and other) as a single digit</li>
<li>How to change permissions, owner and group of a file</li>
<li>Why can&rsquo;t a normal user <code>chown</code> a file</li>
<li>How to run a command with root privileges</li>
<li>How to change user ID or become superuser<br></li>
</ul>

<h3>Other Man Pages</h3>

<ul>
<li>How to create a user</li>
<li>How to create a group</li>
<li>How to print real and effective user and group IDs</li>
<li>How to print the groups a user is in</li>
<li>How to print the effective userid</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your scripts will be tested on Ubuntu 20.04 LTS</li>
<li>All your scripts should be exactly two lines long (<code>$ wc -l file</code> should print 2)</li>
<li>All your files should end with a new line (<a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">why?</a>)</li>
<li>The first line of all your files should be exactly <code>#!/bin/bash</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, describing what each script is doing</li>
<li>You are not allowed to use backticks, <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
<li>All your files must be executable</li>
</ul>
