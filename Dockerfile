ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies early so that the build is cheap
# when changing other files.
RUN apk add --update --no-cache libusb
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /tpc-300

COPY . .

CMD ["./run.sh"]
