# RasberryClockTR4

Itens necessários:
    Raspberry Pi 3 ou superior, 
    Tela LCD 3,5inch touch, 
    Conexao PDA (compartilhamento de internet via bluetooth)
    Conexão 5v (liguei em uma usb da traseira do som)
    
Linguagem Python

Funcionamento previsto:

Ao terminar o boot do SO, será rodado do sh conn e o script python clock, o sh realiza a conexao com o celular cadastrado e habilita a atualização do relógio e condicoes climaticas. Após isso, a conexao é desfeita (para economia de bateria do celular) e cada minuto a cor de fundo do carro e as informações climaticas mudarao de cor. A cada 15 minutos o sistema se reconecta ao celular para atualização do clima.

Arquivos:

conn e disconn -> abre e fecha a conexao bluetooth

clock.py -> script que rodo o relogio

mitr4tran.png -> imagem de fundo com transparencia

Referencia de leitura pra conexoes bluetooth: https://openaps.readthedocs.io/en/latest/docs/Customize-Iterate/bluetooth-tethering-edison.html#phone-selection-for-bt-tethering


Produto final:
![Image of Yaktocat](https://github.com/marianaguimaraes/RasberryClockTR4/blob/master/relogioTR4.jpg)

