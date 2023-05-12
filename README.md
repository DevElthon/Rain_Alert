# Rain_Alert
Sempre que vamos sair para algum lugar, precisamos verificar como estará o tempo para nos preparar para determinadas situações como a chuva. Porque não facilitar gerando um alerta sempre que a previsão estiver propícia a chuva ? 

Por isso criei um programa que através da API "https://api.openweathermap.org/data/2.5/weather" verifica como está o tempo na minha localização e manda um alerta via SMS utilizando o twilio. Assim eu não preciso ficar verificando o clima o tempo todo e caso eu precise de um guarda chuva, serei notificado.

Para receber a notificação, utilizo o pythonanywhere: https://www.pythonanywhere.com para rodar o programa todos os dias em um horário expecífico.
PS: também utilizei o smtplib para receber o mesmo alerta via email.
