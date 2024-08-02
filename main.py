from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hijri_converter import convert
from datetime import datetime

app = FastAPI()

# ������ ������ �� �� ����
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ������ ������� �� ���� �������
    allow_credentials=True,
    allow_methods=["*"],  # ������ ����� ����� ������� (GET, POST, PUT, DELETE, ...���)
    allow_headers=["*"],  # ������ ����� ������
)

# ����� ������ ������ ������� ��������
hijri_months = [
    "����", "���", "���� �����", "���� �����", 
    "����� ������", "����� ������", "���", "�����", 
    "�����", "����", "�� ������", "�� �����"
]

@app.get("/")
def get_hijri_date():
    # ������ ��� ������� �������� ������
    current_date = datetime.now()
    
    # ����� ������� �������� ��� ����
    hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
    
    # ������� ����� ������ ������ �������
    hijri_day = hijri_date.day
    hijri_month = hijri_months[hijri_date.month - 1]  # ������� ����� ������ ��������
    hijri_year = hijri_date.year
    
    # ����� ������� ����� ��� ������� ������
    return {
        "hijri_day": hijri_day,
        "hijri_month": hijri_month,
        "hijri_year": hijri_year
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)