FROM nginx:1.10.1-alpine
RUN apk update
RUN apk add vim
COPY index.html /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
