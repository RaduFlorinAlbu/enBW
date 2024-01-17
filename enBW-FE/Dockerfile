FROM node:16 as build


WORKDIR /app


COPY package.json /app/
RUN npm install

COPY . /app

RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist/en-bw-fe /usr/share/nginx/html

EXPOSE 80