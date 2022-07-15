# GIT



### Repository

> 특정 디렉토리를 버전 관리하는 저장소

- **git init** 명령어로 로컬 저장소를 생성
- **.git** 디렉토리에 **버전 관리에 필요한 모든 것**이 들어있음.



### GIT 명령어

- git init > 해당 디렉토리에 .git이라는 로컬 저장소 생성.
- git status > commit, untracked file 등 변동사항 체크
- git commit -m "메모" > 메모 내용인 변동사항들을 commit
- git log --oneline > 시간 일시 사용자를 제외한 파일내용만 보여줌
- 



---

### GIT 기본기

- README.md 생성하기



- Working Directory (ex > lectures), Staging Area (임시 저장소? 느낌 tracking 하는), Repository

  - 커밋은 이 3가지 영역을 바탕으로 동작

  

- working directory = 내가 작업하고 있는 실제 디렉토리

​															▼ (git add)

- staging area  = 커밋으로 남기고 싶은. 특정 버전으로 관리하고 싶은 파일이 있는 곳

​															▼ (git commit)

- repository = 커밋들이 저장 되는곳



ex) 신발장에 있는 신발들 = working directory

​      사진대에 올라와 잇는 신발 = staging area

​      사진 찍고난 파일 = repository

