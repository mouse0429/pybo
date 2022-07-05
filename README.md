# pybo
 점프 투 장고 책을 기반으로 제작한 질문답변 게시판 웹입니다
 
## 파이보 추가 기능
점프 투 장고 3장의 파이보 추가 기능을 참고해 추가적으로 구현했습니다.
### [1]페이징 기능에서 처음, 마지막 링크 추가 & '...' 생략 기호 추가
현재 active한 페이지를 기준으로 4페이지 전부터 4페이지 후까지 표시하고 <br/>
처음과 마지막 페이지를 생략 기호를 추가해 항상 표시 했습니다.

<div>
<img src="https://user-images.githubusercontent.com/68915238/177259932-8b625084-a77f-4f76-8533-025933bf6383.png" width="300" height="40"/>
<img src="https://user-images.githubusercontent.com/68915238/177260638-bf8d9949-6d8b-4f4a-95b6-d609e2a03e01.png" width="300" height="40"/>
</div>
active 페이지가 2페이지나 마지막 페이지 직전이면 가장 끝페이지와 현재 페이지 사이 <br/>
생략된 페이지가 없으므로 생략 기호가 보이지 않도록 구현했습니다 

<br/><img src="https://user-images.githubusercontent.com/68915238/177260062-44ef41a8-4e18-4322-9f59-796f5565d911.png" width="400" height="40"/><br/>
active 페이지가 중간 정도에 위치하게 되면 
생략기호 및 처음, 마지막 페이지의 확인이 가능합니다

## REFERENCE
1. 점프 투 장고 위키독스 [점프 투 장고](https://wikidocs.net/book/4223)
