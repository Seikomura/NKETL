# PDF Table ETL to MongoDB (with Web UI)

Extract tables from uploaded PDF (matching specific headers) and load to MongoDB.

## Run

1. ติดตั้ง dependencies  
   `pip install -r requirements.txt`

2. Start Web UI  
   `streamlit run web_ui.py`

3. เปิด browser ที่ลิงก์ที่ Streamlit แจ้ง แล้ว upload PDF → extract table → insert MongoDB

## Config

- ตั้งค่า MongoDB connection, header table ที่ต้องการ ใน `config.py`

---

> ใช้งานในองค์กร/Local ได้เลย ไม่ต้องวางไฟล์ในโปรเจกต์ (อัพโหลด-ลบเองอัตโนมัติ)
