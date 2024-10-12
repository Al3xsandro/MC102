# -*- coding: utf-8 -*-
import datetime

complete_orders = []

max_order_time = datetime.datetime(2024, 9, 2, 23, 0)
last_end_order_time = None

while True:
  hour, minute, order_time = [int(x) for x in input().replace(":", " ").split()]
  if (hour == 00 and minute == 0) or (hour == 23) or (hour == 22 and minute == 59):
        print(len(complete_orders))
        break;

  if last_end_order_time == None:
    last_end_order_time = (datetime.datetime(2024, 9, 2, hour, minute) + datetime.timedelta(minutes=order_time))
    # print('horario de entrega do primeiro pedido', last_end_order_time)
    complete_orders.append({ "end_time": last_end_order_time })
    continue

  new_order_time = datetime.datetime(2024, 9, 2, hour, minute)

  # print('último pedido pronto', last_end_order_time)

  new_last_end_order_time = (last_end_order_time + datetime.timedelta(minutes=order_time))
  last_end_order_time = new_last_end_order_time

  # print('previsão do próximo pedido', last_end_order_time)

  calc_new_time = new_order_time + datetime.timedelta(minutes=order_time)
  diff_between_orders = (calc_new_time - last_end_order_time)
  # print(diff_between_orders > calc_new_time)

  have_diff = diff_between_orders.days >= 0

  new_last_end_order_time_with_diff = last_end_order_time + diff_between_orders
  last_end_order_time = new_last_end_order_time_with_diff if (have_diff) else new_last_end_order_time

  is_less_than_max = last_end_order_time < max_order_time
  if is_less_than_max:
    complete_orders.append({ "end_time": last_end_order_time })