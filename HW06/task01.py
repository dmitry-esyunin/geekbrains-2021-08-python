# Урок 6. Объектно-ориентированное программирование
#
# 1. Создать класс TrafficLight (светофор).
# 
#  - определить у него один атрибут color (цвет) и метод running (запуск);
#  - атрибут реализовать как приватный;
#  - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#  - продолжительность первого состояния (красный) составляет 7 секунд, 
#    второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#  - переключение между режимами должно осуществляться только в указанном порядке 
#    (красный, жёлтый, зелёный);
#  - проверить работу примера, создав экземпляр и вызвав описанный метод.
#  
# Задачу можно усложнить, реализовав проверку порядка режимов. 
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
# 

import time


class TrafficLight:

    _color_base = ['красный', 'жёлтый', 'зелёный']
    _timings = [7, 2, 5]
    _color = _color_base[0]
    _periodic = sum(_timings)
    _is_running = False
    _t_last_run = 0
    _status_turn_off = 'выключен'

    def running(self, flag):
        if self._is_running != flag:
            self._t_last_run = time.time()
        self._is_running = flag

    def status(self):
        if not self._is_running:
            return self._status_turn_off
        index = 0
        delta_time = (time.time() - self._t_last_run) % self._periodic
        for i, timing in enumerate(self._timings):
            if delta_time <= timing:
                index = i
                break
            delta_time -= timing

        self._color = self._color_base[index]
        return self._color


traffic_light = TrafficLight()
traffic_light.running(True)
t_curr = time.time()

for _ in range(20):
    time.sleep(1)
    if time.time() - t_curr > 15:
        traffic_light.running(False)
    print(f'Времени прошло: {int(time.time() - t_curr)}c.  \tЦвет светофора: {traffic_light.status()}')
