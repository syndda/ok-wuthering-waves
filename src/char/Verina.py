import time
from src.char.BaseChar import BaseChar, Priority


class Verina(BaseChar):

    def do_perform(self):
        if self.has_intro:
            self.logger.debug(f'switch on flying intro')
            return self.switch_next_char()
        else:
            if self.current_con < 1 and time.time() - self.last_switch_time < 0.5:
                if self.flying():
                    self.sleep(0.3)
                    self.logger.debug(f'pause on air entry')
                self.continues_normal_attack(1.1, click_resonance_if_ready_and_return=False, until_con_full=True)
                self.logger.debug(f'triple land auto')
                return self.switch_next_char()
            if self.resonance_available():
                self.click_resonance()
                self.click_echo()
                self.click_liberation()
                return self.switch_next_char()
            if 0.5 < self.current_con < 1 and not self.is_forte_empty():
                self.jump()
                self.continues_normal_attack(1.55, click_resonance_if_ready_and_return=False, until_con_full=True)
                self.logger.debug(f'triple air auto')
            self.switch_next_char()
    
    def count_base_priority(self):
        return - 1
