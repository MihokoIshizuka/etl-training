FROM python:3.9.1

RUN apt-get update 

RUN apt-get install -y sudo

RUN sudo apt install -y openjdk-11-jdk
RUN sudo apt-get install -y default-mysql-client

RUN wget https://dlcdn.apache.org/kafka/3.0.2/kafka_2.13-3.0.2.tgz
RUN tar -xzvf kafka_2.13-3.0.2.tgz

RUN ln -s kafka_2.13-3.0.2 kafka

COPY start_up.sh  /etc/rc.local/
RUN chmod 755 /etc/rc.local/start_up.sh
