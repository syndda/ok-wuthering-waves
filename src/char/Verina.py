from src.char.BaseChar import BaseChar


class Verina(BaseChar):

    def __init__(self, *args):
        super().__init__(*args)
        self.step = 1

    def reset_state(self):
        self.step = 1
    
    def do_perform(self):
        if self.has_intro:
            # self.logger.debug(f'switch on flying intro')
            return self.switch_next_char()
        else:
            if self.current_con < 1 and self.step == 1:
                self.wait_down()
                # self.logger.debug(f'triple land auto')
                self.continues_normal_attack(1.1, click_resonance_if_ready_and_return=False, until_con_full=True)
                self.step =  2
                return self.switch_next_char()
            if self.resonance_available() and self.step == 2:
                # self.logger.debug(f'reso switch')
                self.click_resonance()
                self.click_echo()
                self.click_liberation()
                self.step = 3
                return self.switch_next_char()
            if 0.5 < self.current_con < 1 and not self.is_forte_empty() and self.step < 1:
                # self.logger.debug(f'triple air auto')
                self.jump()
                self.continues_normal_attack(1.55, click_resonance_if_ready_and_return=False, until_con_full=True)
                self.step = 1
            self.switch_next_char()
    
    def count_base_priority(self):
        return - 1
