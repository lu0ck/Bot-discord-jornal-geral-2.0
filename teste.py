import discord
import json
import requests
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from pytz import timezone

# Substituir os valores sensíveis
TOKEN = os.getenv("TOKEN")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
CANAL_ID = 1328473388783632507

# Caminhos das imagens específicas para cada horário
IMAGENS_HORARIOS = {
    "06:00": "images/bom_dia.jpg",
    "12:00": "images/meio_dia.jpg",
    "18:00": "images/fim_tarde.jpg",
    "23:59": "images/madrugada.jpg",
}

# Caminho da imagem de manutenção
IMAGEM_MANUTENCAO = "images/manutencao.png"

# fuso horario codigo
FUSO_HORARIO_BRASILIA = timezone("America/Sao_Paulo")

# Intents para o bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

ARQUIVO_NOTICIAS = "noticias_enviadas.json"

# Funções para persistência
def carregar_noticias():
    try:
        with open(ARQUIVO_NOTICIAS, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def salvar_noticias():
    with open(ARQUIVO_NOTICIAS, "w") as f:
        json.dump(list(noticias_enviadas), f)

# Histórico de notícias enviadas
noticias_enviadas = carregar_noticias()

# Função para construir URL com filtros
def construir_url(termos):
    base_url = "https://newsapi.org/v2/everything"
    data_ontem = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    parametros = {
        "q": termos,
        "from": data_ontem,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    return f"{base_url}?{'&'.join([f'{k}={v}' for k, v in parametros.items()])}"

# Envio de imagens e notícias nos horários específicos
@tasks.loop(minutes=1)
@tasks.loop(minutes=1)
async def enviar_noticias_horarios():
    agora_utc = datetime.now(pytz.UTC)  # Hora em UTC
    agora_brasilia = agora_utc.astimezone(pytz.timezone("America/Sao_Paulo"))  # Converter para Brasília
    hora_brasilia = agora_brasilia.strftime("%H:%M")

    print(f"[DEBUG] Hora atual em Brasília: {hora_brasilia}")
    if hora_brasilia in IMAGENS_HORARIOS:
        canal = bot.get_channel(CANAL_ID)
        if not canal:
            print("Canal não encontrado! Verifique o ID do canal.")
            return

        # Enviar a imagem correspondente ao horário
        caminho_imagem = IMAGENS_HORARIOS[hora_brasilia]
        with open(caminho_imagem, "rb") as img:
            imagem = discord.File(img)
            await canal.send(file=imagem)
                print(f"✅ Imagem enviada para {agora}")
        except Exception as e:
            print(f"❌ Erro ao enviar a imagem para {agora}: {e}")

        # Enviar as notícias
        termos = '"Aparecida de Goiânia" OR "Goiânia" OR "time Vasco da gama" OR "time vila nova" OR "time goias"'
        url = construir_url(termos)
        response = requests.get(url)
        if response.status_code == 200:
            resultados = response.json().get("articles", [])
            if resultados:
                for noticia in resultados:
                    titulo = noticia.get("title")
                    link = noticia.get("url")
                    if link not in noticias_enviadas:
                        noticias_enviadas.add(link)
                        salvar_noticias()
                        await canal.send(f"**{titulo}**\n[Leia mais]({link})")
                        print(f"✅ Notícia enviada: {titulo}")
            else:
                print("⚠️ Nenhuma notícia encontrada nas últimas 24 horas.")
        else:
            print(f"❌ Erro ao buscar notícias: {response.status_code}")

# Comando /j para buscar notícias específicas
@bot.command(name="j")
async def buscar_noticias(ctx, *, termo: str):
    await ctx.send(f"🔍 Buscando notícias sobre: **{termo}**...")
    url = construir_url(termo)
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json().get("articles", [])
        if resultados:
            noticia = resultados[0]
            titulo = noticia.get("title")
            link = noticia.get("url")
            if link not in noticias_enviadas:
                noticias_enviadas.add(link)
                salvar_noticias()
                await ctx.send(f"**{titulo}**\n[Leia mais]({link})")
            else:
                await ctx.send("⚠️ A notícia já foi enviada anteriormente.")
        else:
            await ctx.send("⚠️ Nenhuma notícia encontrada para o termo especificado.")
    else:
        await ctx.send(f"❌ Erro ao buscar notícias: {response.status_code}")

# Comando /manutencao para enviar imagem de manutenção
@bot.command(name="manutencao")
async def enviar_manutencao(ctx):
    canal = bot.get_channel(CANAL_ID)
    if not canal:
        await ctx.send("❌ Canal não encontrado! Verifique o ID do canal.")
        return

    try:
        with open(IMAGEM_MANUTENCAO, "rb") as img:
            imagem = discord.File(img)
            await canal.send(file=imagem)
        await ctx.send("✅ Imagem de manutenção enviada com sucesso!")
    except Exception as e:
        await ctx.send(f"❌ Erro ao enviar a imagem de manutenção: {e}")

# Evento ao iniciar o bot
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    enviar_noticias_horarios.start()

# Iniciar o bot
bot.run(TOKEN)
