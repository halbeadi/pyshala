FROM python:3.12-slim

# Security: create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appgroup . .

# Create staticfiles dir with correct ownership before switching user
RUN mkdir -p /app/staticfiles && chown -R appuser:appgroup /app/staticfiles

USER appuser

RUN python manage.py collectstatic --noinput || true

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "pyshala.wsgi:application"]
