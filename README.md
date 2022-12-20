celery-flower-docker 是一个快速的celery和flower测试环境。

## 启动容器
下载项目，并进入目录，运行命令
```
docker compose up
```

* Dockerfile: 用于创建celery和flower镜像
* docker-compose.yml：编排容器

## celery项目
* main.py  celery入口和配置
* tasks01.py 任务模块1
* tasks02.py 任务模块2