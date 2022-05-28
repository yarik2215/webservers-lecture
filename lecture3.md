# Docker, SSL and other

## NGINX and Docker

![dockerized-nginx](./media/dockerized-nginx.png)

Мы можем запустить контейнер для nginx, контейнер для нашего приложения и контейнер для БД, они будут в изолированой сети, и наружу будет смотреть только nginx на порту `80`.

### Пример конфигурации nginx

```nginx
upstream backend {
    server web:8000;
}

server {
    listen 80;

    server_name localhost;

    location / {
        proxy_pass http://backend;
        proxy_redirect     off;

        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }
}
```

### Пример compose файла

```yaml
version: "3.6"

services:
  web:
    build: ./app
    expose: 
      - 8000

  nginx:
    build: nginx
    depends_on:
      - web
    ports:
      - 80:80
    volumes:
      - ./nginx:/etc/nginx/conf.d

```

## HTTPS

**HTTPS** (аббр. от англ. HyperText Transfer Protocol Secure) — расширение протокола HTTP для поддержки шифрования в целях повышения безопасности. Данные в протоколе HTTPS передаются поверх криптографических протоколов TLS или устаревшего в 2015 году SSL. В отличие от HTTP с TCP-портом `80`, для HTTPS по умолчанию используется TCP-порт `443`.

HTTPS не является отдельным протоколом. Это обычный HTTP, работающий через шифрованные транспортные механизмы `SSL` и `TLS`. Он обеспечивает защиту от атак, основанных на прослушивании сетевого соединения — от снифферских атак и атак типа man-in-the-middle, при условии, что будут использоваться шифрующие средства и сертификат сервера проверен и ему доверяют.

![https](./media/https.png)

## Полезные ссылки

- ["dockerizing flask"](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)
- ["Gunicorn with Nginx. WSGI"](https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-apps-using-gunicorn-http-server-behind-nginx)
- ["Знакомство с SSL/TLS"](https://habr.com/ru/company/1cloud/blog/326292/)
- ["Как защитить сайт с помощью HTTPS"](https://developers.google.com/search/docs/advanced/security/https?hl=ru#verify-that-your-https-pages-can-be-crawled-and-indexed-by-google)

- ["Self signed certificate"](https://imagineer.in/blog/https-on-localhost-with-nginx/)
- ["Nginx and Certbot" Medium](https://gist.github.com/dancheskus/8d26823d0f5633e9dde63d150afb40b2)
- ["Nginx and Certbot" DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-secure-a-containerized-node-js-application-with-nginx-let-s-encrypt-and-docker-compose-ru)
