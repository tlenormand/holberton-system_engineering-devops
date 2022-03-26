# 0x02. Shell, I/O Redirections and filters

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Kwe7oA6N7iWf8kfnteJLrA" title="Shell, I/O Redirection" target="_blank">Shell, I/O Redirection</a> </li>
<li><a href="/rltoken/6G_Cu3hczr_SdaSzlunjZg" title="Special Characters" target="_blank">Special Characters</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>echo</code></li>
<li><code>cat</code></li>
<li><code>head</code></li>
<li><code>tail</code></li>
<li><code>find</code></li>
<li><code>wc</code></li>
<li><code>sort</code></li>
<li><code>uniq</code></li>
<li><code>grep</code></li>
<li><code>tr</code></li>
<li><code>rev</code></li>
<li><code>cut</code></li>
<li><code>passwd (5)</code> (<em>i.e. <code>man 5 passwd</code></em>)</li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/35eszk_xq3C3s4TzIrb-ng" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>Shell, I/O Redirection</h3>

<ul>
<li>What do the commands <code>head</code>, <code>tail</code>, <code>find</code>, <code>wc</code>, <code>sort</code>, <code>uniq</code>, <code>grep</code>, <code>tr</code> do</li>
<li>How to redirect standard output to a file</li>
<li>How to get standard input from a file instead of the keyboard</li>
<li>How to send the output from one program to the input of another program</li>
<li>How to combine commands and filters with redirections</li>
</ul>

<h3>Special Characters</h3>

<ul>
<li>What are special characters</li>
<li>Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them</li>
</ul>

<h3>Other Man Pages</h3>

<ul>
<li>How to display a line of text</li>
<li>How to concatenate files and print on the standard output</li>
<li>How to reverse a string</li>
<li>How to remove sections from each line of files</li>
<li>What is the <code>/etc/passwd</code> file and what is its format</li>
<li>What is the <code>/etc/shadow</code> file and what is its format</li>
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
<li>You are not allowed to use <code>sed</code> or <code>awk</code></li>
</ul>

<h2>More Info</h2>

<p>Read your <code>/etc/passwd</code> and <code>/etc/shadow</code> files.</p>

<p>Note: You do not have to learn about <code>fmt</code>, <code>pr</code>, <code>du</code>, <code>gzip</code>, <code>tar</code>, <code>lpr</code>, <code>sed</code> and <code>awk</code> yet.</p>
