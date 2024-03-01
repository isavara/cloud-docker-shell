FROM python:3.9

WORKDIR /app
COPY app.py /app
COPY entrypoint.sh /app

RUN chmod +x /app/entrypoint.sh  # Corrected the chmod command to set execute permission

ENTRYPOINT ["/app/entrypoint.sh"]

