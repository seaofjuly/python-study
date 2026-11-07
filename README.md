# 나만의 파이썬 퀴즈 게임

## 1. 프로젝트 개요

Python 기초 문법을 학습하고, 터미널에서 실행되는 퀴즈 게임을 직접 만드는 프로젝트입니다.

사용자가 메뉴를 선택하여 퀴즈를 풀고, 새로운 문제를 추가하고, 퀴즈 목록과 최고 점수를 확인할 수 있는 프로그램을 만드는 것이 목표입니다.

## 2. 개발 환경

- 운영체제: Windows
- 코드 편집기: Visual Studio Code (VS Code)
- 터미널: PowerShell
- Python 버전: 3.14.10
- Git 버전: 2.56.0.windows.1
- 프로젝트 폴더: python-study

## 3. 개발 환경 확인

### Python 버전 확인

터미널에서 다음 명령어를 실행했습니다.

```powershell
py --version
```

실행 결과:

```text
Python 3.14.10
```

### Git 버전 확인

터미널에서 다음 명령어를 실행했습니다.

```powershell
git --version
```

실행 결과:

```text
git version 2.56.0.windows.1
```
![Python 및 Git 버전 확인](docs/screenshots/py_version_git_version.png)



## 4. 개발 진행 기록


### 개발 환경 준비

- [x] Python 3.14.10 설치 및 버전 확인
- [x] Git 2.56.0 설치 및 버전 확인
- [x] VS Code 프로젝트 폴더 `python-study` 준비
- [x] Git 사용자 이름 확인
- [x] `README.md` 생성 및 개발 환경 기록
- [x] 개발 환경 스크린샷 저장
- [x] `.gitignore` 파일 생성
- [x] `git init`으로 로컬 저장소 초기화
- [x] 기본 브랜치를 `master`에서 `main`으로 변경
- [x] `git status`로 저장소 상태 확인
- [x] `git add`로 초기 파일 등록
- [x] 첫 번째 Git 커밋 완료
- [x] GitHub 원격 저장소 생성
- [x] 첫 번째 `git push` 실행

### 첫 번째 Git 커밋 기록

- 커밋 메시지: `Chore: initialize Python quiz project`
- 커밋 ID: `93e2df3`
- 브랜치: `main`
- 기록된 파일: `.gitignore`, `README.md`, 개발 환경 스크린샷
- 현재 커밋 수: 1개 (과제 최소 요구 10개)


### 두 번째 Git 커밋 기록

- 커밋 메시지: `Docs: add Git learning notes and screenshots`
- 커밋 ID: `2d3aee1`
- 작업 내용: Git 명령어 학습 기록과 실행 스크린샷 추가
- 브랜치: `main`

### 세 번째 Git 커밋 기록

- 커밋 메시지: `Feat: add quiz menu`
- 커밋 ID: `7257b23`
- 작업 내용: Python 퀴즈 게임의 기본 메뉴 구현
- 구현 내용:
  - 1~5번 메뉴 화면 출력
  - `input()`으로 사용자 메뉴 번호 입력받기
  - `if`, `elif`로 선택한 메뉴 구분하기
  - `else`로 잘못된 메뉴 번호 안내하기
- 실행 확인: 5번과 9번 입력 테스트 완료
- 브랜치: `main`
- 현재 커밋 수: 3개 (과제 최소 요구 10개)
  
### Git 명령어 학습 기록

| 명령어 | 역할 |
|---|---|
| `git init` | 로컬 Git 저장소 생성 |
| `git status` | 파일과 저장소 상태 확인 |
| `git branch -m main` | 현재 브랜치 이름을 main으로 변경 |
| `git add` | 다음 커밋에 포함할 파일 준비 |
| `git commit -m` | 변경 내용을 설명과 함께 기록 |

### Git 명령어 실행 화면

#### 1. Git 저장소 초기화

`git init` 명령어로 로컬 저장소를 생성했습니다.

![Git 저장소 초기화](docs/screenshots/git%20init.png)

#### 2. Git 상태 확인

`git status` 명령어로 파일 상태를 확인했습니다.

![Git 상태 확인](docs/screenshots/git_status.png)

#### 3. 브랜치 이름 변경

`git branch -m main` 명령어로 브랜치 이름을 변경했습니다.

![브랜치 변경](docs/screenshots/master_to_main.png)

#### 4. Git 파일 등록

`git add` 명령어로 파일을 커밋할 준비를 했습니다.

![Git 파일 등록](docs/screenshots/git_add.png)

#### 5. 첫 번째 커밋

`git commit` 명령어로 첫 번째 변경 이력을 기록했습니다.

![첫 번째 커밋](docs/screenshots/git_commit.png)

#### 6. Python 퀴즈 파일 생성 및 Git 상태 확인

`quiz.py` 파일을 생성하고 Python 코드를 작성하기 시작했습니다.

`git log --oneline`으로 기존 커밋을 확인하고,
`git status`로 새 파일이 아직 Git에 등록되지 않은 상태를 확인했습니다.

![Python 파일 생성 및 Git 상태 확인](docs/screenshots/quiz_initial_git_status.png)

#### 7. Git 커밋 기록 확인

`git log --oneline` 명령어로 지금까지 생성한
3개의 커밋을 확인했습니다.

세 번째 커밋 `7257b23`이 GitHub의
`origin/main`에도 반영된 것을 확인했습니다.

![Git 커밋 3개 확인](docs/screenshots/git_log_3_commits.png)


#### 8. Python 퀴즈 메뉴 개발 및 실행

##### 8-1. 메뉴 출력과 사용자 입력

`print()`로 퀴즈 게임 메뉴를 출력하고,
`input()`으로 사용자의 입력을 받았습니다.

![첫 입력 기능](docs/screenshots/quiz_menu_first_input.png)

![메뉴 5개 출력](docs/screenshots/quiz_menu_display.png)

![입력값 확인 연습](docs/screenshots/quiz_input_test.png)

##### 8-2. Python 실행과 변수 학습

`python quiz.py` 실행 시 Python을 찾지 못하는 문제가 있어
`py quiz.py` 명령어로 실행했습니다.

입력받은 값을 `choice` 변수에 저장하는 방법을 학습했습니다.

![Python 실행 과정](docs/screenshots/quiz_python_execution.png)

##### 8-3. 조건문 구현

`if`, `elif`, `else`를 사용하여 입력 번호에 따라
서로 다른 안내 문구가 출력되도록 구현했습니다.

조건문에 필요한 콜론(`:`)과 들여쓰기의 역할을 학습하고
잘못된 들여쓰기를 수정했습니다.

![들여쓰기 오류 학습](docs/screenshots/quiz_indentation_error.png)

![조건문 구현 코드](docs/screenshots/quiz_condition_code.png)

##### 8-4. 메뉴별 실행 확인

1번부터 5번까지 각각 입력하여
메뉴 안내 문구가 정상적으로 출력되는지 확인했습니다.

![1번 메뉴 실행](docs/screenshots/quiz_menu_first_success.png)

![2번 메뉴 실행](docs/screenshots/quiz_menu_second_test.png)

![3번 메뉴 실행](docs/screenshots/quiz_menu_3.png)

![4번 메뉴 실행](docs/screenshots/quiz_menu_4.png)

![5번 종료 메뉴 실행](docs/screenshots/quiz_menu_5.png)

##### 8-5. 잘못된 입력 처리

처음에는 9번을 입력해도 안내 문구가 나오지 않았습니다.

`else` 조건을 추가한 뒤에는
잘못된 메뉴 번호라는 안내 문구가 출력되도록 수정했습니다.

![else 추가 전](docs/screenshots/quiz_invalid_before_else.png)

![else 추가 후](docs/screenshots/quiz_invalid_after_else.png)

#### 9. 세 번째 Git 커밋 및 GitHub 업로드

`git add .`으로 변경 파일을 준비하고,
`git status`로 커밋할 파일을 확인했습니다.

`git commit -m "Feat: add quiz menu"`로
세 번째 커밋을 생성했습니다.

- 커밋 ID: `7257b23`
- 변경 파일: `quiz.py`
- 추가된 코드: 21줄

![세 번째 커밋 성공](docs/screenshots/git_commit_quiz_menu.png)

`git push` 명령어로 GitHub 원격 저장소에 업로드했습니다.

![GitHub 업로드 성공](docs/screenshots/git_push_quiz_menu.png)



## 5. 퀴즈 주제 및 선정 이유

### 퀴즈 주제: Python 기초 문법

Python을 처음 배우면서 익힌 명령어와 기본 문법을
퀴즈로 복습하기 위해 이 주제를 선택했습니다.

변수, 출력과 입력, 조건문, 반복문 등
Python의 기초 개념을 문제로 만들고,
직접 풀면서 학습 내용을 확인하는 것이 목표입니다.

현재는 퀴즈 게임의 기본 메뉴와
사용자 입력 처리 기능까지 구현했습니다.


## 6. 실행 방법

### 프로그램 실행

VS Code에서 `python-study` 폴더를 열고
터미널에 다음 명령어를 입력합니다.

```powershell
py quiz.py
```

프로그램이 실행되면 다음 메뉴가 나타납니다.

```text
===== 도전! 파이썬 기초 퀴즈 =====
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

원하는 메뉴 번호를 입력하면 해당 안내 문구가 출력됩니다.

현재는 기본 메뉴 기능을 구현한 단계이며,
실제 퀴즈 문제를 풀거나 저장하는 기능은 개발 예정입니다.



## 7. 주요 기능

### 현재 구현한 기능

- [x] 퀴즈 게임 메뉴 5개 출력
- [x] 사용자 메뉴 번호 입력
- [x] `if`, `elif`, `else`를 이용한 메뉴 선택 처리
- [x] 5번 선택 시 종료 안내 문구 출력
- [x] 잘못된 메뉴 번호 입력 시 안내 문구 출력

### 앞으로 구현할 기능

- [ ] 실제 퀴즈 문제 풀기
- [ ] 새로운 퀴즈 문제 추가
- [ ] 퀴즈 목록 확인
- [ ] 최고 점수 확인
- [ ] 메뉴 반복 및 프로그램 종료 처리
- [ ] JSON 파일로 데이터 저장 및 불러오기
- [ ] 빈 입력과 잘못된 입력 등 예외 처리


## 8. 프로젝트 파일 구조

현재 프로젝트는 다음과 같이 구성되어 있습니다.

```text
python-study/
├── quiz.py
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
```

### 파일 및 폴더 설명

| 이름 | 역할 |
|---|---|
| `quiz.py` | Python 퀴즈 게임의 실행 코드 |
| `README.md` | 프로젝트 설명과 개발 학습 기록 |
| `.gitignore` | Git에서 추적하지 않을 파일 설정 |
| `docs/screenshots/` | 개발 과정 및 실행 결과 스크린샷 보관 |



## 9. 데이터 파일 설명

### 데이터 저장 계획

퀴즈 문제와 최고 점수 등의 데이터를
`state.json` 파일에 저장할 예정입니다.

JSON은 데이터를 일정한 형식으로 저장하는 방법입니다.

현재는 기본 메뉴만 구현한 상태이므로
`state.json` 파일은 아직 생성하지 않았습니다.

추후 데이터 저장 기능을 구현한 뒤
실제 JSON 구조와 저장 및 불러오기 방법을 기록하겠습니다.


## 10. 실행 화면 및 개발 과정

Python 퀴즈 게임의 개발 과정과 실행 결과는
**4. 개발 진행 기록**에 정리했습니다.

### 현재까지 확인한 내용

- Python 및 Git 개발 환경 설정
- Git 저장소 생성과 GitHub 연결
- Python 퀴즈 게임 메뉴 작성
- 사용자 입력 및 조건문 학습
- 1~5번 메뉴 실행 테스트
- 잘못된 메뉴 번호 입력 처리
- Git 커밋 및 GitHub 업로드

각 단계의 실행 화면은 `docs/screenshots/` 폴더에
저장했으며 README에서 확인할 수 있습니다.

앞으로 새로운 기능을 구현할 때마다
개발 과정과 실행 결과를 추가할 예정입니다.




