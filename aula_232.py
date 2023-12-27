from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None: #-> == retorno
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:... # tipo de aviso para o desenvolvedor

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail enviando:', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando -', self.mensagem)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação Enviada')
    else:
        print('Notificação Não enviada')

notificacao_email = NotificacaoEmail('Testando e-mail')
notificar(notificacao_email)

noticacao_sms = NotificacaoSMS('Testando SMS')
notificar(noticacao_sms)