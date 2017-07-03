TapNews Project
---
**Week8:**
```
Aim:
    add class for each news.

Tools:
    pull img from dockerhub: https://hub.docker.com/r/qianmao/cs503_tensorflow_jupyter/ 
    pip install jupyter

How to run:
    week8: sudo ./news_pipeline_launcher.sh

Problem encountered:
    1. run docker image, but connection refused.
        port didn't forward. 
        wrong: docker run qianmao/cs503_tensorflow_jupyter
        correct: docker run -it --rm -p 8888:8888 qianmao/cs503_tensorflow_jupyter
        

              
Useful commands to install tools:
    pull docker image:
        (assume docker is running): $docker pull qianmao/cs503_tensorflow_jupyter
    watchdog: need sudo pip install
    padas: pip install
    tensorflow: sudo pip install --ignore-installed numpy
```

