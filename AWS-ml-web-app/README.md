# --- DRAFT DOCUMENT ---
# ___
# A Machine Learning model exposed through a web application
In this project we will:
* Train a ML model (from within a Jupyter notebook) on MNIST Handwritten Digit Classification Dataset, and save the model for it to be used by an application
* Create a webserver front end that allows the a user to draw a digit
* Create a Flask application backend that will get the drawn digits and predict the number drawn and give the answer to the user.

We are using UBUNTU 18.04 (Python3 is alread installed)

This guide assumes VPC and subnets (at least public) have already been created. For creation of VPC, subnets one can refer to documentation here [https://github.com/ddumet/DSTI/tree/master/AWS/r-studio-server-EC2]. In particular, it assumes:
* A VPC with an Internet Gateway
* A Public Subnet 192.168.1.0/24, with a custom Route Table to the Internet Gateway
* A Private Subnet 192.168.2.0/24


## Step-1: Create a ML model
In this step we will launch an EC2 instance to run Jupyter notebook that will generate a model to recognize digits drawn by hand.
### Step-1.1: Launch EC2 instance (*jupyter-instance*)
**AWS Console -> Services -> EC2**, then choose Launch Instance.
* Choose standard free tier eligible instance, we will us here an Ubuntu Server instance *ami-04b9e92b5572fa0d1*
* **Step 3**: Choose the configured VPC and public subnet (public-subnet-VPC-1). Choose **Auto Assign Public IP**
* **Step 6**: Select Security Group *public-subnet-SSH*


## Step 1.2: Connect to *jupyter-instance*
We will install the necessary software for jupyter notebook.
* Upload the requirements.txt file and the jupyter notebook to the jupyter instance:
    ```bash
    scp -i "a-keypair.pem" "requirements.txt" ec2-user@jupyter-instance-public-ip:~/.
    scp -i "a-keypair.pem" "00-mnist-cnn.ipynb" ec2-user@jupyter-instance-public-ip:~/.
    ```
    *Note: for ubuntu instance, **ec2-user** is **ubuntu**. Also instead of the public-ip address, one can use the public DNS name.*
* SSH to the *RDS-access-instance*
* then run the following command:
    ```bash
    # Update/Upgrade Ubuntu
    sudo apt-get update -y
    sudo apt-get upgrade -y

    # Install pip3
    sudo apt install python3-pip -y

    # Install python packages requirements
    sudo pip3 install -r requirements.txt

    # Install and launch jupyter notebook
    sudo pip3 install jupyter

    # Launch Jupyter in background mode
    nohup jupyter notebook --ip=0.0.0.0 &

    # Get the URL/Token to connect to Jupyter notebook
    # cat nohup, from the content of the nohup.out file, get the 
    # jupyter notebook token to be able to connect
    cat nohup.out
    ```

## Run notebook
RUN NOTEBOOK and save cnn.mist file



## Launch EC2 instance (*front-end-webserver*)

Security Group for HTTP and HTTPS

connect SSH 

Then 

    ```bash
    # Update/Upgrade Ubuntu
    sudo apt-get update -y
    sudo apt-get upgrade -y

    # Install pip3
    sudo apt install apache2
    ```
git clone https://github.com/leodsti/AWS_Tutorials.git
cd /AWS_Tutorials/MNIST

sudo cp index.html /var/www/html
sudo cp -r static /var/www/html

DONE.


## Launch EC2 instance (*back-end-flask*)
The Back End server will run prediction. A **Flask** application is receiving a request from the Front End to run recognition of the digits contained into the provided image.

The OpenCV package is used to process the image.

OPEN PORT 5000 security group

 containing the

install flask

install opencv: sudo apt install python3-opencv

Install keras, 

 

Update the front end index.html file to set the IP@ of the back end server
in the POST method.

flask cors allows 

WE NEED TO UPDATE CORS for Flask

imresize from scipy !








## SSH to EC2 instance, then:


jupyter is listening on localhost:8888
Connecting from a distant machine, we will not, by default, be able to connect as our machine connect to IP@:8888
so we need to launch jupyter with --ip=0.0.0.0

Then connect with 
ec2-instance-ip-address:8888

A login page will appear asking for a password
Go back to the ec2 instance, copy the jupyter token, and paste it into the password !

Done !!

Problem here is that if you close your connection (from where you started jupyter notebook) with the EC2 instance, that will close the jupyter notebook as well.

To avoid that, we can use the following command to launch jupyter notebook so that it is independant from our SSH session/console:



a nohup.out file is generated, containing the content of the output of the command luanched with nohup, i.e. it contains the jupyter token

Adding different environment in jupyter notebook

pip install ipy

