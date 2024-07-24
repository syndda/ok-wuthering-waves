import time
from src.char.BaseChar import BaseChar, Priority


class Verina(BaseChar):

    def __init__(self, *args):
        super().__init__(*args)
        self.flowstep = 1

    def reset_state(self):
        self.flowstep = 1
    
    def do_perform(self):
        if self.has_intro:
            self.logger.info(f'switch on flying intro')
            return self.switch_next_char()
        else:
            if self.flowstep == 1:
                if self.resonance_available():
                    self.logger.info(f'reso switch')
                    self.click_resonance()
                    self.click_echo()
                    self.click_liberation()
                    self.flowstep = 2
                    return self.switch_next_char()
                if self.current_con < 1:
                    self.wait_down()
                    self.logger.info(f'triple land auto')
                    self.continues_normal_attack(1.1, click_resonance_if_ready_and_return=False, until_con_full=True)
                    self.flowstep =  2
                    return self.switch_next_char()
            elif self.flowstep == 2:
                if 0.5 < self.current_con < 1 and self.is_forte_full():
                    self.logger.info(f'triple air auto')
                    self.jump()
                    self.continues_normal_attack(1.55, click_resonance_if_ready_and_return=False, until_con_full=True)
                self.flowstep = 1
            else:
                self.heavy_attack()
                self.flowstep = 1
            self.switch_next_char()
    
    def count_base_priority(self):
        return - 1
