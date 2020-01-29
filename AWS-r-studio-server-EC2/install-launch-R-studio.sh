#!/bin/bash

# This script works for an Amazon Linux 2 AMI

# Install and enable EPEL (Extra Packages for Enterprise Linux)
sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

# Update all packages
sudo yum update -y

# Install R
sudo yum install R -y

# Install and run rstudio-server
wget https://download2.rstudio.org/rstudio-server-rhel-1.1.453-x86_64.rpm
sudo yum install rstudio-server-rhel-1.1.453-x86_64.rpm -y

# Start rstudio-server
sudo systemctl status rstudio-server

# Create user&password to be able to login
sudo adduser didier
echo 'didier:didier' | sudo chpasswd

# DONE !