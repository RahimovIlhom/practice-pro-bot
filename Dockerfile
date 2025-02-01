FROM python:3.10-slim

# Ishchi katalogni sozlaymiz
WORKDIR /app

# Talablar faylini nusxalaymiz
COPY requirements.txt .

# Kerakli paketlarni o'rnatamiz
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Loyiha kodini nusxalaymiz
COPY . .

# Botni ishga tushiramiz
CMD ["python", "app.py"]