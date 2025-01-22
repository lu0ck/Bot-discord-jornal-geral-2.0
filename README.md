#In English

# Discord Bot for Sending News and Images

This Discord bot is designed to send news and images at specific times and respond to custom commands directly on the server. It also allows you to send a maintenance message through commands.

## Features

- **Automated News**: Sends news at predefined times (06:00, 12:00, 18:00, 23:59).
- **Image Sending**: Each time a specific image is sent before the news.
- **News Search**: Use the `/j` command followed by a term to search for specific news.
- **Maintenance Mode**: Activate the `/maintenance` command to send a maintenance message to the channel.

## Required Settings

1. **Bot Token**: Replace the value of the `TOKEN` variable with the token of your Discord bot.
2. **News API Key**: Replace `NEWS_API_KEY` with your [News API](https://newsapi.org/) key.
3. **Sending Channel**: Enter your Discord channel ID in the `CANAL_ID` variable.
4. **Image Paths**: Make sure the image paths in `IMAGES_TIME` and `IMAGE_MAINTENANCE` are correct.

## Installation

1. Clone this repository or copy the bot code.
2. Make sure you have [Python 3.8+](https://www.python.org/) installed.
3. Install the necessary dependencies with:

```bash
pip install discord.py requests
```

4. Run the bot:

```bash
python filename.py
```

## Usage

- **Automatic Sending**: The bot will send images and news automatically at the specified times.
- **Search Command**:

```
/j [term]
```
Example: `/j Aparecida de Goiânia`
- **Maintenance Command**:

```
/maintenance
```

## Notes

- Make sure the bot has permission to send messages and images in the specified channel.
- Use images in supported formats (such as .jpg or .png).
- The news sent automatically is filtered to avoid repetitions.

## Customization

- **Schedules**: Change the keys in the `IMAGES_TIME` dictionary to modify the schedules.
- **News Terms**: Edit the terms used in `terms` in the `send_news_times` function.
- **Messages**: Customize the messages sent by editing the code texts.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).



#Em Português:

# Bot de Discord para Envio de Notícias e Imagens

Este bot para Discord foi projetado para enviar notícias e imagens em horários específicos e responder a comandos personalizados diretamente no servidor. Ele também permite o envio de uma mensagem de manutenção através de comandos.

## Recursos

- **Notícias Automatizadas**: Envio de notícias em horários predefinidos (06:00, 12:00, 18:00, 23:59).
- **Envio de Imagens**: Cada horário conta com uma imagem específica enviada antes das notícias.
- **Busca de Notícias**: Use o comando `/j` seguido de um termo para buscar notícias específicas.
- **Modo de Manutenção**: Ative o comando `/manutencao` para enviar uma mensagem de manutenção ao canal.

## Configurações Necessárias

1. **Token do Bot**: Substitua o valor da variável `TOKEN` pelo token do seu bot do Discord.
2. **Chave da API de Notícias**: Substitua `NEWS_API_KEY` pela sua chave da [News API](https://newsapi.org/).
3. **Canal de Envio**: Insira o ID do canal do Discord na variável `CANAL_ID`.
4. **Caminhos das Imagens**: Garanta que os caminhos das imagens em `IMAGENS_HORARIOS` e `IMAGEM_MANUTENCAO` sejam corretos.

## Instalação

1. Clone este repositório ou copie o código do bot.
2. Certifique-se de que você possui o [Python 3.8+](https://www.python.org/) instalado.
3. Instale as dependências necessárias com:

   ```bash
   pip install discord.py requests
   ```

4. Execute o bot:

   ```bash
   python nome_do_arquivo.py
   ```

## Uso

- **Envio Automático**: O bot enviará imagens e notícias automaticamente nos horários especificados.
- **Comando de Busca**:

  ```
  /j [termo]
  ```
  Exemplo: `/j Aparecida de Goiânia`
- **Comando de Manutenção**:

  ```
  /manutencao
  ```

## Observações

- Certifique-se de que o bot possui permissão para enviar mensagens e imagens no canal especificado.
- Utilize imagens de formatos suportados (como .jpg ou .png).
- As notícias enviadas automaticamente são filtradas para evitar repetições.

## Personalização

- **Horários**: Altere as chaves do dicionário `IMAGENS_HORARIOS` para modificar os horários.
- **Termos de Notícias**: Edite os termos usados em `termos` na função `enviar_noticias_horarios`.
- **Mensagens**: Personalize as mensagens enviadas editando os textos do código.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

