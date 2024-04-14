#!/bin/bash

python camping.py --start-date 2024-07-25 --end-date 2024-07-30 --parks 232769 232768 --nights 3 | python notifier.py &
python camping.py --start-date 2024-08-01 --end-date 2024-08-06 --parks 232769 232768 --nights 3 | python notifier.py &
python camping.py --start-date 2024-08-08 --end-date 2024-08-13 --parks 232769 232768 --nights 3 | python notifier.py &
wait
