from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ============================================================
# CONFIGURATION
# ============================================================

TOKEN = "8768287302:AAF1qxcuSm1OAt3lx_XHx_sdlZrX2isdv00"

# Remplace ces liens par les liens de TES canaux.
CANAL_ANIME = "https://t.me/TON_CANAL_ANIME"
CANAL_PC = "https://t.me/TON_CANAL_PC"


# ============================================================
# MENUS
# ============================================================

def menu_principal():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎬 Anime", callback_data="anime"),
            InlineKeyboardButton("🎮 Jeux PC", callback_data="jeux_pc")
        ],
        [
            InlineKeyboardButton("📢 Nos canaux", callback_data="canaux")
        ]
    ])


def menu_anime():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🍥 Naruto", callback_data="anime_naruto"),
            InlineKeyboardButton("⚔️ Berserk", callback_data="anime_berserk")
        ],
        [
            InlineKeyboardButton("🏴‍☠️ One Piece", callback_data="anime_onepiece"),
            InlineKeyboardButton("⚡ Bleach", callback_data="anime_bleach")
        ],
        [
            InlineKeyboardButton("🔙 Retour", callback_data="accueil")
        ]
    ])


def menu_jeux_pc():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎮 GTA V", callback_data="pc_gta"),
            InlineKeyboardButton("🕵️ Watch Dogs", callback_data="pc_watchdogs")
        ],
        [
            InlineKeyboardButton("⚔️ Devil May Cry", callback_data="pc_dmc"),
            InlineKeyboardButton("💀 Max Payne", callback_data="pc_maxpayne")
        ],
        [
            InlineKeyboardButton("🔙 Retour", callback_data="accueil")
        ]
    ])


def menu_canaux():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Canal Anime", url=CANAL_ANIME)],
        [InlineKeyboardButton("🎮 Canal Jeux PC", url=CANAL_PC)],
        [InlineKeyboardButton("🔙 Retour", callback_data="accueil")]
    ])


# ============================================================
# MENUS DE FICHES
# ============================================================
def menu_fiche_anime(anime):
    liens = {
        "naruto": "https://t.me/Naruto_vf_f",
        "berserk": "https://t.me/komijokaa",
        "onepiece": "https://t.me/one_piece_otaku",
        "bleach": "https://t.me/BLEACH_TV_VF",
    }

    return InlineKeyboardMarkup([
        [InlineKeyboardButton("▶️ Regarder maintenant", url=liens[anime])],
        [InlineKeyboardButton("🔙 Retour", callback_data="anime")]
    ])
# ============================================================
# /start
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = (
        "🔥 <b>Bienvenue sur notre bot !</b>\n\n"
        "Choisis une catégorie 👇"
    )

    await update.message.reply_text(
        texte,
        parse_mode="HTML",
        reply_markup=menu_principal()
    )


# ============================================================
# GESTION DES BOUTONS
# ============================================================

async def boutons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    choix = query.data

    # ---------------- MENU PRINCIPAL ----------------

    if choix == "accueil":
        await query.edit_message_text(
            "🔥 <b>Menu principal</b>\n\nChoisis une catégorie 👇",
            parse_mode="HTML",
            reply_markup=menu_principal()
        )

    # ---------------- ANIME ----------------

    elif choix == "anime":
        await query.edit_message_text(
            "🎬 <b>ANIME</b>\n\nChoisis ton anime 👇",
            parse_mode="HTML",
            reply_markup=menu_anime()
        )

    elif choix == "anime_naruto":
        await query.edit_message_text(
            "🍥 <b>NARUTO</b>\n\n"
            "📺 Série : Naruto\n"
            "📦 Épisodes : à compléter\n"
            "🌐 Langue : choisis ci-dessous 👇",
            parse_mode="HTML",
            reply_markup=menu_fiche_anime("naruto")
        )

    elif choix == "anime_berserk":
        await query.edit_message_text(
            "⚔️ <b>BERSERK</b>\n\n"
            "📺 Série : Berserk\n"
            "🌐 Langue : choisis ci-dessous 👇",
            parse_mode="HTML",
            reply_markup=menu_fiche_anime("berserk")
        )

    elif choix == "anime_onepiece":
        await query.edit_message_text(
            "🏴‍☠️ <b>ONE PIECE</b>\n\n"
            "📺 Série : One Piece\n"
            "🌐 Langue : choisis ci-dessous 👇",
            parse_mode="HTML",
            reply_markup=menu_fiche_anime("onepiece")
        )

    elif choix == "anime_bleach":
        await query.edit_message_text(
            "⚡ <b>BLEACH</b>\n\n"
            "📺 Série : Bleach\n"
            "🌐 Langue : choisis ci-dessous 👇",
            parse_mode="HTML",
            reply_markup=menu_fiche_anime("bleach")
        )

    elif choix == "anime_fr":
        await query.answer("🇫🇷 Français sélectionné")
        await query.edit_message_text(
            "🇫🇷 <b>Version française</b>\n\n"
            "Ajoute ici ton lien légal/autorisé.",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Retour", callback_data="anime")]
            ])
        )

    elif choix == "anime_vostfr":
        await query.answer("🇯🇵 VOSTFR sélectionné")
        await query.edit_message_text(
            "🇯🇵 <b>Version VOSTFR</b>\n\n"
            "Ajoute ici ton lien légal/autorisé.",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Retour", callback_data="anime")]
            ])
        )

    # ---------------- JEUX PC ----------------

    elif choix == "jeux_pc":
        await query.edit_message_text(
            "🎮 <b>JEUX PC</b>\n\nChoisis un jeu 👇",
            parse_mode="HTML",
            reply_markup=menu_jeux_pc()
        )

    elif choix == "pc_gta":
        await query.edit_message_text(
            "🎮 <b>GTA V</b>\n\n"
            "💻 Plateforme : PC\n"
            "📦 Taille : à compléter\n"
            "⚙️ Configuration : à compléter",
            parse_mode="HTML",
            reply_markup=menu_fiche_pc()
        )

    elif choix == "pc_watchdogs":
        await query.edit_message_text(
            "🕵️ <b>WATCH DOGS</b>\n\n"
            "💻 Plateforme : PC\n"
            "📦 Taille : à compléter\n"
            "⚙️ Configuration : à compléter",
            parse_mode="HTML",
            reply_markup=menu_fiche_pc()
        )

    elif choix == "pc_dmc":
        await query.edit_message_text(
            "⚔️ <b>DEVIL MAY CRY</b>\n\n"
            "💻 Plateforme : PC\n"
            "📦 Taille : à compléter\n"
            "⚙️ Configuration : à compléter",
            parse_mode="HTML",
            reply_markup=menu_fiche_pc()
        )

    elif choix == "pc_maxpayne":
        await query.edit_message_text(
            "💀 <b>MAX PAYNE</b>\n\n"
            "💻 Plateforme : PC\n"
            "📦 Taille : à compléter\n"
            "⚙️ Configuration : à compléter",
            parse_mode="HTML",
            reply_markup=menu_fiche_pc()
        )

    # ---------------- CANAUX ----------------

    elif choix == "canaux":
        await query.edit_message_text(
            "📢 <b>NOS CANAUX</b>\n\n"
            "Rejoins-nous ici 👇",
            parse_mode="HTML",
            reply_markup=menu_canaux()
        )


# ============================================================
# LANCEMENT
# ============================================================

def main():
    if TOKEN == "8768287302:AAFz0OX4-uumX-NUXpSD1C-SZTWeb5rZUqsI":
        print("❌ Mets ton token BotFather dans la variable TOKEN.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(boutons))

    print("🤖 Bot démarré !")
    app.run_polling()


if __name__ == "__main__":
    main()

