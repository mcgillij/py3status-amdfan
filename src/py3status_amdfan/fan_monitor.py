# -*- coding: utf-8 -*-
"""
Module to display the fan speed and temperature of a amdgpu card
"""
from amdfan.controller import Scanner


class Py3status:
    cache_timeout = 5
    card = "card1"
    format = "{card}: 🌬️{fan_speed} / {gpu_temp}℃🌡️"

    def _get_fan_info(self):
        try:
            scanner = Scanner()
            card = scanner.cards.get(self.card)
            return (card.fan_speed, int(card.gpu_temp))

        except self.py3.Py3Exception as e:
            return f'error: {e}'

    def fan_monitor(self):
        fan_speed, gpu_temp = self._get_fan_info()
        full_text = self.py3.safe_format(
                self.format,
                {"card": self.card,
                 "fan_speed": fan_speed, "gpu_temp": gpu_temp}
        )
        return {
            "full_text": full_text,
            "cached_until": self.py3.time_in(self.cache_timeout),
        }


if __name__ == "__main__":
    from py3status.module_test import module_test
    module_test(Py3status)
