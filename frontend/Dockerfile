# Stage 1
FROM node:14.15.4 as node
RUN mkdir -p /code

COPY . /code
WORKDIR /code
RUN npm install
RUN npm run

# build --prod
