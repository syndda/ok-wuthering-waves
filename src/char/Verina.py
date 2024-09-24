from src.char.Healer import Healer


class Verina(Healer):

    def __init__(self, *args):
        super().__init__(*args)
    
    def do_perform(self):
        if self.has_intro:
            self.logger.info(f'switch on flying intro')
            return self.switch_next_char()
        else:
            if self.resonance_available():
                self.logger.debug(f'reso switch')
                self.click_resonance()
                self.click_echo()
                self.click_liberation()
                return self.switch_next_char()
            if self.is_forte_full():
                if 0.5 < self.current_con < 1:
                    self.logger.debug(f'triple air auto')
                    self.jump()
                    self.continues_normal_attack(1.6, until_con_full=True)
                    return self.switch_next_char()
            else:
                if self.current_con < 1:
                    self.wait_down()
                    self.logger.debug(f'triple land auto')
                    self.continues_normal_attack(1.15, until_con_full=True)
                    return self.switch_next_char()
            self.heavy_attack()
        self.switch_next_char()
    
    def count_base_priority(self):
        return - 1

    def count_echo_priority(self):
        return 0
