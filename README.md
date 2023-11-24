# fastapi-htmx-tailwindcss

1. 환경설정 : 서버 만들고 tailwindcss,htmx 설치 및 테스트 하기  
    - 서버 설치 완료  
    - tailwindcss 설치 및 테스트 완료
    - htmx 설치 및 테스트 완료
    - DB 연결하기
    
2. 기획
    - signin, signup 기능 및 페이지 만들기(진행중)
    

[error]  
 - curl: (7) Failed to connect to 127.0.0.1 port 80 after 0 ms: Connection refused : 80번 포트 쓰지도 않았는데 해당 오류남. 스웨거에서는 정상동작하는데 터미널에서는 안됨. 이유를 모르겠음..  -> 코드 오류가 있기는 했음. 지금은 정상적으로 동작함.  

[HTMX]
    - pass indicator  
    - 모든 페이지를 다 HTMX로 만다는 게 아니라 페이지별로 SPA 사용 목적으로 HTMX를 활용. 기본적인 페이지 이동은 전통적인 방식 따르기  
    
[Cookie]  
    - curl에서 아무리 쿠키 저장을 명령해도 브라우저와 다른 환경이어서 브라우저에 저장 안됨.  
    - 브라우저에게 쿠키 주고 받는 걸 이해함.  

결국 의존성 주입이나 보완 기능의 숙련이 중요...  
