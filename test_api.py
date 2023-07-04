import sys,time

print(sys.argv[1])
map_time_value = {"1m": 1, "2m": 2, "3m": 3,
                    "4m": 4, "5m": 5, "10m": 10, "15m": 15, "20m": 20,"30m":30,"1h":60,"2h":120,"4h":240,"6h":360,"12h":720,"24h":1440}
    
print(map_time_value[sys.argv[1]])