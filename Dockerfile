FROM python:3.12-slim-bookworm as final

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=true \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    QR_CODE_DIR=/myapp/qr_codes

WORKDIR /myapp

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get install -y --allow-downgrades libc-bin=2.36-9+deb12u7 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies globally
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt \
    && pip install alembic psycopg2-binary

# Create a non-root user
RUN useradd -m myuser && mkdir -p ${QR_CODE_DIR} && chown -R myuser:myuser ${QR_CODE_DIR}

# Copy application code
COPY --chown=myuser:myuser . .

# Expose port
EXPOSE 8000

# Create entrypoint script with migration
RUN echo '#!/bin/bash\n\
echo "Running migrations..."\n\
alembic upgrade head || echo "Migration failed, continuing anyway"\n\
echo "Starting application..."\n\
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload\n'\
> /myapp/entrypoint.sh && chmod +x /myapp/entrypoint.sh && chown myuser:myuser /myapp/entrypoint.sh

USER myuser

# Start app using the entrypoint script
CMD ["/myapp/entrypoint.sh"]