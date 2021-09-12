
FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
RUN apt update && apt install -y zip htop screen libgl1-mesa-glx

# Install python dependencies
COPY requirements.txt .
RUN apt-get install -y python3 python3-pip libglib2.0-0
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt coremltools onnx gsutil notebook
RUN pip install --no-cache -U torch torchvision numpy
RUN pip install "paddleocr>=2.0.1"
RUN pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

# Create working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy contents
COPY . /usr/src/app

# Set environment variables
ENV HOME=/usr/src/app

CMD python3 app.py
