### 머신러닝 모델을 서비스하기

#### 1. scikilearn의 iris 데이터를 학습하여 모델을 만들고 새로운 데이터를 입력받아 서비스하기

- [How_FastAPI_and_Gradio_works_together](How_FastAPI_and_Gradio_works_together.png) 가이드 읽기
- [데이터 학습하기](train_model.py) > 학습된 모델 pkl로 저장 > [gradio로 UI 만들기](app_gradio.py) > [Fast API로 백엔드 만들기](api.py) > 새로운 데이터 입력받아 분류 예측하기

작동 방식 설명

step 1. Fast API 백엔드를 먼저 run (Srver 작동)

step 2. gradio UI를 실행하라 (Client 작동)
--- 아래 message 나오는 것 확인하고(로컬 PC에서 작동)
* Running on local URL:  http://127.0.0.1:7860                                                                                 
* To create a public link, set `share=True` in `launch()`.                                                                     
Keyboard interruption in main thread... closing server. 

step 3. 외부 url publish하기
---- if __name__ == "__main__":
         iface.launch(share=True) 코드를 수정하여 다시 실행


#### 2. gemini LLM으로 text 요약하는 서비스 만들기
- gemini LLM API > gradio로 UI 만들기 > Fast API로 백엔드 만들기 > 새로운 text 입력하여 요약하기
