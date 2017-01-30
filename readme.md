# Raspberry
sudo apt-get install rsync


# Computer
Install [NodeJS 7.4.0][1]

Install git bash [Windows][2], [MacOS][3]

# Setup ssh keys

ssh-keygen -t rsa

ssh-copy-id pi@192.168.1.100

pip install pep8

cp pre-commit .git/hooks/pre-commit

chmod +x .git/hooks/pre-commit


# Rsync watcher
./sync IPOMEDT/ pi@192.168.1.100 /home/pi/IPOMEDT

[1]: https://nodejs.org/en/
[2]: https://git-scm.com/download/win
[3]: https://git-scm.com/download/mac
