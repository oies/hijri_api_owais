from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hijri_converter import convert
from datetime import datetime

app = FastAPI()

# ÇäÓåÇÍ È×äÈÇÊ åæ Ãê åÕÏÑ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ÇäÓåÇÍ ÈÇäèÕèä åæ ÌåêÙ ÇäåÕÇÏÑ
    allow_credentials=True,
    allow_methods=["*"],  # ÇäÓåÇÍ ÈÌåêÙ ÃæèÇÙ Çä×äÈÇÊ (GET, POST, PUT, DELETE, ...ÇäÎ)
    allow_headers=["*"],  # ÇäÓåÇÍ ÈÌåêÙ ÇäÑÄèÓ
)

# âÇÆåÉ ÈÃÓåÇÁ ÇäÔçèÑ ÇäçÌÑêÉ ÈÇäÙÑÈêÉ
hijri_months = [
    "åÍÑå", "ÕáÑ", "ÑÈêÙ ÇäÃèä", "ÑÈêÙ ÇäÂÎÑ", 
    "ÌåÇÏé ÇäÃèäé", "ÌåÇÏé ÇäÂÎÑÉ", "ÑÌÈ", "ÔÙÈÇæ", 
    "ÑåÖÇæ", "ÔèÇä", "Ğè ÇäâÙÏÉ", "Ğè ÇäÍÌÉ"
]

@app.get("/")
def get_hijri_date():
    # ÇäÍÕèä Ùäé ÇäÊÇÑêÎ ÇäåêäÇÏê ÇäÍÇäê
    current_date = datetime.now()
    
    # ÊÍèêä ÇäÊÇÑêÎ ÇäåêäÇÏê Åäé çÌÑê
    hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
    
    # ÇÓÊÎÑÇÌ Çäêèå èÇäÔçÑ èÇäÓæÉ ÇäçÌÑêÉ
    hijri_day = hijri_date.day
    hijri_month = hijri_months[hijri_date.month - 1]  # ÇÓÊÎÏÇå ÃÓåÇÁ ÇäÔçèÑ ÈÇäÙÑÈêÉ
    hijri_year = hijri_date.year
    
    # ÅæÔÇÁ ÇÓÊÌÇÈÉ ÊÍÊèê Ùäé ÇäÊÇÑêÎ ÇäçÌÑê
    return {
        "hijri_day": hijri_day,
        "hijri_month": hijri_month,
        "hijri_year": hijri_year
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)