# DataWarehousing-Assignment3
 
 
# INSTALLATION STEPS:
 
We need to create an EC2 instance and install java.
We need to create a twitter account.
We also need to install python 3.
 
Now we need to install Apache Spark on our instance. In order to install it we need to follow the following steps.
 
Install open JDK using the command:
```sh
sudoapt-get -y install openjdk-8-jdk-headless
```
Download Spark
 
Create a new folder
mkdir ~/server
cd ~/server
 
Download apache spark and unpack it
```sh
sudotar zxvfspark-2.3.0-bin-hadoop2.7.tgz
```
Then we need to export to java home and spark home using commands
```sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export SPARK_HOME=~/server/spark-2.3.0-bin-hadoop2.7
```
We have run this command after this
```sh
./spark-2.3.0-bin-hadoop2.7/sbin/start-slave.sh
```
 
#we will start the job on master and run a simple job and submit it.
 
#we will stream the twitter data from spark.
1.  We have to create a tweepy stream listener.
2.  Then we will publish it through internal socket.
3.  We will create spark sockettextstream.
4.  Connect to local socket and stream tweets.
 
 

