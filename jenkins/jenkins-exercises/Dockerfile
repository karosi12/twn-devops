FROM node:13-alpine

RUN mkdir -p /usr/app

COPY package*.json /usr/app/
COPY app/images /usr/app/images/
COPY app/* /usr/app/

WORKDIR /usr/app

EXPOSE 3000

RUN npm install
CMD ["node", "server.js"]
