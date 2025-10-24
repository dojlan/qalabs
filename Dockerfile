FROM nginx:latest

# Copy custom nginx.conf to container path
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
