# 1Path Oracle API

Gets pools and gas price info from redis and serves it in specified format.

## Deployment

### Build image

1. `docker build -t oracle-api .`
2. `docker push oracle-api`

### Add env configuration:

```
# Redis url to shared with Oracle API redis instance (same instance, same DB required), required var

REDIS_URL=redis://some-redis/0:6379

# OpenAPI scheme path, to enable API docs.

OPENAPI_URL=/openapi.json
```

### Add service to docker-compose:

```
oracle-api:
  image: oracle-api
  env_file: oracle-api.env
  depends_on:
    - some-redis
  restart: always
```

### Get results:

```
curl http://oracle-api/api/v1/
```

If docs are set up, you can find them at `http://<api-domain>/docs`.
