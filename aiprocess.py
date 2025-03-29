import google.generativeai as genai
import json
import ast
from TOKENS import geminitoken,geminimodel
genai.configure(api_key=geminitoken)
model = genai.GenerativeModel(geminimodel)

def generate_template(text):
    response = model.generate_content("""
    {
        "name": "Orman Esintisi Çalışma Kulübü",
        "icon": "https://example.com/forest-icon.png",
        "channels": [
          {
            "name": "🍃-duyurular",
            "type": "text",
            "permissions": [
              {
                "role": "@everyone",
                "intent": ["read_messages"],
                "deny": ["send_messages"]
              },
              {
                "role": "admin",
                "intent": ["manage_channels", "send_messages"]
              }
            ]
          },
          {
            "name": "🌲-genel-sohbet",
            "type": "text",
            "permissions": [
              {
                "role": "@everyone",
                "intent": ["read_messages", "send_messages"]
              },
              {
                "role": "moderator",
                "intent": ["manage_messages"]
              }
            ]
          },
          {
            "name": "🍂-çalışma-sohbeti",
            "type": "text",
            "permissions": [
              {
                "role": "@everyone",
                "intent": ["read_messages", "send_messages"]
              },
              {
                "role": "moderator",
                "intent": ["manage_messages"]
              }
            ]
          },
          {
            "name": "🍄-kaynaklar-ve-linkler",
            "type": "text",
            "permissions": [
              {
                "role": "@everyone",
                "intent": ["read_messages", "attach_files"]
              },
              {
                "role": "moderator",
                "intent": ["manage_messages"]
              }
            ]
          },
          {
            "name": "🦉-sessiz-calisma",
            "type": "voice",
            "permissions": [
              {
                "role": "@everyone",
                "intent": ["connect"]
              },
              {
                "role": "moderator",
                "intent": ["mute_members", "deafen_members"]
              }
            ]
          },
          {
            "name": "🌿-ortak-calisma",
            "type": "voice",
            "permissions": [
              {
                "role": "@everyone",
                "intent": ["connect", "speak"]
              },
              {
                "role": "moderator",
                "intent": ["mute_members", "deafen_members"]
              }
            ]
          }
        ],
        "roles": [
          {
            "name": "Admin",
            "color": "#228B22",
            "permissions": ["manage_server", "kick_members", "ban_members"]
          },
          {
            "name": "Moderator",
            "color": "#6B8E23",
            "permissions": ["manage_messages", "mute_members", "deafen_members"]
          },
          {
            "name": "Orman Kaşifi",
            "color": "#8FBC8F",
            "permissions": ["send_messages", "connect"]
          },
          {
            "name": "Yeni Üye",
            "color": "#D3D3D3",
            "permissions": ["read_messages"]
          }
        ],
        "categories": [
          {
            "name": "🌲 Genel",
            "channels": [
              "🍃-duyurular",
              "🌲-genel-sohbet"
            ]
          },
          {
            "name": "🍂 Çalışma Alanları",
            "channels": [
              "🍂-çalışma-sohbeti",
              "🍄-kaynaklar-ve-linkler"
            ]
          },
          {
            "name": "🌿 Sesli Çalışma",
            "channels": [
              "🦉-sessiz-calisma",
              "🌿-ortak-calisma"
            ]
          }
        ]
      }
                                      
    Bana buna benzer şekilde bir emojili bir json dosyası oluştur ve kesinlikle jsondan başika bir şey yazma.
    İşte istediğim: """+text)
    output = response.text
    output = output.replace("```json","")
    output = output.replace("```","")
    print(output)
    output = output.rsplit('}', 1)[0] + '}'
    print(output)
    data =  ast.literal_eval(output)

    with open("config/server_config_ai.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Veri server_config_ai.json dosyasına kaydedildi.")