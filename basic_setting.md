# [Django] 기초 환경 세팅

본격적인 수업을 시작하기 앞서 django의 기초 환경 세팅하는 법을 알려드리겠습니다.



## Django로 프로젝트 시작하기

먼저 바탕화면에 likelion 폴더를 만듭니다. 그후 VS code를 켜고 만든 likelion 폴더를 엽니다. 

~~~
cd Desktop
cd likelion
~~~

혹은 likelion 폴더에 오른쪽 버튼을 누른 후 Git Bash Here을 클릭해 터미널 명령어를 활용하여 VS code를 열어도 좋습니다.

```Bash 
code .
```



### 터미널 Bash로 설정하기

- Vs code를 실행해서 `ctrl`  + ` shift` + `p`를 눌러 설정에 들어갑니다.

- 검색창에 `Terminal: Select Defualt Shell` 를 검색한 후 클릭합니다.

- 그 후 `Git bash` 를 선택합니다.

  > linux 환경을 다운받으라면 아무도 안 받을 거니깐 linux와 문법이 같은 bash 터미널을 사용하기 위함입니다!



### 가상환경 켜기

장고 프로젝트를 시작하려면 가장 먼저 가상환경을 생성한 후 켜야합니다.

#### python -m venv 가상환경명

```
python -m venv myvenv
```

위 명령을 치고 나면 옆에 myvenv라는 폴더가 하나 생깁니다.



#### 가상환경 실행하기

~~~
source myvenv/Scripts/activate
~~~

위 명령어를 치면 터미널의 명령어 줄 위에 (myvenv) 라는 것이 생깁니다. 가상환경이 실행되었다는 뜻입니다.