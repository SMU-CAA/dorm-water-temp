# dorm-water-temp

通过 [海大后勤 - 热水查询](http://hqzx.shmtu.edu.cn/cellphone/getHotWater) 获得数据（校内网访问无需登录），生成 Home Assistant 使用的 JSON 格式

例子：

```json
{
  "1": {
    "level": 77.0,
    "temp": 51.0
  },
  "64": {
    "level": 62.0,
    "temp": 52.0
  }
}
```

## Docker Compose

见 [docker-compose.yml](docker-compose.yml)
