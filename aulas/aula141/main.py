# from log import LogPrintMixin, LogFileMixin

# lp = LogPrintMixin()
# lp.log_error('qualquer coisa')
# lp.log_success('Que legal')
# lf = LogFileMixin()
# lf.log_error('qualquer coisa')
# lf.log_success('Que legal')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

galaxy_s.ligar()
iphone.desligar()