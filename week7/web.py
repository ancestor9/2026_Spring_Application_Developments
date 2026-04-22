from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/items")
async def read_item(request: Request):
    # 클라이언트 호스트(IP) 접속
    client_host = request.client.host
    
    # 요청 헤더 접속
    headers = request.headers
    
    # 쿼리 파라미터 접속
    query_params = request.query_params
    
    # 요청 URL 접속
    url = request.url
    
    # 디버깅을 위한 출력문
    print("path param:", request.path_params)
    print("http method:", request.method)
    print("headers:", headers)
    
    return {
        "client_host": client_host,
        "headers": dict(headers),
        "query_params": dict(query_params),
        "url": str(url),
    }