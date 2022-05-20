# 기업연계 S105팀 싸콤(SSACOM)



[싸콤 노션](https://ninth-tax-ce2.notion.site/c000cf794ec14a3e875947da995ed7ce)

관련된 모든 자세한 사항은 notion에 정리되어 있다.




## 1. 서비스 요약

싸콤(ssacom) 팀은 삼성에스원과 기업연계를 하여, UWB 모듈을 이용해 재실데이터를 받고, 받아온 재실 데이터를 구축한 웹 서버로 전송하여 클라우드 DB에 저장한다. 그리고 웹사이트를 구현하여 해당 데이터를 어떻게 사용하면 좋을지 예시로 보여주기 위한 대시보드를 제작하였다.





## 2. 버전 정리

```bash
asgiref==3.5.0
certifi==2021.10.8
charset-normalizer==2.0.12
django-cors-headers==3.11.0
djangorestframework-jwt==1.11.0
idna==3.3
PyJWT==1.7.1
requests==2.27.1
cycler==0.11.0
Cython==0.29.28
Django==3.2.13
django-extensions==3.1.5
djangorestframework==3.13.1
fonttools==4.32.0
kiwisolver==1.4.2
matplotlib==3.5.1
mysqlclient==2.1.0
numpy==1.21.6
packaging==21.3
Pillow==9.1.0
pyparsing==3.0.8
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
sqlparse==0.4.2
tzdata==2022.1
urllib3==1.26.9
channels==3.0.4
channels-redis==3.4.0
tensorflow==2.9.0
```

- channels와 channels-redis 버전 충돌에 주의한다.





## 3. API 설계

[API 설계](https://www.notion.so/7136f146e4a34c0dbe6b9d2deccb8ae9)





## 4. 배포 과정

[배포 과정 전반](../records/전체 배포 과정 정리.md)
