from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

import os

# ==========================================================
# CONFIGURATION
# ==========================================================

TOKEN = os.getenv("TOKEN")


REPO = "fadb4429-tech/telegram-bot"
BRANCH = "main"

BASE_IMAGE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/images/"


JEUX = {

    "gta": {
        "nom": "Grand Theft Auto V",
        "image": BASE_IMAGE + "gta.jpg",
        "url": "https://ankergames.net/game/grand-theft-auto-v",

        "description":
        "🎮 Grand Theft Auto V\n\n"

        "⭐ Genre : Action / Open World\n"
        "💾 Taille : 110 Go\n\n"

        "⚙ Configuration minimale\n"
        "• Windows 10 64 Bits\n"
        "• Core i5\n"
        "• 8 Go RAM\n"
        "• GTX 660 2 Go"
    },

    "watchdogs": {

        "nom": "Watch Dogs",

        "image": BASE_IMAGE + "watchdogs.jpg",

        "url": "https://ankergames.net/game/watch-dogs",

        "description":
        "🕵 Watch Dogs\n\n"

        "⭐ Genre : Action / Open World\n"
        "💾 Taille : 25 Go\n\n"

        "⚙ Configuration minimale\n"
        "• Windows 10\n"
        "• Core i5\n"
        "• 6 Go RAM\n"
        "• GTX 460"

    },

    "dmc": {

        "nom": "Devil May Cry 5",

        "image": BASE_IMAGE + "dmc.jpg",

        "url": "https://ankergames.net/game/devil-may-cry-5",

        "description":
        "⚔ Devil May Cry 5\n\n"

        "⭐ Genre : Hack & Slash\n"
        "💾 Taille : 35 Go\n\n"

        "⚙ Configuration minimale\n"
        "• Windows 10\n"
        "• Core i5\n"
        "• 8 Go RAM\n"
        "• GTX 760"

    },

    "maxpayne": {

        "nom": "Max Payne 3",

        "image": BASE_IMAGE + "maxpayne.jpg",

        "url": "https://ankergames.net/game/max-payne-3",

        "description":
        "💀 Max Payne 3\n\n"

        "⭐ Genre : TPS\n"
        "💾 Taille : 35 Go\n\n"

        "⚙ Configuration minimale\n"
        "• Windows 7\n"
        "• Core i3\n"
        "• 4 Go RAM\n"
        "• GTX 450"

    }

}


ANIMES = {

    "naruto": {
        "image": BASE_IMAGE + "naruto.jpg",
        "url": "https://t.me/Naruto_vf_f"
    },

    "berserk": {
        "image": BASE_IMAGE + "berserk.jpg",
        "url": "https://t.me/komijokaa"
    },

    "bleach": {
        "image": BASE_IMAGE + "bleach.jpg",
        "url": "https://t.me/BLEACH_TV_VF"
    },

    "onepiece": {
        "image": BASE_IMAGE + "onepiece.jpg",
        "url": "https://t.me/one_piece_otaku"
    }

}


# =====================================================
# MENUS
# =====================================================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def menu_principal():
    clavier = [
        [
            InlineKeyboardButton("🎮 Jeux PC", callback_data="jeux"),
            InlineKeyboardButton("🎌 Animés", callback_data="anime")
        ],
        [
            InlineKeyboardButton("📚 Mangas", callback_data="manga"),
            InlineKeyboardButton("ℹ️ À propos", callback_data="about")
        ]
    ]
    return InlineKeyboardMarkup(clavier)



def menu_manga():
    clavier = [
        [InlineKeyboardButton("🍥 Naruto", callback_data="naruto")],
        [InlineKeyboardButton("🏴‍☠️ One Piece", callback_data="onepiece")],
        [InlineKeyboardButton("⚔️ Bleach", callback_data="bleach")],
        [InlineKeyboardButton("🩸 Berserk", callback_data="berserk")],
        [InlineKeyboardButton("⬅ Retour", callback_data="accueil")]
    ]
    return InlineKeyboardMarkup(clavier)


# ==========================================================
# AFFICHER UN JEU
# ==========================================================

async def afficher_jeu(query, context, jeu_id):

    jeu = JEUX[jeu_id]

    clavier = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "💾 Télécharger",
                url=jeu["url"]
            )
        ],
        [
            InlineKeyboardButton(
                "⬅ Retour",
                callback_data="jeux"
            )
        ]
    ])

    await context.bot.send_photo(
        chat_id=query.message.chat.id,
        photo=jeu["image"],
        caption=jeu["description"],
        reply_markup=clavier
    )



# ==========================================================
# AFFICHER UN ANIME
# ==========================================================

async def afficher_anime(query, context, anime_id):

    anime = ANIMES[anime_id]

    clavier = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "▶ Regarder",
                url=anime["url"]
            )
        ],
        [
            InlineKeyboardButton(
                "⬅ Retour",
                callback_data="anime"
            )
        ]
    ])

    await context.bot.send_photo(
        chat_id=query.message.chat.id,
        photo=anime["image"],
        caption=f"🎌 {anime_id.upper()}",
        reply_markup=clavier
    )


# ==========================================================
# MENU JEUX AUTOMATIQUE
# ==========================================================

def menu_jeux():

    clavier = []

    for jeu_id, jeu in JEUX.items():

        clavier.append([
            InlineKeyboardButton(
                f"🎮 {jeu['nom']}",
                callback_data=jeu_id
            )
        ])

    clavier.append([
        InlineKeyboardButton(
            "⬅ Retour",
            callback_data="accueil"
        )
    ])

    return InlineKeyboardMarkup(clavier)




# ==========================================================
# MENU ANIMES AUTOMATIQUE
# ==========================================================

def menu_anime():

    clavier = []

    for anime_id in ANIMES:

        clavier.append([
            InlineKeyboardButton(
                f"🎌 {anime_id.title()}",
                callback_data=anime_id
            )
        ])

    clavier.append([
        InlineKeyboardButton(
            "⬅ Retour",
            callback_data="accueil"
        )
    ])

    return InlineKeyboardMarkup(clavier)


# ==========================================================
# /START
# ==========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎌 Bienvenue sur Anime Games Hub\n\n"
        "Retrouve tes animés préférés et les meilleurs jeux PC.\n\n"
        "👇 Choisis une catégorie :",
        reply_markup=menu_principal()
    )


# ==========================================================
# GESTION DES BOUTONS
# ==========================================================

async def boutons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    choix = query.data
    
  
    if choix == "accueil":

        await query.edit_message_text(
            "🎌 Bienvenue sur Anime Games Hub\n\n"
            "👇 Choisis une catégorie :",
            reply_markup=menu_principal()
        )

    elif choix == "jeux":

        await query.edit_message_text(
            "🎮 Jeux PC",
            reply_markup=menu_jeux()
        )

    elif choix == "anime":

        await query.edit_message_text(
            "🎌 Animés",
            reply_markup=menu_anime()
        )

    elif choix == "manga":

        await query.edit_message_text(
            "📚 Mangas",
            reply_markup=menu_manga()
        )

    elif choix == "about":

        await query.edit_message_text(
            "🤖 Anime Games Hub\n\n"
            "Version : 2.0\n"
            "Développé avec Python ❤️\n\n"
            "🎮 Jeux PC\n"
            "🎌 Animés\n"
            "📚 Mangas",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⬅ Retour", callback_data="accueil")]
            ])
        )

    elif choix in JEUX:

        await afficher_jeu(query, context, choix)

    elif choix in ANIMES:

        await afficher_anime(query, context, choix)




# ==========================================================
# MAIN
# ==========================================================

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CallbackQueryHandler(boutons))

    print("✅ Bot démarré.")

    app.run_polling()


if __name__ == "__main__":
    main()
