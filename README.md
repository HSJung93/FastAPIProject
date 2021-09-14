## 개요
FastAPI를 이용한 웹 프로젝트 입니다. FastAPI는 비동기/ 병렬처리에서 두각을 나타내는 파이썬 웹 프레임워크 입니다. 비동기/ 병렬처리에 대한 설명은 따로 [이곳][concur-parel]에 포스팅하였습니다. 

## 요구사항 및 설치
* Python 3.8.10: `brew install python3`
* FastAPI 0.68.1: `pip install fastapi`
* uvicorn 0.15.0: `pip install uvicorn` 

## 기능 설명
* path parameter 타입을 설정하여 데이터를 검수.
* path operation에서 상위의 컨트롤러로 우선 순위를 설정
* Enum을 사용한 path parameter 값 사전 정의

[concur-parel]: [https://hsjung93.github.io/%EC%BD%94%EB%93%9C/coroutine/]