FROM pytorch/pytorch:1.12.0-cuda11.3-cudnn8-runtime

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--workers", "2"]