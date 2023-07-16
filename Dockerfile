FROM python:3-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
CMD python setup.py sdist bdist_wheel
CMD pip install ./dist/cicd_tutorial_package-0.0.1-py3-none-any.whl
CMD app
