# data-tools

deploy to heroku - 

```
docker buildx build --platform linux/amd64 -t registry.heroku.com/savantly-custom-report/web . --push
heroku container:release web -a savantly-custom-report
```

## savantly-custom-report

This app give us custom report
