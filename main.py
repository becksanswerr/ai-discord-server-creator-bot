import discord
import json
import datetime
from discord.ext import commands
from aiprocess import generate_template
from TOKENS import dctoken,serverid

TOKEN = dctoken  
SUNUCU_ID = serverid

def log_command(command: str, user: str):
    with open("logs/command_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {user}: {command}\n")


def load_server_data(filename="config/server_config_ai.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_server_data(data, filename="config/server_config_ai.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

server_data = load_server_data()
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} Logged in!")


@bot.command()
async def üret(ctx, *, data: str):
        log_command(f"üret komutu kullanıldı, veri: {data}",ctx.author)
        print("------Üretim Başlanıyor------")
        print(data)
        generate_template(data)
        print("------Üretim Tamamlandı------\n")
        print("------Server Düzenleniyor------")
        server_data = load_server_data()
        guild = bot.get_guild(SUNUCU_ID)
        
        if guild is not None:
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f"{channel.name} kanalı silindi.")
                except discord.Forbidden:
                    print(f"{channel.name} kanalını silemedim. Yetkisiz.")
                except discord.HTTPException as e:
                    print(f"Hata oluştu: {e}")

            for role in guild.roles:
                if role.name != "@everyone":
                    try:
                        await role.delete()
                        print(f"{role.name} rolü silindi.")
                    except discord.Forbidden:
                        print(f"{role.name} rolünü silemedim. Yetkisiz.")
                    except discord.HTTPException as e:
                        print(f"Hata oluştu: {e}")

            try:
                await guild.edit(
                    name=server_data["name"],
                    description=server_data.get("description", "") 
                )
                print("Sunucu ayarları sıfırlandı.")
            except discord.Forbidden:
                print("Sunucu ayarları sıfırlanamadı. Yetkisiz.")
            except discord.HTTPException as e:
                print(f"Hata oluştu: {e}")

            for kategori in server_data["categories"]:
                category = await guild.create_category(kategori["name"])
                print(f"{category.name} kategorisi oluşturuldu.")

                for kanal_ismi in kategori["channels"]:
                    kanal = next((k for k in server_data["channels"] if k["name"] == kanal_ismi), None)
                    if kanal:
                        if kanal["type"] == "text":
                            text_channel = await category.create_text_channel(kanal["name"], topic="Bu kanal zürafalar hakkında sohbet etmek için!")
                            print(f"{text_channel.name} metin kanalı oluşturuldu.")
                            for perm in kanal["permissions"]:
                                role = discord.utils.get(guild.roles, name=perm["role"])
                                if role:
                                    overwrites = {
                                        role: discord.PermissionOverwrite(
                                            read_messages=True,
                                            send_messages="send_messages" in perm["intent"],
                                            attach_files="attach_files" in perm["intent"]
                                        )
                                    }
                                    await text_channel.edit(overwrites=overwrites)
                        elif kanal["type"] == "voice":
                            voice_channel = await category.create_voice_channel(kanal["name"])
                            print(f"{voice_channel.name} sesli kanal oluşturuldu.")
                            for perm in kanal["permissions"]:
                                role = discord.utils.get(guild.roles, name=perm["role"])
                                if role:
                                    overwrites = {
                                        role: discord.PermissionOverwrite(
                                            connect="connect" in perm["intent"],
                                            speak="speak" in perm["intent"]
                                        )
                                    }
                                    await voice_channel.edit(overwrites=overwrites)

            for rol in server_data["roles"]:
                role = await guild.create_role(name=rol["name"], color=discord.Color(int(rol["color"][1:], 16)), mentionable=True)
                print(f"{role.name} rolü oluşturuldu.")
                permissions = discord.Permissions()
                for izin in rol["permissions"]:
                    if izin == "manage_server":
                        permissions.update(manage_guild=True)
                    elif izin == "kick_members":
                        permissions.update(kick_members=True)
                    elif izin == "ban_members":
                        permissions.update(ban_members=True)
                    elif izin == "manage_messages":
                        permissions.update(manage_messages=True)
                    elif izin == "mute_members":
                        permissions.update(mute_members=True)
                    elif izin == "deafen_members":
                        permissions.update(deafen_members=True)
                    elif izin == "send_messages":
                        permissions.update(send_messages=True)
                    elif izin == "read_messages":
                        permissions.update(read_messages=True)
                    elif izin == "attach_files":
                        permissions.update(attach_files=True)
                    elif izin == "connect":
                        permissions.update(connect=True)

                await role.edit(permissions=permissions)

            print("Sunucu başarıyla yapılandırıldı!")
        else:
            print("Sunucu bulunamadı!")




bot.run(TOKEN)