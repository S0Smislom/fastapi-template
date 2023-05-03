FROM snakepacker/python:all as builder

# RUN python3.8 -m venv /usr/share/python3/code
RUN python3.9 -m venv /usr/share/python3/app
RUN /usr/share/python3/app/bin/pip install -U pip

RUN mkdir /usr/share/python3/app/code

COPY requirements/base.txt /usr/share/python3/app/code/req.txt
RUN /usr/share/python3/app/bin/pip install -r /usr/share/python3/app/code/req.txt
COPY ./src /usr/share/python3/app/code
RUN find-libdeps /usr/share/python3/app > /usr/share/python3/app/pkgdeps.txt

RUN ls /usr/share/python3/app/code

#################################################################
####################### TARGET STAGE ############################
#################################################################
# Use the image version used on the build stage
FROM snakepacker/python:3.9

# Copy virtualenv to the target image
COPY --from=builder /usr/share/python3/app /usr/share/python3/app
RUN xargs -ra /usr/share/python3/app/pkgdeps.txt apt-install

RUN ln -snf /usr/share/python3/app/bin/uvicorn /usr/bin/
RUN ln -snf /usr/share/python3/app/bin/aerich /usr/bin/
RUN ln -snf /usr/share/python3/app/bin/python /usr/bin/
RUN ln -snf /usr/share/python3/app/bin/pip /usr/bin/
WORKDIR /usr/share/python3/app/code