# CHAOS
import os
import dotenv

dotenv.load_dotenv()

SBU_LOGO_URL = 'https://cdn.discordapp.com/avatars/937099605265485936/8a5d786e369fdda9f355f12eaf0487fb.png?size=4096'
QOTD_PATH = './data/qotd.json'
SBU_GOLD = 0xc0c09e
SBU_PURPLE = 0x8F49EA
SBU_ERROR = 0xFF0000
SBU_SUCCESS = 0x00FF00

# Pseudo constants
GUILD_ID = 0

JR_MOD_ROLE_ID = 0
MODERATOR_ROLE_ID = 0
JR_ADMIN_ROLE_ID = 0
ADMIN_ROLE_ID = 0
QOTD_ROLE_ID = 0
GUILD_MEMBER_ROLE_ID = 0
VERIFIED_ROLE_ID = 0
ACTIVE_ROLE_ID = 0
SB_UNI_MEMBER_ROLE_ID = 0
SB_KAPPA_MEMBER_ROLE_ID = 0
SB_ALPHA_MEMBER_ROLE_ID = 0
SB_MASTERS_MEMBER_ROLE_ID = 0
SB_DELTA_MEMBER_ROLE_ID = 0
SB_LAMBDA_MEMBER_ROLE_ID = 0
TOP_GUILD_ACTIVE_ROLE_ID = 0
WEIGHT_BANNED_ROLE_ID = 0
FRESHMAN_ROLE_ID = 0
INSTRUCTOR_ROLE_ID = 0
PROFESSOR_ROLE_ID = 0
DEAN_ROLE_ID = 0
PROVOST_ROLE_ID = 0
PRIMUS_ROLE_ID = 0
LEGATUS_ROLE_ID = 0
BOOSTER_ROLE_ID = 0

QOTD_CHANNEL_ID = 0
MOD_CHAT_CHANNEL_ID = 0
ADMIN_CHAT_CHANNEL_ID = 0
BANNED_LIST_CHANNEL_ID = 0
SUGGESTIONS_CHANNEL_ID = 0
SBU_BOT_LOGS_CHANNEL_ID = 0
CARRY_SERVICE_REPS_CHANNEL_ID = 0
CRAFT_REPS_CHANNEL_ID = 0
MOD_ACTION_LOG_CHANNEL_ID = 0
BOOSTER_LOG_ID = 0

# Category IDs
ADMIN_CHANNELS_CATEGORY_ID = 0

# VC IDs
UNI_VC_ID = 0
ALPHA_VC_ID = 0
KAPPA_VC_ID = 0
DELTA_VC_ID = 0
LAMBDA_VC_ID = 0
RHO_VC_ID = 0
MASTERS_VC_ID = 0

TOTAL_MEMBER_COUNT_VC_ID = 0

BRIDGE_CHANNEL_IDS = []
BRIDGE_BOT_IDS = []

if os.getenv('MODE') == 'PRODUCTION':
    GUILD_ID = 764326796736856066

    # Roles
    JR_MOD_ROLE_ID = 924332988743966751
    MODERATOR_ROLE_ID = 801634222577156097
    JR_ADMIN_ROLE_ID = 808070562046935060
    ADMIN_ROLE_ID = 766041783137468506
    GUILD_MEMBER_ROLE_ID = 824993223436533810
    VERIFIED_ROLE_ID = 812725363686899743
    ACTIVE_ROLE_ID = 809902629760139314
    SB_UNI_MEMBER_ROLE_ID = 803695821094125585
    SB_ALPHA_MEMBER_ROLE_ID = 821080619332796437
    SB_KAPPA_MEMBER_ROLE_ID = 832803831166926859
    SB_DELTA_MEMBER_ROLE_ID = 838121681931075594
    SB_LAMBDA_MEMBER_ROLE_ID = 843871813481267270
    SB_MASTERS_MEMBER_ROLE_ID = 944524838553399326
    TOP_GUILD_ACTIVE_ROLE_ID = 1031644373823262801
    WEIGHT_BANNED_ROLE_ID = 1041544214061776977
    FRESHMAN_ROLE_ID = 765539703016521729
    INSTRUCTOR_ROLE_ID = 801505303854055497
    PROFESSOR_ROLE_ID = 801541534247944253
    DEAN_ROLE_ID = 803273909951922227
    PROVOST_ROLE_ID = 818478619646623797
    PRIMUS_ROLE_ID = 946963518350045224
    LEGATUS_ROLE_ID = 947841300240138290
    BOOSTER_ROLE_ID = 803053116076589068

    # Channels
    QOTD_CHANNEL_ID = 868630191080083476
    TOTAL_MEMBER_COUNT_VC_ID = 890288776302190602
    SBU_BOT_LOGS_CHANNEL_ID = 946591422616838264
    MOD_CHAT_CHANNEL_ID = 802982854291488808
    ADMIN_CHAT_CHANNEL_ID = 911601330219532328
    QOTD_ROLE_ID = 868630686712614922
    BANNED_LIST_CHANNEL_ID = 830188559964307526
    SUGGESTIONS_CHANNEL_ID = 803320921393856602
    CARRY_SERVICE_REPS_CHANNEL_ID = 957773469431525396
    CRAFT_REPS_CHANNEL_ID = 860357041474371614
    MOD_ACTION_LOG_CHANNEL_ID = 823938991345893417
    BOOSTER_LOG_ID = 1033820228934709308

    ADMIN_CHANNELS_CATEGORY_ID = 801476879248261160

    # VCs
    UNI_VC_ID = 945493379599446056
    ALPHA_VC_ID = 945493468539654205
    KAPPA_VC_ID = 945493492434604072
    DELTA_VC_ID = 945493508398153808
    LAMBDA_VC_ID = 945493526047776889
    RHO_VC_ID = 945493556909473812
    MASTERS_VC_ID = 945493573263040522

    BRIDGE_CHANNEL_IDS = [812416103372292126, 819929855008178246, 832346801876107365,
                          837142928957898812, 944526812166361088]
    BRIDGE_BOT_IDS = [1021641891470651423, 1021641933866663986, 1021641967920222208,
                      1021642068751294504, 1021642225223999508]

else:
    GUILD_ID = 1017925960177303612

    # Roles
    JR_MOD_ROLE_ID = 1017925960571568344
    MODERATOR_ROLE_ID = 1017925960571568345
    ADMIN_ROLE_ID = 1017925960592531591
    JR_ADMIN_ROLE_ID = 1017925960571568346
    GUILD_MEMBER_ROLE_ID = 1017925960458313783
    VERIFIED_ROLE_ID = 1017925960374435895
    ACTIVE_ROLE_ID = 1017925960416366669
    SB_UNI_MEMBER_ROLE_ID = 1017925960571568339
    SB_ALPHA_MEMBER_ROLE_ID = 1017925960571568338
    SB_KAPPA_MEMBER_ROLE_ID = 1017925960554786835
    SB_DELTA_MEMBER_ROLE_ID = 1017925960554786834
    SB_LAMBDA_MEMBER_ROLE_ID = 1017925960554786833
    SB_MASTERS_MEMBER_ROLE_ID = 1017925960554786829
    TOP_GUILD_ACTIVE_ROLE_ID = 1030894413016203365
    WEIGHT_BANNED_ROLE_ID = 1041542973055324200
    FRESHMAN_ROLE_ID = 1017925960500265079
    INSTRUCTOR_ROLE_ID = 1017925960525414561
    PROFESSOR_ROLE_ID = 1017925960525414562
    DEAN_ROLE_ID = 1017925960525414563
    PROVOST_ROLE_ID = 1017925960525414564
    PRIMUS_ROLE_ID = 1017925960525414565
    LEGATUS_ROLE_ID = 1017925960525414566
    BOOSTER_ROLE_ID = 1037515948283936900

    # Channels
    QOTD_CHANNEL_ID = 1017925962194747402
    TOTAL_MEMBER_COUNT_VC_ID = 1017925961406238727
    SBU_BOT_LOGS_CHANNEL_ID = 1017925964690358399
    MOD_CHAT_CHANNEL_ID = 1017925964270932022
    ADMIN_CHAT_CHANNEL_ID = 1017925964690358392
    QOTD_ROLE_ID = 1017925960223436836
    BANNED_LIST_CHANNEL_ID = 1017925964065415294
    SUGGESTIONS_CHANNEL_ID = 1017925961779515488
    CARRY_SERVICE_REPS_CHANNEL_ID = 1022831138923884594
    CRAFT_REPS_CHANNEL_ID = 1017925963666960515
    MOD_ACTION_LOG_CHANNEL_ID = 1017925964270932020
    BOOSTER_LOG_ID = 1042923026213249084

    ADMIN_CHANNELS_CATEGORY_ID = 1017925964505829443

    # VCs
    UNI_VC_ID = 1017925961406238728
    ALPHA_VC_ID = 1017925961406238729
    KAPPA_VC_ID = 1017925961603358890
    DELTA_VC_ID = 1017925961603358891
    LAMBDA_VC_ID = 1017925961603358892
    MASTERS_VC_ID = 1017925961603358895

    BRIDGE_CHANNEL_IDS = [1022179121457025196, 1017925963088146482, 1017925963088146483]
    BRIDGE_BOT_IDS = [981945056267210842, 983145287264657508]

WEIGHT_ROLES_INFO = {
    "INSTRUCTOR": {
        "role_id": INSTRUCTOR_ROLE_ID,
        "weight_req": 700,
        "name": "Instructor",
        "previous": {}
    },
    "PROFESSOR": {
        "role_id": PROFESSOR_ROLE_ID,
        "weight_req": 2100,
        "name": "Professor",
        "previous": {INSTRUCTOR_ROLE_ID}
    },
    "DEAN": {
        "role_id": DEAN_ROLE_ID,
        "weight_req": 4200,
        "name": "Dean",
        "previous": {INSTRUCTOR_ROLE_ID, PROFESSOR_ROLE_ID}
    },
    "PROVOST": {
        "role_id": PROVOST_ROLE_ID,
        "weight_req": 8400,
        "name": "Provost",
        "previous": {INSTRUCTOR_ROLE_ID, PROFESSOR_ROLE_ID, DEAN_ROLE_ID}
    },
    "PRIMUS": {
        "role_id": PRIMUS_ROLE_ID,
        "weight_req": 12600,
        "name": "Primus",
        "previous": {INSTRUCTOR_ROLE_ID, PROFESSOR_ROLE_ID, DEAN_ROLE_ID, PROVOST_ROLE_ID}
    },
    "LEGATUS": {
        "role_id": PROVOST_ROLE_ID,
        "weight_req": 18800,
        "name": "Legatus",
        "previous": {INSTRUCTOR_ROLE_ID, PROFESSOR_ROLE_ID, DEAN_ROLE_ID, PROVOST_ROLE_ID, PRIMUS_ROLE_ID}
    }
}

GUILD_MEMBER_ROLES_IDS = [SB_UNI_MEMBER_ROLE_ID, SB_ALPHA_MEMBER_ROLE_ID, SB_DELTA_MEMBER_ROLE_ID,
                          SB_KAPPA_MEMBER_ROLE_ID, SB_LAMBDA_MEMBER_ROLE_ID, SB_MASTERS_MEMBER_ROLE_ID]

GUILDS_INFO = {
    "SKYBLOCK UNI": {
        "role_id": SB_UNI_MEMBER_ROLE_ID,
        "guild_uuid": '6111fcb48ea8c95240436c57',
        "bridge_uuid": 'e3020a41a5c24597ad11a2348c46f815',
        "vc_id": UNI_VC_ID
    },
    "SB ALPHA PSI": {
        "role_id": SB_ALPHA_MEMBER_ROLE_ID,
        "guild_uuid": '604a765e8ea8c962f2bb3b7a',
        "bridge_uuid": 'a42c79f6f60841c38ae6ee1bf2eb7d35',
        "vc_id": ALPHA_VC_ID
    },
    "SB KAPPA ETA": {
        "role_id": SB_KAPPA_MEMBER_ROLE_ID,
        "guild_uuid": '607a0d7c8ea8c9c0ff983976',
        "bridge_uuid": '384248632f3942069a80327a94150f6d',
        "vc_id": KAPPA_VC_ID
    },
    "SB DELTA OMEGA": {
        "role_id": SB_DELTA_MEMBER_ROLE_ID,
        "guild_uuid": '608d91e98ea8c9925cdb91b7',
        "bridge_uuid": 'd35172fc9191404c9671532569b62585',
        "vc_id": DELTA_VC_ID
    },
    "SB MASTERS": {
        "role_id": SB_MASTERS_MEMBER_ROLE_ID,
        "guild_uuid": '570940fb0cf2d37483e106b3',
        "bridge_uuid": '87de0116d5834793a3f2ad0d99b4e8f2',
        "vc_id": MASTERS_VC_ID
    }
}
