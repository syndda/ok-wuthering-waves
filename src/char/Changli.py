from src.char.BaseChar import BaseChar, Priority


class Changli(BaseChar):

    def __init__(self, *args):
        super().__init__(*args)
        self.enhanced_normal = False
        self.last_e = 0
        self.lib_ok = False

    def reset_state(self):
        self.enhanced_normal = False
        if self.liberation_available():
            self.lib_ok = True
        else:  
            self.lib_ok = False

    def do_get_switch_priority(self, current_char: BaseChar, has_intro=False, target_low_con=False):
        if self.time_elapsed_accounting_for_freeze(self.last_e) < 4:
            self.logger.info(
                f'switch priority MIN because e not finished')
            return Priority.MIN
        else:
            return super().do_get_switch_priority(current_char, has_intro)

    def do_perform(self):
        if self.has_intro or self.enhanced_normal:
            if not self.is_forte_full() or not (self.lib_ok and self.liberation_available()):
                self.continues_normal_attack(0.5)
                self.enhanced_normal = False
        if self.is_forte_full():
        #    self.logger.debug('Changli click heavy attack without ult')
            self.heavy_attack(0.8)
            self.lib_ok=True
            self.enhanced_normal = False
            return self.switch_next_char()
        if self.liberation_available() and self.lib_ok:
            self.click_liberation(add_heavy=True)
            self.lib_ok = False
            self.enhanced_normal = False
        elif self.resonance_available():
            self.send_resonance_key()
            self.enhanced_normal = True
        elif self.click_echo(1.45):
            self.logger.debug('Changli click echo success')
            pass
        else:
            self.continues_normal_attack(1.05, until_con_full=True)
            self.enhanced_normal = True
            self.logger.info('Changli nothing is available')
        self.switch_next_char()
