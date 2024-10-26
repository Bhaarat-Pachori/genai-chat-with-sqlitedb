FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY flights.db /app/flights.db

# Expose the Streamlit port
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]