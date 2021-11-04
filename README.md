# food-detection-web
이 깃 저장소는 광운대학교 국방 ict 창의과제 프로젝트를 위해서 제작된 것입니다.

웹을 만들었지만 이 프로젝트를 실행하기 위해서는 darknet53을 설치해야합니다. 
https://pjreddie.com/darknet/yolo/

사용환경은 <br>
 - cuda 11.4<br>
 - cudnn 11.4에 상응하는 버전<br>
 - opencv 4.5.3<br>
 - django <br>
 - bootstrap 4.5.3<br>
 
을 사용하였습니다.<br>



목적 : yolov3를 이용하여서 입력으로 넣은 식단 사진의 음식의 이름을 예상하고 그와 관련된 영양정보를 정리하여 사용자가 보기 좋게 출력한다.


사용법
---
해당 프로젝트를 사용하기 위해서는 darknet.exe의 경로를 cheak.py 에 darknet경로에 저장되어 있어야합니다. (명령어 실행을 위해서)
그리고 음식 인식을 위해 가중치 파일과 학습에 사용한 .data 파일의 경로 또한 같이 지정해주면 해당 프로젝트가 정상적으로 작동할 것입니다.

웹 시연 영상
---
https://youtu.be/uaUEoLFddLw


