# 싸콤(SSACOM)
## readme 입니다.



#### 현재 배포 설정 중

- Django 설치 완료
- MySQL 연동 완료 (Docker)
- Jenkins 설치 완료 (GitLab push시 aws GitLab 파일 pull 동작 설정 중)
- Nginx 설치 완료 (Docker)



### 현재 Jenkins 오류사항

```
git pull 시 git 계정을 불러오지 못함
```

###### pipeline code

```shell
pipeline {
    agent any

    stages {
        stage('move dir') {
            steps {
                echo 'move dir'
                sh """
                cd ../../../../../home/ubuntu/deploy/S06P31S105/backend
                
                PROC=`ps aux | grep manage.py`
                if [[ $PROC == *"manage.py"* ]]; then
                  echo "Process is running."
                  sudo kill -15 `ps -ef | grep manage.py | grep -v grep | awk '{print ${2}}'`
                else
                  echo "Process is not running."
                fi
                
                nohup python3 manage.py runserver 0:8000 1> /dev/null 2>&1 &
                """
                echp 'pull success'
            }
        }
    }
}
```



### arduino websocket 오류사항

##### 1. 버전 지원 문제 (오류 내용)

```
In file included from C:\Users\SSAFY\Documents\Arduino\libraries\arduino_875911\src/WebSocketsClient_Generic.h:53:0,

                 from C:\Users\SSAFY\Documents\Arduino\socketio3\socketio3.ino:5:

C:\Users\SSAFY\Documents\Arduino\libraries\arduino_875911\src/WebSockets_Generic.h:72:4: error: #error Version 2.x.x currently does not support Arduino with AVR since there is no support for std namespace of c++.

   #error Version 2.x.x currently does not support Arduino with AVR since there is no support for std namespace of c++.

    ^~~~~

C:\Users\SSAFY\Documents\Arduino\libraries\arduino_875911\src/WebSockets_Generic.h:73:4: error: #error Use Version 1.x.x. (ATmega branch)

   #error Use Version 1.x.x. (ATmega branch)

    ^~~~~

exit status 1

보드 Arduino Uno 컴파일 에러.
```

##### 2. sketch 내용 오버 (오류 내용)

```
치는 프로그램 저장 공간 40184 바이트(124%)를 사용. 최대 32256 바이트.text section exceeds available space in board



전역 변수는 동적 메모리 1180바이트(57%)를 사용, 868바이트의 지역변수가 남음.  최대는 2048 바이트. 

Sketch too big; see https://support.arduino.cc/hc/en-us/articles/360013825179 for tips on reducing it.

보드 Arduino Uno 컴파일 에러.
```

