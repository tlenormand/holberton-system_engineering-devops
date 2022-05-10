# 0x14. MySQL

0. Install MySQL
<pre><code>
sudo apt update
sudo apt install wget -y
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
# choose Ubuntu Bionic and click Ok
# Choose the first option and click OK
# select MySQL 5.7 server and click OK
# Choose the last otpion Ok and click OK
sudo apt-get update
==> erreur : The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 467B942D3A79BD29
==> on récpère la clé manquante : dans mon cas 467B942D3A79BD29
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <la clé ici>
sudo apt-get update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
# Enter and re-enter root password when prompted ==> pas obligé
sudo mysql_secure_installation ==> pas obligé si vous mettez un mot de passe blanck
mysql --version
sudo mysql -u root -p
$ SELECT VERSION();
</code></pre>
Pour le checkeur, il faut ajouter la clé ssh du checkeur dans nos deux serveur, pour ça, oucrir le fichier et coller la clé :
<pre><code>
sudo vi ~/.ssh/authorized_keys
# add for school
ssh-rsa xxxxxxxxxxxxxxxxx
</code></pre>
</br>


# 1. Let us in!

<pre><code>
sudo mysql -u root -p
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* to 'holberton_user'@'localhost';
</code></pre>
</br>


# 2. If only you could see what I've seen with your eyes

<pre><code>
sudo mysql -u root -p
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;
USE `tyrell_corp`;
CREATE TABLE IF NOT EXISTS `nexus6`(
    `id` INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
INSERT INTO `nexus6` (id, name) VALUES (1, 'Leon');
GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';
</code></pre>
</br>


# 3. Quite an experience to live in fear, isn't it?

<pre><code>
sudo mysql -u root -p
CREATE USER 'replica_user'@'%';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';
GRANT SELECT ON `mysql`.`user` TO 'holberton_user'@'localhost';
</code></pre>
</br>

# 4. Setup a Primary-Replica infrastructure using MySQL

<pre><code>
# sur web-01
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
############
server-id       = 1
        log_bin                 = /var/log/mysql/mysql-bin.log
        expire_logs_days        = 10
        max_binlog_size         = 100M
        binlog_do_db            = tyrell_corp
# By default we only accept connections from localhost
bind-address    = 0.0.0.0
############
sudo service mysql restart
sudo mysql -u root -p
SHOW MASTER STATUS;
exit
sudo mysqldump -u root -p --opt tyrell_corp > slave-init.sql

# sur web-02, copier le fichier "slave-init.sql" de web-01 vers web-02
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
############
server-id       = 2
        relay-log               = /var/log/mysql/mysql-relay-bin.log
        log_bin                 = /var/log/mysql/mysql-bin.log
        expire_logs_days        = 10
        max_binlog_size         = 100M
        binlog_do_db            = tyrell_corp
# By default we only accept connections from localhost
bind-address    = 0.0.0.0
############
sudo service mysql restart
sudo mysql -u root -p
CREATE DATABASE tyrell_corp;
exit
sudo mysql -u root tyrell_corp < slave-init.sql

# sur le web-01
sudo mysql -u root -p
show master status;
# copier la colone "file" et "Position"
exit

# sur le web-02
sudo mysql -u root -p
CHANGE MASTER TO MASTER_HOST='34.139.172.50', MASTER_USER='replica_user', MASTER_PASSWORD='', MASTER_LOG_FILE='mysql-bin.000002', MASTER_LOG_POS= 154; ==> MASTER_HOST : IP du web-01, MASTER_USER : usr du replica, MASTER_PASSWORD : mdp du usr replica, MASTER_LOG_FILE : colone "File" copier avant, MASTER_LOG_POS : colone "Position" copier avant
START SLAVE;
exit
sudo service mysql restart
mysql -uholberton_user -p
show slave status\G
CREATE USER 'replica_user'@'%';
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'replica_user'@'%';

# sur web-01
sudo mysql -u root -p
GRANT ALL ON `tyrell_corp`.`nexus6` TO `replica_user`@`35.243.158.214` IDENTIFIED BY '1234';
FLUSH PRIVILEGES;
SELECT host FROM mysql.user WHERE user = "replica_user";
GRANT ALL ON `tyrell_corp`.* to 'replica_user'@'35.243.158.214' IDENTIFIED BY '1234';
</code></pre>
</br>
