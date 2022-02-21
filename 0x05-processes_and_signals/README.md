# 0x05. Processes and signals

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/FcpEdqz8hau7eEB0Pi8Ong" title="Linux PID" target="_blank">Linux PID</a> </li>
<li><a href="/rltoken/hX_t2YK0erLPbdTq0-uKwQ" title="Linux process" target="_blank">Linux process</a> </li>
<li><a href="/rltoken/SojW4zvL8j1yaoa7_NM6rA" title="Linux signal" target="_blank">Linux signal</a> </li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>ps</code></li>
<li><code>pgrep</code></li>
<li><code>pkill</code></li>
<li><code>kill</code></li>
<li><code>exit</code></li>
<li><code>trap</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lg0QA0Ewi3RfiD5UUUNUXw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a PID</li>
<li>What is a process</li>
<li>How to find a process&rsquo; PID</li>
<li>How to kill a process</li>
<li>What is a signal</li>
<li>What are the 2 signals that cannot be ignored</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.7.0</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>More Info</h2>

<p>For those who want to know more and learn about all signals, check out <a href="/rltoken/yhnvsg_MvXuhE84jKTeXkQ" title="this article" target="_blank">this article</a>.</p>

</div>
</br>

## 0. What is my PID
<p>Write a Bash script that displays its own PID.</p>

<pre><code>sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
</code></pre>
</br>

## 1. List your processes
<p>Write a Bash script that displays a list of currently running processes.</p>

<p>Requirements:</p>

<ul>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display in a user-oriented format</li>
<li>Show process hierarchy</li>
</ul>

<pre><code>sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
root        12  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [watchdog/0]
root        13  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [khelper]
root        14  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kdevtmpfs]
root        15  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [netns]
root        16  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [writeback]
root        17  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kintegrityd]
root        18  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [bioset]
root        19  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kworker/u3:0]
root        20  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kblockd]
root        21  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [ata_sff]
root        22  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khubd]
root        23  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [md]
root        24  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [devfreq_wq]
root        25  0.0  0.0      0     0 ?        S    Feb13   0:41  \_ [kworker/0:1]
root        27  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khungtaskd]
root        28  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kswapd0]
root        29  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [vmstat]
root        30  0.0  0.0      0     0 ?        SN   Feb13   0:00  \_ [ksmd]
root        31  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [fsnotify_mark]
root        32  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ecryptfs-kthrea]
root        33  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [crypto]
root        45  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kthrotld]
root        46  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:1]
root        65  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [deferwq]
root        66  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [charger_manager]
root       108  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kpsmoused]
root       125  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [scsi_eh_0]
root       126  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:2]
root       172  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [jbd2/sda1-8]
root       173  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [ext4-rsv-conver]
root       409  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [iprt]
root       549  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kworker/u3:1]
root       808  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kauditd]
root       834  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [rpciod]
root       846  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [nfsiod]
root         1  0.0  0.4  33608  2168 ?        Ss   Feb13   0:00 /sbin/init
root       373  0.0  0.0  19472   408 ?        S    Feb13   0:00 upstart-udev-bridge --daemon
root       378  0.0  0.2  49904  1088 ?        Ss   Feb13   0:00 /lib/systemd/systemd-udevd --daemon
root       518  0.0  0.1  23416   644 ?        Ss   Feb13   0:00 rpcbind
statd      547  0.0  0.1  21536   852 ?        Ss   Feb13   0:00 rpc.statd -L
sylvain@ubuntu$
</code></pre>
</br>

## 2. Show your Bash PID
<p>Using your previous exercise command, write a Bash script that displays lines containing the <code>bash</code> word, thus allowing you to easily get the PID of your Bash process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>pgrep</code></li>
<li>The third line of your script must be <code># shellcheck disable=SC2009</code> (for more info about ignoring <code>shellcheck</code> error <a href="/rltoken/BYXAGPH5zbPpsqIR84ndFQ" title="here" target="_blank">here</a>)</li>
</ul>

<pre><code>sylvain@ubuntu$ sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
sylvain@ubuntu$ 
</code></pre>
</br>

## 3. Show your Bash PID made easy
<p>Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word <code>bash</code>.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>ps</code></li>
</ul>

<pre><code>sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
sylvain@ubuntu$ 
</code></pre>
</br>

## 4. To infinity and beyond
<p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>

<p>Requirements:</p>

<ul>
<li>In between each iteration of the loop, add a <code>sleep 2</code></li>
</ul>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
sylvain@ubuntu$ 
</code></pre>
</br>

## 5. Don't stop me now!
<p>We stopped our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>

<p>Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>kill</code></li>
</ul>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./5-dont_stop_me_now 
sylvain@ubuntu$ 
</code></pre>

<p>I opened 2 terminals in this example, started by running my <code>4-to_infinity_and_beyond</code> Bash script in terminal #0 and then moved on terminal #1 to run <code>5-dont_stop_me_now</code>. We can then see in terminal #0 that my process has been terminated.</p>
</br>

## 6. Stop me if you can
<p>Write a Bash script that stops <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
</ul>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./6-stop_me_if_you_can
sylvain@ubuntu$ 
</code></pre>

<p>I opened 2 terminals in this example, started by running my <code>4-to_infinity_and_beyond</code> Bash script in terminal #0 and then moved on terminal #1 to run <code>6-stop_me_if_you_can</code>. We can then see in terminal #0 that my process has been terminated.</p>
</br>

## 7. Highlander
<p>Write a Bash script that displays: </p>

<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>

<p>Make a copy of your <code>6-stop_me_if_you_can</code> script, name it <code>67-stop_me_if_you_can</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./67-stop_me_if_you_can 
sylvain@ubuntu$ ./67-stop_me_if_you_can
sylvain@ubuntu$ ./67-stop_me_if_you_can
sylvain@ubuntu$ 
</code></pre>

<p>I started <code>7-highlander</code> in Terminal #0 and then run <code>67-stop_me_if_you_can</code> in terminal #1, for every iteration we can see <code>I am invincible!!!</code> appearing in terminal #0.</p>
</br>

## 8. Beheaded process
<p>Write a Bash script that kills the process <code>7-highlander</code>.</p>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./8-beheaded_process
sylvain@ubuntu$ 
</code></pre>

<p>I started <code>7-highlander</code> in Terminal #0 and then run <code>8-beheaded_process</code> in terminal #1 and we can see that the <code>7-highlander</code> has been killed.</p>
</br>

## 9. Process and PID file
<p>Write a Bash script that: </p>

<ul>
<li>Creates the file <code>/var/run/myscript.pid</code> containing its PID</li>
<li>Displays <code>To infinity and beyond</code> indefinitely</li>
<li>Displays <code>I hate the kill command</code> when receiving a SIGTERM signal</li>
<li>Displays <code>Y U no love me?!</code> when receiving a SIGINT signal</li>
<li>Deletes the file <code>/var/run/myscript.pid</code> and terminates itself when receiving a SIGQUIT or SIGTERM signal</li>
</ul>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/d8ecfe9109334898b9540ffd20cf64d1c06f0c09.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220221%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220221T130741Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d03b366d7776ea94a05e86a8cbe3f4dd35b306828715e0394e7b50fb24e77245" alt="" style="" /></p>

<pre><code>sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
^CY U no love me?!
</code></pre>

<p>Executing the <code>100-process_and_pid_file</code> script and killing it with <code>ctrl+c</code>.</p>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
I hate the kill command
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ sudo pkill -f 100-process_and_pid_file
sylvain@ubuntu$ 
</code></pre>

<p>Starting <code>100-process_and_pid_file</code> in the terminal #0 and then killing it in the terminal #1.</p>
</br>

## 10. Manage my process
<p>Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: <code>start</code>, <code>restart</code> and <code>stop</code>. The most popular way of doing so on Unix system is to use the init scripts.</p>

<p>Write a <code>manage_my_process</code> Bash script that: </p>

<ul>
<li>Indefinitely writes <code>I am alive!</code> to the file <code>/tmp/my_process</code></li>
<li>In between every <code>I am alive!</code> message, the program should pause for 2 seconds</li>
</ul>

<p>Write Bash (init) script <code>101-manage_my_process</code> that manages <code>manage_my_process</code>. (both files need to be pushed to git)</p>

<p>Requirements:</p>

<ul>
<li>When passing the argument <code>start</code>:

<ul>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process started</code></li>
</ul></li>
<li>When passing the argument <code>stop</code>: 

<ul>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process stopped</code></li>
</ul></li>
<li>When passing the argument <code>restart</code>

<ul>
<li>Stops <code>manage_my_process</code><br></li>
<li>Deletes the file  <code>/var/run/my_process.pid</code></li>
<li>Starts <code>manage_my_process</code></li>
<li>Creates a file containing its PID in <code>/var/run/my_process.pid</code></li>
<li>Displays <code>manage_my_process restarted</code></li>
</ul></li>
<li>Displays <code>Usage: manage_my_process {start|stop|restart}</code> if any other argument or no argument is passed</li>
</ul>

<p>Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing <code>./101-manage_my_process start</code>, in our case it will simply create a new process instead of saying that it is already started.</p>

<pre><code>sylvain@ubuntu$ sudo ./101-manage_my_process
Usage: manage_my_process {start|stop|restart}
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
I am alive!
^C
sylvain@ubuntu$ sudo ./101-manage_my_process stop
manage_my_process stopped
sylvain@ubuntu$ cat /var/run/my_process.pid 
cat: /var/run/my_process.pid: No such file or directory
sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
^C
sylvain@ubuntu$ sudo ./101-manage_my_process start
manage_my_process started
sylvain@ubuntu$ cat /var/run/my_process.pid 
11864
sylvain@ubuntu$ sudo ./101-manage_my_process restart
manage_my_process restarted
sylvain@ubuntu$ cat /var/run/my_process.pid 
11918
sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
^C
sylvain@ubuntu$ 
</code></pre>
</br>

## 11. Zombie
<p>Write a C program that creates 5 zombie processes.</p>

<p>Requirements:</p>

<ul>
<li>For every zombie process created, it displays <code>Zombie process created, PID: ZOMBIE_PID</code></li>
<li>Your code should use the Betty style. It will be checked using <code>betty-style.pl</code> and <code>betty-doc.pl</code></li>
<li>When your code is done creating the parent process and the zombies, use the function bellow</li>
</ul>

<pre><code>int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
</code></pre>

<p>Example:</p>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ gcc 102-zombie.c -o zombie
sylvain@ubuntu$ ./zombie 
Zombie process created, PID: 13527
Zombie process created, PID: 13528
Zombie process created, PID: 13529
Zombie process created, PID: 13530
Zombie process created, PID: 13531
^C
sylvain@ubuntu$
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ps aux | grep -e &#39;Z+.*&lt;defunct&gt;&#39;
sylvain  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] &lt;defunct&gt;
sylvain  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] &lt;defunct&gt;
sylvain  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] &lt;defunct&gt;
sylvain  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] &lt;defunct&gt;
sylvain  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] &lt;defunct&gt;
sylvain  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep --color=auto -e Z+.*&lt;defunct&gt;
sylvain@ubuntu$ 
</code></pre>

<p>In Terminal #0, I start by compiling <code>102-zombie.c</code> and executing <code>zombie</code> which creates 5 zombie processes.
In Terminal #1, I display the list of processes and look for lines containing <code>Z+.*&lt;defunct&gt;</code> which catches zombie process.</p>
</br>
