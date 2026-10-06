# Frontend

The Presentation Tier of the AWS three-tier application.

## Deployment

Copy `index.html`:

```bash
sudo cp index.html /usr/share/nginx/html/index.html
```

Copy the Nginx configuration:

```bash
sudo cp proxy.conf /etc/nginx/conf.d/reverse-proxy.conf
sudo nginx -t
sudo systemctl enable nginx
sudo systemctl restart nginx
```

The frontend calls the backend using relative paths such as `/users`.
