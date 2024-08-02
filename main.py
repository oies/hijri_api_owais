from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hijri_converter import convert
from datetime import datetime

app = FastAPI()

# السماح بطلبات من أي مصدر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # السماح بالوصول من جميع المصادر
    allow_credentials=True,
    allow_methods=["*"],  # السماح بجميع أنواع الطلبات (GET, POST, PUT, DELETE, ...الخ)
    allow_headers=["*"],  # السماح بجميع الرؤوس
)

# قائمة بأسماء الشهور الهجرية بالعربية
hijri_months = [
    "محرم", "صفر", "ربيع الأول", "ربيع الآخر", 
    "جمادى الأولى", "جمادى الآخرة", "رجب", "شعبان", 
    "رمضان", "شوال", "ذو القعدة", "ذو الحجة"
]

@app.get("/")
def get_hijri_date():
    # الحصول على التاريخ الميلادي الحالي
    current_date = datetime.now()
    
    # تحويل التاريخ الميلادي إلى هجري
    hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
    
    # استخراج اليوم والشهر والسنة الهجرية
    hijri_day = hijri_date.day
    hijri_month = hijri_months[hijri_date.month - 1]  # استخدام أسماء الشهور بالعربية
    hijri_year = hijri_date.year
    
    # تحويل النصوص إلى UTF-8 يدويًا
    hijri_day = str(hijri_day).encode('utf-8').decode('utf-8')
    hijri_month = hijri_month.encode('utf-8').decode('utf-8')
    hijri_year = str(hijri_year).encode('utf-8').decode('utf-8')
    
    # إنشاء استجابة تحتوي على التاريخ الهجري
    return {
        "hijri_day": hijri_day,
        "hijri_month": hijri_month,
        "hijri_year": hijri_year
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)