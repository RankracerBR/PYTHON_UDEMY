from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod #não pode ser usada diretamente
    def _log(self, msg):... #Assinatura do método


    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()#
l.log_error('Oi')