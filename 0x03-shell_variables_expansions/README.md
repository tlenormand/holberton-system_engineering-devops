# 0x03. Shell, init files, variables and expansions

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/G5p7gU70olYFxbN_DfuXpQ" title="Expansions" target="_blank">Expansions</a> </li>
<li><a href="/rltoken/C2JAWjeSMt5I0EmuplF32A" title="Shell Arithmetic" target="_blank">Shell Arithmetic</a> </li>
<li><a href="/rltoken/zj7i19F9iE9eUdjBgR6C3Q" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/lHvzUhLmLgBVfsoJzYDj_w" title="Shell initialization files" target="_blank">Shell initialization files</a> </li>
<li><a href="/rltoken/5JiNabFuBFXpJKqGGh9EjQ" title="The alias Command" target="_blank">The alias Command</a> </li>
<li><a href="/rltoken/lPsbE1Ecs4tmGU2RuTZ5YA" title="Technical Writing" target="_blank">Technical Writing</a></li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>printenv</code></li>
<li><code>set</code></li>
<li><code>unset</code></li>
<li><code>export</code></li>
<li><code>alias</code></li>
<li><code>unalias</code></li>
<li><code>.</code></li>
<li><code>source</code></li>
<li><code>printf</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/73iGFpBHBJtQgO1RmDM-_A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What happens when you type <code>$ ls -l *.txt</code></li>
</ul>

<h3>Shell Initialization Files</h3>

<ul>
<li>What are the <code>/etc/profile</code> file and the <code>/etc/profile.d</code> directory</li>
<li>What is the <code>~/.bashrc</code> file</li>
</ul>

<h3>Variables</h3>

<ul>
<li>What is the difference between a local and a global variable</li>
<li>What is a reserved variable</li>
<li>How to create, update and delete shell variables</li>
<li>What are the roles of the following reserved variables: HOME, PATH, PS1</li>
<li>What are special parameters</li>
<li>What is the special parameter <code>$?</code>?</li>
</ul>

<h3>Expansions</h3>

<ul>
<li>What is expansion and how to use them</li>
<li>What is the difference between single and double quotes and how to use them properly</li>
<li>How to do command substitution with <code>$()</code> and backticks</li>
</ul>

<h3>Shell Arithmetic</h3>

<ul>
<li>How to perform arithmetic operations with the shell</li>
</ul>

<h3>The <code>alias</code> Command</h3>

<ul>
<li>How to create an alias</li>
<li>How to list aliases</li>
<li>How to temporarily disable an alias</li>
</ul>

<h3>Other <code>help</code> pages</h3>

<ul>
<li>How to execute commands from a file in the current shell</li>
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
<li>You are not allowed to use <code>&amp;&amp;</code>, <code>||</code> or <code>;</code></li>
<li>You are not allowed to use <code>bc</code>, <code>sed</code> or <code>awk</code></li>
<li>All your files must be executable</li>
</ul>

<h2>More Info</h2>

<p>Read your <code>/etc/profile</code>, <code>/etc/inputrc</code> and <code>~/.bashrc</code> files.</p>

<p>Look at some files in the <code>/etc/profile.d</code> directory.</p>

<p>Note: You do not have to learn about <code>awk</code>, <code>tar</code>, <code>bzip2</code>, <code>date</code>, <code>scp</code>, <code>ulimit</code>, <code>umask</code>, or shell scripting, yet.</p>

<h3>Manual QA Review</h3>

<p><strong>It is your responsibility to request a review for your blog from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong></p>
