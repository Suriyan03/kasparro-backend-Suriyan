# STAGE 1: Builder (The Factory)
FROM python:3.9-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential

# Install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# STAGE 2: Runtime (The Shipping Container)
FROM python:3.9-slim

WORKDIR /app

# Install runtime libs (like libpq for Postgres)
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy only the installed packages from Builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Update PATH to use installed packages
ENV PATH=/root/.local/bin:$PATH

# Permission executable
RUN chmod +x run.sh

CMD ["./run.sh"]