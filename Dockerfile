FROM python:3.6

WORKDIR /code 

RUN apt-get update && apt-get install --no-install-recommends -y \
	python-opencv \
	python-pip \
	x11-apps

RUN pip install --upgrade pip setuptools
RUN pip install imutils \
				opencv-python \
				numpy \
				pillow

COPY . /code

ENV IMAGE_PATH         kill-feed-cropped.png
ENV QT_X11_NO_MITSHM   1           

CMD ["python", "main.py"]