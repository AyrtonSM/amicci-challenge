FROM node:20.12.2-alpine

WORKDIR /app

COPY /amicci-weather/package.json ./

RUN npm install

COPY amicci-weather/ .

EXPOSE 3000

CMD [ "npm", "run" , "dev"]
