Capstone_TapNews Project
---
**Week1:**
```
Aim:
    Start a config_service on port 4000. All the other services ask this service for
their config information, serverhost, and serverport.

What's been done:
    Config_service now hosts config information about: backend_server, news_recommendation_service, click_log_processor, and news_pipeline. 

Where i stuck:
    When i try to utilize web_server_rpc_client to call config_service, i only get response json file within the function. But out of the function scope, the json file cannot be read.

Merits:
    Now it's easier to modify config constants for all the services.

Drawbacks:
    All the other services are too dependent on the config service. Once 
    config_service can't start correctly, all the other services can't start.
____________________________________________________________________________________
STUDY ABOUT NGINX
Aim:
    add nginx.

Default Ports:
    nginx:8080

How to run:
    nginx
    nginx -s stop
    nginx -s reload
    

Problem encountered:
    Q1. can't find nginx directories.
    A1: "nginx -t" shows one the directory of nginx.conf. "vim nginx.conf", we can see in server{ root html}. since i used "brew" to install nginx, therefore, root html => root /usr/local/var/www. The reason is because this is where brew located. see Ref3 for details.

    so in short:
        nginx.conf is at: /usr/local/etc/nginx/nginx.conf
        index.html is at: /usr/local/var/www/index.html

    Q2: how to config nginx.conf?
    A2: comment out the server{ } block. include a folder we wrote, with server{ } defined by ourseves. server { } has listen+port, server-name, root, and location.
    Make sure the root folder has a index.html inside.
              
Useful commands to install tools:
    brew install nginx

Refs:
https://stackoverflow.com/questions/19910042/locate-the-nginx-conf-file-my-nginx-is-actually-using

https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor

https://stackoverflow.com/questions/10674867/nginx-default-public-www-location
```

