sudo /etc/init.d/mysql start

mysql -u root -e "CREATE DATABASE kira";

mysql -u root -e "CREATE USER 'kira'@'%' IDENTIFIED BY 'password'"
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'kira'@'%' WITH GRANT OPTION"


