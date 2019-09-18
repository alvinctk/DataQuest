`game_log.csv` is split into two files due to github max 100 MB file upload limit. 
- `game_log_1.csv`
- `game_log_2.csv`

```bash
$ split -b 95m game_log.csv
```


To reconstruct the file `game_log.csv`:
```bash
$ cat x* > game_log.csv
```
