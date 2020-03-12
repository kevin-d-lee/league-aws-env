## Custom Dockerfile
FROM consol/ubuntu-xfce-vnc
ENV REFRESHED_AT 2018-03-18

# Switch to root user to install additional software
USER 0

## Install a gedit
RUN  apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:mmk2410/intellij-idea \
    && apt-get update \
    && apt-get install -y sudo \
    && apt-get install -y git \
    && apt-get install -y intellij-idea-community

## switch back to default user
USER 1000

