###### Nginx ubuntu 설치 - vue (아직 미시행)

- https://daily-life-of-bsh.tistory.com/223

###### Nginx ubuntu 설치 - django

```bash
# nginx 설치
sudo apt-get install -y nginx

# nginx 상태 확인
sudo service nginx status

# backend로 이동 후 실행
cd ~/deploy/S06P31S105/backend
source venv/bin/activate

# 백그라운드 동작
nohup python3 manage.py runserver 0:8000 &

# 백그라운드 동작 확인
ps -ef | grep manage.py

# 백그라운드 동작 취소
kill 프로세스 아이디
```

jenkins 사용할 명령어 (django - nginx 부분)

```sh
PROC=`ps aux | grep manage.py`
if [[ $PROC == *"manage.py"* ]]; then
  echo "Process is running."
  sudo kill -15 `ps -ef | grep manage.py | grep -v grep | awk '{print $2}'`
else
  echo "Process is not running."
fi

# sudo 를 붙이지 않으면 실행되지 않았음.(nohup 이 붙어서 그런걸로 판단)
nohup python3 manage.py runserver 0:8000 1> /dev/null 2>&1 &
```

