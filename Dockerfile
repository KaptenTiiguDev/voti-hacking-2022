FROM httpd:2.4
COPY ./public-html/ /usr/local/apache2/htdocs/
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf

# docker built -t hacking .
# docker run -dit -p 8080:80 hacking