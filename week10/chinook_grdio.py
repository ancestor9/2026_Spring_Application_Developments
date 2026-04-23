from fastapi import FastAPI
import gradio as gr
import sqlite3
import pandas as pd
import os
import requests

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib.font_manager as fm

# 한글 폰트 설정 (한글 깨짐 방지)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

app = FastAPI()

# ==========================================================
# 1️⃣ DB 파일 자동 다운로드 (없을 시 GitHub에서 가져옴)
# ==========================================================
DB_URL = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
DB_PATH = "chinook.db"

def download_chinook_db():
    if not os.path.exists(DB_PATH):
        print("📥 Downloading Chinook database...")
        try:
            response = requests.get(DB_URL, timeout=30)
            response.raise_for_status()
            with open(DB_PATH, "wb") as f:
                f.write(response.content)
            print("✅ Download complete.")
        except Exception as e:
            print(f"❌ Download failed: {e}")
    else:
        print("✅ Chinook DB already exists.")

download_chinook_db()

# ==========================================================
# SQLite 연결 및 테이블 조회 함수
# ==========================================================

# 1️⃣ 테이블 목록 조회
def get_tables():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            tables = pd.read_sql_query(
                "SELECT name FROM sqlite_master WHERE type='table';", conn
            )
        return tables["name"].tolist()
    except Exception as e:
        print(f"Error getting tables: {e}")
        return []


# 2️⃣ 테이블 미리보기
def preview_table(table_name):
    if not table_name:
        return pd.DataFrame({"Error": ["Please select a table"]})
    try:
        with sqlite3.connect(DB_PATH) as conn:
            # SQL Injection 방지를 위한 검증
            valid_tables = get_tables()
            if table_name not in valid_tables:
                return pd.DataFrame({"Error": ["Invalid table name"]})
            df = pd.read_sql_query(f"SELECT * FROM [{table_name}] LIMIT 10;", conn)
        return df
    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]})


# 3️⃣ SQL 직접 실행
def run_sql(query):
    if not query or not query.strip():
        return pd.DataFrame({"Error": ["Please enter a SQL query"]})
    try:
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]})


# 4️⃣ EDA 시각화: 장르별 트랙 수
def plot_genre_distribution():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query("""
                SELECT g.Name AS Genre, COUNT(*) AS TrackCount
                FROM Track t
                JOIN Genre g ON t.GenreId = g.GenreId
                GROUP BY g.Name
                ORDER BY TrackCount DESC
                LIMIT 15;
            """, conn)
        
        plt.figure(figsize=(10, 6))
        plt.bar(df["Genre"], df["TrackCount"], color='steelblue')
        plt.xticks(rotation=45, ha='right')
        plt.title("Track Count by Genre (Top 15)", fontsize=14, fontweight='bold')
        plt.xlabel("Genre", fontsize=12)
        plt.ylabel("Count", fontsize=12)
        plt.tight_layout()
        
        # 이미지 변환
        buf = BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches='tight')
        plt.close()
        buf.seek(0)
        
        from PIL import Image
        img = Image.open(buf)
        return img
    except Exception as e:
        print(f"Error in plot_genre_distribution: {e}")
        # 에러 메시지가 포함된 빈 이미지 반환
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.text(0.5, 0.5, f'Error: {str(e)}', ha='center', va='center')
        ax.axis('off')
        buf = BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        from PIL import Image
        return Image.open(buf)


# 5️⃣ EDA 시각화: 국가별 매출
def eda_dashboard():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            df = pd.read_sql_query("""
                SELECT BillingCountry, SUM(Total) AS Revenue
                FROM Invoice
                GROUP BY BillingCountry
                ORDER BY Revenue DESC
                LIMIT 15;
            """, conn)
        
        plt.figure(figsize=(10, 6))
        plt.bar(df["BillingCountry"], df["Revenue"], color='coral')
        plt.xticks(rotation=45, ha='right')
        plt.title("Revenue by Country (Top 15)", fontsize=14, fontweight='bold')
        plt.xlabel("Country", fontsize=12)
        plt.ylabel("Revenue ($)", fontsize=12)
        plt.tight_layout()
        
        buf = BytesIO()
        plt.savefig(buf, format="png", dpi=100, bbox_inches='tight')
        plt.close()
        buf.seek(0)
        
        from PIL import Image
        img = Image.open(buf)
        return img
    except Exception as e:
        print(f"Error in eda_dashboard: {e}")
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.text(0.5, 0.5, f'Error: {str(e)}', ha='center', va='center')
        ax.axis('off')
        buf = BytesIO()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        from PIL import Image
        return Image.open(buf)


# 🎨 Gradio UI 정의
def launch_gradio():
    with gr.Blocks(title="Chinook EDA Dashboard", theme=gr.themes.Soft()) as demo:
        gr.Markdown("# 🎵 Chinook Database EDA Dashboard")
        gr.Markdown("Explore the Chinook music store database with SQL queries and visualizations")
        
        with gr.Tab("1️⃣ 테이블 목록"):
            gr.Markdown("### Available Tables in Chinook Database")
            btn = gr.Button("Show Tables", variant="primary")
            table_output = gr.Textbox(label="Tables", interactive=False, lines=3)
            btn.click(fn=lambda: ", ".join(get_tables()), outputs=table_output)
        
        with gr.Tab("2️⃣ 테이블 미리보기"):
            gr.Markdown("### Preview Table Contents")
            table_dropdown = gr.Dropdown(
                choices=get_tables(), 
                label="Select Table",
                value=get_tables()[0] if get_tables() else None
            )
            preview_btn = gr.Button("Preview", variant="primary")
            preview_output = gr.Dataframe(label="Preview (First 10 rows)")
            preview_btn.click(fn=preview_table, inputs=table_dropdown, outputs=preview_output)
        
        with gr.Tab("3️⃣ SQL 실행"):
            gr.Markdown("### Execute Custom SQL Queries")
            sql_input = gr.Textbox(
                label="Enter SQL Query", 
                lines=5,
                placeholder="SELECT * FROM Artist LIMIT 10;"
            )
            sql_btn = gr.Button("Run SQL", variant="primary")
            sql_output = gr.Dataframe(label="Query Result")
            
            gr.Markdown("#### Example Queries:")
            gr.Markdown("""
            ```sql
            SELECT * FROM Artist LIMIT 10;
            SELECT COUNT(*) FROM Track;
            SELECT a.Title, ar.Name FROM Album a JOIN Artist ar ON a.ArtistId = ar.ArtistId LIMIT 10;
            ```
            """)
            
            sql_btn.click(fn=run_sql, inputs=sql_input, outputs=sql_output)
        
        with gr.Tab("4️⃣ 기본 EDA 시각화"):
            gr.Markdown("### Data Visualizations")
            
            with gr.Row():
                with gr.Column():
                    genre_btn = gr.Button("장르별 트랙 분포 📊", variant="primary", size="lg")
                    genre_plot = gr.Image(label="Genre Distribution", type="pil")
                
                with gr.Column():
                    rev_btn = gr.Button("국가별 매출 💰", variant="primary", size="lg")
                    rev_plot = gr.Image(label="Revenue by Country", type="pil")
            
            genre_btn.click(fn=plot_genre_distribution, outputs=genre_plot)
            rev_btn.click(fn=eda_dashboard, outputs=rev_plot)
        
    return demo


# 🏁 FastAPI + Gradio 통합 실행
@app.get("/")
def read_root():
    return {
        "message": "Chinook EDA Dashboard API",
        "gradio_url": "/gradio",
        "status": "running"
    }

# Gradio 앱을 FastAPI에 마운트
demo = launch_gradio()
app = gr.mount_gradio_app(app, demo, path="/gradio")


# 개발 서버 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    
#################################################GRDIO INTEGRATION WITH FASTAPI BELOW##################################################
# separate services in the sense that they are running on different ports and handle different requests:
# FastAPI: Handles requests to its main port (e.g., http://127.0.0.1:8000/) and serves the root endpoint /.
# Gradio: Handles requests to its own port (http://127.0.0.1:7860/) and serves the interactive dashboard.

# # 🏁 FastAPI + Gradio 별도 서비 실행
# @app.get("/")
# def read_root():
#     return {"message": "Go to /gradio for the EDA dashboard."}


# @app.on_event("startup")
# async def startup_event():
#     import threading
#     demo = launch_gradio()
#     threading.Thread(target=lambda: demo.launch(server_name="127.0.0.1", server_port=7860, share=True)).start()

'''
🖥 FastAPI (포트 8000)
        │
        ├──▶ API 엔드포인트 처리 (/gradio 등)
        │
        └──▶ startup_event()
                │
                └──▶ threading.Thread → Gradio(포트 7860)
                             │
                             └── Web UI (EDA Dashboard)
'''
###########################################################