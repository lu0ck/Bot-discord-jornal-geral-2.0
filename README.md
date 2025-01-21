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

