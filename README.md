## Introduction
- 비동기/ 병렬 처리를 지원하는 파이썬 기반의 웹 프레임워크인 FastAPI를 이용한 프로젝트입니다.
- 파이썬은 객체를 참조하는 객체들의 갯수를 기록한 뒤, 그 갯수가 0이 되면 메모리를 정리합니다. 이에 복수의 스레드 이용을 방지하는 GIL이 걸려져 있습니다. 이에 파이썬은 비동기/병렬 처리를 위하여 코루틴이라는 기법을 사용합니다.
- 블로그 포스팅에 따로 비동기/ 병렬 처리와 코루틴에 대한 내용을 공부하고 정리하였습니다.

## 개요
FastAPI를 이용한 웹 프로젝트 입니다. FastAPI는 비동기/ 병렬처리에서 두각을 나타내는 파이썬 웹 프레임워크 입니다. 비동기/ 병렬처리에 대한 설명은 따로 [이곳][concur-parel]에 포스팅하였습니다. 

## 요구사항 및 설치
* Python 3.8.10: `brew install python3`
* FastAPI 0.68.1: `pip install fastapi`
* uvicorn 0.15.0: `pip install uvicorn` 

## 실행
```
uvicorn main:app --reload
```

## 기능 설명
* path parameter 타입을 설정하여 데이터를 검수.
* path operation에서 상위의 컨트롤러로 우선 순위를 설정
* Enum을 사용한 path parameter 값 사전 정의
* path 파라매터와 query 파라매터의 구분과 조건 부여

[concur-parel]: https://hsjung93.github.io/%EC%BD%94%EB%93%9C/coroutine/
