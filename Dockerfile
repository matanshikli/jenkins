
# Stage 1: Building dependencies
FROM python:3.10 as builder
WORKDIR /build
COPY requirements.txt .
# Install dependencies and build wheels
RUN pip install --upgrade pip &&     pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2: Setting up the linter (Flake8)
RUN pip install flake8
COPY . .
RUN flake8 --exit-zero

# Stage 3: Final image
FROM python:3.10-alpine
WORKDIR /app
# Copy built wheels from builder stage
COPY --from=builder /wheels /wheels
# Install the packages from wheels
RUN pip install --no-cache /wheels/*
COPY . .
CMD ["python", "app.py"]
