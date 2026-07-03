FROM alpine:latest

RUN apk add --no-cache bash curl tar ncurses && \
    mkdir -p /tmp/bashcrawl && \
    curl -L https://gitlab.com/slackermedia/bashcrawl/-/archive/master/bashcrawl-master.tar.gz | tar -xz -C /tmp/bashcrawl --strip-components=1 && \
    mv /tmp/bashcrawl/* /root/ && \
    cp -r /root/entrance/. /root/ && \
    rm -rf /root/LICENSE /root/README.md /root/entrance /tmp/bashcrawl && \
    apk del curl tar

ENV TERM=xterm-256color

WORKDIR /root

RUN echo 'export TERM=xterm-256color' >> /root/.bashrc && \
    echo 'export PS1="\[\033[01;32m\][crawler@dungeon]\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> /root/.bashrc && \
    echo 'cat scroll' >> /root/.bashrc && \
    echo 'echo ""' >> /root/.bashrc

CMD ["/bin/bash", "--rcfile", "/root/.bashrc"]
