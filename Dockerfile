FROM python:3-alpine

WORKDIR /app

COPY cidr_convert_api/python/requirements.txt .
RUN pip install -r requirements.txt

COPY cidr_convert_api/python/ .
CMD ["ash", "-c", "python api.py"]

# docker build -t pym .
# docker run -ti -p 8000:8000 pym% 