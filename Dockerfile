FROM condaforge/miniforge3:latest

WORKDIR /app
ENV TMPDIR=/tmp

# Basic system dependencies for OpenCV/OCR (no GUI needed)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Setup user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Environment setup
COPY requirements.txt .
RUN conda create --name my_env python=3.12 -y && \
    conda run -n my_env pip install --no-cache-dir -r requirements.txt

# Auto-activate my_env in every new shell
RUN echo "conda activate my_env" >> ~/.bashrc

COPY . .

CMD ["/bin/bash"]