# konlpy-on-docker
konlpy를 docker에 띄우고 http 프로토콜을 통해 데이터를 주고 받자.

```shell
docker build -t konlpy-on-docker .
docker run -d -p 8899:8899 --name konlpy-on-docker-inst konlpy-on-docker
```